// Run with: node --test tests/functions/
// Checks the bundled quiz bank (js/quiz-bank.js) the way the quiz pages use it.
const { describe, it } = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

function loadBank() {
  const file = path.join(__dirname, '../../js/quiz-bank.js');
  delete require.cache[require.resolve(file)];
  global.window = {};
  const log = console.log;
  console.log = () => {};
  try { require(file); } finally { console.log = log; }
  return global.window.SITE_CONFIG;
}

const CHAPTERS = [
  'Computers, Phones and the Internet',
  'Artificial Intelligence',
  'Machine Learning',
  'Chatbots and Large Language Models',
  'Robotics',
  'Staying Safe Online',
  'Programming and Apps',
  'Making Websites',
  'Data',
  'Technology and Everyone',
];
const LEVELS = ['Super easy', 'Easy', 'Medium', 'Hard'];

describe('stored quiz copy versus the bundled bank', () => {
  it('replaces a stored Tech quiz from an older bank with the bundled one', () => {
    const cfg = loadBank();
    const tech = cfg.QUIZZES.find(q => q.id === 'tech-challenge');
    const staleStored = [
      { id: 'tech-challenge', title: 'Tech Challenge', questions: [{ q: 'old question', options: ['a', 'b', 'c', 'd'], answer: 0 }] },
      { id: 'football-arena', title: 'Football Arena', questions: [{ q: 'admin football edit', options: ['a', 'b', 'c', 'd'], answer: 1 }] },
    ];
    const resolved = cfg.resolveQuizzes(staleStored);
    assert.deepEqual(resolved.find(q => q.id === 'tech-challenge').questions, tech.questions);
    assert.equal(resolved.find(q => q.id === 'football-arena').questions[0].q, 'admin football edit');
  });

  it('keeps admin edits made on top of the current bank', () => {
    const cfg = loadBank();
    const tech = cfg.QUIZZES.find(q => q.id === 'tech-challenge');
    const edited = { ...tech, questions: [{ q: 'admin fixed a typo', options: ['a', 'b', 'c', 'd'], answer: 2 }] };
    const resolved = cfg.resolveQuizzes([edited]);
    assert.equal(resolved[0].questions[0].q, 'admin fixed a typo');
  });

  it('falls back to the bundled bank when nothing is stored', () => {
    const cfg = loadBank();
    assert.deepEqual(cfg.resolveQuizzes(null).map(q => q.id), cfg.QUIZZES.map(q => q.id));
    assert.deepEqual(cfg.resolveQuizzes([]).map(q => q.id), cfg.QUIZZES.map(q => q.id));
  });
});

describe('Tech quiz follows the Introduction to Tech book', () => {
  const tech = loadBank().QUIZZES.find(q => q.id === 'tech-challenge');

  it('tags every question with one of the book\'s ten chapters and a level', () => {
    for (const q of tech.questions) {
      assert.ok(CHAPTERS.includes(q.topic), `unknown topic "${q.topic}" on: ${q.q}`);
      assert.ok(LEVELS.includes(q.level), `unknown level "${q.level}" on: ${q.q}`);
    }
  });

  it('has every level in every chapter', () => {
    for (const ch of CHAPTERS) {
      const levels = new Set(tech.questions.filter(q => q.topic === ch).map(q => q.level));
      assert.deepEqual([...LEVELS].filter(l => !levels.has(l)), [], `chapter "${ch}" is missing levels`);
    }
  });

  it('gives every question four distinct options and a valid answer', () => {
    for (const q of tech.questions) {
      assert.equal(q.options.length, 4, q.q);
      assert.equal(new Set(q.options).size, 4, q.q);
      const answers = Array.isArray(q.answer) ? q.answer : [q.answer];
      assert.equal(Array.isArray(q.answer), !!q.multi, `multi flag mismatch: ${q.q}`);
      for (const a of answers) assert.ok(Number.isInteger(a) && a >= 0 && a < 4, q.q);
      assert.ok(q.explanation && q.explanation.length > 20, `missing explanation: ${q.q}`);
    }
  });

  it('has enough questions for a 30-question session', () => {
    assert.equal(tech.sessionSize, 30);
    assert.ok(tech.questions.length >= 100, `only ${tech.questions.length} questions`);
  });
});
