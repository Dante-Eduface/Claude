"""Bouwt een bewerkbare A4-pptx uit layout.json (uitgelezen uit de HTML-pagina's)."""
import json
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn

PX = 9525  # EMU per CSS-pixel (96 dpi)
E = lambda v: Emu(int(round(v * PX)))
ALIGN = {'left': PP_ALIGN.LEFT, 'right': PP_ALIGN.RIGHT, 'center': PP_ALIGN.CENTER}

def blend(c):
    """Doorschijnende kleur op wit of op navy uitrekenen zou context vragen; wit is hier de enige ondergrond."""
    if c['a'] >= 1: return c['hex']
    r, g, b = (int(c['hex'][i:i+2], 16) for i in (0, 2, 4))
    a = c['a']; base = (0, 3, 38)  # alle doorschijnende vlakken liggen op het donkere blauw
    return ''.join(f'{round(v*a + bb*(1-a)):02x}' for v, bb in zip((r, g, b), base))

prs = Presentation()
prs.slide_width, prs.slide_height = E(794), E(1123)
for nr, items in enumerate(json.load(open('layout.json')), 1):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    for it in items:
        if it['k'] == 'rect':
            oval = it['r'] >= min(it['w'], it['h']) / 2 - 0.5 and abs(it['w'] - it['h']) < 1
            shp = MSO_SHAPE.OVAL if oval else MSO_SHAPE.ROUNDED_RECTANGLE if it['r'] else MSO_SHAPE.RECTANGLE
            sh = s.shapes.add_shape(shp, E(it['x']), E(it['y']), E(it['w']), E(it['h']))
            # Geen schaduw: het standaardthema zet er anders een onder elk vlak
            for ref in sh._element.iter(qn('a:effectRef')): ref.set('idx', '0')
            if it['fill']: sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(blend(it['fill']))
            else: sh.fill.background()
            if it['line']:
                sh.line.color.rgb = RGBColor.from_string(blend(it['line'])); sh.line.width = E(it['lw'])
            else: sh.line.fill.background()
            if shp == MSO_SHAPE.ROUNDED_RECTANGLE:
                sh.adjustments[0] = min(0.5, it['r'] / min(it['w'], it['h']))
            sh.text_frame.text = ''
        elif it['k'] == 'svg':
            s.shapes.add_picture(it['file'], E(it['x']), E(it['y']), E(it['w']), E(it['h']))
        else:
            # Iets ruimer dan in de browser, zodat afwijkende fontmetriek niet tot een extra regel leidt
            # Breedte van het eigen blok, plus marge: fontmetriek verschilt per programma
            w = max(it['blockW'], it['w'] * 1.12 + 6)
            x = it['x'] if it['align'] == 'left' else it['x'] - (w - it['w']) if it['align'] == 'right' else it['x'] - (w - it['w']) / 2
            tb = s.shapes.add_textbox(E(x), E(it['y']), E(w), E(it['h']))
            tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
            # Nooit laten krimpen: elke titel houdt overal dezelfde grootte
            tf.auto_size = MSO_AUTO_SIZE.NONE
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            p = tf.paragraphs[0]; p.alignment = ALIGN[it['align']]; p.line_spacing = Pt(it['lh'] * 0.75)
            runs = it['runs']
            while runs and not runs[-1]['t'].strip(): runs = runs[:-1]
            first = True
            for ru in runs:
                parts = ru['t'].split('\n')
                for j, t in enumerate(parts):
                    if j > 0:
                        p = tf.add_paragraph(); p.alignment = ALIGN[it['align']]; p.line_spacing = Pt(it['lh'] * 0.75)
                        first = True
                    if first: t = t.lstrip()
                    if not t: continue
                    first = False
                    r = p.add_run(); r.text = t.upper() if ru['upper'] else t
                    f = r.font; f.name = ru['font']; f.size = Pt(ru['size'] * 0.75); f.bold = ru['bold']
                    f.color.rgb = RGBColor.from_string(ru['color'])
    # Logo Academica: groot boven de opening, klein linksonder op de rest (verhouding 1648 x 320)
    if nr == 1:
        s.shapes.add_picture('academica.png', E(76), E(40), height=E(32))
    else:
        s.shapes.add_picture('academica.png', E(76), E(1123 - 54), height=E(16))
    # Paginanummer rechtsonder, in de marge van 20 mm
    tb = s.shapes.add_textbox(E(794 - 76 - 60), E(1123 - 52), E(60), E(16))
    tf = tb.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
    r = p.add_run(); r.text = str(nr)
    r.font.name = 'Inter'; r.font.size = Pt(8); r.font.color.rgb = RGBColor.from_string('555a78')
prs.save('../eduface-document-bewerkbaar.pptx')
