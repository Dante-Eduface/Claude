"""Bewerkbare PPTX van de 'Not built for grading' redesign. Posities uit geometry.json (gemeten in redesign.html)."""
import json
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

PX = 6350
E = lambda v: Emu(int(round(v * PX)))
P = lambda v: Pt(v / 2)
C = lambda h: RGBColor.from_string(h)
NAVY, GREEN, INK500, INK300, WHITE = '002333', '00E075', '5B7480', 'A9BCC4', 'FFFFFF'
SOFT = 'A6B5BD'   # wit 62% op navy, voorgemengd (pptx kent geen tekst-alfa)
HEAD, BODY = 'League Spartan', 'Inter'
g = json.load(open('geometry.json'))

prs = Presentation()
prs.slide_width, prs.slide_height = E(1080), E(1350)
s = prs.slides.add_slide(prs.slide_layouts[6])

def rect(x, y, w, h, fill, r=0):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if r else MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = C(fill); sh.line.fill.background(); sh.shadow.inherit = False
    if r: sh.adjustments[0] = r / min(w, h)
    return sh

def oval(x, y, d, fill):
    sh = s.shapes.add_shape(MSO_SHAPE.OVAL, E(x), E(y), E(d), E(d))
    sh.fill.solid(); sh.fill.fore_color.rgb = C(fill); sh.line.fill.background(); sh.shadow.inherit = False
    return sh

def stroke(paths, color, width):
    """Open polylines als bewerkbare vorm, ronde uiteinden."""
    fb = s.shapes.build_freeform(E(paths[0][0][0]), E(paths[0][0][1]), scale=1.0)
    for i, pts in enumerate(paths):
        if i: fb.move_to(E(pts[0][0]), E(pts[0][1]))
        fb.add_line_segments([(E(x), E(y)) for x, y in pts[1:]], close=False)
    sh = fb.convert_to_shape()
    sh.fill.background(); sh.shadow.inherit = False
    sh.line.color.rgb = C(color); sh.line.width = P(width)
    ln = sh.line._get_or_add_ln(); ln.set('cap', 'rnd')
    etree.SubElement(ln, qn('a:round'))
    return sh

def text(box, runs, *, font=BODY, size=32, color=NAVY, lh=None, spc=0.0, w_extra=0, name=None):
    x, y, w, h = box
    tb = s.shapes.add_textbox(E(x), E(y), E(w + w_extra), E(h))
    if name: tb.name = name
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
    if lh: p.line_spacing = P(lh)
    for t, bold, col in runs:
        r = p.add_run(); r.text = t
        f = r.font; f.name = font; f.size = P(size); f.bold = bold; f.color.rgb = C(col or color)
        if spc: r._r.get_or_add_rPr().set('spc', str(int(round(spc * size / 2 * 100))))
    return tb

# --- kop
text(g['h1'], [('Not built for grading.', True, None)], font=HEAD, size=76, lh=76, spc=-0.02, w_extra=40, name='Titel')
text(g['names'], [('ChatGPT, Gemini, Claude', False, None)], size=26, color=INK500, lh=31, name='Chatbots')

# --- drie rijen: klacht, pijl, vinkje, antwoord
Q = [
  ([('Same rubric, same essay, uploaded twice. ', False), ('Two different grades.', True)], 'Job title, public university', 'Trained on how instructors grade.'),
  ([('After a few essays it goes generic. ', False), ('Every student gets the same feedback.', True)], 'Head of academic innovation, private university', 'Feedback per student.'),
  ([('You have to re-prompt it ', False), ('for every single assignment.', True)], 'AVP instructional design, US technical college', 'Set up once.'),
]
for i, (q, who, a) in enumerate(Q):
    text(g['q'][i], [(t, b, None) for t, b in q], size=32, lh=41.6, spc=-0.01, name=f'Klacht {i+1}')
    text(g['who'][i], [(who, False, None)], size=20, color=INK500, lh=28, name=f'Bron {i+1}')
    ax, ay, _, _ = g['arrow'][i]; k = 48 / 56; oy = ay + (16 - 16 * k) / 2
    m = lambda px, py: (ax + px * k, oy + py * k)
    stroke([[m(4, 8), m(48, 8)], [m(42, 2), m(48, 8), m(42, 14)]], INK300, 2.5)
    tx, ty, d, _ = g['tick'][i]
    oval(tx, ty, d, GREEN)
    ck = 22 / 24
    stroke([[(tx + 11 + px * ck, ty + 11 + py * ck) for px, py in [(5, 12.5), (9.5, 17), (19, 7.5)]]], NAVY, 3.2 * ck)
    ab = list(g['a'][i]); ab[2] = g['a'][0][2]
    text(ab, [(a, True, None)], font=HEAD, size=40, lh=44, spc=-0.015, name=f'Antwoord {i+1}')

# --- bewijsblok
px_, py_, pw, ph = g['proof']
rect(px_, py_, pw, ph, NAVY, r=20).name = 'Bewijsblok'
text(g['kicker'], [('Eduface AI', True, WHITE)], font=HEAD, size=28, lh=26, spc=-0.01, name='Productnaam')
text(g['num'], [('250,000', True, WHITE)], font=HEAD, size=128, lh=121.6, spc=-0.02, w_extra=60, name='Getal')
text(g['cap'], [('education-specific feedback examples', False, SOFT)], size=22, lh=26, name='Toelichting getal')
text(g['dev'], [('Developed with the help of ', False, WHITE), ('Leiden University', True, WHITE), (' and ', False, WHITE), ('Radboud University.', True, WHITE)],
     size=26, lh=36.4, name='Ontwikkeld met')

# --- voet
text(g['lbl'], [('Integrated with your LMS', False, INK500)], size=18, lh=21, name='LMS label')
x, y, w, h = g['lms']; s.shapes.add_picture('lms_clean.png', E(x), E(y), E(w), E(h)).name = 'LMS-logos'
x, y, w, h = g['logo']; s.shapes.add_picture('/home/user/Claude/Design/Merk/logos/logo_navy.png', E(x), E(y), E(w), E(h)).name = 'Eduface logo'

# themastijl (schaduw-verwijzing) van alle vormen halen, zodat niets een ongevraagde schaduw krijgt
for sh in s.shapes:
    st = sh._element.find(qn('p:style'))
    if st is not None: sh._element.remove(st)
prs.save('eduface-not-built-for-grading-bewerkbaar.pptx')

# controle: niets buiten het canvas
for sh in s.shapes:
    if sh.left < 0 or sh.top < 0 or sh.left + sh.width > prs.slide_width or sh.top + sh.height > prs.slide_height:
        print('BUITEN CANVAS:', sh.name)
print('ok', len(s.shapes), 'vormen')
