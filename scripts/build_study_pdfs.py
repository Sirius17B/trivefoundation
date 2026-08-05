#!/usr/bin/env python3
"""Render TECH_STUDY_BOOK.md and FOOTBALL_STUDY_BOOK.md into branded,
cover-paged PDFs for download from the repo and upload to the site's
Resources page. Uses the site's actual palette/typography stack
(css/style.css tokens; Georgia/Calibri as local stand-ins for the site's
Playfair Display/DM Sans web fonts, which aren't installed as local TTFs).

Usage: python3 scripts/build_study_pdfs.py
Outputs: dist/TECH_STUDY_BOOK.pdf, dist/FOOTBALL_STUDY_BOOK.pdf
"""
import os
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, PageBreak,
    Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable,
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.styles import ParagraphStyle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = 'C:/Windows/Fonts'
OUT_DIR = os.path.join(ROOT, 'dist')

# ── Brand palette, lifted straight from css/style.css :root ──
FOREST = colors.HexColor('#1A3D2B')
GREEN = colors.HexColor('#2E7D4F')
GREEN_LT = colors.HexColor('#3DB870')
GREEN_XL = colors.HexColor('#C6EDD6')
TEAL = colors.HexColor('#1B7B78')
TEAL_LT = colors.HexColor('#25A89F')
ORANGE = colors.HexColor('#E8621A')
ORANGE_LT = colors.HexColor('#F5874A')
AMBER = colors.HexColor('#D4940A')
AMBER_LT = colors.HexColor('#F5C842')
CREAM = colors.HexColor('#F8F4EE')
SAND = colors.HexColor('#EDE7DC')
WHITE = colors.white
INK = colors.HexColor('#1C2B1C')
MUTED = colors.HexColor('#5C6E5C')
BORDER = colors.HexColor('#D8E5D8')
BROWN = colors.HexColor('#6B3D1E')

PAGE_W, PAGE_H = A4
MARGIN_L, MARGIN_R = 20 * mm, 20 * mm
MARGIN_TOP, MARGIN_BOTTOM = 26 * mm, 22 * mm

pdfmetrics.registerFont(TTFont('Georgia', f'{FONT_DIR}/georgia.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Bold', f'{FONT_DIR}/georgiab.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Italic', f'{FONT_DIR}/georgiai.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-BoldItalic', f'{FONT_DIR}/georgiaz.ttf'))
pdfmetrics.registerFont(TTFont('Calibri', f'{FONT_DIR}/calibri.ttf'))
pdfmetrics.registerFont(TTFont('Calibri-Bold', f'{FONT_DIR}/calibrib.ttf'))
pdfmetrics.registerFont(TTFont('Calibri-Italic', f'{FONT_DIR}/calibrii.ttf'))

# ═══════════════════════════════════════════════════════════════
# Markdown -> inline reportlab markup
# ═══════════════════════════════════════════════════════════════

def to_hex(c):
    return '#%02X%02X%02X' % (int(c.red * 255), int(c.green * 255), int(c.blue * 255))

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<i>\1</i>', s)
    return s

# ═══════════════════════════════════════════════════════════════
# Styles
# ═══════════════════════════════════════════════════════════════

def build_styles():
    S = {}
    S['h1'] = ParagraphStyle('h1', fontName='Georgia-Bold', fontSize=20, leading=25,
                              textColor=GREEN, spaceBefore=0, spaceAfter=14)
    S['h2'] = ParagraphStyle('h2', fontName='Georgia-Bold', fontSize=13.5, leading=17,
                              textColor=FOREST, spaceBefore=16, spaceAfter=7)
    S['body'] = ParagraphStyle('body', fontName='Calibri', fontSize=9.6, leading=14.6,
                                textColor=INK, alignment=TA_JUSTIFY, spaceAfter=9)
    S['intro'] = ParagraphStyle('intro', parent=S['body'], fontSize=10, leading=15.4)
    S['list'] = ParagraphStyle('list', parent=S['body'], leftIndent=12, spaceAfter=6)
    S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=16, spaceAfter=6,
                                  bulletIndent=4, alignment=TA_LEFT)
    S['tagline'] = ParagraphStyle('tagline', fontName='Georgia-Italic', fontSize=10.5,
                                   leading=14, textColor=GREEN_XL, alignment=TA_CENTER)
    S['ex_label'] = ParagraphStyle('ex_label', fontName='Calibri-Bold', fontSize=9,
                                    leading=12, textColor=GREEN, spaceAfter=5)
    S['ex_scenario'] = ParagraphStyle('ex_scenario', fontName='Georgia-Italic', fontSize=9.8,
                                       leading=14.5, textColor=INK, spaceAfter=7)
    S['ex_option'] = ParagraphStyle('ex_option', fontName='Calibri', fontSize=8.9,
                                     leading=13, textColor=INK, spaceAfter=4, leftIndent=2)
    S['ex_walk'] = ParagraphStyle('ex_walk', fontName='Calibri', fontSize=8.7,
                                   leading=13, textColor=MUTED, spaceBefore=6)
    S['toc_chap'] = ParagraphStyle('toc_chap', fontName='Georgia-Bold', fontSize=12.5,
                                    leading=18, textColor=FOREST)
    S['toc_sub'] = ParagraphStyle('toc_sub', fontName='Calibri', fontSize=9, leading=13,
                                   textColor=MUTED, leftIndent=14)
    S['front_tagline'] = ParagraphStyle('front_tagline', fontName='Georgia-Italic', fontSize=10.5,
                                         leading=15, textColor=GREEN, alignment=TA_CENTER, spaceAfter=14)
    return S

