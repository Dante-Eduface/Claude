"""Kostenpagina (variant A) van de business case als bewerkbare pptx.
De grafiek is een echte PowerPoint-grafiek: rechtsklik > Gegevens bewerken om cijfers aan te passen.
Gebruik: python3 kosten_pptx.py uitvoer.pptx"""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
import sys

# Invoer: pas deze getallen per klant aan
TARIEF = 35
OPDR_J1, OPDR_J2 = 1057, 1307
EDUFACE_MAAND = 1500

PX = 6350
KLANT = RGBColor(0x0B, 0x15, 0x33)
TINT = RGBColor(0xEE, 0xF1, 0xF7)
NU = RGBColor(0x9A, 0xA3, 0xB2)
LIJN = RGBColor(0xD9, 0xDD, 0xE4)
TEKST = RGBColor(0x1D, 0x24, 0x33)
ZACHT = RGBColor(0x5B, 0x64, 0x74)
FONT = 'Inter'
E = lambda v: Emu(int(v * PX))
eur = lambda v: '€ ' + f'{round(v):,}'.replace(',', '.')

prs = Presentation()
prs.slide_width, prs.slide_height = E(1920), E(1080)
s = prs.slides.add_slide(prs.slide_layouts[6])

def vorm(soort, x, y, w, h, vul):
    v = s.shapes.add_shape(soort, E(x), E(y), E(w), E(h))
    v.fill.solid(); v.fill.fore_color.rgb = vul; v.line.fill.background(); v.shadow.inherit = False
    return v

def lijn(x1, y1, x2, y2):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, E(x1), E(y1), E(x2), E(y2))
    c.line.color.rgb = LIJN; c.line.width = Pt(1)

def tekst(x, y, w, h, regels, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, (t, size, bold, kleur) in enumerate(regels):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r = p.add_run(); r.text = t
        r.font.name, r.font.size, r.font.bold, r.font.color.rgb = FONT, Pt(size), bold, kleur

L, B = 120, 1680
nu_j1, nu_j2 = TARIEF * OPDR_J1, TARIEF * OPDR_J2
nu_cum, ed_cum, a, b = [], [], 0, 0
for m in range(1, 25):
    a += (nu_j1 if m <= 12 else nu_j2) / 12; b += EDUFACE_MAAND
    nu_cum.append(round(a)); ed_cum.append(b)

tekst(L, 70, B, 30, [('KOSTEN', 11, True, KLANT)])
tekst(L, 102, B, 60, [('Eduface kost de helft van wat nakijken nu kost', 26, True, TEKST)])
tekst(L, 168, 1500, 70, [(f'Nakijken kost nu gemiddeld € {TARIEF} per opdracht, door eigen docenten en externe beoordelaars samen. '
                          'Eduface kost een vast bedrag per maand, ook als het aantal opdrachten groeit.', 14, False, ZACHT)])

# Betaalgegevens
lijn(L, 252, L + B, 252); lijn(L, 352, L + B, 352)
for i, (getal, label) in enumerate([(eur(EDUFACE_MAAND), 'per maand, vooraf'), (eur(EDUFACE_MAAND * 12), 'per jaar'),
                                    (eur(TARIEF), 'gemiddeld per opdracht nu')]):
    tekst(L + i * 340, 266, 320, 80, [(getal, 20, True, TEKST), (label, 12, False, ZACHT)])

# Grafiek
tekst(L, 372, B, 30, [(f'Opgeteld na twee jaar: nakijken nu {eur(nu_cum[-1])}, Eduface {eur(ed_cum[-1])}. '
                       f'Verschil {eur(nu_cum[-1] - ed_cum[-1])}.', 13, True, TEKST)])
cd = CategoryChartData()
cd.categories = [f'mnd {m}' if m in (1, 6, 12, 18, 24) else ' ' * m for m in range(1, 25)]
cd.add_series('Nakijken nu', nu_cum)
cd.add_series('Eduface', ed_cum)
gf = s.shapes.add_chart(XL_CHART_TYPE.LINE, E(L - 10), E(410), E(B + 10), E(440), cd)
ch = gf.chart
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False
ch.legend.font.size = Pt(11); ch.legend.font.color.rgb = ZACHT; ch.legend.font.name = FONT
va = ch.value_axis
va.maximum_scale, va.minimum_scale, va.major_unit = 90000, 0, 30000
va.tick_labels.number_format = '#,##0'; va.tick_labels.number_format_is_linked = False
va.tick_labels.font.size = Pt(10); va.tick_labels.font.color.rgb = ZACHT
va.major_gridlines.format.line.color.rgb = RGBColor(0xEC, 0xEE, 0xF2)
va.format.line.fill.background()
ca = ch.category_axis
ca.tick_labels.font.size = Pt(10); ca.tick_labels.font.color.rgb = ZACHT
ca.format.line.color.rgb = NU
from pptx.oxml.ns import qn
from lxml import etree
skip = etree.Element(qn('c:tickLblSkip')); skip.set('val', '6')
anker = ca._element.find(qn('c:noMultiLvlLbl'))
if anker is not None: anker.addprevious(skip)
else: ca._element.append(skip)
for serie, kleur, breed in [(ch.plots[0].series[0], NU, 2.5), (ch.plots[0].series[1], KLANT, 2.5)]:
    serie.format.line.color.rgb = kleur; serie.format.line.width = Pt(breed); serie.smooth = False
    serie.marker.style = None
    from pptx.enum.chart import XL_MARKER_STYLE
    serie.marker.style = XL_MARKER_STYLE.NONE
    pt = serie.points[23]
    dl = pt.data_label; dl.position = XL_LABEL_POSITION.RIGHT
    r = dl.text_frame.paragraphs[0].add_run(); r.text = eur(serie.values[23])
    r.font.size = Pt(11); r.font.bold = True; r.font.color.rgb = TEKST; r.font.name = FONT

# Kader
vorm(MSO_SHAPE.RECTANGLE, L, 872, 8, 92, KLANT)
vorm(MSO_SHAPE.RECTANGLE, L + 8, 872, B - 8, 92, TINT)
tekst(L + 36, 872, B - 72, 92, [('BIJ GROEI', 10, True, KLANT),
      (f'Jaar 2 telt {OPDR_J2 - OPDR_J1} opdrachten meer. De kosten van nakijken stijgen mee, de prijs van Eduface blijft gelijk.', 14, True, TEKST)],
      anchor=MSO_ANCHOR.MIDDLE)

tekst(L, 984, B, 70, [(f'Jaar 1: {OPDR_J1:,} opdrachten, jaar 2: {OPDR_J2:,} opdrachten. '.replace(',', '.') +
      'Prijs blijft gelijk zolang het aantal studenten binnen dezelfde staffel valt. '
      f'€ {TARIEF} is een gemiddeld tarief over alle opdrachttypes, van kennischeck tot thesis, intern en extern. '
      'Uren van eigen docenten tellen mee: die kunnen ook naar lesgeven en training.', 10, False, ZACHT)])

out = sys.argv[1]; prs.save(out)
p = Presentation(out)
for sl in p.slides:
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print('buiten canvas:', buiten or 'geen')
