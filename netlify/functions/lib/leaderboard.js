/**
 * Quiz leaderboard storage — the one place that writes or reads scores.
 *
 * Each score is its own blob, keyed by quiz and access code:
 *   quiz_score/<quizId>/<code>  ->  { name, pct, correct, total, timeTaken, date }
 * so (a) a code can hold at most one score, and (b) children who finish at
 * the same moment never overwrite each other (the old single-blob board was
 * a read-modify-write that could lose scores, and any visitor could replace
 * it wholesale).
 *
 * The pages still read the board as the old key `thrive_v5_quiz_lb`
 * ({ [quizId]: [entry, ...] }, best first, top 50); admin-data builds that
 * view from these blobs plus whatever is left in the legacy blob.
 */
const LEGACY_KEY = 'thrive_v5_quiz_lb';
const PREFIX = 'quiz_score/';
const TOP_N = 50;

const scoreKey = (quizId, code) => `${PREFIX}${quizId}/${code}`;

function byRank(a, b) {
  return b.pct - a.pct || a.timeTaken - b.timeTaken;
}

/* Check a submitted score once, here, at the edge. Returns the clean entry or
   an error message. pct is worked out on the server, never taken from the
   browser. */
function cleanScore({ name, correct, total, timeTaken }) {
  const isInt = (n) => Number.isInteger(n);
  const cleanName = String(name ?? '').trim().slice(0, 60);
  if (!cleanName) return { error: 'name is required' };
  if (!isInt(total) || total < 1 || total > 100) return { error: 'total must be a whole number from 1 to 100' };
  if (!isInt(correct) || correct < 0 || correct > total) return { error: 'correct must be a whole number from 0 to total' };
  if (!isInt(timeTaken) || timeTaken < 0 || timeTaken > 4 * 60 * 60) return { error: 'timeTaken must be a whole number of seconds' };
  return {
    entry: {
      name: cleanName,
      pct: Math.round((correct / total) * 100),
      correct, total, timeTaken,
      date: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Africa/Lagos' }),
    },
  };
}

async function hasScore(store, quizId, code) {
  return (await store.get(scoreKey(quizId, code))) != null;
}

async function saveScore(store, quizId, code, entry) {
  await store.set(scoreKey(quizId, code), JSON.stringify(entry));
}

async function readBoard(store) {
  const board = {};
  try {
    const legacy = JSON.parse((await store.get(LEGACY_KEY)) || '{}');
    if (legacy && typeof legacy === 'object') {
      for (const [quizId, list] of Object.entries(legacy)) if (Array.isArray(list)) board[quizId] = [...list];
    }
  } catch { /* a corrupt legacy blob just contributes nothing */ }

  const { blobs } = await store.list({ prefix: PREFIX });
  const entries = await Promise.all(blobs.map(async ({ key }) => {
    const quizId = key.slice(PREFIX.length).split('/')[0];
    try { return [quizId, JSON.parse(await store.get(key))]; } catch { return null; }
  }));
  for (const item of entries) {
    if (!item || !item[1]) continue;
    (board[item[0]] ||= []).push(item[1]);
  }
  for (const quizId of Object.keys(board)) board[quizId] = board[quizId].sort(byRank).slice(0, TOP_N);
  return board;
}

/* 1-based position of a just-saved entry on its quiz's board. */
function rankOf(board, quizId, entry) {
  return (board[quizId] || []).findIndex(e =>
    e.name === entry.name && e.pct === entry.pct && e.timeTaken === entry.timeTaken) + 1;
}

/* Admin only (callers check the PIN): remove every score for one quiz. */
async function clearQuiz(store, quizId) {
  const { blobs } = await store.list({ prefix: `${PREFIX}${quizId}/` });
  await Promise.all(blobs.map(({ key }) => store.delete(key)));
  let removed = blobs.length;
  try {
    const legacy = JSON.parse((await store.get(LEGACY_KEY)) || '{}');
    if (Array.isArray(legacy[quizId])) {
      removed += legacy[quizId].length;
      delete legacy[quizId];
      await store.set(LEGACY_KEY, JSON.stringify(legacy));
    }
  } catch { /* nothing usable to clear */ }
  return removed;
}

module.exports = { LEGACY_KEY, cleanScore, hasScore, saveScore, readBoard, rankOf, clearQuiz };
