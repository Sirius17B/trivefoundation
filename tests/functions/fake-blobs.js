// In-memory stand-in for @netlify/blobs, faithful in the two ways that matter:
//  - explicit credentials are checked, so a stale manual token fails with 401
//    exactly as production did;
//  - credentials supplied per request via connectLambda(event) are trusted.
// Install it with install() BEFORE requiring any function under test.
const VALID_TOKEN = 'invocation-token';

class BlobsInternalError extends Error {
  constructor(status) {
    super(`Netlify Blobs has generated an internal error (${status} status code)`);
    this.name = 'BlobsInternalError';
  }
}
class MissingBlobsEnvironmentError extends Error {
  constructor() {
    super('The environment has not been configured to use Netlify Blobs.');
    this.name = 'MissingBlobsEnvironmentError';
  }
}

const data = new Map(); // `${store}/${key}` -> { value: Buffer, metadata }
let context = null;
const calls = { connectLambda: 0 };

function connectLambda(event) {
  const parsed = JSON.parse(Buffer.from(event.blobs, 'base64').toString('utf8'));
  context = { token: parsed.token };
  calls.connectLambda++;
}

function getStore(arg) {
  const opts = typeof arg === 'string' ? { name: arg } : arg;
  let token;
  if (opts.token) token = opts.token;
  else if (context) token = context.token;
  else throw new MissingBlobsEnvironmentError();
  const guard = () => { if (token !== VALID_TOKEN) throw new BlobsInternalError(401); };
  const k = (key) => `${opts.name}/${key}`;
  return {
    async get(key, o) {
      guard();
      const e = data.get(k(key));
      if (!e) return null;
      if (o && o.type === 'arrayBuffer') return e.value.buffer.slice(e.value.byteOffset, e.value.byteOffset + e.value.byteLength);
      return e.value.toString('utf8');
    },
    async getWithMetadata(key, o) {
      guard();
      const e = data.get(k(key));
      if (!e) return null;
      const buf = e.value.buffer.slice(e.value.byteOffset, e.value.byteOffset + e.value.byteLength);
      return { data: o && o.type === 'arrayBuffer' ? buf : e.value.toString('utf8'), metadata: e.metadata };
    },
    async set(key, value, o) {
      guard();
      data.set(k(key), { value: Buffer.from(value), metadata: o && o.metadata });
    },
    async delete(key) {
      guard();
      data.delete(k(key));
    },
    // Same shape as @netlify/blobs: { blobs: [{ key, etag }], directories: [] }.
    async list(o = {}) {
      guard();
      const head = `${opts.name}/`;
      const blobs = [...data.keys()]
        .filter(full => full.startsWith(head))
        .map(full => full.slice(head.length))
        .filter(key => key.startsWith(o.prefix || ''))
        .map(key => ({ key, etag: 'etag-' + key }));
      return { blobs, directories: [] };
    },
  };
}

function install() {
  const id = require.resolve('@netlify/blobs');
  require.cache[id] = { id, filename: id, loaded: true, exports: { getStore, connectLambda } };
}

function reset() {
  data.clear();
  context = null;
  calls.connectLambda = 0;
}

// What Netlify attaches to every function invocation.
function netlifyEvent(extra = {}) {
  return {
    blobs: Buffer.from(JSON.stringify({ url: 'https://edge.example', token: VALID_TOKEN })).toString('base64'),
    headers: { 'x-nf-site-id': 'site-1', 'x-nf-deploy-id': 'deploy-1', 'x-nf-client-connection-ip': '203.0.113.7' },
    ...extra,
  };
}

module.exports = { install, reset, netlifyEvent, calls, data, VALID_TOKEN };
