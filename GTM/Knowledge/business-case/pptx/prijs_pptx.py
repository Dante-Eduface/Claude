"""Prijspagina (variant A, simpel en groot) als bewerkbare pptx.
Gebruik: python3 prijs_pptx.py uitvoer.pptx"""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
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
    return tb

L, B = 120, 1680
tekst(L, 70, B, 30, [('KOSTEN', 11, True, KLANT, 0)])
tekst(L, 104, B, 70, [('Dit kost Eduface', 30, True, TEKST, 0)])

# Prijsblok: bedrag links, prijsregel rechts in hetzelfde blok
blok(L, 190, B, 280, KLANT, 0.08)
tekst(L + 70, 190, 760, 280, [('€ 1.500', 56, True, WIT, 0),
                               ('per maand, vooraf betaald', 18, False, WIT, 6),
                               ('€ 18.000 per jaar, exclusief btw', 13, False, WITZACHT, 4)], anchor=MSO_ANCHOR.MIDDLE)
scheid = s.shapes.add_connector(1, E(L + 900), E(234), E(L + 900), E(426))
scheid.line.color.rgb = RGBColor(0x3A, 0x45, 0x66); scheid.line.width = Pt(1)
tekst(L + 960, 190, B - 1020, 280, [('Eerste 400 studenten', 16, True, WIT, 0),
                                     ('€ 3,75 per student per maand, samen € 1.500', 13, False, WITZACHT, 2),
                                     ('Elke student daarboven', 16, True, WIT, 18),
                                     ('€ 3 per student per maand', 13, False, WITZACHT, 2)], anchor=MSO_ANCHOR.MIDDLE)

# Wat de instelling ervoor krijgt: drie brede kaarten onder elkaar
import os
HIER = os.path.dirname(os.path.abspath(__file__))
tekst(L, 500, B, 30, [('WAT DE INSTELLING ERVOOR KRIJGT', 11, True, KLANT, 0)])
RIJ, GAP = 150, 16
for i, (icoon, kop, sub, accent) in enumerate([
        ('consistent', 'Uniforme beoordeling', 'Elke opdracht wordt langs dezelfde criteria beoordeeld, door elke beoordelaar.', None),
        ('koppeling', 'Integratie in NEO LMS', 'Opdrachten en cijfers lopen via NEO. Docenten en studenten werken in de omgeving die ze kennen.', None),
        ('feedback', 'Formatieve feedback voor elke student', 'Nu krijgt de helft van de studenten formatieve feedback. Met Eduface is dat iedereen.', '50% → 100%')]):
    y = 538 + i * (RIJ + GAP)
    blok(L, y, B, RIJ, TINT, 0.14)
    rondje = s.shapes.add_shape(MSO_SHAPE.OVAL, E(L + 40), E(y + 27), E(96), E(96))
    rondje.fill.solid(); rondje.fill.fore_color.rgb = WIT; rondje.line.fill.background(); rondje.shadow.inherit = False
    s.shapes.add_picture(os.path.join(HIER, 'assets', icoon + '.png'), E(L + 64), E(y + 51), E(48), E(48))
    breed = 900 if accent else B - 220
    tekst(L + 176, y, breed, RIJ, [(kop, 20, True, TEKST, 0), (sub, 14, False, TEKST, 6)], anchor=MSO_ANCHOR.MIDDLE)
    if accent:
        tekst(L + 1100, y, B - 1140, RIJ, [(accent, 32, True, KLANT, 0)], anchor=MSO_ANCHOR.MIDDLE).text_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT

out = sys.argv[1]; prs.save(out)
p = Presentation(out)
for sl in p.slides:
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print('buiten canvas:', buiten or 'geen')
