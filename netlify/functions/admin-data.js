/**
 * Admin content persistence — reads are public, every write requires the
 * admin PIN. Visitors cannot write anything here. The quiz leaderboard key
 * is read-only here: it is assembled from per-code scores (lib/leaderboard.js),
 * which visitors can only add through quiz-code's submitScore, one per code.
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
const leaderboard = require('./lib/leaderboard');

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

// Keys anyone can read but nobody writes through this endpoint.
const READ_ONLY_KEYS = new Set([
  leaderboard.LEGACY_KEY,     // quiz leaderboard, built from per-code scores
]);

const ALLOWED_KEYS = new Set([...ADMIN_WRITE_KEYS, ...READ_ONLY_KEYS]);

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
      if (key === leaderboard.LEGACY_KEY) {
        return response(200, { value: JSON.stringify(await leaderboard.readBoard(store)) });
      }
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
    if (READ_ONLY_KEYS.has(key)) return response(403, { error: 'This data cannot be written here' });
    if (typeof value !== 'string') return response(400, { error: 'value must be a string' });
    if (Buffer.byteLength(value, 'utf8') > MAX_VALUE_BYTES) return response(413, { error: 'Value too large' });

    const auth = await checkPin(event, pin);
    if (!auth.ok) return response(auth.status, auth.body);

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
