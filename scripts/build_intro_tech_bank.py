#!/usr/bin/env python3
"""Build the Tech Challenge question bank in js/quiz-bank.js from
scripts/content/intro_tech.py (questions written from INTRO_TO_TECH_BOOK.md).

    python scripts/build_intro_tech_bank.py          # audit only, changes nothing
    python scripts/build_intro_tech_bank.py --write  # audit, then rewrite techQ

Safe to run again: the output depends only on the content file, so a second
run writes the same bytes.

What it does to each question:
  * single-answer: the correct option is placed on a letter chosen so that,
    within every chapter, the correct letters are spread evenly over A-D
    (a per-question hash alone left some chapters lopsided); the wrong
    options are shuffled around it.
  * multi-select: all four options are shuffled; the answer becomes the
    sorted list of the correct positions.

Audit (both modes): per-chapter letter spread, level mix, and the
correct-vs-wrong option length ratio. A question is flagged when the correct
option is much longer or shorter than the wrong ones, because a length tell
lets a student guess without knowing the subject.
"""
import hashlib, importlib.util, json, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'js' / 'quiz-bank.js'
CONTENT = ROOT / 'scripts' / 'content' / 'intro_tech.py'
LEVELS = ['Super easy', 'Easy', 'Medium', 'Hard']
RATIO_LOW, RATIO_HIGH = 0.75, 1.35   # mean correct length / mean wrong length


def seed(text):
    return int(hashlib.sha256(text.encode('utf-8')).hexdigest(), 16)


