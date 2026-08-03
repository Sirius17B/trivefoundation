#!/usr/bin/env python3
"""Audit a study book's worked examples for the two bugs caught in
TECH_STUDY_BOOK.md: distractor length imbalance and correct-answer-letter
clustering. Run after every chapter, not just at the end.
Usage: python3 scripts/audit_study_book.py <file.md>
"""
import re, sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else 'TECH_STUDY_BOOK.md'
with open(path, encoding='utf-8') as f:
    text = f.read()

examples = re.findall(
    r'\*\*Example \d+\*\*\n\n\*(.*?)\*\n\nA\) (.*?)\nB\) (.*?)\nC\) (.*?)\nD\) (.*?)\n\n\*Walk through it:\*(.*?)(?=\n\n(?:\*\*Example|\-\-\-))',
    text, re.S)

print(f"Found {len(examples)} examples in {path}\n")
letter_dist = Counter()
flagged = []
for i, (q, a, b, c, d, walk) in enumerate(examples, 1):
    lens = {'A': len(a), 'B': len(b), 'C': len(c), 'D': len(d)}
    m2 = list(re.finditer(r'\*\*([ABCD])\*\*', walk))
    correct = m2[-1].group(1) if m2 else None
    if correct is None:
        print(f"Ex{i}: COULD NOT FIND BOLDED ANSWER LETTER"); continue
    letter_dist[correct] += 1
    correct_len = lens[correct]
    other_lens = [v for k, v in lens.items() if k != correct]
    avg_other = sum(other_lens) / len(other_lens)
    ratio = correct_len / avg_other if avg_other else 0
    flag = ratio > 1.3 or ratio < 0.7
    if flag:
        flagged.append((i, correct, ratio))
    print(f"Ex{i}: correct={correct} ratio={ratio:.2f}" + (" <<<< FLAG" if flag else ""))

print("\nletter distribution:", dict(letter_dist))
print(f"flagged: {len(flagged)} / {len(examples)}")
if flagged:
    print("  ", flagged)