# ═══════════════════════════════════════════════════════════════
# Markdown parsing
# ═══════════════════════════════════════════════════════════════

def parse(md_text):
    """Returns a list of block dicts. Chapters are split out explicitly so
    the builder can page-break and register TOC entries."""
    lines = [l.rstrip('\n') for l in md_text.split('\n')]
    blocks = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('# ') and not line.startswith('## '):
            heading = line[2:].strip()
            # Only a real "# Chapter N: ..." heading starts a new chapter —
            # the document's own top-of-file title ("# THE THRIVE ... BOOK")
            # is front matter, already shown on the cover page, not a chapter.
            btype = 'chapter_h1' if heading.startswith('Chapter ') else 'doctitle'
            blocks.append({'type': btype, 'text': heading})
        elif line.startswith('## '):
            blocks.append({'type': 'h2', 'text': line[3:].strip()})
        elif line == '---':
            blocks.append({'type': 'hr'})
        elif re.match(r'^\*\*Example \d+\*\*$', line):
            # Blank-line-aware scan (the source separates every element with
            # a blank line except the four options, which run consecutively)
            # rather than fixed offsets, which broke the moment spacing
            # varied even slightly.
            label = line.strip('*')
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            scenario = lines[j].strip().strip('*')
            j += 1
            options = []
            while j < n and len(options) < 4:
                lj = lines[j].strip()
                if not lj:
                    j += 1
                    continue
                if re.match(r'^[ABCD]\)', lj):
                    options.append(lj)
                    j += 1
                else:
                    break
            while j < n and not lines[j].strip():
                j += 1
            walk = lines[j].strip()
            blocks.append({'type': 'example', 'label': label, 'scenario': scenario,
                            'options': options, 'walk': walk})
            i = j
        elif re.match(r'^\d+\.\s', line):
            blocks.append({'type': 'list', 'text': line})
        elif line.startswith('- '):
            blocks.append({'type': 'bullet', 'text': line[2:].strip()})
        else:
            blocks.append({'type': 'p', 'text': line})
        i += 1
    return blocks

# ═══════════════════════════════════════════════════════════════
# Cover page + header/footer canvas painting
# ═══════════════════════════════════════════════════════════════

def draw_leaf_mark(c, cx, cy, scale, accent):
    """Abstract canopy-and-trunk mark echoing the real THRIVE logo, built
    from primitive shapes only (no SVG rasterisation dependency)."""
    c.saveState()
    c.translate(cx, cy)
    c.scale(scale, scale)
    # trunk
    c.setFillColor(BROWN)
    c.roundRect(-4, -34, 8, 22, 3, fill=1, stroke=0)
    # canopy — layered circles in the brand's leaf palette
    leaf_positions = [
        (0, 6, 22, GREEN_LT), (-16, -2, 16, GREEN), (16, -2, 16, GREEN),
        (-9, 20, 14, accent), (9, 20, 14, accent), (0, -8, 15, TEAL_LT),
    ]
    for dx, dy, r, col in leaf_positions:
        c.setFillColor(col)
        c.circle(dx, dy, r, fill=1, stroke=0)
    c.restoreState()