def load_chapters():
    spec = importlib.util.spec_from_file_location('intro_tech', CONTENT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTERS


def place(chapter, items):
    singles = [it for it in items if not it.get('multi')]
    # Rotate the starting letter per chapter, so the spare slot in a chapter
    # whose count is not a multiple of 4 is not always D.
    offset = seed(chapter) % 4
    slots = [(i + offset) % 4 for i in range(len(singles))]
    random.Random(seed(chapter)).shuffle(slots)
    slot_for = {id(it): s for it, s in zip(singles, slots)}
    out = []
    for it in items:
        rng = random.Random(seed(it['q']))
        if it.get('multi'):
            opts = it['right'] + it['wrongs']
            rng.shuffle(opts)
            answer = sorted(opts.index(r) for r in it['right'])
        else:
            wrongs = list(it['wrongs'])
            rng.shuffle(wrongs)
            answer = slot_for[id(it)]
            opts = wrongs[:answer] + it['right'] + wrongs[answer:]
        q = {'topic': chapter, 'level': it['level'], 'q': it['q'],
             'options': opts, 'answer': answer}
        if it.get('multi'):
            q['multi'] = True
        q['explanation'] = it['explanation']
        out.append(q)
    return out


def mark_test_set(built):
    """Mark the fixed test set (inTest: true): every candidate sits these same
    questions, each in their own shuffled order. Three per chapter (10 x 3 =
    30, the session size); chapter n leaves out level n mod 4, so over the
    ten chapters the set holds 7 Super easy, 7 Easy, 8 Medium and 8 Hard.
    Within a chapter and level the pick is fixed by a hash of the question
    text, so rebuilding gives the same set."""
    for n, (ch, qs) in enumerate(built.items()):
        skip = LEVELS[n % 4]
        for level in LEVELS:
            if level == skip:
                continue
            pool = [q for q in qs if q['level'] == level]
            min(pool, key=lambda q: seed(q['q']))['inTest'] = True


def validate(chapter, items):
    errors = []
    for it in items:
        where = f"[{chapter}] {it['q'][:60]}"
        n = len(it['right']) + len(it['wrongs'])
        if n != 4:
            errors.append(f"{where}: {n} options, need 4")
        if len(set(it['right'] + it['wrongs'])) != n:
            errors.append(f"{where}: duplicate options")
        if it['level'] not in LEVELS:
            errors.append(f"{where}: bad level {it['level']!r}")
        if bool(it.get('multi')) != (len(it['right']) > 1):
            errors.append(f"{where}: multi flag does not match number of right answers")
    return errors


def ratio(it):
    mean = lambda xs: sum(len(x) for x in xs) / len(xs)
    return mean(it['right']) / mean(it['wrongs'])


def audit(chapters, built):
    print(f"{'chapter':38} {'n':>3}  levels SE/E/M/H   letters A/B/C/D (single answers)")
    total_letters, total_levels = Counter(), Counter()
    for ch, qs in built.items():
        lv = Counter(q['level'] for q in qs)
        le = Counter('ABCD'[q['answer']] for q in qs if not q.get('multi'))
        total_letters.update(le); total_levels.update(lv)
        print(f"{ch:38} {len(qs):>3}  {'/'.join(str(lv[l]) for l in LEVELS):>14}   "
              f"{'/'.join(str(le[c]) for c in 'ABCD')}")
    n = sum(len(qs) for qs in built.values())
    print(f"{'TOTAL':38} {n:>3}  {'/'.join(str(total_levels[l]) for l in LEVELS):>14}   "
          f"{'/'.join(str(total_letters[c]) for c in 'ABCD')}")
    multi = sum(1 for qs in built.values() for q in qs if q.get('multi'))
    print(f"multi-select questions: {multi}")

    ratios = [(ratio(it), ch, it) for ch, items in chapters.items() for it in items]
    flagged = [r for r in ratios if not RATIO_LOW <= r[0] <= RATIO_HIGH]
    mean_ratio = sum(r[0] for r in ratios) / len(ratios)
    longest = sum(1 for _, _, it in ratios
                  if len(it['right'][0]) > max(len(w) for w in it['wrongs']) and not it.get('multi'))
    singles = sum(1 for _, _, it in ratios if not it.get('multi'))
    print(f"length ratio correct/wrong: mean {mean_ratio:.2f}; "
          f"correct option is the single longest in {longest}/{singles} questions (chance is ~{singles // 4})")
    for r, ch, it in flagged:
        print(f"  FLAG ratio {r:.2f} [{ch}] {it['q'][:70]}")
    return flagged


def to_js(q):
    parts = [f"{k}:{json.dumps(q[k], ensure_ascii=False)}" for k in ('topic', 'level', 'q', 'options', 'answer')]
    if q.get('multi'):
        parts.append('multi:true')
    if q.get('inTest'):
        parts.append('inTest:true')
    parts.append('explanation:' + json.dumps(q['explanation'], ensure_ascii=False))
    return '{' + ','.join(parts) + '},'


def write(built):
    text = BANK.read_text(encoding='utf-8')
    # techQ holds one question per line, so the first line that is just "];"
    # closes it (footballQ follows after a comment block).
    pattern = re.compile(r"(const techQ = \[\n)(.*?)(\n\];\n)", re.S)
    if not pattern.search(text):
        sys.exit('Could not find the techQ array in js/quiz-bank.js; nothing written.')
    lines = []
    for ch, qs in built.items():
        lines.append(f"// ── {ch.upper()} ({len(qs)}) " + '─' * max(4, 60 - len(ch)))
        lines.extend(to_js(q) for q in qs)
    new = pattern.sub(lambda m: m.group(1) + '\n'.join(lines) + m.group(3), text, count=1)
    BANK.write_text(new, encoding='utf-8', newline='\n')
    print(f"wrote {sum(len(q) for q in built.values())} questions to {BANK.relative_to(ROOT)}")


def main():
    chapters = load_chapters()
    errors = [e for ch, items in chapters.items() for e in validate(ch, items)]
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    built = {ch: place(ch, items) for ch, items in chapters.items()}
    mark_test_set(built)
    audit(chapters, built)
    test = [q for qs in built.values() for q in qs if q.get('inTest')]
    lv = Counter(q['level'] for q in test)
    le = Counter('ABCD'[q['answer']] for q in test if not q.get('multi'))
    print(f"test set: {len(test)} questions; levels "
          f"{'/'.join(str(lv[l]) for l in LEVELS)}; letters {'/'.join(str(le[c]) for c in 'ABCD')}; "
          f"multi {sum(1 for q in test if q.get('multi'))}")
    if '--write' in sys.argv:
        write(built)


if __name__ == '__main__':
    main()
