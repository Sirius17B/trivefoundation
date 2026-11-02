/**
 * Admin content persistence — reads are public, most writes require the
 * admin PIN. One key is the exception: the quiz leaderboard is written by
 * every visitor who finishes a quiz, not just admins, so it's public-write.
 *
 * GET  /.netlify/functions/admin-data?key=<key>       -> { value: string|null }
 * POST /.netlify/functions/admin-data  { key, value, pin } -> { ok: true }
 *
 * Backed by Netlify Blobs (getStore('thrive-admin')) — a single site-wide,
 * durable key-value store that persists across deploys. No separate database
 * to provision; this is included on every Netlify site.
 *
 * Requires the ADMIN_PIN environment variable to be set in the Netlify
 * dashboard (Site settings -> Environment variables). This is the
 * authoritative PIN check for admin writes — the client-side check in
 * js/main.js is only a UX convenience and is never trusted for persistence.
 *
 * Storage credentials come from Netlify per request — see lib/blobs.js.
 */
const { connect, openStore, describeStorageError } = require('./lib/blobs');
const { checkPin } = require('./lib/auth');

const JSON_HEADERS = {
  'Content-Type': 'application/json',
  'Cache-Control': 'no-store',
};

// Keys that require the admin PIN to write.
const ADMIN_WRITE_KEYS = new Set([
  'thrive_cms_v1_data',       // CMS text/image overrides, gallery items, bank override
  'thrive_team_photos_v1',    // About page team member photos
  'thrive_stories_v1',        // Activities page news/stories feed
  'thrive_v5_quizzes',        // Admin-edited quiz questions
  'thrive_league_v3_boys',    // Boys football league teams/results
  'thrive_league_v3_girls',   // Girls football league teams/results
  'thrive_tech_v2_data',      // Tech rankings participants
]);

// Keys any visitor can write without a PIN — currently just the quiz
// leaderboard, since submitting your own score after finishing a quiz is a
// normal visitor action, not an admin one.
const PUBLIC_WRITE_KEYS = new Set([
  'thrive_v5_quiz_lb',
]);

const ALLOWED_KEYS = new Set([...ADMIN_WRITE_KEYS, ...PUBLIC_WRITE_KEYS]);

const MAX_VALUE_BYTES = 2_000_000; // 2MB — generous for text/JSON, blocks abuse

function response(statusCode, body) {
  return { statusCode, headers: JSON_HEADERS, body: JSON.stringify(body) };
}

exports.handler = async (event) => {
  connect(event);
  let store;
  try {
    store = openStore('thrive-admin');
  } catch (e) {
    return blobsErrorResponse(e);
  }

  if (event.httpMethod === 'GET') {
    const key = event.queryStringParameters?.key;
    if (!key || !ALLOWED_KEYS.has(key)) return response(400, { error: 'Unknown key' });
    try {
      const value = await store.get(key);
      return response(200, { value: value ?? null });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (event.httpMethod === 'POST') {
    let payload;
    try {
      payload = JSON.parse(event.body || '{}');
    } catch {
      return response(400, { error: 'Invalid JSON' });
    }

    // Login: the PIN is checked here, on the server, never in the browser.
    if (payload.action === 'verify') {
      const auth = await checkPin(event, payload.pin);
      return auth.ok ? response(200, { ok: true }) : response(auth.status, auth.body);
    }

    const key = String(payload.key || '');
    const value = payload.value;
    const pin = payload.pin;

    if (!ALLOWED_KEYS.has(key)) return response(400, { error: 'Unknown key' });
    if (typeof value !== 'string') return response(400, { error: 'value must be a string' });
    if (Buffer.byteLength(value, 'utf8') > MAX_VALUE_BYTES) return response(413, { error: 'Value too large' });

    if (ADMIN_WRITE_KEYS.has(key)) {
      const auth = await checkPin(event, pin);
      if (!auth.ok) return response(auth.status, auth.body);
    }

    try {
      await store.set(key, value);
      return response(200, { ok: true });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  return response(405, { error: 'Method not allowed' });
};

function blobsErrorResponse(e) {
  const { status, error } = describeStorageError(e);
  return response(status, { error });
}
