"""Bouwt de backwall als bewerkbare pptx op schaal 1:4 (PowerPoint-maximum is 142 cm per kant).
Posities komen uit measured.json (gemeten uit backwall.html, 1 px = 1 mm op de echte wand).
Eerst `node measure.js`, dan dit script. Tekst en vormen zijn bewerkbaar, achtergrond, logo's en iconen zijn plaatjes."""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree
import os, json

HERE = os.path.dirname(os.path.abspath(__file__)); A = lambda n: os.path.join(HERE, 'assets2', n)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
M = json.load(open(os.path.join(HERE, 'measured.json')))['rects']
S = 9000; PT = 0.25 * 72 / 25.4
E = lambda px: Emu(int(round(px * S)))
NAVY, GREEN, RED = '002333', '00E075', 'B3261E'
HEAD, BODY = 'League Spartan', 'Inter'
rgb = lambda h: RGBColor.from_string(h)
prs = Presentation(); prs.slide_width, prs.slide_height = E(2954), E(2520)
slide = prs.slides.add_slide(prs.slide_layouts[6])

def _alpha(parent, pct):
    clr = parent.find('.//' + qn('a:srgbClr')); etree.SubElement(clr, qn('a:alpha')).set('val', str(int(pct * 1000)))

def shadow(shape, blur, dist, color, alpha):
    eff = etree.SubElement(shape._element.spPr, qn('a:effectLst'))
    sh = etree.SubElement(eff, qn('a:outerShdw'), blurRad=str(int(blur*S)), dist=str(int(dist*S)), dir='5400000', algn='t', rotWithShape='0')
    etree.SubElement(etree.SubElement(sh, qn('a:srgbClr'), val=color), qn('a:alpha'), val=str(int(alpha*1000)))

def box(r, fill=None, fill_alpha=None, line=None, line_w=0, radius=None, oval=False, name=None):
    x, y, w, h = r
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL if oval else MSO_SHAPE.ROUNDED_RECTANGLE, E(x), E(y), E(w), E(h))
    if radius is not None and not oval: shp.adjustments[0] = min(radius / min(w, h), .5)
    if fill:
        shp.fill.solid(); shp.fill.fore_color.rgb = rgb(fill)
        if fill_alpha is not None: _alpha(shp._element.spPr.find(qn('a:solidFill')), fill_alpha)
    else: shp.fill.background()
    if line: shp.line.color.rgb = rgb(line); shp.line.width = E(line_w)
    else: shp.line.fill.background()
    shp.shadow.inherit = False
    if name: shp.name = name
    return shp

def flow(r, paras, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, name=None, extra_h=0, grow_w=0):
    """Een tekstvak met meerdere alinea's. Een alinea is een dict: parts=[(tekst, kleur, font, highlight)], size, lh, before."""
    x, y, w, h = r
    x0 = x - grow_w / 2 if align == PP_ALIGN.CENTER else x   # links uitgelijnd: alleen naar rechts verbreden
    tb = slide.shapes.add_textbox(E(x0), E(y), E(w + grow_w), E(h + extra_h)); tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE; tf.vertical_anchor = anchor
    for i, d in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        size = d['size']; p.alignment = align; p.line_spacing = Pt(d.get('lh', 1.2) * size * PT)
        p.space_before = Pt(d.get('before', 0) * PT); p.space_after = Pt(0)
        for part in d['parts']:
            t, c = part[0], part[1]; font = part[2] if len(part) > 2 and part[2] else d.get('font', BODY); hl = part[3] if len(part) > 3 else None
            r_ = p.add_run(); r_.text = t; f = r_.font; f.name = font; f.size = Pt(size * PT); f.bold = (font == HEAD); f.color.rgb = rgb(c)
            rPr = r_._r.get_or_add_rPr()
            if d.get('spc'): rPr.set('spc', str(int(d['spc'] * size * PT * 100)))
            if hl:
                h = etree.SubElement(rPr, qn('a:highlight')); etree.SubElement(h, qn('a:srgbClr'), val=hl)
            for tag in ('a:latin', 'a:ea', 'a:cs'):
                el = rPr.find(qn(tag))
                if el is None: el = etree.SubElement(rPr, qn(tag))
                el.set('typeface', font)
    if name: tb.name = name
    return tb

def pic(path, r, name=None, inset=0):
    x, y, w, h = r
    p = slide.shapes.add_picture(path, E(x + inset), E(y + inset), E(w - 2 * inset), E(h - 2 * inset))
    if name: p.name = name
    return p

def centered(path, r, size, name=None):
    """Plaatje van vaste grootte in het midden van een rechthoek."""
    x, y, w, h = r; return pic(path, (x + (w - size) / 2, y + (h - size) / 2, size, size), name)

# ---- achtergrond ----
slide.shapes.add_picture(os.path.join(HERE, 'assets', 'bg.png'), 0, 0, prs.slide_width, prs.slide_height).name = 'Achtergrond'

# ---- links: donker, quotes ----
card = box(M['.q'][0], NAVY, radius=56, name='Links donker'); shadow(card, 70, 28, NAVY, 34)
HL_DARK, QM, WHITE, GREYBLUE = '294654', '667B84', 'FFFFFF', 'A9BCC4'
QUOTES = [([("Same rubric, same essay, uploaded twice. ", WHITE), ("Two different grades.", WHITE, None, HL_DARK)], '[job title], public university'),
          ([("After a few essays it goes generic. ", WHITE), ("Every student gets the same feedback.", WHITE, None, HL_DARK)], 'Head of academic innovation, private university'),
          ([("You have to re-prompt it ", WHITE), ("for every single assignment.", WHITE, None, HL_DARK)], 'AVP instructional design, US technical college')]
