"""Bouwt de 'Eigen model'-pagina van folder v5 als bewerkbare pptx (A5 staand).

Posities, tekst en kleuren komen uit assets/layout.json, dat uit folder-v5.html wordt
gehaald. Zo lopen de folder en de pptx niet uit elkaar. Tekst en vlakken zijn bewerkbaar,
iconen en logo's zijn PNG's.
"""
import json, re, os
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'assets/layout.json')))
PXE = 9525                                  # EMU per CSS-pixel
E = lambda v: Emu(int(round(v * PXE)))
NAVY = (0, 35, 51)

def rgba(s):
    n = [float(x) for x in re.findall(r'[\d.]+', s)]
    return n[:3], (n[3] if len(n) > 3 else 1.0)

def solid(s, base=NAVY):
    """rgba op navy omrekenen naar een vaste kleur, want pptx kent hier geen transparantie."""
    (r, g, b), a = rgba(s)
    mix = [round(c * a + o * (1 - a)) for c, o in zip((r, g, b), base)]
    return RGBColor(*mix)

prs = Presentation()
prs.slide_width, prs.slide_height = E(D['panel']['w']), E(D['panel']['h'])
s = prs.slides.add_slide(prs.slide_layouts[6])
s.background.fill.solid(); s.background.fill.fore_color.rgb = RGBColor(*NAVY)

# witte modelkaart: kinderen erop mengen met wit in plaats van navy
card = next(x for x in D['shapes'] if rgba(x['bg'])[0] == [255, 255, 255] and rgba(x['bg'])[1] == 1)
def on_card(x): return card['x'] <= x['x'] and x['x'] + x['w'] <= card['x'] + card['w'] + 1 and card['y'] <= x['y'] <= card['y'] + card['h']

for sh in D['shapes']:
    base = (255, 255, 255) if (sh is not card and on_card(sh)) else NAVY
    kind = MSO_SHAPE.OVAL if sh.get('cross') else (MSO_SHAPE.ROUNDED_RECTANGLE if sh['r'] else MSO_SHAPE.RECTANGLE)
    o = s.shapes.add_shape(kind, E(sh['x']), E(sh['y']), E(sh['w']), E(sh['h']))
    o.shadow.inherit = False
    if rgba(sh['bg'])[1] == 0: o.fill.background()
    else: o.fill.solid(); o.fill.fore_color.rgb = solid(sh['bg'], base)
    if sh['bw'] and sh['bs'] != 'none':
        o.line.color.rgb = solid(sh['bc'], base); o.line.width = Pt(sh['bw'] * .75)
        if sh['bs'] == 'dashed': o.line.dash_style = MSO_LINE.DASH
    else: o.line.fill.background()
    if kind == MSO_SHAPE.ROUNDED_RECTANGLE: o.adjustments[0] = sh['r'] / min(sh['w'], sh['h'])
    if sh.get('cross'):
        tf = o.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = '×'; r.font.size = Pt(10.5); r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255); r.font.name = 'Inter'

for ic in D['icons']:
    s.shapes.add_picture(os.path.join(HERE, f"assets/{ic['id']}.png"), E(ic['x']), E(ic['y']), E(ic['w']), E(ic['h']))

for t in D['texts']:
    base = (255, 255, 255) if on_card(t) else NAVY
    tb = s.shapes.add_textbox(E(t['x']), E(t['y']), E(t['w'] + 4), E(t['h']))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    head = 'League Spartan' in t['family']
    lh = t['lh']; ls = float(lh[:-2]) / t['size'] if lh.endswith('px') else 1.2
    for i, line in enumerate(t['t'].split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = ls
        r = p.add_run(); r.text = line
        r.font.name = 'League Spartan' if head else 'Inter'
        r.font.size = Pt(t['size'] * .75); r.font.bold = int(t['weight']) >= 600
        r.font.color.rgb = solid(t['color'], base)

out = os.path.join(HERE, 'eigen-model-bewerkbaar.pptx')
prs.save(out)
buiten = [x.shape_id for x in s.shapes if x.left < 0 or x.top < 0 or x.left + x.width > prs.slide_width or x.top + x.height > prs.slide_height]
print(out, 'vormen:', len(s.shapes), 'buiten canvas:', buiten or 'geen')
