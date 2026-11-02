/**
 * The one place that decides whether a submitted admin PIN is acceptable.
 * Every function that takes a PIN calls checkPin(); nothing else compares
 * PINs.
 *
 * Why it limits guesses: the PIN is checked on the server, so guessing it
 * online is the only attack left, and it has to be slow. Five wrong PINs
 * from one client lock that client out for 15 minutes. While locked, even
 * the correct PIN is refused, so a locked-out client cannot use the answer
 * to confirm a guess. A correct PIN clears the count.
 *
 * Fails closed: if the attempt counter can't be read or saved, the answer is
 * "unavailable", never "OK".
 *
 * Known limits, stated plainly: this limit is BEST-EFFORT, not exact.
 *  - Netlify Blobs reads are eventually consistent (they can be stale for up
 *    to about a minute) and connectLambda() offers no strongly-consistent
 *    reads, so a fast burst of parallel guesses can read an old counter and
 *    be under-counted. It reliably slows slow, sequential guessing; it does
 *    not stop a determined burst.
 *  - The limit is per client address, so an attacker with many addresses
 *    gets five guesses per address.
 *  Making it exact needs atomic conditional writes (`onlyIfNew`), which
 *  @netlify/blobs 8.x lacks (11.x has them): claim one of five attempt slots
 *  per client per window before comparing, so parallel requests can't share
 *  a slot. Until then the real defence is a long, random ADMIN_PIN.
 *  tests/functions/auth.check.js proves the logic against a fake that IS
 *  strongly consistent; it does not prove Netlify's behaviour.
 */
const crypto = require('node:crypto');
const { openStore } = require('./blobs');

const MAX_FAILURES = 5;
const WINDOW_MS = 15 * 60 * 1000;
const LOCK_MS = 15 * 60 * 1000;

function pinMatches(submitted, expected) {
  const a = Buffer.from(String(submitted ?? ''));
  const b = Buffer.from(String(expected ?? ''));
  if (a.length !== b.length) {
    crypto.timingSafeEqual(a, a); // keep timing flat for wrong-length guesses
    return false;
  }
  return crypto.timingSafeEqual(a, b);
}

// Stored as a hash so the counter never holds a raw IP address.
function clientKey(event) {
  const h = (event && event.headers) || {};
  const ip = h['x-nf-client-connection-ip']
    || String(h['x-forwarded-for'] || '').split(',')[0].trim()
    || 'unknown';
  return 'fail:' + crypto.createHash('sha256').update(ip).digest('hex').slice(0, 32);
}

const deny = (status, error, extra) => ({ ok: false, status, body: { error, ...extra } });

function locked(ms) {
  const retryAfterSeconds = Math.max(1, Math.ceil(ms / 1000));
  const minutes = Math.ceil(retryAfterSeconds / 60);
  return deny(429, `Too many incorrect attempts. Try again in ${minutes} minute${minutes === 1 ? '' : 's'}.`, { retryAfterSeconds });
}

async function loadRecord(store, key) {
  const raw = await store.get(key);
  if (!raw) return { count: 0, windowStart: 0, lockedUntil: 0 };
  try { return { count: 0, windowStart: 0, lockedUntil: 0, ...JSON.parse(raw) }; } catch { return { count: 0, windowStart: 0, lockedUntil: 0 }; }
}

/**
 * @returns {Promise<{ok:true} | {ok:false, status:number, body:object}>}
 * On failure, respond with `response(result.status, result.body)`.
 */
async function checkPin(event, submitted) {
  const expected = process.env.ADMIN_PIN;
  if (!expected) return deny(503, 'Admin backend is not configured — set ADMIN_PIN in Netlify environment variables');

  const now = Date.now();
  let store, key, record;
  try {
    store = openStore('thrive-auth');
    key = clientKey(event);
    record = await loadRecord(store, key);
  } catch {
    return deny(503, 'Sign-in is temporarily unavailable. Please try again shortly.');
  }

  if (record.lockedUntil > now) return locked(record.lockedUntil - now);

  if (pinMatches(submitted, expected)) {
    if (record.count || record.lockedUntil) {
      try { await store.delete(key); } catch { /* a stale counter only makes the next login stricter */ }
    }
    return { ok: true };
  }

  const stale = now - record.windowStart > WINDOW_MS;
  const count = (stale ? 0 : record.count) + 1;
  const lockNow = count >= MAX_FAILURES;
  const next = lockNow
    ? { count: 0, windowStart: now, lockedUntil: now + LOCK_MS }
    : { count, windowStart: stale ? now : record.windowStart, lockedUntil: 0 };
  try {
    await store.set(key, JSON.stringify(next));
  } catch {
    return deny(503, 'Sign-in is temporarily unavailable. Please try again shortly.');
  }
  return lockNow ? locked(LOCK_MS) : deny(401, 'Invalid PIN', { attemptsLeft: MAX_FAILURES - count });
}

module.exports = { checkPin };
