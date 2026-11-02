#!/usr/bin/env python3
"""Render TECH_STUDY_BOOK.md and FOOTBALL_STUDY_BOOK.md as branded PDFs.

Usage:   python3 scripts/build_study_pdfs.py
Output:  dist/TECH_STUDY_BOOK.pdf, dist/FOOTBALL_STUDY_BOOK.pdf  (dist/ is gitignored)
Needs:   pip install reportlab fonttools brotli pymupdf pillow
Then:    python3 scripts/check_study_pdfs.py

The brand comes from the site, not from this file:
  - colours are read from the :root tokens in css/style.css
  - logos are the files in assets/
  - Fredoka (headings) and Lexend (body) are the site's own variable web fonts
    in assets/fonts/, cut into the static weights ReportLab needs
See BRAND.md for the rules (names, logo use, colour, type).
"""
import re
import sys
from pathlib import Path

from fontTools.ttLib import TTFont as SourceFont
from fontTools.varLib import instancer
from PIL import Image
import fitz  # PyMuPDF: renders the logo mark from SVG, nothing else
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
CACHE = DIST / "cache"
PAGE_W, PAGE_H = A4
MARGIN_X = 22 * mm
TEXT_W = PAGE_W - 2 * MARGIN_X
ORG = "Trivefoundation"
ORG_LINE = "Equipping young Nigerians through technology, sport and inspiration."
SITE = "trivefoundation.netlify.app"

# Pillar colours: Tech = green, Football = navy (BRAND.md section 3).
BOOKS = {
    "TECH_STUDY_BOOK": {"name": "Tech", "pillar": "green", "challenge": "Tech Challenge"},
    "FOOTBALL_STUDY_BOOK": {"name": "Football", "pillar": "navy", "challenge": "Football Challenge"},
}


class BuildError(Exception):
    pass


# ───────────────────────── brand: colours ─────────────────────────

def load_tokens():
    css = (ROOT / "css/style.css").read_text(encoding="utf-8")
    root_block = css[css.index(":root"):]
    root_block = root_block[:root_block.index("}")]
    return dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", root_block))


TOKENS = load_tokens()


def tok(name):
    if name not in TOKENS:
        raise BuildError(f"colour token --{name} not found in css/style.css")
    return TOKENS[name]


def col(name):
    return colors.HexColor(tok(name))


