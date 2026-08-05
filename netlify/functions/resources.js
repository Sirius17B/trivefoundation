/**
 * Downloadable resources (study books, flyers, slide decks) + embedded video
 * links, for the public Resources page. Uploads are admin-only (PIN); every
 * visitor can list and download.
 *
 * GET  /.netlify/functions/resources?action=list                -> public
 *   Returns the resources metadata array (no binary file content).
 * GET  /.netlify/functions/resources?action=download&id=<id>     -> public
 *   Streams the actual file back with a forced-download Content-Disposition.
 * GET  /.netlify/functions/resources?action=thumbnail&id=<thumbId> -> public
 *   Streams a document's page-1 preview JPEG inline (no forced download) —
 *   thumbId is a separate id from the document's own id, only ever handed
 *   out via the list action, and only served if it matches a live entry.
 * POST /.netlify/functions/resources
 *   { action:'uploadDocument', pin, title, description, filename, mimeType, base64Data, thumbnailData? }
 *     -> admin only. Strict allowlist (PDF/Word/PowerPoint), magic-byte
 *        signature check, 4MB cap. See SECURITY NOTES below. thumbnailData
 *        is an optional base64 JPEG (rendered client-side from a PDF's
 *        first page — see resources.html) that fails soft: a rejected or
 *        missing thumbnail never fails the document upload itself.
 *   { action:'addVideo', pin, title, description, url }
 *     -> admin only. URL must match a YouTube or Vimeo watch-page pattern;
 *        the provider + video ID are extracted server-side, never trusted
 *        as freeform input, since they're later used to build an iframe src.
 *   { action:'delete', pin, id }
 *     -> admin only. Removes the metadata entry and, for a document, its
 *        stored file blob.
 *
 * SECURITY NOTES (this function is the site's only file-upload surface):
 *  - No public upload path exists anywhere — every write action requires
 *    the same server-side PIN check as the rest of the admin backend.
 *  - Documents are restricted to a narrow allowlist (PDF, DOC/DOCX,
 *    PPT/PPTX). The claimed MIME type is not trusted on its own — the
 *    actual file bytes are checked against the real signature for that
 *    type (see MAGIC_SIGNATURES), so renaming a script or executable to
 *    "study-book.pdf" is rejected rather than silently accepted.
 *  - Stored files are keyed by a random UUID, never by the user-supplied
 *    filename — the original filename is kept only as a sanitised display
 *    string, so there's no path-traversal or filename-injection surface.
 *  - Downloads are always served with Content-Disposition: attachment and
 *    X-Content-Type-Options: nosniff, and the Content-Type sent is the
 *    server-validated type stored at upload time, not anything supplied
 *    at download time — this stops an uploaded file from ever being
 *    rendered inline as HTML/script by a browser.
 *  - Video "uploads" are never actual files — only a validated YouTube/
 *    Vimeo URL is stored, and only the extracted numeric/alphanumeric
 *    video ID (never the raw stored URL) is used to build the iframe src
 *    the page actually renders, so this can't become an arbitrary-iframe
 *    or open-redirect vector.
 *  - This is real, meaningful protection against the common attack
 *    patterns (disguised executables, script injection via file content,
 *    unauthorised uploads) but is not a substitute for a dedicated
 *    antivirus/malware scanning service — there's no such scan here. If
 *    that matters for your threat model, a service like VirusTotal's API
 *    could be added as an extra check before accepting an upload.
 */
const { getStore } = require('@netlify/blobs');
const crypto = require('node:crypto');

const META_KEY = 'thrive_resources_v1';
const FILES_STORE_NAME = 'thrive-resource-files';
const THUMBS_STORE_NAME = 'thrive-resource-thumbs';
const JSON_HEADERS = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' };
const MAX_FILE_BYTES = 4 * 1024 * 1024; // 4MB — see note on Netlify's ~6MB sync function payload limit
const MAX_THUMB_BYTES = 300 * 1024; // a page-1 preview JPEG has no business being large

const ALLOWED_MIME_TYPES = new Set([
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/vnd.ms-powerpoint',
  'application/vnd.openxmlformats-officedocument.presentationml.presentation',
]);

// First bytes that genuinely identify each allowed file family, independent
// of whatever extension or MIME type the upload claims. OLE2 covers legacy
// .doc/.ppt (same container format); ZIP covers modern .docx/.pptx (both
// are ZIP-based OOXML) — this can't perfectly tell .docx from .pptx apart
// from the signature alone, but that's not the point: the point is
// confirming the bytes are a real Office/PDF document, not a renamed
// executable or script.
const MAGIC_SIGNATURES = {
  'application/pdf': [[0x25, 0x50, 0x44, 0x46, 0x2d]], // %PDF-
  'application/msword': [[0xd0, 0xcf, 0x11, 0xe0, 0xa1, 0xb1, 0x1a, 0xe1]],
  'application/vnd.ms-powerpoint': [[0xd0, 0xcf, 0x11, 0xe0, 0xa1, 0xb1, 0x1a, 0xe1]],
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document': [[0x50, 0x4b, 0x03, 0x04]],
  'application/vnd.openxmlformats-officedocument.presentationml.presentation': [[0x50, 0x4b, 0x03, 0x04]],
};

