"""Bouwt de backwall als bewerkbare pptx op schaal 1:4 (PowerPoint-maximum is 142 cm per kant).
Ontwerpraster: 1 px = 1 mm op de echte wand (2954 x 2520). Alles in tekstvakken en vormen, behalve
achtergrond, logo's en iconen. Bron van de lay-out: backwall-verticaal-2026-11-25.html."""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree
import os

HERE = os.path.dirname(os.path.abspath(__file__)); A = lambda n: os.path.join(HERE, 'assets', n)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
S = 9000                      # EMU per wandpixel (1:4)
PT = 0.25 * 72 / 25.4         # pt per wandpixel op schaal 1:4
E = lambda px: Emu(int(round(px * S)))
NAVY, GD, GREEN, RED, I3, I5, I7 = '002333', '007B54', '00E075', 'B3261E', 'A9BCC4', '5B7480', '2C4A57'
HEAD, BODY = 'League Spartan', 'Inter'
rgb = lambda h: RGBColor.from_string(h)

prs = Presentation()
prs.slide_width, prs.slide_height = E(2954), E(2520)
slide = prs.slides.add_slide(prs.slide_layouts[6])

def _alpha(fill_or_line_elm, pct):
    clr = fill_or_line_elm.find('.//' + qn('a:srgbClr'))
    a = etree.SubElement(clr, qn('a:alpha')); a.set('val', str(int(pct * 1000)))

def shadow(shape, blur, dist, color, alpha):
    spPr = shape._element.spPr
    eff = etree.SubElement(spPr, qn('a:effectLst'))
    sh = etree.SubElement(eff, qn('a:outerShdw'), blurRad=str(int(blur*S)), dist=str(int(dist*S)), dir='5400000', algn='t', rotWithShape='0')
    c = etree.SubElement(sh, qn('a:srgbClr'), val=color); etree.SubElement(c, qn('a:alpha'), val=str(int(alpha*1000)))

def box(kind, x, y, w, h, fill=None, fill_alpha=None, line=None, line_w=0, line_alpha=None, radius=None, name=None):
    shp = slide.shapes.add_shape(kind, E(x), E(y), E(w), E(h))
    if radius is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        shp.adjustments[0] = min(radius / min(w, h), .5)
    if fill: 
        shp.fill.solid(); shp.fill.fore_color.rgb = rgb(fill)
        if fill_alpha is not None: _alpha(shp._element.spPr.find(qn('a:solidFill')), fill_alpha)
    else: shp.fill.background()
    if line:
        shp.line.color.rgb = rgb(line); shp.line.width = E(line_w)
        if line_alpha is not None: _alpha(shp._element.spPr.find(qn('a:ln')), line_alpha)
    else: shp.line.fill.background()
    shp.shadow.inherit = False
    if name: shp.name = name
    return shp

def text(x, y, w, h, runs_by_line, *, font=BODY, size=40, lh=1.2, color=NAVY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spc=0, name=None):
    """runs_by_line: lijst regels; elke regel is een tekst of een lijst (tekst, kleur) stukjes. Regelafstand exact (lh x size)."""
    tb = slide.shapes.add_textbox(E(x), E(y), E(w), E(h)); tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE; tf.vertical_anchor = anchor
    if isinstance(runs_by_line, str): runs_by_line = [runs_by_line]
    for i, line in enumerate(runs_by_line):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.line_spacing = Pt(lh * size * PT); p.space_before = p.space_after = Pt(0)
        for part in ([(line, color)] if isinstance(line, str) else line):
            t, c = part; r = p.add_run(); r.text = t
            f = r.font; f.name = font; f.size = Pt(size * PT); f.bold = (font == HEAD); f.color.rgb = rgb(c)
            rPr = r._r.get_or_add_rPr()
            if spc: rPr.set('spc', str(int(spc * size * PT * 100)))
            for tag in ('a:latin', 'a:ea', 'a:cs'):
                el = rPr.find(qn(tag))
                if el is None: el = etree.SubElement(rPr, qn(tag))
                el.set('typeface', font)
    if name: tb.name = name
    return tb

def flow(x, y, w, h, paras, name=None):
    """Een tekstvak met meerdere alinea's, elk met eigen font, maat, kleur en ruimte ervoor. Loopt vanzelf door."""
    tb = slide.shapes.add_textbox(E(x), E(y), E(w), E(h)); tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE; tf.vertical_anchor = MSO_ANCHOR.TOP
    for i, d in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        size = d['size']; font = d.get('font', BODY); lh = d.get('lh', 1.2)
        p.alignment = PP_ALIGN.LEFT; p.line_spacing = Pt(lh * size * PT)
        p.space_before = Pt(d.get('before', 0) * PT); p.space_after = Pt(0)
        parts = d['parts'] if isinstance(d['parts'], list) else [(d['parts'], d.get('color', NAVY))]
        for t, c in parts:
            r = p.add_run(); r.text = t; f = r.font; f.name = font; f.size = Pt(size * PT); f.bold = (font == HEAD); f.color.rgb = rgb(c)
            rPr = r._r.get_or_add_rPr()
            if d.get('spc'): rPr.set('spc', str(int(d['spc'] * size * PT * 100)))
            for tag in ('a:latin', 'a:ea', 'a:cs'):
                el = rPr.find(qn(tag))
                if el is None: el = etree.SubElement(rPr, qn(tag))
                el.set('typeface', font)
    if name: tb.name = name
    return tb

