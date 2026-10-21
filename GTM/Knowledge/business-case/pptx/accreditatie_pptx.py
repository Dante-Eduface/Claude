"""Accreditatie-onderdeel van de business case als bewerkbare pptx.
Gebruik: python3 accreditatie_pptx.py uitvoer.pptx  (iconen staan in assets/)"""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR
import os, sys

PX = 6350
KLANT = RGBColor(0x0B, 0x15, 0x33)   # hoofdkleur klant
TINT = RGBColor(0xEE, 0xF1, 0xF7)
LIJN = RGBColor(0xD9, 0xDD, 0xE4)
TEKST = RGBColor(0x1D, 0x24, 0x33)
ZACHT = RGBColor(0x5B, 0x64, 0x74)
WIT = RGBColor(0xFF, 0xFF, 0xFF)
FONT = 'Inter'
HIER = os.path.dirname(os.path.abspath(__file__))

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(1920 * PX), Emu(1080 * PX)
s = prs.slides.add_slide(prs.slide_layouts[6])
E = lambda v: Emu(int(v * PX))

def vorm(soort, x, y, w, h, vul=None, lijn=None, rond=None):
    v = s.shapes.add_shape(soort, E(x), E(y), E(w), E(h))
    if rond is not None: v.adjustments[0] = rond
    if vul: v.fill.solid(); v.fill.fore_color.rgb = vul
    else: v.fill.background()
    if lijn: v.line.color.rgb = lijn; v.line.width = Pt(1)
    else: v.line.fill.background()
    v.shadow.inherit = False
    return v

def tekst(x, y, w, h, regels, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, (t, size, bold, kleur) in enumerate(regels):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if i: p.space_before = Pt(4)
        r = p.add_run(); r.text = t
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = FONT, Pt(size), bold, kleur
    return tb

L, B = 120, 1680
tekst(L, 90, B, 30, [('ACCREDITATIE', 11, True, KLANT)])
tekst(L, 124, 1500, 130, [('Elke beoordeling blijft navolgbaar, de docent blijft eindverantwoordelijk', 26, True, TEKST)])

KOL = [
    ('navolgbaar', 'Beoordeling is navolgbaar',
     ['Elk cijfer heeft een onderbouwing per rubriccriterium.',
      'Een audit trail die voldoet aan de AI Act legt elke summatieve beoordeling vast.'],
     'de docent stelt het cijfer vast'),
    ('consistent', 'Beoordelaars oordelen consistent',
     ['Een overzicht toont welke beoordelaar afwijkt van het team.'],
     'kalibratie twee keer per jaar'),
    ('commissie', 'De examencommissie borgt de kwaliteit',
     ['Per beoordeling is de onderbouwing direct in te zien.'],
     'de steekproef'),
]
GAP = 40; KW = (B - 2 * GAP) / 3; KY, KH = 280, 610
for i, (icoon, eis, met, blijft) in enumerate(KOL):
    x = L + i * (KW + GAP)
    vorm(MSO_SHAPE.ROUNDED_RECTANGLE, x, KY, KW, KH, vul=TINT, rond=0.05)
    vorm(MSO_SHAPE.OVAL, x + 40, KY + 40, 96, 96, vul=WIT)
    s.shapes.add_picture(os.path.join(HIER, 'assets', icoon + '.png'), E(x + 60), E(KY + 60), E(56), E(56))
    tekst(x + 40, KY + 164, KW - 80, 30, [('EIS', 10, True, ZACHT)])
    tekst(x + 40, KY + 192, KW - 80, 90, [(eis, 17, True, TEKST)])
    ln = s.shapes.add_connector(1, E(x + 40), E(KY + 292), E(x + KW - 40), E(KY + 292)); ln.line.color.rgb = LIJN; ln.line.width = Pt(1)
    tekst(x + 40, KY + 312, KW - 80, 30, [('MET EDUFACE', 10, True, KLANT)])
    tekst(x + 40, KY + 340, KW - 80, 120, [(t, 13, False, TEKST) for t in met])
    # Wat blijft: onderaan elke kolom, zelfde plek
    vorm(MSO_SHAPE.ROUNDED_RECTANGLE, x + 32, KY + KH - 92, KW - 64, 60, vul=WIT, lijn=LIJN, rond=0.5)
    tekst(x + 56, KY + KH - 92, KW - 112, 60, [('Blijft: ' + blijft, 11, True, TEKST)], anchor=MSO_ANCHOR.MIDDLE)

# Kader onderaan
vorm(MSO_SHAPE.RECTANGLE, L, 922, 8, 96, vul=KLANT)
vorm(MSO_SHAPE.RECTANGLE, L + 8, 922, B - 8, 96, vul=TINT)
tekst(L + 40, 922, B - 80, 96, [('WAAROM NU', 10, True, KLANT),
      ('Bij nieuwe accreditaties is consistent beoordelen een aandachtspunt. De Pabo zit nu in accreditatie.', 14, True, TEKST)],
      anchor=MSO_ANCHOR.MIDDLE)

out = sys.argv[1]; prs.save(out)
p = Presentation(out)
for sl in p.slides:
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print('buiten canvas:', buiten or 'geen')
