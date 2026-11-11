/**
 * One-time quiz access codes — lets an admin pre-generate a batch of codes
 * for an event (e.g. "50 codes for Tech Challenge"), hand them out, and have
 * each one unlock exactly one quiz attempt.
 *
 * POST /.netlify/functions/quiz-code
 *   { action:'generate', quizId, count, label, pin } -> admin only (PIN)
 *     Creates `count` new codes for `quizId`, returns them for printing.
 *   { action:'redeem', code, quizId }                -> public, no PIN
 *     Validates the code is real, matches quizId, and unused; marks it used.
 *   { action:'list', pin }                           -> admin only (PIN)
 *     Returns every code and its used/unused status, for review.
 *   { action:'reset', quizId, pin }                  -> admin only (PIN)
 *     Deletes every code (used and unused) for `quizId` — for starting a
 *     new season/year clean instead of accumulating codes indefinitely.
 *   { action:'submitScore', code, quizId, name, correct, total, timeTaken }
 *                                                    -> public, no PIN
 *     The ONLY way a visitor can add to the leaderboard: one score per real
 *     code for that quiz (409 on a second try). The server works out pct.
 *     Stored per code by lib/leaderboard.js. Returns { ok, rank }.
 *   { action:'clearScores', quizId, pin }            -> admin only (PIN)
 *     Removes every leaderboard score for `quizId`.
 *
 * Stored as one flat map in Netlify Blobs under key thrive_quiz_codes_v1:
 *   { "THRV-7F3K": { quizId, used, usedBy, usedAt, batchLabel }, ... }
 *
 * Concurrency note: redeem does a read-modify-write against Blobs that isn't
 * perfectly atomic under simultaneous requests. For the realistic scale this
 * is used at (an in-person school quiz event, codes handed out one at a
 * time on paper), that's an accepted, documented tradeoff rather than a
 * practical risk — not worth the complexity of real distributed locking.
 */
const { connect, openStore, describeStorageError } = require('./lib/blobs');
const { checkPin } = require('./lib/auth');
const leaderboard = require('./lib/leaderboard');
const crypto = require('node:crypto');

const CODES_KEY = 'thrive_quiz_codes_v1';
const JSON_HEADERS = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' };
const MAX_GENERATE = 1000;
// Unambiguous charset — no 0/O, 1/I/L, to stay readable off a printed sheet.
const CODE_CHARS = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';

function response(statusCode, body) {
  return { statusCode, headers: JSON_HEADERS, body: JSON.stringify(body) };
}

function getCodesStore() {
  return openStore('thrive-admin');
}

function randomCode() {
  const bytes = crypto.randomBytes(4);
  let suffix = '';
  for (let i = 0; i < 4; i++) suffix += CODE_CHARS[bytes[i] % CODE_CHARS.length];
  return 'THRV-' + suffix;
}

async function loadCodes(store) {
  const raw = await store.get(CODES_KEY);
  if (!raw) return {};
  try { return JSON.parse(raw) || {}; } catch { return {}; }
}

function blobsErrorResponse(e) {
  const { status, error } = describeStorageError(e);
  return response(status, { error });
}