for i, (parts, who) in enumerate(QUOTES):
    box(M['.q .it'][i], 'FFFFFF', fill_alpha=10, radius=40, name=f'Quote {i+1} icoontegel')
    centered(A(f'q-icon-{i+1}.png'), M['.q .it'][i], 128, f'Quote {i+1} icoon')
    qt, wh = M['.q .qt'][i], M['.q .who'][i]
    flow((qt[0], qt[1], qt[2], wh[1] + wh[3] - qt[1]),
         [dict(parts=[("“", QM, HEAD)] + parts, size=88, lh=1.16),
          dict(parts=[(who, GREYBLUE)], size=46, lh=1.2, before=16)], grow_w=40, extra_h=40, name=f'Quote {i+1}')

lab = M['.tools .lab'][0]
flow(lab, [dict(parts=[("Not built for grading.", WHITE, HEAD)], size=84, lh=1, spc=-.01)], align=PP_ALIGN.CENTER, grow_w=200, name='Not built for grading')
box(M['.redbox'][0], 'F8E3E0', line='EEC3BE', line_w=4, radius=40, name='Lichtrode box')
for i, (nm) in enumerate(['ChatGPT', 'Gemini', 'Claude']):
    t = M['.tl'][i]; box(t, 'FFFFFF', line='EFC9C4', line_w=4, radius=28, name=f'Tegel {nm}')
    pic(A(f'tool-{i+1}.png'), M['.tl img'][i], f'Logo {nm}')
    flow((t[0], t[1] + 21 + 66 + 14, t[2], 50), [dict(parts=[(nm, '2C4A57')], size=46, lh=1)], align=PP_ALIGN.CENTER, name=f'Naam {nm}')
    pic(A('x.png'), M['.x'][i], f'X {nm}')

# ---- rechts: wit, groen ----
card = box(M['.e'][0], 'FFFFFF', radius=56, name='Rechts wit'); shadow(card, 60, 24, NAVY, 22)
HEADS = [[("Trained on how ", NAVY), ("instructors grade.", NAVY, None, GREEN)], [("Feedback ", NAVY), ("per student.", NAVY, None, GREEN)], [("Set up ", NAVY), ("once.", NAVY, None, GREEN)]]
for i, parts in enumerate(HEADS):
    box(M['.e .it'][i], GREEN, radius=40, name=f'Voordeel {i+1} icoontegel')
    centered(A(f'e-icon-{i+1}.png'), M['.e .it'][i], 128, f'Voordeel {i+1} icoon')
    eh = M['.e .eh'][i]
    flow(eh, [dict(parts=parts, size=84, lh=1.12, font=HEAD, spc=-.015)], grow_w=40, extra_h=30, name=f'Voordeel {i+1}')
pic(A('arrow.png'), M['.arrow'][0], 'Pijl')
own = box(M['.own'][0], GREEN, radius=40, name='Eduface AI blok'); shadow(own, 40, 14, '00E075', 32)
box(M['.own .top'][0], 'FFFFFF', radius=34, name='Logo-vlakje')
pic(os.path.join(ROOT, 'Design/Merk/logos/logo_navy.png'), M['.own .top img'][0], 'Eduface logo (AI blok)')
ai = M['.own .top .ai'][0]
flow((ai[0], ai[1] - 4, ai[2] + 20, ai[3] + 8), [dict(parts=[("AI", NAVY, HEAD)], size=84, lh=1, spc=-.01)], name='AI')
n, l, d = M['.own .n'][0], M['.own .l'][0], M['.own .d'][0]
flow(n, [dict(parts=[("250,000", NAVY, HEAD)], size=150, lh=1, spc=-.025)], align=PP_ALIGN.CENTER, name='250.000')
flow(l, [dict(parts=[("education-specific feedback examples", NAVY)], size=46, lh=1.2)], align=PP_ALIGN.CENTER, grow_w=60, name='Label 250.000')
flow(d, [dict(parts=[("Developed with the help of Leiden University and Radboud University.", '00493F')], size=46, lh=1.2)], align=PP_ALIGN.CENTER, grow_w=20, extra_h=20, name='Leiden en Radboud')

# ---- LMS-rij en logo ----
flow(M['.lms .lab'][0], [dict(parts=[("Integrated with your LMS", '5B7480')], size=46, lh=1)], grow_w=200, name='LMS label')
for i, nm in enumerate(['Canvas', 'Moodle', 'Blackboard', 'Brightspace']): pic(A(f'lms-{i+1}.png'), M['.lms img'][i], f'LMS {nm}')
pic(os.path.join(ROOT, 'Design/Merk/logos/logo_navy.png'), M['.logo'][0], 'Eduface logo')

out = os.path.join(HERE, '..', 'backwall-bewerkbaar.pptx'); prs.save(out); print('opgeslagen', os.path.normpath(out))
buiten = [s.name for s in slide.shapes if s.left < 0 or s.top < 0 or s.left + s.width > prs.slide_width or s.top + s.height > prs.slide_height]
print('buiten canvas:', buiten or 'geen')
