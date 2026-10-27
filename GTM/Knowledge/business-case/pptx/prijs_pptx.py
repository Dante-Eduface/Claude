"""Prijspagina (variant A, simpel en groot) als bewerkbare pptx.
Gebruik: python3 prijs_pptx.py uitvoer.pptx"""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR
import sys

PX = 6350
KLANT = RGBColor(0x0B, 0x15, 0x33)
TINT = RGBColor(0xEE, 0xF1, 0xF7)
TEKST = RGBColor(0x1D, 0x24, 0x33)
WIT = RGBColor(0xFF, 0xFF, 0xFF)
WITZACHT = RGBColor(0xC9, 0xCE, 0xD9)
FONT = 'Inter'
E = lambda v: Emu(int(v * PX))

prs = Presentation()
prs.slide_width, prs.slide_height = E(1920), E(1080)
s = prs.slides.add_slide(prs.slide_layouts[6])

def blok(x, y, w, h, vul, rond):
    v = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, E(x), E(y), E(w), E(h))
    v.adjustments[0] = rond
    v.fill.solid(); v.fill.fore_color.rgb = vul; v.line.fill.background(); v.shadow.inherit = False

def tekst(x, y, w, h, regels, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, (t, size, bold, kleur, voor) in enumerate(regels):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_before = Pt(voor)
        r = p.add_run(); r.text = t
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = FONT, Pt(size), bold, kleur

L, B = 120, 1680
tekst(L, 90, B, 30, [('KOSTEN', 11, True, KLANT, 0)])
tekst(L, 124, B, 70, [('Dit kost Eduface', 30, True, TEKST, 0)])

blok(L, 250, B, 430, KLANT, 0.06)
tekst(L + 90, 250, B - 180, 430, [('€ 1.500', 96, True, WIT, 0),
                                   ('per maand, vooraf betaald', 22, False, WIT, 10),
                                   ('€ 18.000 per jaar, exclusief btw', 15, False, WITZACHT, 6)], anchor=MSO_ANCHOR.MIDDLE)

W = (B - 24) / 2
for i, (kop, sub) in enumerate([('Eerste 400 studenten', '€ 3,75 per student per maand, samen € 1.500'),
                                ('Elke student daarboven', '€ 3 per student per maand')]):
    x = L + i * (W + 24)
    blok(x, 708, W, 190, TINT, 0.1)
    tekst(x + 44, 708, W - 88, 190, [(kop, 22, True, KLANT, 0), (sub, 14, False, TEKST, 6)], anchor=MSO_ANCHOR.MIDDLE)

out = sys.argv[1]; prs.save(out)
p = Presentation(out)
for sl in p.slides:
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print('buiten canvas:', buiten or 'geen')