# ───────────────────────── brand: fonts ─────────────────────────
# (file, weight, family, style) — weights follow BRAND.md: Fredoka 600/700, Lexend 400 + 500/600 for emphasis.
FONT_CUTS = [
    ("fredoka-latin-wght.woff2", 600, "Fredoka", "SemiBold"),
    ("fredoka-latin-wght.woff2", 700, "Fredoka", "Bold"),
    ("lexend-latin-wght.woff2", 400, "Lexend", "Regular"),
    ("lexend-latin-wght.woff2", 500, "Lexend", "Medium"),
    ("lexend-latin-wght.woff2", 600, "Lexend", "SemiBold"),
]
# Used only for characters the brand fonts lack (the Naira sign). Calibri is
# the brand's own document font (BRAND.md section 4).
FALLBACK_CANDIDATES = [
    "C:/Windows/Fonts/calibri.ttf", "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def cut_static_font(src_name, weight, family, style):
    out = CACHE / f"{family}-{style}.ttf"
    src = ROOT / "assets/fonts" / src_name
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    font = SourceFont(src)
    font.flavor = None
    static = instancer.instantiateVariableFont(font, {"wght": weight}, inplace=False)
    names = static["name"]
    full, ps = f"{family} {style}", f"{family}-{style}"
    for name_id, value in ((1, family), (2, style), (3, ps), (4, full), (6, ps)):
        names.removeNames(nameID=name_id)
        names.setName(value, name_id, 3, 1, 0x409)
    for name_id in (16, 17, 25):
        names.removeNames(nameID=name_id)
    static.save(out)
    return out


def register_fonts():
    CACHE.mkdir(parents=True, exist_ok=True)
    for src, weight, family, style in FONT_CUTS:
        pdfmetrics.registerFont(TTFont(f"{family}-{style}", str(cut_static_font(src, weight, family, style))))
    registerFontFamily("Lexend", normal="Lexend-Regular", bold="Lexend-SemiBold",
                       italic="Lexend-Medium", boldItalic="Lexend-SemiBold")
    covered = set(pdfmetrics.getFont("Lexend-Regular").face.charToGlyph) & \
        set(pdfmetrics.getFont("Fredoka-SemiBold").face.charToGlyph)
    fallback = next((p for p in FALLBACK_CANDIDATES if Path(p).exists()), None)
    fallback_cover = set()
    if fallback:
        pdfmetrics.registerFont(TTFont("Fallback", fallback))
        fallback_cover = set(pdfmetrics.getFont("Fallback").face.charToGlyph)
    return covered, fallback_cover


COVERED, FALLBACK_COVERED = register_fonts()


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def shape(markup):
    """Route any character the brand fonts lack to the fallback font, or fail.
    Never lets a missing glyph print as an empty box."""
    out = []
    for ch in markup:
        code = ord(ch)
        if code < 127 or code in COVERED:
            out.append(ch)
        elif code in FALLBACK_COVERED:
            out.append(f'<font name="Fallback">{ch}</font>')
        else:
            raise BuildError(f"no font has U+{code:04X} ({ch!r}); add a fallback font or change the text")
    return "".join(out)


def plain(s):
    return shape(esc(s))


def inline(s):
    """Markdown emphasis -> brand emphasis. Lexend and Fredoka have no italics,
    so *emphasis* is carried by weight and colour instead."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", rf'<font name="Lexend-Medium" color="{tok("navy")}">\1</font>', s)
    return shape(s)


# ───────────────────────── brand: images ─────────────────────────

def watermark_png(alpha):
    """The logo mark (white) as a faint transparent PNG for the cover panel."""
    out = CACHE / "mark-watermark.png"
    svg = ROOT / "assets/logo-mark-white.svg"
    if out.exists() and out.stat().st_mtime >= svg.stat().st_mtime:
        return out
    page = fitz.open(svg)[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(8, 8), alpha=True)
    tmp = CACHE / "mark-raw.png"
    pix.save(tmp)
    img = Image.open(tmp).convert("RGBA")
    img.putalpha(img.getchannel("A").point(lambda a: int(a * alpha)))
    img.save(out)
    return out


LOGO_COLOUR = str(ROOT / "assets/logo-1600.png")
LOGO_RATIO = 674 / 1600


# ───────────────────────── styles ─────────────────────────

def styles():
    ink, muted, navy, deep = col("ink"), col("muted"), col("navy"), col("green-deep")
    S = {}
    S["body"] = ParagraphStyle("body", fontName="Lexend-Regular", fontSize=9.4, leading=15.6,
                               textColor=ink, spaceAfter=8.5)
    S["lead"] = ParagraphStyle("lead", parent=S["body"], fontName="Lexend-Medium", fontSize=10,
                               textColor=deep, spaceAfter=12)
    S["h1"] = ParagraphStyle("h1", fontName="Fredoka-SemiBold", fontSize=23, leading=27,
                             textColor=navy, spaceAfter=14)
    S["h2"] = ParagraphStyle("h2", fontName="Fredoka-SemiBold", fontSize=14, leading=18,
                             textColor=navy, spaceBefore=17, spaceAfter=6, keepWithNext=1)
    S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=15, bulletIndent=3,
                                 bulletFontName="Lexend-SemiBold", bulletFontSize=9.4,
                                 bulletColor=deep, spaceAfter=6)
    S["number"] = ParagraphStyle("number", parent=S["body"], leftIndent=20, bulletIndent=0,
                                 bulletFontName="Fredoka-SemiBold", bulletFontSize=10,
                                 bulletColor=deep, spaceAfter=7)
    S["band_eyebrow"] = ParagraphStyle("band_eyebrow", fontName="Lexend-SemiBold", fontSize=7.8,
                                       leading=11, textColor=colors.white, spaceAfter=3)
    S["band_title"] = ParagraphStyle("band_title", fontName="Fredoka-SemiBold", fontSize=21,
                                     leading=25, textColor=colors.white)
    S["toc_chapter"] = ParagraphStyle("toc_chapter", fontName="Fredoka-SemiBold", fontSize=12.5,
                                      leading=17, textColor=navy, spaceBefore=9, keepWithNext=1)
    S["toc_sub"] = ParagraphStyle("toc_sub", fontName="Lexend-Regular", fontSize=8.3, leading=12.6,
                                  textColor=muted, leftIndent=13, bulletIndent=3,
                                  bulletFontName="Lexend-SemiBold", bulletColor=col("leaf"))
    S["ex_label"] = ParagraphStyle("ex_label", fontName="Lexend-SemiBold", fontSize=7.6, leading=11,
                                   textColor=deep, spaceAfter=3)
    S["ex_scenario"] = ParagraphStyle("ex_scenario", fontName="Lexend-Medium", fontSize=9.6, leading=15,
                                      textColor=navy, spaceAfter=5)
    S["ex_option"] = ParagraphStyle("ex_option", fontName="Lexend-Regular", fontSize=8.8, leading=13.6,
                                    textColor=ink, leftIndent=17, bulletIndent=0,
                                    bulletFontName="Fredoka-SemiBold", bulletFontSize=9.5,
                                    bulletColor=deep, spaceAfter=3.5)
    S["ex_walk"] = ParagraphStyle("ex_walk", fontName="Lexend-Regular", fontSize=8.7, leading=13.8,
                                  textColor=ink)
    return S


# ───────────────────────── markdown ─────────────────────────

def parse(md_text):
    """Blocks: chapter_h1, doctitle, h2, hr, example, list, bullet, p."""
    lines = md_text.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("# ") and not line.startswith("## "):
            heading = line[2:].strip()
            blocks.append({"type": "chapter_h1" if heading.startswith("Chapter ") else "doctitle", "text": heading})
        elif line.startswith("## "):
            blocks.append({"type": "h2", "text": line[3:].strip()})
        elif line == "---":
            blocks.append({"type": "hr"})
        elif re.match(r"^\*\*Example \d+\*\*$", line):
            # The source puts a blank line between elements except the four
            # consecutive options, so scan by content, not by fixed offsets.
            number = int(re.search(r"\d+", line).group())
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            scenario = lines[j].strip().strip("*")
            j += 1
            options = []
            while j < n and len(options) < 4:
                lj = lines[j].strip()
                if not lj:
                    j += 1
                    continue
                if not re.match(r"^[ABCD]\)", lj):
                    break
                options.append(lj)
                j += 1
            while j < n and not lines[j].strip():
                j += 1
            if len(options) != 4:
                raise BuildError(f"example {number}: expected 4 options, found {len(options)}")
            blocks.append({"type": "example", "number": number, "scenario": scenario,
                           "options": options, "walk": lines[j].strip()})
            i = j
        elif re.match(r"^\d+\.\s", line):
            blocks.append({"type": "list", "text": line})
        elif line.startswith("- "):
            blocks.append({"type": "bullet", "text": line[2:].strip()})
        else:
            blocks.append({"type": "p", "text": line})
        i += 1
    return blocks


def split_book(blocks):
    intro, chapters, cur = [], [], None
    for b in blocks:
        if b["type"] == "chapter_h1":
            cur = {"title": b["text"], "blocks": []}
            chapters.append(cur)
        elif b["type"] == "doctitle":
            continue
        elif cur is None:
            intro.append(b)
        else:
            cur["blocks"].append(b)
    return intro, chapters


# ───────────────────────── flowables ─────────────────────────

def heading2(text, S):
    m = re.match(r"^(\d+\.\d+)\s+(.*)$", text)
    if m:
        return Paragraph(f'<font color="{tok("green-deep")}">{plain(m.group(1))}</font>&nbsp;&nbsp;{plain(m.group(2))}', S["h2"])
    return Paragraph(plain(text), S["h2"])


def chapter_band(title, pillar, S):
    m = re.match(r"^Chapter (\d+):\s*(.*)$", title)
    eyebrow, name = (f"CHAPTER {m.group(1)}", m.group(2)) if m else ("", title)
    cell = [Paragraph(eyebrow, S["band_eyebrow"]), Paragraph(plain(name), S["band_title"])]
    t = Table([[cell]], colWidths=[TEXT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), col(pillar)),
        ("ROUNDEDCORNERS", [10, 10, 10, 10]),
        ("LEFTPADDING", (0, 0), (-1, -1), 18), ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 15), ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
    ]))
    return t


def example_card(b, S):
    rows = [[Paragraph(f"EXAMPLE {b['number']}", S["ex_label"])],
            [Paragraph(inline(b["scenario"]), S["ex_scenario"])]]
    for opt in b["options"]:
        letter, rest = re.match(r"^([ABCD])\)\s*(.*)$", opt).groups()
        rows.append([Paragraph(inline(rest), S["ex_option"], bulletText=f"{letter})")])
    walk = re.sub(r"^\*Walk through it:\*\s*", "", b["walk"])
    label = f'<font name="Lexend-SemiBold" color="{tok("green-deep")}">Walk through it</font>'
    rows.append([Paragraph(f"{label}&nbsp;&nbsp;{inline(walk)}", S["ex_walk"])])
    last = len(rows) - 1
    t = Table(rows, colWidths=[TEXT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, last - 1), colors.white),
        ("BACKGROUND", (0, last), (-1, last), col("mint")),
        ("BOX", (0, 0), (-1, -1), 0.8, col("line")),
        ("ROUNDEDCORNERS", [9, 9, 9, 9]),
        ("LEFTPADDING", (0, 0), (-1, -1), 15), ("RIGHTPADDING", (0, 0), (-1, -1), 15),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ("TOPPADDING", (0, 0), (-1, 0), 13),
        ("TOPPADDING", (0, last), (-1, last), 11), ("BOTTOMPADDING", (0, last), (-1, last), 13),
        ("BOTTOMPADDING", (0, last - 1), (-1, last - 1), 9),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 11)])


def render_blocks(blocks, S, pillar, story, first_h2_as_h1=False):
    for b in blocks:
        kind = b["type"]
        if kind == "h2":
            story.append(heading2(b["text"], S))
        elif kind == "p":
            text = b["text"]
            whole_emphasis = text.startswith("*") and text.endswith("*") and not text.startswith("**")
            story.append(Paragraph(inline(text), S["lead"] if whole_emphasis else S["body"]))
        elif kind == "list":
            number, rest = re.match(r"^(\d+)\.\s+(.*)$", b["text"]).groups()
            story.append(Paragraph(inline(rest), S["number"], bulletText=f"{number}."))
        elif kind == "bullet":
            story.append(Paragraph(inline(b["text"]), S["bullet"], bulletText="\u2022"))
        elif kind == "example":
            story.append(example_card(b, S))
        elif kind == "hr":
            story.append(Spacer(1, 2))


# ───────────────────────── pages ─────────────────────────

def tracked(c, text, x, y, font, size, colour, space=1.4, align="left"):
    width = pdfmetrics.stringWidth(text, font, size) + space * (len(text) - 1)
    if align == "right":
        x -= width
    # Character spacing is part of the PDF graphics state and outlives the text
    # object, so it must be confined or every later line gets stretched too.
    c.saveState()
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColor(colour)
    t.setCharSpace(space)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()


def cover_drawer(cfg, title, chapters, n_examples):
    pillar = col(cfg["pillar"])
    on_navy = cfg["pillar"] == "navy"

    def draw(c, doc):
        c.saveState()
        c.setFillColor(col("paper"))
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

        logo_w = 62 * mm
        logo_h = logo_w * LOGO_RATIO
        c.drawImage(LOGO_COLOUR, MARGIN_X, PAGE_H - 20 * mm - logo_h, logo_w, logo_h, mask="auto")
        tracked(c, "STUDY GUIDE", PAGE_W - MARGIN_X, PAGE_H - 20 * mm - logo_h / 2 - 2, "Lexend-SemiBold", 8,
                col("green-deep"), 1.8, "right")

        top, bottom = 232 * mm, 116 * mm
        c.setFillColor(pillar)
        c.rect(0, bottom, PAGE_W, top - bottom, fill=1, stroke=0)
        c.saveState()
        p = c.beginPath()
        p.rect(0, bottom, PAGE_W, top - bottom)
        c.clipPath(p, stroke=0, fill=0)
        mark_h = 150 * mm
        mark_w = mark_h * 0.78
        c.drawImage(str(watermark_png(0.13)), PAGE_W - mark_w + 14 * mm, bottom - 6 * mm, mark_w, mark_h,
                    mask="auto", preserveAspectRatio=True)
        c.restoreState()

        tracked(c, cfg["challenge"].upper(), MARGIN_X, top - 20 * mm, "Lexend-SemiBold", 9.5, colors.white, 2)
        c.setFillColor(col("sun"))
        c.rect(MARGIN_X, top - 26 * mm, 22 * mm, 1.8 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Fredoka-Bold", 46)
        c.drawString(MARGIN_X, top - 52 * mm, cfg["name"])
        c.drawString(MARGIN_X, top - 70 * mm, "Study Book")
        c.setFont("Lexend-Regular", 12.5)
        c.drawString(MARGIN_X, top - 88 * mm, f"A deep-dive guide for the {cfg['challenge']}")
        c.setFont("Lexend-Regular", 10)
        c.setFillColor(col("leaf-lt") if on_navy else colors.white)
        c.drawString(MARGIN_X, top - 97 * mm, "Concepts explained properly, then practised on worked examples.")

        tracked(c, "INSIDE", MARGIN_X, 104 * mm, "Lexend-SemiBold", 8, col("green-deep"), 1.8)
        c.setFont("Lexend-Regular", 8.5)
        c.setFillColor(col("muted"))
        c.drawRightString(PAGE_W - MARGIN_X, 104 * mm,
                          f"{len(chapters)} chapters \u00b7 {n_examples} worked examples")
        y = 95 * mm
        for number, chapter in enumerate(chapters, start=1):
            name = re.sub(r"^Chapter \d+:\s*", "", chapter["title"])
            c.setFont("Fredoka-SemiBold", 12)
            c.setFillColor(col("green-deep"))
            c.drawString(MARGIN_X, y, f"{number:02d}")
            c.setFillColor(col("navy"))
            c.drawString(MARGIN_X + 11 * mm, y, shape_plain(name))
            y -= 7 * mm

        c.setStrokeColor(col("line"))
        c.setLineWidth(0.8)
        c.line(MARGIN_X, 31 * mm, PAGE_W - MARGIN_X, 31 * mm)
        c.setFont("Fredoka-SemiBold", 11)
        c.setFillColor(col("navy"))
        c.drawString(MARGIN_X, 23.5 * mm, ORG)
        c.setFont("Lexend-Regular", 7.6)
        c.setFillColor(col("muted"))
        c.drawString(MARGIN_X, 18 * mm, ORG_LINE)
        c.drawRightString(PAGE_W - MARGIN_X, 23.5 * mm, SITE)
        c.restoreState()
    return draw


def shape_plain(s):
    """Canvas text can't take markup; just refuse characters the font lacks."""
    for ch in s:
        if ord(ch) >= 127 and ord(ch) not in COVERED:
            raise BuildError(f"cover text has U+{ord(ch):04X} which the brand fonts lack")
    return s


class NumberedCanvas(pdfcanvas.Canvas):
    """Draws the running header and footer once the total page count is known."""
    chrome = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pages = []

    def showPage(self):
        self._pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._pages)
        for number, state in enumerate(self._pages, start=1):
            self.__dict__.update(state)
            if number > 1:
                self.chrome(self, number, total)
            super().showPage()
        super().save()


