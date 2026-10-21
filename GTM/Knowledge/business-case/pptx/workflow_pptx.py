from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import sys

PX = 6350  # 1 px op een 1920x1080 raster
KLANT = RGBColor(0x1F, 0x4E, 0x79)      # placeholder: hoofdkleur klant
TINT = RGBColor(0xEE, 0xF3, 0xF8)       # placeholder: lichte tint klantkleur
TEKST = RGBColor(0x1D, 0x24, 0x33)
ZACHT = RGBColor(0x5B, 0x64, 0x74)
FONT = 'Inter'

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(1920 * PX), Emu(1080 * PX)
s = prs.slides.add_slide(prs.slide_layouts[6])

def tekst(x, y, w, h, regels, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(Emu(x * PX), Emu(y * PX), Emu(w * PX), Emu(h * PX))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, (t, size, bold, kleur) in enumerate(regels):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r = p.add_run(); r.text = t
        r.font.name, r.font.size, r.font.bold = FONT, Pt(size), bold
        r.font.color.rgb = kleur
    return tb

def kaart(x, y, w, h, nr, wat, tijd):
    k = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(x * PX), Emu(y * PX), Emu(w * PX), Emu(h * PX))
    k.adjustments[0] = 0.09
    k.fill.solid(); k.fill.fore_color.rgb = TINT
    k.line.fill.background()
    k.shadow.inherit = False
    tekst(x + 32, y + 28, w - 64, 40, [(nr, 11, True, ZACHT)])
    tekst(x + 32, y + 62, w - 64, 90, [(wat, 17, True, TEKST)])
    tekst(x + 32, y + h - 70, w - 64, 44, [(tijd, 22, True, KLANT)])

def pijl(x, y):
    p = s.shapes.add_shape(MSO_SHAPE.CHEVRON, Emu(x * PX), Emu(y * PX), Emu(18 * PX), Emu(28 * PX))
    p.fill.solid(); p.fill.fore_color.rgb = ZACHT
    p.line.fill.background(); p.shadow.inherit = False

L, W_K, GAP, H_K = 120, 800, 80, 220
tekst(L, 96, 1200, 30, [('DE HUIDIGE SITUATIE', 11, True, KLANT)])
tekst(L, 132, 1680, 60, [('Docenten besteden meer tijd aan feedback dan aan lezen', 24, True, TEKST)])
tekst(L, 196, 1680, 70, [('Het lezen van een opdracht blijft werk van de docent. De winst zit in het beoordelen en formuleren van de feedback. Percentages zijn aandelen van de totale nakijktijd per opdracht.', 13, False, ZACHT)])

for rij, (kop, y, tot, a, b) in enumerate([
    ('Nu', 300, '100% van de nakijktijd', ('1', 'Docent leest de opdracht', '40%'),
                ('2', 'Docent beoordeelt per criterium en formuleert de feedback', '60%')),
    ('Met Eduface', 640, '70% van de nakijktijd, 30% minder', ('1', 'Docent leest de opdracht', '40%, gelijk aan nu'),
                ('2', 'Docent controleert het voorstel van Eduface en past de feedback aan', '30%')),
]):
    tekst(L, y, 600, 44, [(kop, 18, True, TEKST)])
    tekst(L + W_K + GAP + W_K - 600, y + 6, 600, 40, [(tot, 13, True, TEKST)]).text_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT
    kaart(L, y + 60, W_K, H_K, *a)
    pijl(L + W_K + GAP / 2 - 9, y + 60 + H_K / 2 - 14)
    kaart(L + W_K + GAP, y + 60, W_K, H_K, *b)

out = sys.argv[1]
prs.save(out)
p = Presentation(out)
for i, sl in enumerate(p.slides, 1):
    buiten = [sh.shape_id for sh in sl.shapes if sh.left < 0 or sh.top < 0
              or sh.left + sh.width > p.slide_width or sh.top + sh.height > p.slide_height]
    print(i, 'buiten canvas:', buiten or 'geen')
