"""Builds the Trivefoundation logo set as plain-path SVGs (no font dependency at display time).

Lettering : outlines derived from Fredoka (SIL Open Font License 1.1) - weight 700 / width 106 for TRIVE,
            weight 500 for 'foundation'.
Figure    : hand-drawn cubic Beziers following the logo direction supplied by the client.
Knock-out : the figure is separated from the R and the V by a clear gap (KNOCK), cut out of the letters
            geometrically so the logo stays transparent on any background.

Run:  python3 build_logo.py <output-dir>
Needs: fonttools, brotli, shapely, skia-pathops, cairosvg, pillow
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import bounds, glyph_to_pen
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union
import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.basePen import BasePen

NAVY = '#08365B'; GREEN = '#1C854B'; LEAF = '#45A24A'
REV_BODY = '#7DD181'; REV_DARK = '#3FAE5A'       # figure colours on navy backgrounds

CAP = 297.0; S = CAP / 700.0      # px per font unit for TRIVE (cap height 297 on a 1774-wide artboard)
WG, WD = 700, 106                 # Fredoka weight / width
BASE = 555.0; X0 = 221.0; GAP = 16.0
SLOT = 156.0                      # space kept for the figure (it replaces the letter I)
FFAM, FW, FXH = os.environ.get('FFAM','quicksand'), int(os.environ.get('FW','700')), 503.0   # 'foundation' face
FBASE = 722.0                    # baseline of 'foundation'
ROUND = float(os.environ.get('ROUND','24'))   # extra rounding of the TRIVE corners (0 = Fredoka as drawn)
KNOCK = 9.0                       # clear gap between the figure and the letters

def place(seq):
    x = X0; out = []
    for ch, gap_after in seq:
        (xmin, _, xmax, _), _adv = bounds(ch, WG, WD)
        out.append((ch, x - xmin * S, x, x + (xmax - xmin) * S))
        x += (xmax - xmin) * S + gap_after
    return out

LETTERS = place([('T', GAP), ('R', SLOT), ('V', GAP), ('E', 0)])
RIGHT = LETTERS[-1][3]
CX = (LETTERS[1][3] + LETTERS[2][2]) / 2      # centre line of the figure

# ---- figure (coordinates drawn around a centre line at x = 926) ------------------------------
HEAD = (926.0, 216.0, 43.0)
BODY = [(786,234), [(815,243),(850,262),(880,271)], [(905,278),(945,279),(969,271)],
        [(1006,259),(1040,225),(1064,196)], [(1046,240),(1006,282),(966,320)],
        [(926,358),(891,418),(879,468)], [(875,484),(873,497),(872,508)],
        [(865,482),(860,442),(862,402)], [(864,362),(871,332),(863,306)],
        [(853,280),(816,255),(786,234)]]
LEAFP = [(989,322), [(953,346),(905,396),(889,446)], [(877,484),(886,524),(932,577)],
         [(914,540),(917,500),(934,456)], [(949,416),(975,361),(989,322)]]

def shift(shape, o):
    return [(shape[0][0] + o, shape[0][1])] + [[(x + o, y) for x, y in seg] for seg in shape[1:]]

def d_of(shape):
    s = f'M{shape[0][0]:.1f},{shape[0][1]:.1f}'
    for seg in shape[1:]:
        s += 'C' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in seg)
    return s + 'Z'

def flatten(shape, n=24):
    pts = [shape[0]]; p0 = shape[0]
    for c1, c2, p3 in shape[1:]:
        for i in range(1, n + 1):
            t = i / n; u = 1 - t
            pts.append((u**3*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t**3*p3[0],
                        u**3*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t**3*p3[1]))
        p0 = p3
    return pts

def figure(cx):
    o = cx - 926.0
    return (HEAD[0] + o, HEAD[1], HEAD[2]), shift(BODY, o), shift(LEAFP, o)

class FlattenPen(BasePen):
    """Collects glyph contours as polylines (curves sampled finely)."""
    def __init__(self): super().__init__(None); self.contours = []
    def _moveTo(self, p): self.contours.append([p])
    def _lineTo(self, p): self.contours[-1].append(p)
    def _curveToOne(self, c1, c2, p3):
        p0 = self.contours[-1][-1]
        for i in range(1, 17):
            t = i / 16; u = 1 - t
            self.contours[-1].append((u**3*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t**3*p3[0],
                                      u**3*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t**3*p3[1]))
    def _closePath(self): pass

def poly_d(geom):
    """Shapely geometry -> SVG path data (straight segments; sampled finely enough to read as curves)."""
    geoms = [geom] if geom.geom_type == 'Polygon' else list(geom.geoms)
    out = []
    for g in geoms:
        for ring in [g.exterior] + list(g.interiors):
            xy = list(ring.coords)[:-1]
            out.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in xy) + 'Z')
    return ''.join(out)

def figure_blob(grow):
    head, body, leaf = figure(CX)
    return unary_union([Point(head[0], head[1]).buffer(head[2], 64),
                        Polygon(flatten(body)).buffer(0), Polygon(flatten(leaf)).buffer(0)]).buffer(grow, 24)

def letters_path(knock=True):
    """TRIVE as one path: Fredoka outlines, corners softened by ROUND, figure (grown by KNOCK) cut out."""
    shape = None
    for ch, dx, _, _ in LETTERS:
        raw = pathops.Path(); glyph_to_pen(ch, WG, WD, S, dx, BASE, raw.getPen())
        raw.simplify(fix_winding=True)                             # merge the variable font's overlapping strokes
        fp = FlattenPen(); raw.draw(fp)
        g = None
        for c in fp.contours:
            p = Polygon(c).buffer(0)
            g = p if g is None else g.symmetric_difference(p)      # counters become holes
        if ROUND > 0:
            g = g.buffer(-ROUND, 32).buffer(ROUND, 32)             # round the outer corners
            g = g.buffer(ROUND * 0.3, 32).buffer(-ROUND * 0.3, 32) # ease the inner corners
        shape = g if shape is None else shape.union(g)
    if knock: shape = shape.difference(figure_blob(KNOCK))
    return poly_d(shape.simplify(0.12))

def word_foundation(left, right, baseline=FBASE, xh=87.0, wght=FW, fam=FFAM):
    s = xh / FXH; word = 'foundation'
    ext = [bounds(ch, wght, 100, fam)[0] for ch in word]
    total = sum((b[2] - b[0]) * s for b in ext)
    gap = (right - left - total) / (len(word) - 1)
    x = left; sp = SVGPathPen(None, ntos=lambda v: ('%.1f' % v).rstrip('0').rstrip('.'))
    for ch, b in zip(word, ext):
        glyph_to_pen(ch, wght, 100, s, x - b[0] * s, baseline, sp, fam); x += (b[2] - b[0]) * s + gap
    return sp.getCommands()

PALETTES = {
    'primary':    (NAVY, LEAF, GREEN),
    'reversed':   ('#FFFFFF', REV_BODY, REV_DARK),
    'mono-navy':  (NAVY, NAVY, NAVY),
    'mono-white': ('#FFFFFF', '#FFFFFF', '#FFFFFF'),
}
TRIVE_D = letters_path(True)
FOUND_D = word_foundation(X0, RIGHT)

def figure_svg(cx, c_body, c_dark):
    head, body, leaf = figure(cx)
    return (f'<path fill="{c_body}" d="{d_of(body)}"/>'
            f'<circle fill="{c_dark}" cx="{head[0]:.1f}" cy="{head[1]:.0f}" r="{head[2]:.0f}"/>'
            f'<path fill="{c_dark}" d="{d_of(leaf)}"/>')

def lockup(variant='primary', with_word=True, pad=0, title='Trivefoundation'):
    c_text, c_body, c_dark = PALETTES[variant]
    top = 173; bottom = FBASE + 8 if with_word else 577
    x0 = X0 - pad; y0 = top - pad; w = RIGHT - X0 + 2 * pad; h = bottom - top + 2 * pad
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{title}">',
             f'<title>{title}</title>',
             f'<path fill="{c_text}" d="{TRIVE_D}"/>']
    if with_word: parts.append(f'<path fill="{c_text}" d="{FOUND_D}"/>')
    parts.append(figure_svg(CX, c_body, c_dark)); parts.append('</svg>')
    return '\n'.join(parts)

def mark(variant='primary', tile=None, title='Trivefoundation'):
    """Figure only. tile = background colour for a rounded-square app icon / favicon, or None."""
    c_text, c_body, c_dark = PALETTES[variant]
    size = 452.0; cx = 926.0; cy = 375.0
    x0 = cx - size / 2; y0 = cy - size / 2
    bg = f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{size:.0f}" height="{size:.0f}" rx="{size*0.22:.0f}" fill="{tile}"/>' if tile else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {size:.0f} {size:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{bg}{figure_svg(926.0, c_body, c_dark)}</svg>')

FILES = {
    'logo.svg':              lambda: lockup('primary'),
    'logo-white.svg':        lambda: lockup('reversed'),
    'logo-mono-navy.svg':    lambda: lockup('mono-navy'),
    'logo-mono-white.svg':   lambda: lockup('mono-white'),
    'logo-wordmark.svg':     lambda: lockup('primary', with_word=False),
    'logo-wordmark-white.svg': lambda: lockup('reversed', with_word=False),
    'logo-mark.svg':         lambda: mark('primary'),
    'logo-mark-white.svg':   lambda: mark('reversed'),
    'favicon.svg':           lambda: mark('reversed', tile=NAVY),
}

if __name__ == '__main__':
    import cairosvg
    out = sys.argv[1] if len(sys.argv) > 1 else 'out'
    os.makedirs(out, exist_ok=True)
    for name, fn in FILES.items():
        open(os.path.join(out, name), 'w').write(fn())
    # PNG exports (transparent) for Word, social and touch icons
    cairosvg.svg2png(bytestring=lockup('primary', pad=0).encode(), write_to=os.path.join(out, 'logo-1600.png'), output_width=1600)
    cairosvg.svg2png(bytestring=lockup('reversed', pad=0).encode(), write_to=os.path.join(out, 'logo-white-1600.png'), output_width=1600)
    cairosvg.svg2png(bytestring=mark('reversed', tile=NAVY).encode(), write_to=os.path.join(out, 'apple-touch-icon.png'), output_width=180)
    cairosvg.svg2png(bytestring=mark('reversed', tile=NAVY).encode(), write_to=os.path.join(out, 'icon-512.png'), output_width=512)
    print('letters', [(c, round(a), round(b)) for c, _, a, b in LETTERS], 'right', round(RIGHT), 'cx', round(CX))
    for n in sorted(os.listdir(out)): print(f'{os.path.getsize(os.path.join(out,n)):>8}  {n}')
