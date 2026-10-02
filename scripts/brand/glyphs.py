"""Glyph outlines from Fredoka (SIL OFL 1.1). Used only to build the logo lettering;
the output SVGs contain plain paths, so the logo has no font dependency."""
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
import functools, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
FILES = {'fredoka':   os.path.join(ROOT, 'fredoka-latin-standard-normal.woff2'),    # weight + width axes
         'quicksand': os.path.join(ROOT, 'quicksand-latin-wght-normal.woff2')}

@functools.lru_cache(None)
def font(fam, wght, wdth):
    axes = {'wght': wght}
    if fam == 'fredoka': axes['wdth'] = wdth
    return instancer.instantiateVariableFont(TTFont(FILES[fam]), axes)

def _g(ch, wght, wdth, fam='fredoka'):
    f = font(fam, wght, wdth); gs = f.getGlyphSet(); return gs, gs[f.getBestCmap()[ord(ch)]]

def bounds(ch, wght, wdth, fam='fredoka'):
    gs, g = _g(ch, wght, wdth, fam); bp = BoundsPen(gs); g.draw(bp); return bp.bounds, g.width

def glyph_to_pen(ch, wght, wdth, scale, dx, dy, pen, fam='fredoka'):
    """Draw a glyph into any pen, y flipped; (dx, dy) is where the glyph origin (baseline) lands."""
    gs, g = _g(ch, wght, wdth, fam)
    rec = DecomposingRecordingPen(gs); g.draw(rec)          # flatten composite glyphs (i, etc.)
    rec.replay(TransformPen(pen, (scale, 0, 0, -scale, dx, dy)))