function response(statusCode, body, extraHeaders) {
  return { statusCode, headers: { ...JSON_HEADERS, ...extraHeaders }, body: JSON.stringify(body) };
}

function getMetaStore() {
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) return getStore({ name: 'thrive-admin', siteID, token });
  return getStore('thrive-admin');
}

function getFilesStore() {
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) return getStore({ name: FILES_STORE_NAME, siteID, token });
  return getStore(FILES_STORE_NAME);
}

function getThumbsStore() {
  const siteID = process.env.SITE_ID || process.env.NETLIFY_SITE_ID;
  const token = process.env.NETLIFY_BLOBS_TOKEN;
  if (siteID && token) return getStore({ name: THUMBS_STORE_NAME, siteID, token });
  return getStore(THUMBS_STORE_NAME);
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

async function loadMeta(store) {
  const raw = await store.get(META_KEY);
  if (!raw) return [];
  try { return JSON.parse(raw) || []; } catch { return []; }
}

function blobsErrorResponse(e) {
  if (e?.name === 'MissingBlobsEnvironmentError') {
    return response(503, {
      error: 'Storage is not configured. Set the NETLIFY_BLOBS_TOKEN environment variable — see README.md Section 16.',
    });
  }
  return response(500, { error: e?.message || 'Unexpected storage error' });
}

// Strip anything except a conservative safe character set, so the stored
// display filename can never carry a path separator, control character, or
// markup — this is a display string only, never used to build a storage key.
function sanitiseFilename(name) {
  const base = String(name || 'file').replace(/[\\/]/g, '').replace(/[^\w .\-]/g, '_').trim();
  return base.slice(0, 150) || 'file';
}

function bytesStartWith(bytes, sig) {
  if (bytes.length < sig.length) return false;
  for (let i = 0; i < sig.length; i++) if (bytes[i] !== sig[i]) return false;
  return true;
}

function isJpeg(buffer) {
  return buffer.length >= 3 && buffer[0] === 0xff && buffer[1] === 0xd8 && buffer[2] === 0xff;
}

function matchesSignature(buffer, mimeType) {
  const sigs = MAGIC_SIGNATURES[mimeType];
  if (!sigs) return false;
  const head = new Uint8Array(buffer.buffer, buffer.byteOffset, Math.min(buffer.length, 16));
  return sigs.some((sig) => bytesStartWith(head, sig));
}

// Only YouTube and Vimeo, and only their normal watch/short-link URL shapes.
// The extracted ID is the only thing ever used to build an embed src later —
// the raw submitted URL is stored for display/reference only.
function parseVideoUrl(url) {
  const u = String(url || '').trim();
  let m = u.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/shorts\/)([\w-]{6,20})/i);
  if (m) return { provider: 'youtube', videoId: m[1] };
  m = u.match(/vimeo\.com\/(?:video\/)?(\d{6,12})/i);
  if (m) return { provider: 'vimeo', videoId: m[1] };
  return null;
}