def pic(path, x, y, w, h, name=None):
    p = slide.shapes.add_picture(path, E(x), E(y), E(w), E(h))
    if name: p.name = name
    return p

# ---- achtergrond (afbeelding) ----
pic(A('bg.png'), 0, 0, 2954, 2520, 'Achtergrond')

# ---- titel ----
text(128, 96, 2698, 340, ["Generic AI doesn't grade", [("like a teacher. ", NAVY), ("Eduface does.", GD)]],
     font=HEAD, size=168, lh=.98, spc=-.025, name='Titel')

# ---- quotes ----
X3 = [128, 1047, 1966]
Q = [("We didn’t find any platform that can mark and give feedback the way a teacher does.", "Head of academic innovation, private university", 3),
     ("At some point it gets generic: every student gets the same feedback.", "Head of academic innovation, private university", 3),
     ("You would have to prompt the agent every single time.", "AVP instructional design, US technical college", 2)]
for i, (q, who, nlines) in enumerate(Q):
    text(X3[i], 500, 76, 150, "\u201C", font=HEAD, size=150, lh=.8, color=I3, name=f'Quote {i+1} aanhaalteken')
    flow(X3[i] + 98, 500, 800, 330, [dict(parts=q, size=52, lh=1.2, color=NAVY),
                                      dict(parts=who, size=34, lh=1.2, color=I5, before=18)], name=f'Quote {i+1}')

# ---- chevron-knopen ----
def link(y, n):
    box(MSO_SHAPE.OVAL, 1439, y, 76, 76, fill=NAVY, line='FFFFFF', line_w=6, name=f'Pijl {n}')
    pic(A('chevron.png'), 1439 + 18, y + 18, 40, 40, f'Pijl {n} icoon')
link(806, 1)

# ---- rode band ----
band = box(MSO_SHAPE.ROUNDED_RECTANGLE, 128, 872, 2698, 214, fill=RED, radius=56, name='Rode band')
shadow(band, 60, 24, NAVY, 22)
tw = (2698 - 68 - 48) / 3
for i, (logo, name) in enumerate([('openai', 'ChatGPT'), ('googlegemini', 'Gemini'), ('claude', 'Claude')]):
    x = 128 + 34 + i * (tw + 24)
    box(MSO_SHAPE.ROUNDED_RECTANGLE, x, 906, tw, 146, fill='FFFFFF', fill_alpha=14, line='FFFFFF', line_w=4, line_alpha=45, radius=34, name=f'No-tegel {name}')
    pic(A(f'logo-{logo}.png'), x + 40, 938, 82, 82, f'Logo {name}')
    text(x + 152, 921, tw - 170, 70, f'No {name}', font=HEAD, size=70, lh=1, color='FFFFFF', spc=-.01, name=f'No {name}')
    text(x + 152, 1001, tw - 170, 36, 'Not built for marking', size=36, lh=1, color='D9E0E2', name=f'Not built for marking {i+1}')
link(1096, 2)

# ---- drie kaarten ----
CARDS = [("teacher", [("Trained on how ", 'FFFFFF'), ("teachers mark.", GREEN)], 2, "Our own model. You approve or change every grade."),
         ("bubbles", [("Feedback ", 'FFFFFF'), ("per student.", GREEN)], 1, "Based on their own answer and the course material."),
         ("sheets", [("Set up ", 'FFFFFF'), ("once.", GREEN)], 1, "Rubric and instructions per assignment, copied across courses.")]
for i, (ic, head, hl, sub) in enumerate(CARDS):
    x = X3[i]
    card = box(MSO_SHAPE.ROUNDED_RECTANGLE, x, 1160, 860, 530, fill=NAVY, radius=56, name=f'Kaart {i+1}')
    shadow(card, 70, 28, NAVY, 34)
    n = box(MSO_SHAPE.OVAL, x + 48, 1208, 88, 88, fill=GREEN, name=f'Nummer {i+1}')
    tf = n.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; r = p.add_run(); r.text = str(i + 1)
    r.font.name = HEAD; r.font.size = Pt(56 * PT); r.font.bold = True; r.font.color.rgb = rgb(NAVY)
    box(MSO_SHAPE.ROUNDED_RECTANGLE, x + 652, 1208, 160, 160, fill='FFFFFF', fill_alpha=10, radius=44, name=f'Icoontegel {i+1}')
    pic(A(f'icon-{ic}.png'), x + 652 + 12, 1208 + 12, 136, 136, f'Icoon {i+1}')
    flow(x + 48, 1398, 764, 400, [dict(parts=head, font=HEAD, size=68, lh=1.02, spc=-.01),
                                  dict(parts=sub, size=42, lh=1.22, color='C7CFD2', before=16)], name=f'Kaart {i+1} tekst')

# ---- logo ----
pic(os.path.join(ROOT, 'Design/Merk/logos/logo_navy.png'), 2406, 2278, 420, 420 * 703 / 2596, 'Eduface logo')

out = os.path.join(HERE, '..', 'backwall-bewerkbaar.pptx')
prs.save(out); print('opgeslagen', os.path.normpath(out))

# controle: niets buiten het canvas
buiten = [s.name for s in slide.shapes if s.left < 0 or s.top < 0 or s.left + s.width > prs.slide_width or s.top + s.height > prs.slide_height]
print('buiten canvas:', buiten or 'geen')
