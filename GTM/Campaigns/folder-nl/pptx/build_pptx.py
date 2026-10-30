"""Bouwt een folderpaneel als bewerkbare pptx (A5 staand) uit de layout.json van extract.js.

Gebruik: python3 build_pptx.py <assetmap> <uit.pptx>
Tekst en vlakken zijn bewerkbaar, iconen en logo's zijn PNG's.
"""
import json, re, os, sys
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

A, OUT = sys.argv[1], sys.argv[2]
D = json.load(open(os.path.join(A, 'layout.json')))
E = lambda v: Emu(int(round(v * 9525)))      # EMU per CSS-pixel
NAVY, WHITE = (0, 35, 51), (255, 255, 255)
ALIGN = {'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}

def rgba(s):
    n = [float(x) for x in re.findall(r'[\d.]+', s)]
    return n[:3], (n[3] if len(n) > 3 else 1.0)

def solid(s, base):
    """rgba op de ondergrond omrekenen naar een vaste kleur; pptx kent hier geen transparantie."""
    (r, g, b), a = rgba(s)
    return RGBColor(*[round(c * a + o * (1 - a)) for c, o in zip((r, g, b), base)])

# ondergrond: wit binnen een witte kaart, anders navy
whites = [x for x in D['shapes'] if rgba(x['bg']) == ([255, 255, 255], 1.0)]
def base(x):
    cx, cy = x['x'] + x['w'] / 2, x['y'] + x['h'] / 2
    inside = any(w is not x and w['x'] <= cx <= w['x'] + w['w'] and w['y'] <= cy <= w['y'] + w['h'] for w in whites)
    return WHITE if inside else NAVY

prs = Presentation()
prs.slide_width, prs.slide_height = E(D['panel']['w']), E(D['panel']['h'])
s = prs.slides.add_slide(prs.slide_layouts[6])
s.background.fill.solid(); s.background.fill.fore_color.rgb = RGBColor(*NAVY)

for sh in D['shapes']:
    b = base(sh)
    kind = MSO_SHAPE.OVAL if sh.get('cross') else (MSO_SHAPE.ROUNDED_RECTANGLE if sh['r'] else MSO_SHAPE.RECTANGLE)
    o = s.shapes.add_shape(kind, E(sh['x']), E(sh['y']), E(sh['w']), E(sh['h']))
    o.shadow.inherit = False
    if rgba(sh['bg'])[1] == 0: o.fill.background()
    else: o.fill.solid(); o.fill.fore_color.rgb = solid(sh['bg'], b)
    if sh['bw'] and sh['bs'] != 'none':
        o.line.color.rgb = solid(sh['bc'], b); o.line.width = Pt(sh['bw'] * .75)
        if sh['bs'] == 'dashed': o.line.dash_style = MSO_LINE.DASH
    else: o.line.fill.background()
    if kind == MSO_SHAPE.ROUNDED_RECTANGLE: o.adjustments[0] = min(.5, sh['r'] / min(sh['w'], sh['h']))
    if sh.get('cross'):
        tf = o.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = '×'; r.font.size = Pt(10.5); r.font.bold = True
        r.font.color.rgb = RGBColor(*WHITE); r.font.name = 'Inter'

for ic in D['icons']:
    s.shapes.add_picture(os.path.join(A, f"{ic['id']}.png"), E(ic['x']), E(ic['y']), E(ic['w']), E(ic['h']))

for t in D['texts']:
    b = base(t)
    tb = s.shapes.add_textbox(E(t['x']), E(t['y']), E(t['w'] + 4), E(t['h']))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    lh = t['lh']; ls = float(lh[:-2]) / t['size'] if lh.endswith('px') else 1.2
    al = ALIGN.get(t['align'], PP_ALIGN.LEFT)
    p = tf.paragraphs[0]; p.line_spacing = ls; p.alignment = al
    first = True
    for run in t['runs']:
        if run.get('br'):
            p = tf.add_paragraph(); p.line_spacing = ls; p.alignment = al; first = True
            continue
        txt = run['t'].lstrip() if first else run['t']
        if first and not txt.strip(): continue
        first = False
        r = p.add_run(); r.text = txt
        r.font.name = 'League Spartan' if 'League Spartan' in run['family'] else 'Inter'
        r.font.size = Pt(run['size'] * .75); r.font.bold = int(run['weight']) >= 600
        r.font.color.rgb = solid(run['color'], b)

prs.save(OUT)
buiten = [x.shape_id for x in s.shapes if x.left < 0 or x.top < 0
          or x.left + x.width > prs.slide_width or x.top + x.height > prs.slide_height]
print(OUT, 'vormen:', len(s.shapes), 'buiten canvas:', buiten or 'geen')
