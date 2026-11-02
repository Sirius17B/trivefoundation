/**
 * The one place that decides how a function reaches Netlify Blobs.
 *
 * Netlify attaches short-lived storage credentials to every invocation as
 * event.blobs; connectLambda(event) hands them to the Blobs client. That is
 * the supported route for functions written as `exports.handler`, needs no
 * secret of ours, and cannot expire underneath us.
 *
 * Why this exists: in July 2026 these functions never called connectLambda,
 * which surfaces as MissingBlobsEnvironmentError, and the workaround was a
 * personal access token in NETLIFY_BLOBS_TOKEN. Personal tokens expire. In
 * early November 2026 it did, and every storage-backed feature (content,
 * league tables, quiz leaderboard, resources) failed with 401 at once.
 *
 * The manual token is kept only as a fallback for when Netlify supplies no
 * context (it never wins over per-request credentials).
 */
const { getStore, connectLambda } = require('@netlify/blobs');

let connected = false;

// Call first thing in every handler. Safe to call on every invocation.
function connect(event) {
  connected = false;
  if (event && event.blobs) {
    try {
      connectLambda(event);
      connected = true;
    } catch {
      // Unreadable context: fall through to the manual-credentials fallback.
    }
  }
}

function openStore(name) {
  if (connected) return getStore(name);
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) return getStore({ name, siteID, token });
  return getStore(name);
}

// Maps a storage failure to an HTTP status and a message that says what to do.
function describeStorageError(e) {
  if (e && e.name === 'MissingBlobsEnvironmentError') {
    return {
      status: 503,
      error: 'Storage is unavailable: Netlify did not supply storage credentials to this function and no NETLIFY_BLOBS_TOKEN is set.',
    };
  }
  if (e && /\(401\b/.test(String(e.message))) {
    return {
      status: 503,
      error: 'Storage rejected the credentials (401). If the NETLIFY_BLOBS_TOKEN environment variable is set it has probably expired: delete it in the Netlify dashboard (Site settings, Environment variables) so the site uses Netlify\'s automatic credentials, or replace it with a new token.',
    };
  }
  return { status: 500, error: (e && e.message) || 'Unexpected storage error' };
}

module.exports = { connect, openStore, describeStorageError };