def chrome_drawer(title):
    def draw(c, number, total):
        c.saveState()
        logo_w = 26 * mm
        logo_h = logo_w * LOGO_RATIO
        c.drawImage(LOGO_COLOUR, MARGIN_X, PAGE_H - 11 * mm - logo_h, logo_w, logo_h, mask="auto")
        c.setFont("Lexend-Regular", 7.6)
        c.setFillColor(col("muted"))
        c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 17.5 * mm, title)
        c.setStrokeColor(col("line"))
        c.setLineWidth(0.7)
        c.line(MARGIN_X, PAGE_H - 25 * mm, PAGE_W - MARGIN_X, PAGE_H - 25 * mm)
        c.line(MARGIN_X, 17 * mm, PAGE_W - MARGIN_X, 17 * mm)
        c.drawString(MARGIN_X, 11.5 * mm, f"{ORG} \u00b7 {title}")
        c.drawRightString(PAGE_W - MARGIN_X, 11.5 * mm, f"Page {number} of {total}")
        c.restoreState()
    return draw


# ───────────────────────── build ─────────────────────────

def build(stem):
    cfg = BOOKS[stem]
    title = f"{cfg['name']} Study Book"
    S = styles()
    intro, chapters = split_book(parse((ROOT / f"{stem}.md").read_text(encoding="utf-8")))
    n_examples = sum(1 for ch in chapters for b in ch["blocks"] if b["type"] == "example")

    story = [NextPageTemplate("Body"), PageBreak()]
    # Front matter: the book's own "How to use this book" page.
    for b in intro:
        if b["type"] == "h2":
            if b["text"].startswith("A Deep-Dive Guide"):
                continue  # already on the cover
            story.append(Paragraph(plain(b["text"]), S["h1"] if b["text"].startswith("How to use") else S["h2"]))
        else:
            render_blocks([b], S, cfg["pillar"], story)

    story += [PageBreak(), Paragraph("Contents", S["h1"])]
    for number, chapter in enumerate(chapters, start=1):
        name = re.sub(r"^Chapter \d+:\s*", "", chapter["title"])
        story.append(Paragraph(f'<font color="{tok("green-deep")}">{number:02d}</font>&nbsp;&nbsp;{plain(name)}', S["toc_chapter"]))
        for sub in (b["text"] for b in chapter["blocks"] if b["type"] == "h2"):
            story.append(Paragraph(plain(sub), S["toc_sub"], bulletText="\u2022"))

    for chapter in chapters:
        story += [PageBreak(), chapter_band(chapter["title"], cfg["pillar"], S), Spacer(1, 10)]
        render_blocks(chapter["blocks"], S, cfg["pillar"], story)

    DIST.mkdir(exist_ok=True)
    out = DIST / f"{stem}.pdf"
    doc = BaseDocTemplate(str(out), pagesize=A4, title=f"{ORG} {title}", author=ORG,
                          subject=f"Study guide for the {cfg['challenge']}", creator=f"{ORG} study guide builder")
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[Frame(0, 0, PAGE_W, PAGE_H, id="cover", leftPadding=0, rightPadding=0,
                                               topPadding=0, bottomPadding=0)],
                     onPage=cover_drawer(cfg, title, chapters, n_examples)),
        PageTemplate(id="Body", frames=[Frame(MARGIN_X, 22 * mm, TEXT_W, PAGE_H - 32 * mm - 22 * mm, id="body",
                                              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)]),
    ])
    canvas_cls = type("BrandCanvas", (NumberedCanvas,), {"chrome": staticmethod(chrome_drawer(title))})
    doc.build(story, canvasmaker=canvas_cls)
    return out


def main():
    for stem in BOOKS:
        print(f"Wrote {build(stem)}")


if __name__ == "__main__":
    try:
        main()
    except BuildError as e:
        sys.exit(f"Build failed: {e}")