def cover_page(subtitle, accent, edition_label):
    def _draw(c, doc):
        c.saveState()
        c.setFillColor(FOREST)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        # decorative diagonal band
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.035))
        c.saveState()
        c.translate(0, PAGE_H * 0.62)
        c.rotate(-8)
        c.rect(-40 * mm, 0, PAGE_W + 80 * mm, 34 * mm, fill=1, stroke=0)
        c.restoreState()
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.025))
        c.saveState()
        c.translate(0, PAGE_H * 0.18)
        c.rotate(6)
        c.rect(-40 * mm, 0, PAGE_W + 80 * mm, 46 * mm, fill=1, stroke=0)
        c.restoreState()

        draw_leaf_mark(c, PAGE_W / 2, PAGE_H - 78 * mm, 1.35, accent)

        c.setFillColor(WHITE)
        c.setFont('Georgia-Bold', 15)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 106 * mm, 'THRIVE')
        c.setFillColor(accent)
        c.setFont('Calibri-Bold', 9.5)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 111.5 * mm, edition_label.upper())

        c.setFillColor(WHITE)
        c.setFont('Georgia-Bold', 30)
        title_lines = ['THE THRIVE', subtitle.upper() + ' STUDY BOOK']
        ty = PAGE_H - 132 * mm
        for tl in title_lines:
            c.drawCentredString(PAGE_W / 2, ty, tl)
            ty -= 12.5 * mm

        c.setStrokeColor(accent)
        c.setLineWidth(1.2)
        c.line(PAGE_W / 2 - 26 * mm, ty - 2 * mm, PAGE_W / 2 + 26 * mm, ty - 2 * mm)

        c.setFillColor(GREEN_XL)
        c.setFont('Georgia-Italic', 11.5)
        c.drawCentredString(PAGE_W / 2, ty - 12 * mm,
                             'A Deep-Dive Guide for the ' + subtitle + ' Challenge')

        c.setFillColor(colors.Color(1, 1, 1, alpha=0.75))
        c.setFont('Calibri', 8.5)
        tagline = 'Technology, Hard work, Resilience, Innovation, Vision, and Excellence'
        c.drawCentredString(PAGE_W / 2, 30 * mm, tagline)
        c.setFont('Calibri', 8)
        c.drawCentredString(PAGE_W / 2, 24 * mm, 'trivefoundation.netlify.app')
        c.restoreState()
    return _draw

def toc_header_footer(running_title, accent):
    def _draw(c, doc):
        c.saveState()
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.6)
        c.line(MARGIN_L, PAGE_H - 16 * mm, PAGE_W - MARGIN_R, PAGE_H - 16 * mm)
        c.setFillColor(MUTED)
        c.setFont('Calibri', 7.6)
        c.drawString(MARGIN_L, PAGE_H - 13.6 * mm, 'THRIVE')
        c.setFillColor(accent)
        c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 13.6 * mm, running_title)

        c.setStrokeColor(BORDER)
        c.line(MARGIN_L, 14 * mm, PAGE_W - MARGIN_R, 14 * mm)
        c.setFillColor(MUTED)
        c.setFont('Calibri', 7.6)
        c.drawCentredString(PAGE_W / 2, 9.5 * mm, str(c.getPageNumber() - 1))
        c.restoreState()
    return _draw

# ═══════════════════════════════════════════════════════════════
# Flowable: worked-example box
# ═══════════════════════════════════════════════════════════════

def example_flowable(block, S, accent):
    label = block['label'].replace('Example ', 'EXAMPLE ')
    rows = [Paragraph(f'<font color="{to_hex(accent)}">&#9670;</font>&nbsp;&nbsp;{esc(label)}', S['ex_label'])]
    rows.append(Paragraph(inline(block['scenario']), S['ex_scenario']))
    letters = ['A', 'B', 'C', 'D']
    for opt in block['options']:
        m = re.match(r'^([ABCD])\)\s*(.*)$', opt)
        if m:
            letter, rest = m.group(1), m.group(2)
        else:
            letter, rest = '', opt
        rows.append(Paragraph(f'<b>{letter})</b>&nbsp; {inline(rest)}', S['ex_option']))
    walk = block['walk']
    walk = re.sub(r'^\*Walk through it:\*\s*', '', walk)
    rows.append(Paragraph(f'<b>Walk through it:</b> {inline(walk)}', S['ex_walk']))

    data = [[r] for r in rows]
    t = Table(data, colWidths=[PAGE_W - MARGIN_L - MARGIN_R - 4 * mm])
    n_rows = len(data)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SAND),
        ('BOX', (0, 0), (-1, -1), 0.9, accent),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, n_rows - 1), (-1, n_rows - 1), 11),
    ]))
    return KeepTogether([Spacer(1, 4), t, Spacer(1, 10)])

def chapter_banner(title, S, accent):
    p = Paragraph(f'<font color="white">{esc(title)}</font>',
                  ParagraphStyle('banner', fontName='Georgia-Bold', fontSize=16.5, leading=20))
    t = Table([[p]], colWidths=[PAGE_W - MARGIN_L - MARGIN_R])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), FOREST),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 11),
        ('LINEBELOW', (0, 0), (-1, -1), 2.4, accent),
    ]))
    return t