exports.handler = async (event) => {
  connect(event);
  if (event.httpMethod !== 'POST') return response(405, { error: 'Method not allowed' });

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return response(400, { error: 'Invalid JSON' });
  }

  const action = String(payload.action || '');
  let store;
  try {
    store = getCodesStore();
  } catch (e) {
    return blobsErrorResponse(e);
  }

  if (action === 'generate') {
    const auth = await checkPin(event, payload.pin);
    if (!auth.ok) return response(auth.status, auth.body);

    const quizId = String(payload.quizId || '').trim();
    const count = Math.floor(Number(payload.count));
    const label = String(payload.label || '').trim().slice(0, 120);
    if (!quizId) return response(400, { error: 'quizId is required' });
    if (!Number.isFinite(count) || count < 1 || count > MAX_GENERATE) {
      return response(400, { error: `count must be between 1 and ${MAX_GENERATE}` });
    }

    try {
      const codes = await loadCodes(store);
      const generated = [];
      let guard = 0;
      while (generated.length < count && guard < count * 20) {
        guard++;
        const code = randomCode();
        if (codes[code]) continue; // extremely unlikely collision — skip and retry
        codes[code] = { quizId, used: false, usedBy: null, usedAt: null, batchLabel: label || null, createdAt: new Date().toISOString() };
        generated.push(code);
      }
      await store.set(CODES_KEY, JSON.stringify(codes));
      return response(200, { ok: true, codes: generated, quizId, label });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'redeem') {
    const code = String(payload.code || '').trim().toUpperCase();
    const quizId = String(payload.quizId || '').trim();
    const usedBy = String(payload.name || '').trim().slice(0, 80);
    if (!code) return response(400, { error: 'Enter your access code' });
    if (!quizId) return response(400, { error: 'quizId is required' });

    try {
      const codes = await loadCodes(store);
      const entry = codes[code];
      if (!entry) return response(404, { error: 'That code was not found. Check it and try again.' });
      if (entry.quizId !== quizId) return response(400, { error: 'That code is not valid for this quiz.' });
      if (entry.used) return response(409, { error: 'This code has already been used.' });
      // A score already stored under this code also means it was used (this
      // check survives the codes-map race described at the top of the file).
      if (await leaderboard.hasScore(store, quizId, code)) return response(409, { error: 'This code has already been used.' });

      entry.used = true;
      entry.usedBy = usedBy || null;
      entry.usedAt = new Date().toISOString();
      await store.set(CODES_KEY, JSON.stringify(codes));
      return response(200, { ok: true });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'submitScore') {
    const code = String(payload.code || '').trim().toUpperCase();
    const quizId = String(payload.quizId || '').trim();
    if (!code) return response(400, { error: 'code is required' });
    if (!quizId) return response(400, { error: 'quizId is required' });
    const { entry: score, error } = leaderboard.cleanScore(payload);
    if (error) return response(400, { error });

    try {
      // Only the code's existence and quiz are required, not its "used" flag:
      // the codes map can lose that flag under simultaneous redeems.
      const entry = (await loadCodes(store))[code];
      if (!entry) return response(404, { error: 'That code was not found.' });
      if (entry.quizId !== quizId) return response(400, { error: 'That code is not valid for this quiz.' });
      if (await leaderboard.hasScore(store, quizId, code)) return response(409, { error: 'A score has already been saved for this code.' });
      await leaderboard.saveScore(store, quizId, code, score);
      const rank = leaderboard.rankOf(await leaderboard.readBoard(store), quizId, score);
      return response(200, { ok: true, rank });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'clearScores') {
    const auth = await checkPin(event, payload.pin);
    if (!auth.ok) return response(auth.status, auth.body);
    const quizId = String(payload.quizId || '').trim();
    if (!quizId) return response(400, { error: 'quizId is required' });
    try {
      return response(200, { ok: true, removed: await leaderboard.clearQuiz(store, quizId) });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'list') {
    const auth = await checkPin(event, payload.pin);
    if (!auth.ok) return response(auth.status, auth.body);

    try {
      const codes = await loadCodes(store);
      const list = Object.entries(codes).map(([code, v]) => ({ code, ...v }));
      list.sort((a, b) => (b.createdAt || '').localeCompare(a.createdAt || ''));
      return response(200, { ok: true, codes: list });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'reset') {
    const auth = await checkPin(event, payload.pin);
    if (!auth.ok) return response(auth.status, auth.body);

    const quizId = String(payload.quizId || '').trim();
    if (!quizId) return response(400, { error: 'quizId is required' });

    try {
      const codes = await loadCodes(store);
      let removed = 0;
      for (const code of Object.keys(codes)) {
        if (codes[code].quizId === quizId) { delete codes[code]; removed++; }
      }
      await store.set(CODES_KEY, JSON.stringify(codes));
      return response(200, { ok: true, removed, quizId });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  return response(400, { error: 'Unknown action' });
};
