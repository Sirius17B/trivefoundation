#!/usr/bin/env python3
"""Replace all quiz-bank.js lines tagged with a given topic with freshly
authored questions from a scripts/content/<module>.py file's QUESTIONS list.
Preserves line position/order and every other topic's lines untouched.
Usage: python3 scripts/inject_questions.py <module_name> "<Topic Name>"

Redistributes each single-answer question's correct option across A/B/C/D
(seeded per-question, so it's stable but not a suspicious round-robin
pattern) before writing — hand-authoring answers tends to unconsciously
cluster on one letter (this bit us twice already: an earlier batch landed
~95% on B, and the very first version of this script's own AI Foundations
batch landed 32/34 on A). quiz-play.html re-shuffles per session regardless,
but the raw source data itself should never look skewed either.
"""
import sys, json, random, hashlib, importlib.util, re

PATH = 'js/quiz-bank.js'

def redistribute(questions):
    out = []
    for q in questions:
        if q.get('multi') or isinstance(q['answer'], list):
            out.append(q)  # leave multi-select option order as authored
            continue
        # Seed from a hash of the question text, not a local list index —
        # an index-based seed repeats identically across every batch's
        # first/second/... question (each batch restarts at i=0), which
        # correlated skew across batches even though each batch alone
        # looked fine. Hashing the question text is globally unique.
        seed = int(hashlib.sha256(q['q'].encode('utf-8')).hexdigest(), 16)
        rng = random.Random(seed)
        idx = [0, 1, 2, 3]
        rng.shuffle(idx)
        # new slot k holds the option originally at position idx[k]
        new_options = [q['options'][idx[k]] for k in range(4)]
        new_answer = idx.index(q['answer'])
        out.append({**q, 'options': new_options, 'answer': new_answer})
    return out

def to_js_object(q):
    parts = []
    if q.get('topic'):
        parts.append('topic:' + json.dumps(q['topic'], ensure_ascii=False))
    parts.append('q:' + json.dumps(q['q'], ensure_ascii=False))
    parts.append('options:' + json.dumps(q['options'], ensure_ascii=False))
    parts.append('answer:' + json.dumps(q['answer'], ensure_ascii=False))
    if q.get('multi'):
        parts.append('multi:true')
    if q.get('explanation'):
        parts.append('explanation:' + json.dumps(q['explanation'], ensure_ascii=False))
    return '{' + ','.join(parts) + '},'

def main():
    module_name, topic = sys.argv[1], sys.argv[2]
    spec = importlib.util.spec_from_file_location(module_name, f'scripts/content/{module_name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    new_questions = redistribute(mod.QUESTIONS)

    with open(PATH, encoding='utf-8') as f:
        lines = f.read().split('\n')

    pat = re.compile(r"""\{topic:['"]%s['"],""" % re.escape(topic))
    target_indices = [i for i, l in enumerate(lines) if pat.match(l.strip())]
    if len(target_indices) != len(new_questions):
        print(f"MISMATCH: file has {len(target_indices)} lines tagged '{topic}', "
              f"but {module_name}.py has {len(new_questions)} questions. Aborting — no changes made.")
        sys.exit(1)

    for idx, q in zip(target_indices, new_questions):
        if not q.get('topic'):
            q = {**q, 'topic': topic}
        lines[idx] = to_js_object(q)

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Replaced {len(target_indices)} '{topic}' questions from {module_name}.py")

if __name__ == '__main__':
    main()
