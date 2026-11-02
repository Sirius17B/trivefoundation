// Run with: node --test "tests/functions/*.check.js"
const { describe, it, beforeEach, afterEach } = require('node:test');
const assert = require('node:assert/strict');
const fake = require('./fake-blobs');
fake.install();

const adminData = require('../../netlify/functions/admin-data');
const resources = require('../../netlify/functions/resources');
const gallery = require('../../netlify/functions/gallery');
const quizCode = require('../../netlify/functions/quiz-code');

const PIN = 'correct-horse-battery';
const MINUTE = 60 * 1000;

let clock;
const originalNow = Date.now;

function request(handler, ip, body, extra = {}) {
  const base = fake.netlifyEvent();
  return handler.handler({
    ...base,
    httpMethod: 'POST',
    headers: { ...base.headers, 'x-nf-client-connection-ip': ip },
    body: JSON.stringify(body),
    ...extra,
  });
}
const verify = (pin, ip = '203.0.113.7') => request(adminData, ip, { action: 'verify', pin });
const json = (res) => JSON.parse(res.body);

describe('admin PIN check (server side)', () => {
  beforeEach(() => {
    fake.reset();
    process.env.ADMIN_PIN = PIN;
    delete process.env.NETLIFY_BLOBS_TOKEN;
    clock = 1_800_000_000_000;
    Date.now = () => clock;
  });
  afterEach(() => { Date.now = originalNow; });

  it('accepts the right PIN', async () => {
    const res = await verify(PIN);
    assert.equal(res.statusCode, 200, res.body);
    assert.deepEqual(json(res), { ok: true });
  });

  it('rejects a wrong PIN and says how many tries are left', async () => {
    const res = await verify('nope');
    assert.equal(res.statusCode, 401);
    assert.equal(json(res).error, 'Invalid PIN');
    assert.equal(json(res).attemptsLeft, 4);
  });

  it('locks a client out after 5 wrong PINs, and then refuses even the right one', async () => {
    for (let i = 0; i < 4; i++) assert.equal((await verify('wrong' + i)).statusCode, 401);
    const fifth = await verify('wrong4');
    assert.equal(fifth.statusCode, 429);
    assert.ok(json(fifth).retryAfterSeconds > 0);

    const rightButLocked = await verify(PIN);
    assert.equal(rightButLocked.statusCode, 429, 'a locked-out client must not be able to confirm a guess');
  });

  it('lets the client back in once the lock has run out', async () => {
    for (let i = 0; i < 5; i++) await verify('wrong' + i);
    assert.equal((await verify(PIN)).statusCode, 429);
    clock += 16 * MINUTE;
    assert.equal((await verify(PIN)).statusCode, 200);
  });

  it('a correct PIN wipes the failure count', async () => {
    for (let i = 0; i < 4; i++) await verify('wrong' + i);
    assert.equal((await verify(PIN)).statusCode, 200);
    for (let i = 0; i < 4; i++) assert.equal((await verify('again' + i)).statusCode, 401);
  });

  it('forgets old mistakes after the window passes', async () => {
    for (let i = 0; i < 4; i++) await verify('wrong' + i);
    clock += 16 * MINUTE;
    assert.equal((await verify('late')).statusCode, 401);
    assert.equal(json(await verify('late2')).attemptsLeft, 3);
  });

  it('keeps clients separate: one locked client does not lock another', async () => {
    for (let i = 0; i < 5; i++) await verify('wrong' + i, '198.51.100.1');
    assert.equal((await verify(PIN, '198.51.100.1')).statusCode, 429);
    assert.equal((await verify(PIN, '198.51.100.2')).statusCode, 200);
  });

  it('counts wrong guesses made through ANY endpoint toward the same lock', async () => {
    // Guessing against a write endpoint must not be a way around the limit.
    for (let i = 0; i < 3; i++) {
      const res = await request(adminData, '203.0.113.9', { key: 'thrive_cms_v1_data', value: '{}', pin: 'guess' + i });
      assert.equal(res.statusCode, 401);
    }
    for (let i = 0; i < 2; i++) {
      const res = await request(resources, '203.0.113.9', { action: 'delete', pin: 'guess' + i, id: 'x' });
      assert.equal(res.statusCode, i === 1 ? 429 : 401);
    }
    assert.equal((await verify(PIN, '203.0.113.9')).statusCode, 429);
  });

  // Every endpoint that takes a PIN: [name, handler, body builder]. "Passes the
  // PIN check" means any outcome other than 401/429/503-from-auth.
  const PIN_PROTECTED = [
    ['admin-data write', adminData, (pin) => ({ key: 'thrive_cms_v1_data', value: '{}', pin })],
    ['resources delete', resources, (pin) => ({ action: 'delete', id: 'missing', pin })],
    ['resources addVideo', resources, (pin) => ({ action: 'addVideo', title: 't', url: 'https://youtu.be/abcdefghijk', pin })],
    ['resources uploadDocument', resources, (pin) => ({ action: 'uploadDocument', title: 't', mimeType: 'application/pdf', base64Data: '', pin })],
    ['gallery upload', gallery, (pin) => ({ action: 'upload', mimeType: 'image/png', base64Data: '', pin })],
    ['gallery delete', gallery, (pin) => ({ action: 'delete', id: 'missing', pin })],
    ['quiz-code generate', quizCode, (pin) => ({ action: 'generate', quizId: 'tech-challenge', count: 1, pin })],
    ['quiz-code list', quizCode, (pin) => ({ action: 'list', pin })],
    ['quiz-code reset', quizCode, (pin) => ({ action: 'reset', quizId: 'tech-challenge', pin })],
  ];
  for (const [name, handler, body] of PIN_PROTECTED) {
    it(`${name}: rejects a wrong PIN with 401 and does not reject the right one`, async () => {
      const bad = await request(handler, '203.0.113.50', body('wrong'));
      assert.equal(bad.statusCode, 401, `${name} accepted or mishandled a wrong PIN: ${bad.body}`);
      const good = await request(handler, '203.0.113.51', body(PIN));
      assert.notEqual(good.statusCode, 401, `${name} rejected the right PIN: ${good.body}`);
      assert.notEqual(good.statusCode, 429);
    });
  }

  it('still lets the right PIN write protected content', async () => {
    const ok = await request(adminData, '203.0.113.7', { key: 'thrive_cms_v1_data', value: '{"a":1}', pin: PIN });
    assert.equal(ok.statusCode, 200, ok.body);
    const bad = await request(adminData, '203.0.113.7', { key: 'thrive_cms_v1_data', value: '{"a":2}', pin: 'wrong' });
    assert.equal(bad.statusCode, 401);
  });

  it('never stores a raw IP address', async () => {
    await verify('wrong', '203.0.113.77');
    assert.ok(fake.data.size > 0, 'expected a failure record to exist');
    for (const [key, entry] of fake.data) {
      assert.ok(!key.includes('203.0.113.77'), key);
      assert.ok(!entry.value.toString().includes('203.0.113.77'));
    }
  });

  it('refuses to authenticate anyone when ADMIN_PIN is not configured', async () => {
    delete process.env.ADMIN_PIN;
    assert.equal((await verify('')).statusCode, 503);
    assert.equal((await verify('anything')).statusCode, 503);
  });

  it('fails closed when it cannot reach storage to count attempts', async () => {
    // No Netlify credentials on the request and a rejected manual token.
    process.env.SITE_ID = 'site-1';
    process.env.NETLIFY_BLOBS_TOKEN = 'expired-token';
    const res = await adminData.handler({
      httpMethod: 'POST',
      headers: { 'x-nf-client-connection-ip': '203.0.113.7' },
      body: JSON.stringify({ action: 'verify', pin: PIN }),
    });
    assert.equal(res.statusCode, 503);
    assert.notEqual(res.statusCode, 200);
  });
});
