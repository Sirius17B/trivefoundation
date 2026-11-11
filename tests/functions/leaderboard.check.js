// Run with: node --test "tests/functions/*.check.js"
// The quiz leaderboard: visitors may add ONE score per access code and
// nothing else; only the admin (PIN) can clear it.
const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert/strict');
const fake = require('./fake-blobs');
fake.install();

const adminData = require('../../netlify/functions/admin-data');
const quizCode = require('../../netlify/functions/quiz-code');

const PIN = 'correct-horse-battery';
const LB_KEY = 'thrive_v5_quiz_lb';

const post = (handler, body) => handler.handler(fake.netlifyEvent({ httpMethod: 'POST', body: JSON.stringify(body) }));
const json = (res) => JSON.parse(res.body);
async function board() {
  const res = await adminData.handler(fake.netlifyEvent({ httpMethod: 'GET', queryStringParameters: { key: LB_KEY } }));
  assert.equal(res.statusCode, 200, res.body);
  return JSON.parse(json(res).value || '{}');
}
async function makeCodes(quizId, count) {
  const res = await post(quizCode, { action: 'generate', quizId, count, pin: PIN });
  assert.equal(res.statusCode, 200, res.body);
  return json(res).codes;
}
const score = (code, extra = {}) => post(quizCode, {
  action: 'submitScore', code, quizId: 'tech-challenge', name: 'Ada Obi', correct: 24, total: 30, timeTaken: 600, ...extra,
});

describe('quiz leaderboard is locked to one score per access code', () => {
  beforeEach(() => {
    fake.reset();
    process.env.ADMIN_PIN = PIN;
    delete process.env.NETLIFY_BLOBS_TOKEN;
  });

  it('refuses a visitor who tries to overwrite the whole leaderboard', async () => {
    const res = await post(adminData, { key: LB_KEY, value: '{}' });
    assert.ok([401, 403].includes(res.statusCode), `got ${res.statusCode}`);
  });

  it('records a score sent with a real code, working out the percentage itself', async () => {
    const [code] = await makeCodes('tech-challenge', 1);
    assert.equal((await post(quizCode, { action: 'redeem', code, quizId: 'tech-challenge', name: 'Ada Obi' })).statusCode, 200);
    const res = await score(code, { pct: 100 });
    assert.equal(res.statusCode, 200, res.body);
    assert.equal(json(res).rank, 1);
    const lb = await board();
    assert.equal(lb['tech-challenge'].length, 1);
    assert.deepEqual(
      (({ name, pct, correct, total, timeTaken }) => ({ name, pct, correct, total, timeTaken }))(lb['tech-challenge'][0]),
      { name: 'Ada Obi', pct: 80, correct: 24, total: 30, timeTaken: 600 });
  });

  it('accepts only one score per code', async () => {
    const [code] = await makeCodes('tech-challenge', 1);
    assert.equal((await score(code)).statusCode, 200);
    assert.equal((await score(code, { correct: 30 })).statusCode, 409);
    assert.equal((await board())['tech-challenge'].length, 1);
    assert.equal((await board())['tech-challenge'][0].correct, 24);
  });

  it('refuses scores with no code, an unknown code, or a code for another quiz', async () => {
    const [footballCode] = await makeCodes('football-arena', 1);
    assert.equal((await score('')).statusCode, 400);
    assert.equal((await score('THRV-ZZZZ')).statusCode, 404);
    assert.equal((await score(footballCode)).statusCode, 400);
    assert.deepEqual(await board(), {});
  });

  it('refuses impossible numbers', async () => {
    const [code] = await makeCodes('tech-challenge', 1);
    for (const bad of [{ correct: 31 }, { correct: -1 }, { total: 0 }, { total: 500 }, { correct: 'all' }, { timeTaken: -5 }, { name: '' }]) {
      assert.equal((await score(code, bad)).statusCode, 400, JSON.stringify(bad));
    }
    assert.deepEqual(await board(), {});
  });

  it('keeps every score when many children finish at the same moment', async () => {
    const codes = await makeCodes('tech-challenge', 19);
    const results = await Promise.all(codes.map((c, i) => score(c, { name: 'Child ' + i, correct: i % 31 })));
    assert.ok(results.every(r => r.statusCode === 200));
    assert.equal((await board())['tech-challenge'].length, 19);
  });

  it('will not let a code start a new attempt after its score is in', async () => {
    const [code] = await makeCodes('tech-challenge', 1);
    assert.equal((await score(code)).statusCode, 200);
    const again = await post(quizCode, { action: 'redeem', code, quizId: 'tech-challenge', name: 'Ada Obi' });
    assert.equal(again.statusCode, 409);
  });

  it('lets only the admin clear a quiz leaderboard', async () => {
    const [t] = await makeCodes('tech-challenge', 1);
    const [f] = await makeCodes('football-arena', 1);
    await score(t);
    await post(quizCode, { action: 'submitScore', code: f, quizId: 'football-arena', name: 'Bayo', correct: 10, total: 15, timeTaken: 100 });
    assert.equal((await post(quizCode, { action: 'clearScores', quizId: 'tech-challenge' })).statusCode, 401);
    assert.equal((await board())['tech-challenge'].length, 1);
    const ok = await post(quizCode, { action: 'clearScores', quizId: 'tech-challenge', pin: PIN });
    assert.equal(ok.statusCode, 200, ok.body);
    const lb = await board();
    assert.equal((lb['tech-challenge'] || []).length, 0);
    assert.equal(lb['football-arena'].length, 1);
  });
});
