/**
 * Real file uploads for the public Gallery page — images and short video
 * clips, uploaded directly from the admin's own device rather than pasted
 * in as an external URL. Mirrors the security model already established in
 * resources.js (same repo, same author): admin-PIN-gated writes, magic-byte
 * signature validation against the claimed MIME type, random-UUID storage
 * keys, Netlify Blobs for the actual binary content.
 *
 * GET  /.netlify/functions/gallery?action=download&id=<id>   -> public
 *   Streams the file back with its real Content-Type and NO forced
 *   download — unlike resources.js's document downloads, gallery media is
 *   meant to render inline as <img>/<video> on the page, so this
 *   deliberately omits Content-Disposition: attachment.
 * POST /.netlify/functions/gallery
 *   { action:'upload', pin, mimeType, filename, base64Data } -> admin only.
 *     Allowlisted image/video types, magic-byte check, 4MB cap (see note
 *     below on why this ceiling exists). Returns { id, mimeType }.
 *   { action:'delete', pin, id } -> admin only. Deletes the stored blob.
 *
 * gallery.html remains the source of truth for *metadata* (caption, alt
 * text, category tag, ordering) via the existing CMS `gallery_items` array
 * — this function only ever stores and serves the raw binary content, keyed
 * by a random id, with its real MIME type kept alongside as blob metadata
 * so a correct Content-Type can be served back without a separate JSON
 * store to keep in sync.
 *
 * SIZE NOTE: Netlify's synchronous Functions have a hard ~6MB request-body
 * ceiling. A base64-encoded upload runs about 1/3 larger than the raw file,
 * so a 4MB cap here (same cap resources.js already uses for documents)
 * keeps every upload safely under that limit. This means "short video
 * clips" genuinely means short — a few seconds at modest resolution, not a
 * full event recording. There is no way to raise this without a different
 * upload mechanism (e.g. a signed direct-to-storage upload), which is a
 * larger change than this fix.
 */
const { getStore } = require('@netlify/blobs');
const crypto = require('node:crypto');

const FILES_STORE_NAME = 'thrive-gallery-files';
const JSON_HEADERS = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' };
const MAX_FILE_BYTES = 4 * 1024 * 1024; // 4MB — see SIZE NOTE above

const ALLOWED_MIME_TYPES = new Set([
  'image/jpeg', 'image/png', 'image/webp', 'image/gif',
  'video/mp4', 'video/webm', 'video/quicktime',
]);

// Each entry is a list of alternative signature "sets"; a file matches a
// MIME type if ANY set's every {offset, bytes} check passes at that byte
// offset in the file. WEBP needs two checks at different offsets (a RIFF
// container tag at 0, a WEBP tag at 8) — a plain "starts with" check can't
// express that, which is why this is offset-aware rather than a simple
// prefix list like resources.js's simpler, offset-0-only document types.
const MAGIC_SIGNATURES = {
  'image/jpeg': [[{ offset: 0, bytes: [0xff, 0xd8, 0xff] }]],
  'image/png': [[{ offset: 0, bytes: [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a] }]],
  'image/gif': [[{ offset: 0, bytes: [0x47, 0x49, 0x46, 0x38] }]], // "GIF8"
  'image/webp': [[
    { offset: 0, bytes: [0x52, 0x49, 0x46, 0x46] }, // "RIFF"
    { offset: 8, bytes: [0x57, 0x45, 0x42, 0x50] }, // "WEBP"
  ]],
  'video/mp4': [[{ offset: 4, bytes: [0x66, 0x74, 0x79, 0x70] }]], // "....ftyp"
  'video/quicktime': [[{ offset: 4, bytes: [0x66, 0x74, 0x79, 0x70] }]], // modern .mov also uses an ftyp box
  'video/webm': [[{ offset: 0, bytes: [0x1a, 0x45, 0xdf, 0xa3] }]], // EBML header (also covers Matroska)
};

function response(statusCode, body, extraHeaders) {
  return { statusCode, headers: { ...JSON_HEADERS, ...extraHeaders }, body: JSON.stringify(body) };
}

function getFilesStore() {
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) return getStore({ name: FILES_STORE_NAME, siteID, token });
  return getStore(FILES_STORE_NAME);
}