# ═══════════════════════════════════════════════════════════════
# Build
# ═══════════════════════════════════════════════════════════════

def build_pdf(md_path, out_path, subtitle, accent, edition_label, running_title):
    with open(md_path, encoding='utf-8') as f:
        text = f.read()
    blocks = parse(text)
    S = build_styles()

    # Split into: front matter (intro), then a list of chapters (title + body blocks)
    chapters = []
    intro_blocks = []
    cur = None
    for b in blocks:
        if b['type'] == 'chapter_h1':
            cur = {'title': b['text'], 'blocks': []}
            chapters.append(cur)
        elif b['type'] == 'doctitle':
            continue  # already shown on the cover page
        elif cur is None:
            intro_blocks.append(b)
        else:
            cur['blocks'].append(b)

    story = []

    # ── Front matter page(s) ──
    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())
    for b in intro_blocks:
        if b['type'] == 'h2':
            if b['text'].startswith('A Deep-Dive Guide'):
                continue  # already shown prominently on the cover page
            sty = S['h1'] if b['text'].startswith('How to use') else S['h2']
            story.append(Paragraph(esc(b['text']), sty))
        elif b['type'] in ('p', 'list'):
            txt = b['text']
            if txt.startswith('*') and txt.endswith('*') and not txt.startswith('**'):
                story.append(Paragraph(inline(txt), S['front_tagline']))
            else:
                sty = S['list'] if b['type'] == 'list' else S['intro']
                story.append(Paragraph(inline(txt), sty))
        elif b['type'] == 'bullet':
            story.append(Paragraph('&#8226;&nbsp;&nbsp;' + inline(b['text']), S['bullet']))
        elif b['type'] == 'hr':
            story.append(Spacer(1, 4))

    # ── Table of contents ──
    story.append(PageBreak())
    story.append(Paragraph('Contents', S['h1']))
    story.append(Spacer(1, 6))
    for idx, ch in enumerate(chapters, 1):
        story.append(Paragraph(esc(ch['title']), S['toc_chap']))
        subs = [b['text'] for b in ch['blocks'] if b['type'] == 'h2']
        for s in subs:
            story.append(Paragraph('&#8226;&nbsp; ' + esc(s), S['toc_sub']))
        story.append(Spacer(1, 8))

    # ── Chapters ──
    for ch in chapters:
        story.append(PageBreak())
        story.append(chapter_banner(ch['title'], S, accent))
        story.append(Spacer(1, 12))
        for b in ch['blocks']:
            if b['type'] == 'h2':
                story.append(Paragraph(esc(b['text']), S['h2']))
            elif b['type'] == 'p':
                txt = b['text']
                story.append(Paragraph(inline(txt), S['body']))
            elif b['type'] == 'list':
                story.append(Paragraph(inline(b['text']), S['list']))
            elif b['type'] == 'bullet':
                story.append(Paragraph('&#8226;&nbsp;&nbsp;' + inline(b['text']), S['bullet']))
            elif b['type'] == 'example':
                story.append(example_flowable(b, S, accent))
            elif b['type'] == 'hr':
                story.append(Spacer(1, 2))

    # ── Document assembly with two page templates ──
    doc = BaseDocTemplate(out_path, pagesize=A4,
                           leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                           topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
                           title=f'THRIVE {subtitle} Study Book', author='TriveFoundation')
    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id='cover', leftPadding=0, rightPadding=0,
                         topPadding=0, bottomPadding=0)
    body_frame = Frame(MARGIN_L, MARGIN_BOTTOM, PAGE_W - MARGIN_L - MARGIN_R,
                        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id='body')
    doc.addPageTemplates([
        PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_page(subtitle, accent, edition_label)),
        PageTemplate(id='Body', frames=[body_frame], onPage=toc_header_footer(running_title, accent)),
    ])
    doc.build(story)
    print(f'Wrote {out_path}')

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    build_pdf(os.path.join(ROOT, 'TECH_STUDY_BOOK.md'),
              os.path.join(OUT_DIR, 'TECH_STUDY_BOOK.pdf'),
              subtitle='Tech', accent=TEAL_LT, edition_label='Tech Challenge Edition',
              running_title='Tech Study Book')
    build_pdf(os.path.join(ROOT, 'FOOTBALL_STUDY_BOOK.md'),
              os.path.join(OUT_DIR, 'FOOTBALL_STUDY_BOOK.pdf'),
              subtitle='Football', accent=AMBER_LT, edition_label='Football Challenge Edition',
              running_title='Football Study Book')

if __name__ == '__main__':
    main()
