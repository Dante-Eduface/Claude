"""Bouwt de gevel (fascia 3020 x 350 mm, met standnummer C11) als bewerkbare pptx op schaal 1:4 (755 x 87,5 mm).
Posities komen uit measured_facade.json (gemeten uit facade-print.html). Eerst `node measure_facade.js`, dan dit script."""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree
import os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
M = json.load(open(os.path.join(HERE, 'measured_facade.json')))
S = 9000; PT = 0.25 * 72 / 25.4; E = lambda px: Emu(int(round(px * S)))
NAVY, GD, GREY = '002333', '007B54', '5B7480'; HEAD, BODY = 'League Spartan', 'Inter'
rgb = lambda h: RGBColor.from_string(h)
prs = Presentation(); prs.slide_width, prs.slide_height = E(3020), E(350)
slide = prs.slides.add_slide(prs.slide_layouts[6])

def text(r, paras, anchor=MSO_ANCHOR.TOP, grow=0, name=None):
    x, y, w, h = r
    tb = slide.shapes.add_textbox(E(x), E(y), E(w + grow), E(h)); tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = False; tf.auto_size = MSO_AUTO_SIZE.NONE; tf.vertical_anchor = anchor
    for i, d in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        size = d['size']; p.alignment = PP_ALIGN.LEFT; p.line_spacing = Pt(d['lh'] * size * PT); p.space_before = p.space_after = Pt(0)
        for t, c in d['parts']:
            run = p.add_run(); run.text = t; f = run.font; f.name = d['font']; f.size = Pt(size * PT); f.bold = (d['font'] == HEAD); f.color.rgb = rgb(c)
            rPr = run._r.get_or_add_rPr()
            if d.get('spc'): rPr.set('spc', str(int(d['spc'] * size * PT * 100)))
            for tag in ('a:latin', 'a:ea', 'a:cs'):
                el = rPr.find(qn(tag))
                if el is None: el = etree.SubElement(rPr, qn(tag))
                el.set('typeface', d['font'])
    if name: tb.name = name
    return tb

slide.shapes.add_picture(os.path.join(HERE, 'assets3', 'gevel-bg.png'), 0, 0, prs.slide_width, prs.slide_height).name = 'Achtergrond'
x, y, w, h = M['logo']; slide.shapes.add_picture(os.path.join(ROOT, 'Design/Merk/logos/logo_navy.png'), E(x), E(y), E(w), E(h)).name = 'Eduface logo'
for i, (x, y, w, h) in enumerate(M['sep']):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(h)); s.fill.solid(); s.fill.fore_color.rgb = rgb('C9D1D5'); s.line.fill.background(); s.shadow.inherit = False; s.name = f'Scheidingslijn {i+1}'
hx, hy, hw, hh = M['h']
text((hx, hy, hw, hh), [dict(parts=[('Chatbots ', NAVY), ("don't", GD), (' grade', NAVY)], font=HEAD, size=100, lh=1.04, spc=-.02),
                        dict(parts=[('like instructors.', NAVY)], font=HEAD, size=100, lh=1.04, spc=-.02)], grow=60, name='Kop')
text(M['l'], [dict(parts=[('Stand', GREY)], font=BODY, size=44, lh=1)], grow=40, name='Stand')
text(M['n'], [dict(parts=[('C11', NAVY)], font=HEAD, size=150, lh=.95, spc=-.02)], grow=40, name='Standnummer C11')
out = os.path.join(HERE, '..', 'gevel-bewerkbaar.pptx'); prs.save(out); print('opgeslagen', os.path.normpath(out))
print('buiten canvas:', [s.name for s in slide.shapes if s.left < 0 or s.top < 0 or s.left + s.width > prs.slide_width or s.top + s.height > prs.slide_height] or 'geen')