function pinMatches(submitted, expected) {
  const a = Buffer.from(String(submitted ?? ''));
  const b = Buffer.from(String(expected ?? ''));
  if (a.length !== b.length) {
    crypto.timingSafeEqual(a, a);
    return false;
  }
  return crypto.timingSafeEqual(a, b);
}

function requirePin(payload) {
  const expectedPin = process.env.ADMIN_PIN;
  if (!expectedPin) return { ok: false, res: response(503, { error: 'Admin backend is not configured — set ADMIN_PIN in Netlify environment variables' }) };
  if (!pinMatches(payload.pin, expectedPin)) return { ok: false, res: response(401, { error: 'Invalid PIN' }) };
  return { ok: true };
}

function blobsErrorResponse(e) {
  if (e?.name === 'MissingBlobsEnvironmentError') {
    return response(503, {
      error: 'Storage is not configured. Set the NETLIFY_BLOBS_TOKEN environment variable — see README.md Section 16.',
    });
  }
  return response(500, { error: e?.message || 'Unexpected storage error' });
}

function bytesAt(buffer, offset, bytes) {
  if (buffer.length < offset + bytes.length) return false;
  for (let i = 0; i < bytes.length; i++) if (buffer[offset + i] !== bytes[i]) return false;
  return true;
}

function matchesSignature(buffer, mimeType) {
  const sigSets = MAGIC_SIGNATURES[mimeType];
  if (!sigSets) return false;
  return sigSets.some((set) => set.every(({ offset, bytes }) => bytesAt(buffer, offset, bytes)));
}

exports.handler = async (event) => {
  const qs = event.queryStringParameters || {};

  // ── Public read (GET) ──
  if (event.httpMethod === 'GET' && qs.action === 'download') {
    const id = String(qs.id || '').trim();
    if (!id) return response(400, { error: 'id is required' });
    try {
      const store = getFilesStore();
      const result = await store.getWithMetadata(id, { type: 'arrayBuffer' });
      if (!result || !result.data) return response(404, { error: 'File not found' });
      const mimeType = result.metadata?.mimeType || 'application/octet-stream';
      return {
        statusCode: 200,
        headers: {
          'Content-Type': mimeType,
          'X-Content-Type-Options': 'nosniff',
          'Cache-Control': 'public, max-age=31536000, immutable',
        },
        body: Buffer.from(result.data).toString('base64'),
        isBase64Encoded: true,
      };
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (event.httpMethod === 'GET') return response(400, { error: 'Unknown action' });
  if (event.httpMethod !== 'POST') return response(405, { error: 'Method not allowed' });

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return response(400, { error: 'Invalid JSON' });
  }
  const action = String(payload.action || '');

  // ── Admin writes (POST, PIN required) ──
  if (action === 'upload') {
    const auth = requirePin(payload);
    if (!auth.ok) return auth.res;

    const mimeType = String(payload.mimeType || '').trim();
    if (!ALLOWED_MIME_TYPES.has(mimeType)) {
      return response(400, { error: 'File type not allowed — only JPEG, PNG, WEBP, GIF images or MP4/WEBM/MOV video clips can be uploaded' });
    }

    let buffer;
    try {
      buffer = Buffer.from(String(payload.base64Data || ''), 'base64');
    } catch {
      return response(400, { error: 'Invalid file data' });
    }
    if (!buffer.length) return response(400, { error: 'File is empty' });
    if (buffer.length > MAX_FILE_BYTES) {
      return response(400, { error: `File is too large — max ${Math.floor(MAX_FILE_BYTES / (1024 * 1024))}MB (keep video clips short)` });
    }
    if (!matchesSignature(buffer, mimeType)) {
      return response(400, { error: "This file's actual content doesn't match its claimed type — upload rejected" });
    }

    try {
      const store = getFilesStore();
      const id = crypto.randomUUID();
      await store.set(id, buffer, { metadata: { mimeType, sizeBytes: buffer.length } });
      return response(200, { ok: true, id, mimeType });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'delete') {
    const auth = requirePin(payload);
    if (!auth.ok) return auth.res;

    const id = String(payload.id || '').trim();
    if (!id) return response(400, { error: 'id is required' });

    try {
      await getFilesStore().delete(id);
      return response(200, { ok: true });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  return response(400, { error: 'Unknown action' });
};
