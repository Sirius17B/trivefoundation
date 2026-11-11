// Run with: node --test tests/functions/
// Named *.check.js (not *.test.js) so Playwright, which owns ./tests, ignores it.
const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert/strict');
const fake = require('./fake-blobs');
fake.install();

const resources = require('../../netlify/functions/resources');
const adminData = require('../../netlify/functions/admin-data');

// The exact production situation on 2026-11-02: a personal access token set
// as an environment variable months ago, now rejected by Netlify with 401.
const STALE_ENV = { SITE_ID: 'site-1', NETLIFY_BLOBS_TOKEN: 'expired-token' };

describe('storage credentials', () => {
  beforeEach(() => {
    fake.reset();
    Object.assign(process.env, STALE_ENV);
  });

  it('lists resources using the credentials Netlify sends with the request, ignoring a stale token', async () => {
    const res = await resources.handler(fake.netlifyEvent({ httpMethod: 'GET', queryStringParameters: { action: 'list' } }));
    assert.equal(res.statusCode, 200, res.body);
    assert.deepEqual(JSON.parse(res.body), { ok: true, resources: [] });
  });

  it('reads site content using the credentials Netlify sends with the request, ignoring a stale token', async () => {
    const res = await adminData.handler(fake.netlifyEvent({ httpMethod: 'GET', queryStringParameters: { key: 'thrive_cms_v1_data' } }));
    assert.equal(res.statusCode, 200, res.body);
    assert.deepEqual(JSON.parse(res.body), { value: null });
  });

  it('saves and reloads a quiz score end to end', async () => {
    // Scores go in through an access code (quiz-code submitScore), never by
    // writing the leaderboard key; see leaderboard.check.js for the rules.
    process.env.ADMIN_PIN = 'pin-for-storage-test';
    const quizCode = require('../../netlify/functions/quiz-code');
    const call = (body) => quizCode.handler(fake.netlifyEvent({ httpMethod: 'POST', body: JSON.stringify(body) }));
    const gen = await call({ action: 'generate', quizId: 'tech-challenge', count: 1, pin: 'pin-for-storage-test' });
    assert.equal(gen.statusCode, 200, gen.body);
    const [code] = JSON.parse(gen.body).codes;
    const post = await call({ action: 'submitScore', code, quizId: 'tech-challenge', name: 'Ada', correct: 9, total: 10, timeTaken: 60 });
    assert.equal(post.statusCode, 200, post.body);
    const get = await adminData.handler(fake.netlifyEvent({ httpMethod: 'GET', queryStringParameters: { key: 'thrive_v5_quiz_lb' } }));
    const board = JSON.parse(JSON.parse(get.body).value);
    assert.deepEqual(board['tech-challenge'].map(e => [e.name, e.pct]), [['Ada', 90]]);
  });

  it('when Netlify sends no credentials and the manual token is rejected, says exactly what to fix', async () => {
    const res = await resources.handler({ httpMethod: 'GET', queryStringParameters: { action: 'list' }, headers: {} });
    assert.equal(res.statusCode, 503);
    const { error } = JSON.parse(res.body);
    assert.match(error, /NETLIFY_BLOBS_TOKEN/);
    assert.match(error, /expired|rejected/i);
  });
});
