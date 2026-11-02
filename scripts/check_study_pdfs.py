#!/usr/bin/env python3
"""Check the generated study-guide PDFs against their markdown sources.

Usage: python3 scripts/check_study_pdfs.py [folder]     (default: dist)
Needs PyMuPDF (pip install pymupdf). Exits 1 if any check fails.

What "right" means here, each point a way these PDFs have been wrong before:
  - brand fonts (Fredoka, Lexend) are embedded and the old fonts are gone
  - nothing from the markdown was dropped: every heading and every worked
    example (with its walk-through) is present
  - no wrong spelling of the organisation name
  - nothing runs off the page (a table once spilled past the margins)
  - the cover shows the right title, the organisation name and a logo image
"""
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parent.parent
BOOKS = [
    ("TECH_STUDY_BOOK", "Tech Study Book"),
    ("FOOTBALL_STUDY_BOOK", "Football Study Book"),
]
WRONG_NAMES = ("TriveFoundation", "Trive Foundation", "THRIVE Foundation")
# Text the Foundation has retired; it must not come back.
RETIRED_TEXT = ("Technology, Hard work, Resilience",)  # the old THRIVE acronym tagline
FALLBACK_ONLY = {"₦"}  # the only character the brand fonts lack
SIDE_MARGIN_PT = 28  # nothing on a body page may sit closer than this to the edge


def norm(text):
    return re.sub(r"\s+", " ", text.replace(" ", " ")).strip().lower()


def flat_case(text):
    return re.sub(r"\s+", " ", text)


def strip_md(text):
    return re.sub(r"[*_`]", "", text)


def check_book(stem, title, folder):
    problems = []
    pdf_path = folder / f"{stem}.pdf"
    if not pdf_path.exists():
        return [f"{pdf_path.name}: not found, build it first"]
    md = (ROOT / f"{stem}.md").read_text(encoding="utf-8")
    doc = fitz.open(pdf_path)
    pages = [p.get_text() for p in doc]
    full = "\n".join(pages)
    flat = norm(full)

    used = {}
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    used.setdefault(span["font"], set()).update(span["text"])
    fonts = set(used)
    if not any("Fredoka" in f for f in fonts):
        problems.append(f"headings are not set in Fredoka (fonts used: {sorted(fonts)})")
    if not any("Lexend" in f for f in fonts):
        problems.append(f"body text is not set in Lexend (fonts used: {sorted(fonts)})")
    old = sorted(f for f in fonts if any(x in f for x in ("Georgia", "Times", "Helvetica")))
    if old:
        problems.append(f"old fonts used for text: {old}")
    for f, chars in used.items():
        if "Calibri" in f and not chars <= FALLBACK_ONLY:
            problems.append(f"fallback font used for more than the Naira sign: {sorted(chars - FALLBACK_ONLY)}")

    for wrong in WRONG_NAMES:
        if wrong in full:
            problems.append(f"contains the wrong spelling '{wrong}'")
    for retired in RETIRED_TEXT:
        if retired in flat_case(full):
            problems.append(f"contains retired text '{retired}'")

    headings = [strip_md(m.group(2)).strip() for m in re.finditer(r"^(#{1,2}) (.+)$", md, re.M)]
    headings = [h for h in headings if not h.startswith("THE THRIVE") and not h.startswith("A Deep-Dive")]
    def present(heading):
        m = re.match(r"^Chapter (\d+):\s*(.*)$", heading)
        if m:  # the design shows "CHAPTER n" above the name rather than one line
            return f"chapter {m.group(1)}" in flat and norm(m.group(2)) in flat
        return norm(heading) in flat

    missing = [h for h in headings if not present(h)]
    if missing:
        problems.append(f"{len(missing)} heading(s) from the markdown are missing, e.g. {missing[:3]}")

    n_examples = len(re.findall(r"^\*\*Example \d+\*\*$", md, re.M))
    got_examples = len(re.findall(r"EXAMPLE \d+", full))
    got_walks = len(re.findall(r"Walk through it", full))
    if got_examples != n_examples:
        problems.append(f"{got_examples} worked examples in the PDF, {n_examples} in the markdown")
    if got_walks != n_examples:
        problems.append(f"{got_walks} walk-throughs in the PDF, {n_examples} examples in the markdown")

    cover = norm(pages[0])
    if norm(title) not in cover:
        problems.append(f"cover does not show the title '{title}'")
    if "trivefoundation" not in cover:
        problems.append("cover does not name Trivefoundation")
    if not doc[0].get_images():
        problems.append("cover has no logo image")

    for number, page in enumerate(doc, start=1):
        if number == 1:
            continue
        width = page.rect.width
        for x0, y0, x1, y1, *_ in page.get_text("blocks"):
            if x0 < SIDE_MARGIN_PT - 1 or x1 > width - SIDE_MARGIN_PT + 1:
                problems.append(f"page {number}: text outside the margins (x {x0:.0f} to {x1:.0f} of {width:.0f})")
                break

    if "Trivefoundation" not in (doc.metadata.get("title") or ""):
        problems.append(f"document title metadata is '{doc.metadata.get('title')}'")
    if not problems:
        print(f"  ok   {stem}.pdf  ({len(doc)} pages, {n_examples} examples, {len(headings)} headings, fonts {sorted(fonts)})")
    return problems


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    failed = False
    for stem, title in BOOKS:
        problems = check_book(stem, title, folder)
        for p in problems:
            failed = True
            print(f"  FAIL {stem}.pdf: {p}")
    if failed:
        raise SystemExit(1)
    print("Study guide PDFs passed.")


if __name__ == "__main__":
    main()