exports.handler = async (event) => {
  const qs = event.queryStringParameters || {};

  // ── Public reads (GET) ──
  if (event.httpMethod === 'GET' && qs.action === 'list') {
    try {
      const store = getMetaStore();
      const list = await loadMeta(store);
      list.sort((a, b) => (b.addedAt || '').localeCompare(a.addedAt || ''));
      return response(200, { ok: true, resources: list });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (event.httpMethod === 'GET' && qs.action === 'download') {
    const id = String(qs.id || '').trim();
    if (!id) return response(400, { error: 'id is required' });
    try {
      const metaStore = getMetaStore();
      const list = await loadMeta(metaStore);
      const entry = list.find((r) => r.id === id && r.type === 'document');
      if (!entry) return response(404, { error: 'Resource not found' });
      const filesStore = getFilesStore();
      const fileBuf = await filesStore.get(entry.fileId, { type: 'arrayBuffer' });
      if (!fileBuf) return response(404, { error: 'File not found' });
      return {
        statusCode: 200,
        headers: {
          'Content-Type': entry.mimeType,
          'Content-Disposition': `attachment; filename="${entry.originalName.replace(/"/g, '')}"`,
          'X-Content-Type-Options': 'nosniff',
          'Cache-Control': 'private, max-age=3600',
        },
        body: Buffer.from(fileBuf).toString('base64'),
        isBase64Encoded: true,
      };
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (event.httpMethod === 'GET' && qs.action === 'thumbnail') {
    const id = String(qs.id || '').trim();
    if (!id) return response(400, { error: 'id is required' });
    try {
      const metaStore = getMetaStore();
      const list = await loadMeta(metaStore);
      const entry = list.find((r) => r.thumbId === id);
      if (!entry) return response(404, { error: 'Thumbnail not found' });
      const thumbBuf = await getThumbsStore().get(id, { type: 'arrayBuffer' });
      if (!thumbBuf) return response(404, { error: 'Thumbnail not found' });
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'image/jpeg',
          'X-Content-Type-Options': 'nosniff',
          'Cache-Control': 'public, max-age=31536000, immutable',
        },
        body: Buffer.from(thumbBuf).toString('base64'),
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
  if (action === 'uploadDocument') {
    const auth = requirePin(payload);
    if (!auth.ok) return auth.res;

    const title = String(payload.title || '').trim().slice(0, 150);
    const description = String(payload.description || '').trim().slice(0, 500);
    const mimeType = String(payload.mimeType || '').trim();
    const filename = sanitiseFilename(payload.filename);
    if (!title) return response(400, { error: 'Title is required' });
    if (!ALLOWED_MIME_TYPES.has(mimeType)) {
      return response(400, { error: 'File type not allowed — only PDF, Word, or PowerPoint files can be uploaded' });
    }

    let buffer;
    try {
      buffer = Buffer.from(String(payload.base64Data || ''), 'base64');
    } catch {
      return response(400, { error: 'Invalid file data' });
    }
    if (!buffer.length) return response(400, { error: 'File is empty' });
    if (buffer.length > MAX_FILE_BYTES) {
      return response(400, { error: `File is too large — max ${Math.floor(MAX_FILE_BYTES / (1024 * 1024))}MB` });
    }
    if (!matchesSignature(buffer, mimeType)) {
      return response(400, { error: "This file's actual content doesn't match its claimed type — upload rejected" });
    }

    // Optional page-1 preview thumbnail, rendered client-side (see
    // resources.html) so this function never needs a PDF-rendering
    // dependency of its own. Validated the same way as the document itself:
    // real JPEG bytes required, size-capped, never trusted just because the
    // client claims it's an image.
    let thumbBuffer = null;
    if (payload.thumbnailData) {
      try {
        thumbBuffer = Buffer.from(String(payload.thumbnailData), 'base64');
      } catch {
        return response(400, { error: 'Invalid thumbnail data' });
      }
      if (!thumbBuffer.length || thumbBuffer.length > MAX_THUMB_BYTES || !isJpeg(thumbBuffer)) {
        thumbBuffer = null; // don't fail the whole upload over a bad thumbnail — just skip it
      }
    }

    try {
      const metaStore = getMetaStore();
      const filesStore = getFilesStore();
      const list = await loadMeta(metaStore);
      const id = crypto.randomUUID();
      const fileId = crypto.randomUUID();
      await filesStore.set(fileId, buffer);
      let thumbId = null;
      if (thumbBuffer) {
        thumbId = crypto.randomUUID();
        await getThumbsStore().set(thumbId, thumbBuffer);
      }
      list.push({
        id, type: 'document', title, description,
        fileId, originalName: filename, mimeType, sizeBytes: buffer.length, thumbId,
        addedAt: new Date().toISOString(),
      });
      await metaStore.set(META_KEY, JSON.stringify(list));
      return response(200, { ok: true, id });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  if (action === 'addVideo') {
    const auth = requirePin(payload);
    if (!auth.ok) return auth.res;

    const title = String(payload.title || '').trim().slice(0, 150);
    const description = String(payload.description || '').trim().slice(0, 500);
    if (!title) return response(400, { error: 'Title is required' });
    const parsed = parseVideoUrl(payload.url);
    if (!parsed) return response(400, { error: 'Enter a valid YouTube or Vimeo link' });

    try {
      const store = getMetaStore();
      const list = await loadMeta(store);
      const id = crypto.randomUUID();
      list.push({
        id, type: 'video', title, description,
        provider: parsed.provider, videoId: parsed.videoId, url: String(payload.url).trim().slice(0, 500),
        addedAt: new Date().toISOString(),
      });
      await store.set(META_KEY, JSON.stringify(list));
      return response(200, { ok: true, id });
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
      const metaStore = getMetaStore();
      const list = await loadMeta(metaStore);
      const idx = list.findIndex((r) => r.id === id);
      if (idx === -1) return response(404, { error: 'Resource not found' });
      const [removed] = list.splice(idx, 1);
      await metaStore.set(META_KEY, JSON.stringify(list));
      if (removed.type === 'document' && removed.fileId) {
        try { await getFilesStore().delete(removed.fileId); } catch { /* best effort */ }
      }
      if (removed.thumbId) {
        try { await getThumbsStore().delete(removed.thumbId); } catch { /* best effort */ }
      }
      return response(200, { ok: true });
    } catch (e) {
      return blobsErrorResponse(e);
    }
  }

  return response(400, { error: 'Unknown action' });
};
