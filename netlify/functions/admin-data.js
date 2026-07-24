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
 * Blobs config: zero-config getStore(name) relies on Netlify auto-injecting
 * site/token context into the function at deploy time. On some accounts/
 * deploys that automatic injection doesn't happen (surfaces as
 * MissingBlobsEnvironmentError even though the function runs fine
 * otherwise) — so this also supports explicit manual config via
 * NETLIFY_BLOBS_TOKEN, which is used whenever it's set. See README.md
 * Section 16 for how to create that token if you hit that error.
 */
const { getStore } = require('@netlify/blobs');
const crypto = require('node:crypto');

function getAdminStore() {
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) {
    return getStore({ name: 'thrive-admin', siteID, token });
  }
  return getStore('thrive-admin');
}

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

function pinMatches(submitted, expected) {
  const a = Buffer.from(String(submitted ?? ''));
  const b = Buffer.from(String(expected ?? ''));
  // timingSafeEqual requires equal-length buffers — pad rather than
  // short-circuit on length, so a wrong-length guess still takes the same
  // code path as a same-length wrong guess.
  if (a.length !== b.length) {
    crypto.timingSafeEqual(a, a); // constant-time no-op to keep timing flat
    return false;
  }
  return crypto.timingSafeEqual(a, b);
}

exports.handler = async (event) => {
  let store;
  try {
    store = getAdminStore();
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

    const key = String(payload.key || '');
    const value = payload.value;
    const pin = payload.pin;

    if (!ALLOWED_KEYS.has(key)) return response(400, { error: 'Unknown key' });
    if (typeof value !== 'string') return response(400, { error: 'value must be a string' });
    if (Buffer.byteLength(value, 'utf8') > MAX_VALUE_BYTES) return response(413, { error: 'Value too large' });

    if (ADMIN_WRITE_KEYS.has(key)) {
      const expectedPin = process.env.ADMIN_PIN;
      if (!expectedPin) return response(503, { error: 'Admin backend is not configured — set ADMIN_PIN in Netlify environment variables' });
      if (!pinMatches(pin, expectedPin)) return response(401, { error: 'Invalid PIN' });
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
  if (e?.name === 'MissingBlobsEnvironmentError') {
    return response(503, {
      error: 'Storage is not configured. Create a Netlify personal access token and set it as the NETLIFY_BLOBS_TOKEN environment variable — see README.md Section 16.',
    });
  }
  return response(500, { error: e?.message || 'Unexpected storage error' });
}
