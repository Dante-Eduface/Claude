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
tekst(L, 70, B, 30, [('KOSTEN', 11, True, KLANT, 0)])
tekst(L, 104, B, 70, [('Dit kost Eduface', 30, True, TEKST, 0)])

blok(L, 210, B, 320, KLANT, 0.07)
tekst(L + 90, 210, B - 180, 320, [('€ 1.500', 68, True, WIT, 0),
                                   ('per maand, vooraf betaald', 20, False, WIT, 8),
                                   ('€ 18.000 per jaar, exclusief btw', 14, False, WITZACHT, 4)], anchor=MSO_ANCHOR.MIDDLE)

W = (B - 24) / 2
for i, (kop, sub) in enumerate([('Eerste 400 studenten', '€ 3,75 per student per maand, samen € 1.500'),
                                ('Elke student daarboven', '€ 3 per student per maand')]):
    x = L + i * (W + 24)
    blok(x, 548, W, 124, TINT, 0.12)
    tekst(x + 44, 548, W - 88, 124, [(kop, 18, True, KLANT, 0), (sub, 13, False, TEKST, 4)], anchor=MSO_ANCHOR.MIDDLE)

# Wat de instelling ervoor krijgt
import os
HIER = os.path.dirname(os.path.abspath(__file__))
LIJNKLR = RGBColor(0xD9, 0xDD, 0xE4)
tekst(L, 712, B, 30, [('WAT DE INSTELLING ERVOOR KRIJGT', 11, True, KLANT, 0)])
RIJ, GAP = 84, 12
for i, (icoon, kop, sub) in enumerate([
        ('consistent', 'Uniforme beoordeling', 'Elke opdracht wordt langs dezelfde criteria beoordeeld, door elke beoordelaar.'),
        ('koppeling', 'Integratie in NEO LMS', 'Opdrachten en cijfers lopen via NEO. Docenten en studenten werken in de omgeving die ze kennen.'),
        ('feedback', 'Formatieve feedback van 50% naar 100%', 'Elke student krijgt formatieve feedback. Nu is dat de helft.')]):
    y = 748 + i * (RIJ + GAP)
    v = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, E(L), E(y), E(B), E(RIJ))
    v.adjustments[0] = 0.18; v.fill.solid(); v.fill.fore_color.rgb = WIT
    v.line.color.rgb = LIJNKLR; v.line.width = Pt(1); v.shadow.inherit = False
    rondje = s.shapes.add_shape(MSO_SHAPE.OVAL, E(L + 24), E(y + 14), E(56), E(56))
    rondje.fill.solid(); rondje.fill.fore_color.rgb = TINT; rondje.line.fill.background(); rondje.shadow.inherit = False
    s.shapes.add_picture(os.path.join(HIER, 'assets', icoon + '.png'), E(L + 38), E(y + 28), E(28), E(28))
    tekst(L + 108, y, 660, RIJ, [(kop, 16, True, TEKST, 0)], anchor=MSO_ANCHOR.MIDDLE)
    tekst(L + 790, y, B - 820, RIJ, [(sub, 13, False, TEKST, 0)], anchor=MSO_ANCHOR.MIDDLE)

out = sys.argv[1]; prs.save(out)
p = Presentation(out)
for sl in p.slides:
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print('buiten canvas:', buiten or 'geen')
