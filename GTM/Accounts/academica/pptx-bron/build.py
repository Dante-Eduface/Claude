"""Business case Academica als bewerkbare pptx (A4 staand), voor Canva.

Bron van de inhoud: ../business-case.md en ../business-case-academica.html.
Alles in mm vanaf linksboven. Eerst `python3 render_assets.py`, dan dit script.
"""
import pathlib
from pptx import Presentation
from pptx.util import Mm, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.ns import qn

HIER = pathlib.Path(__file__).parent
A = HIER / 'assets'
UIT = HIER.parent / 'business-case-academica-bewerkbaar.pptx'

KLANT, TINT, TINT2 = '000326', 'EAF3FB', 'CFE4F6'
TEKST, ZACHT, LIJN, WIT = '1D2433', '5B6474', 'D9DDE4', 'FFFFFF'
FONT = 'Inter'
M, BREED = 18, 174          # marge en inhoudsbreedte
OPEN = '[?]'                # open waarde, in te vullen op 22-10

prs = Presentation()
prs.slide_width, prs.slide_height = Mm(210), Mm(297)
LEEG = prs.slide_layouts[6]


def rgb(h): return RGBColor.from_string(h)


# ---------- basis ----------
def vlak(s, x, y, w, h, fill=None, r=0, lijn=None, streep=False, lw=0.75):
    vorm = MSO_SHAPE.ROUNDED_RECTANGLE if r else MSO_SHAPE.RECTANGLE
    sh = s.shapes.add_shape(vorm, Mm(x), Mm(y), Mm(w), Mm(h))
    if r: sh.adjustments[0] = min(0.5, r / min(w, h))
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    else: sh.fill.background()
    if lijn:
        sh.line.color.rgb = rgb(lijn); sh.line.width = Pt(lw)
        if streep: sh.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    else: sh.line.fill.background()
    st = sh._element.find(qn('p:style'))  # themastijl weg, anders krijgt elk vlak schaduw
    if st is not None: sh._element.remove(st)
    sh.text_frame.text = ''
    return sh


def tekst(s, x, y, w, h, alineas, size=10, color=TEKST, bold=False, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.TOP, ruimte=0, bullet=False, regel=1.15):
    """alineas: str, of lijst van alinea's; een alinea is str of lijst (tekst, {opties}) runs."""
    tb = s.shapes.add_textbox(Mm(x), Mm(y), Mm(w), Mm(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    if isinstance(alineas, str): alineas = [alineas]
    for i, al in enumerate(alineas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = regel
        if i: p.space_before = Pt(ruimte)
        runs = [(al, {})] if isinstance(al, str) else al
        if bullet: runs = [('•  ', {})] + runs
        for t, o in runs:
            r = p.add_run(); r.text = t
            f = r.font; f.name = FONT; f.size = Pt(o.get('size', size))
            f.bold = o.get('bold', bold); f.color.rgb = rgb(o.get('color', color))
    return tb


def label(s, x, y, t, w=BREED):
    tekst(s, x, y, w, 5, t.upper(), size=8.5, bold=True, color=KLANT)


def kop(s, y, t, w=150):
    tekst(s, M, y, w, 18, t, size=20, bold=True, regel=1.05)


def open_(t=OPEN): return (t, {'color': ZACHT, 'bold': True})


def icoon(s, x, y, naam, d=11, rond=True):
    if rond: vlak(s, x, y, d, d, WIT, r=d / 2)
    from PIL import Image
    iw, ih = Image.open(A / f'icoon-{naam}.png').size
    schaal = d * 0.5 / max(iw, ih)
    w, h = iw * schaal, ih * schaal
    s.shapes.add_picture(str(A / f'icoon-{naam}.png'), Mm(x + (d - w) / 2), Mm(y + (d - h) / 2), Mm(w), Mm(h))


def logo(s, naam, x, y, h=None, w=None):
    from PIL import Image
    iw, ih = Image.open(A / f'logo-{naam}.png').size
    if h and not w: w = h * iw / ih
    if w and not h: h = w * ih / iw
    s.shapes.add_picture(str(A / f'logo-{naam}.png'), Mm(x), Mm(y), Mm(w), Mm(h))
    return w, h


def voet(s, nr):
    tekst(s, M, 284, 140, 5, 'Business case Eduface · Academica University of Applied Sciences · concept', size=8, color=ZACHT)
    tekst(s, M + BREED - 10, 284, 10, 5, str(nr), size=8, bold=True, color=ZACHT, align=PP_ALIGN.RIGHT)


def aanname(s, y, t, h=10):
    tekst(s, M, y, BREED, h, t, size=8.5, color=ZACHT)


def besluit(s, y, h, alineas):
    vlak(s, M, y, BREED, h, TINT)
    vlak(s, M, y, 1.2, h, KLANT)
    tekst(s, M + 6, y, BREED - 10, h, alineas, size=10, bold=True, anchor=MSO_ANCHOR.MIDDLE, ruimte=2)


def tabel(s, x, y, breedtes, rijen, num=(), totaal=False, rijhoogte=8):
    """rijen[0] is de kop. Cellen zijn str of lijst runs. num: kolomindexen rechts uitgelijnd."""
    n, k = len(rijen), len(breedtes)
    gs = s.shapes.add_table(n, k, Mm(x), Mm(y), Mm(sum(breedtes)), Mm(rijhoogte * n))
    t = gs.table
    # standaard tabelstijl uitzetten, zodat alleen onze opmaak telt
    tblPr = t._tbl.tblPr
    for attr in ('bandRow', 'firstRow'): tblPr.set(attr, '0')
    for i, b in enumerate(breedtes): t.columns[i].width = Mm(b)
    for ri, rij in enumerate(rijen):
        t.rows[ri].height = Mm(rijhoogte)
        kopr, tot = ri == 0, totaal and ri == n - 1
        for ci, cel in enumerate(rij):
            c = t.cell(ri, ci)
            c.fill.solid(); c.fill.fore_color.rgb = rgb(KLANT if kopr else TINT if tot else WIT)
            c.margin_left = c.margin_right = Mm(3); c.margin_top = c.margin_bottom = Mm(2)
            tf = c.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT if ci in num else PP_ALIGN.LEFT
            runs = [(cel, {})] if isinstance(cel, str) else cel
            for tt, o in runs:
                r = p.add_run(); r.text = tt
                f = r.font; f.name = FONT; f.size = Pt(8.5 if kopr else 9.5)
                f.bold = o.get('bold', kopr or tot or (ci == 0 and o.get('eis', False)))
                f.color.rgb = rgb(WIT if kopr else o.get('color', TEKST))
            # alleen een lijn onder de rij
            tcPr = c._tc.get_or_add_tcPr()
            for pos, zijde in enumerate(('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB')):
                ln = tcPr.makeelement(qn(zijde), {'w': '9525' if zijde == 'a:lnB' and not kopr and not tot else '0'})
                if ln.get('w') == '0':
                    ln.append(ln.makeelement(qn('a:noFill'), {}))
                else:
                    sf = ln.makeelement(qn('a:solidFill'), {}); clr = sf.makeelement(qn('a:srgbClr'), {'val': LIJN})
                    sf.append(clr); ln.append(sf)
                tcPr.insert(pos, ln)  # lijnen horen voor de vulling in tcPr
    return gs


def kaart(s, x, y, w, h, fill=TINT, **kw): return vlak(s, x, y, w, h, fill, r=4, **kw)


# ================= 1. Managementsamenvatting =================
s = prs.slides.add_slide(LEEG)
logo(s, 'academica', M, 18, h=9)
tekst(s, M + BREED - 50, 18, 50, 9, ['Business case', 'opgesteld met Eduface'], size=8.5, color=ZACHT, align=PP_ALIGN.RIGHT)
vlak(s, M, 38, 84, 6, None, r=1.5, lijn=LIJN)
tekst(s, M + 2.5, 38, 80, 6, [[('Concept voor 22 oktober 2026 · ', {}), open_(), (' = nog in te vullen', {})]],
      size=8, color=ZACHT, anchor=MSO_ANCHOR.MIDDLE)
label(s, M, 50, 'Managementsamenvatting')
kop(s, 56, 'Nederlands onderwijskundig AI-model voor formatieve feedback', w=140)
tekst(s, M, 79, 162, 34,
      'Wij stellen voor Eduface in te voeren bij alle geaccrediteerde opleidingen. Eduface doet bij elke opdracht '
      'een eerste beoordeling en een feedbackvoorstel per criterium. De docent controleert dat voorstel, past het '
      'aan en houdt het laatste woord. Zo besteden docenten minder tijd aan het formuleren van feedback, krijgt '
      'elke student formatieve feedback, en vangen we de groei op zonder evenredig meer nakijkers. Dat is een '
      'concrete invulling van het koerspunt efficiency.', size=10.5, color=ZACHT, regel=1.25)

cijfers = [
    ('geld', [('€ ', {}), open_('?')], 'besparing per jaar',
     'Bespaarde uren feedback schrijven × ons normbedrag per uur, tegen een licentie van € 18.000 per jaar.'),
    ('tijd', [open_('?'), (' uur', {})], 'minder uren feedback schrijven per jaar',
     'Over ongeveer 1.100 opdrachten. Leestijd niet meegerekend.'),
    ('mensen', [('100%', {})], 'van de studenten krijgt formatieve feedback',
     'Bij elke module. Nu is dat de helft, in twee modules.'),
]
y = 118
for ic, getal, vet, zacht in cijfers:
    kaart(s, M, y, BREED, 21)
    icoon(s, M + 6, y + 5, ic)
    tekst(s, M + 23, y, 45, 21, [getal], size=24, bold=True, color=KLANT, anchor=MSO_ANCHOR.MIDDLE)
    tekst(s, M + 72, y, 96, 21, [[(vet, {'bold': True})], [(zacht, {'color': ZACHT})]], size=9.5,
          anchor=MSO_ANCHOR.MIDDLE, ruimte=1)
    y += 24
besluit(s, y + 6, 22, [[('BESLUIT', {'size': 8.5, 'color': KLANT})],
                       'Wij vragen het MT akkoord op invoering van Eduface bij alle geaccrediteerde opleidingen, '
                       'te beginnen met een proof of value van twee weken.'])

# ================= 2. Huidige situatie =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'Huidige situatie')
kop(s, 24, 'Docenten zijn minder tijd kwijt aan het formuleren van feedback')
tekst(s, M, 44, 165, 12, 'Bij ongeveer 1.100 opdrachten per jaar is dat 460 uur nakijkwerk. Met Eduface doet het '
      'platform de eerste beoordeling en controleert de docent die.', size=10.5, color=ZACHT, regel=1.25)

SW, SG = 39, 6.0


def stroom(s, y, naam, rechts, stappen):
    tekst(s, M, y, 60, 6, naam, size=11, bold=True)
    if rechts: tekst(s, M + 74, y, 100, 6, rechts, size=9.5, bold=True, align=PP_ALIGN.RIGHT)
    for i, (docent, wat, tijd) in enumerate(stappen):
        x = M + i * (SW + SG)
        if docent: kaart(s, x, y + 8, SW, 34)
        else: kaart(s, x, y + 8, SW, 34, fill=None, lijn=LIJN, streep=True, lw=1.25)
        tekst(s, x + 3.5, y + 11, SW - 7, 5, str(i + 1), size=8.5, bold=True, color=ZACHT)
        tekst(s, x + 3.5, y + 16, SW - 7, 18, wat, size=9.5, bold=True, regel=1.1)
        tekst(s, x + 3.5, y + 35, SW - 7, 5, [tijd], size=9, bold=docent, color=KLANT if docent else ZACHT)
        if i: tekst(s, x - SG, y + 21, SG, 8, '›', size=16, color=ZACHT, align=PP_ALIGN.CENTER)


stroom(s, 62, 'Nu', 'Paper, module-opdracht van ~3.000 woorden', [
    (False, 'Student levert in via NEO', [('automatisch', {})]),
    (True, 'Docent leest de opdracht', [open_(), (' min', {})]),
    (True, 'Docent beoordeelt per criterium en formuleert de feedback', [open_(), (' min', {})]),
    (True, 'Docent vult de rubric in, cijfer gaat via NEO naar Progress', [open_(), (' min', {})]),
])
stroom(s, 110, 'Met Eduface', None, [
    (False, 'Student levert in via NEO', [('automatisch', {})]),
    (True, 'Docent leest de opdracht', [open_(), (' min, gelijk aan nu', {})]),
    (True, 'Docent controleert het voorstel van Eduface en past de feedback aan', [open_(), (' min', {})]),
    (False, 'Cijfer gaat terug naar NEO en naar Progress', [('automatisch', {})]),
])
vlak(s, M, 158, 4, 3, TINT, r=0.8)
tekst(s, M + 6, 157, 40, 5, 'Werk van de docent', size=8.5, color=ZACHT)
vlak(s, M + 44, 158, 4, 3, None, r=0.8, lijn=LIJN, streep=True)
tekst(s, M + 50, 157, 40, 5, 'Gaat automatisch', size=8.5, color=ZACHT)
aanname(s, 165, 'Lezen wordt niet sneller. De winst zit in het formuleren van feedback. Alle minuten zijn geklokt '
        'door onze eigen docenten; de proof of value meet dezelfde stappen opnieuw.')
tekst(s, M, 184, 100, 6, 'Wat kost niets doen', size=11, bold=True)
kaart(s, M, 192, BREED, 26)
tekst(s, M + 6, 196, BREED - 12, 20, [
    'Het nakijkwerk groeit van 520 naar 710 uur per jaar, door de Pabo, de theses vanaf jaar 2 en de groei van de MET.',
    'Elke extra nakijker vraagt een BKE-traject en herbeoordeling, of een externe nakijker tegen een extern tarief.',
], size=10, bullet=True, ruimte=3)
voet(s, 2)

# ================= 3 en 4. Koersplan en impact =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'Koersplan')
kop(s, 24, 'Efficiency')
tabel(s, M, 36, [62, 112], [
    ['Doel uit ons koersplan', 'Bijdrage van Eduface'],
    [[('Efficiency: "', {'bold': True}), open_('?'), ('"', {'bold': True})],
     'Minder nakijkwerk per opdracht, en groei opvangen zonder evenredig meer nakijkers.'],
])
aanname(s, 57, 'Na een jaar evalueren we de bijdrage binnen het koerspunt efficiency.', h=5)

label(s, M, 74, 'Impact')
KW = (BREED - 10) / 3
kolommen = [
    ('geld', 'Geld', [('€ ', {}), open_('?')], 'Terugverdienpunt per uur.',
     [('Elke externe beoordeling die we niet hoeven in te kopen, komt hierbovenop: ', {}), open_()]),
    ('tijd', 'Tijd', [open_('?'), (' uur', {})], 'Minder uren feedback schrijven per jaar.',
     [('Leestijd niet meegerekend.', {})]),
    ('mensen', 'Mensen', [('100%', {})],
     'Van de studenten krijgt formatieve feedback bij elke module. Nu is dat de helft, in twee modules.', None),
]
for i, (ic, naam, getal, p1, p2) in enumerate(kolommen):
    x = M + i * (KW + 5)
    kaart(s, x, 81, KW, 66)
    icoon(s, x + 5, 86, ic)
    tekst(s, x + 5, 101, KW - 10, 5, naam.upper(), size=8.5, bold=True, color=KLANT)
    tekst(s, x + 5, 107, KW - 10, 11, [getal], size=22, bold=True, color=KLANT)
    tekst(s, x + 5, 120, KW - 10, 14, p1, size=9.5)
    if p2: tekst(s, x + 5, 132, KW - 10, 14, [p2], size=9, color=ZACHT)
aanname(s, 150, 'Aannames: 1.098 opdrachten, 120 formatieve rondes en 10 theses per jaar. Overleg bij de thesis en het '
        'inwerken van nakijkers blijven gelijk. Tijden worden bevestigd in de proof of value.')
voet(s, 3)

# ================= 5 en 6. Accreditatie en toekomstbestendig =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'Accreditatie')
kop(s, 24, 'Elke beoordeling blijft navolgbaar, de docent blijft eindverantwoordelijk')
tabel(s, M, 46, [58, 116], [
    ['Eis', 'Hoe geborgd met Eduface'],
    [[('Beoordeling is navolgbaar', {'bold': True})],
     'Elk cijfer heeft een onderbouwing per rubriccriterium. Een audit trail die voldoet aan de AI Act legt elke summatieve beoordeling vast.'],
    [[('Beoordelaars oordelen consistent', {'bold': True})],
     'Een overzicht toont welke beoordelaar afwijkt van het team. De kalibratie twee keer per jaar blijft.'],
    [[('De examencommissie borgt de kwaliteit', {'bold': True})],
     'De steekproef blijft. Per beoordeling is de onderbouwing direct in te zien.'],
], rijhoogte=12)
aanname(s, 98, 'Bij nieuwe accreditaties is consistent beoordelen een aandachtspunt. De Pabo zit nu in accreditatie.', h=5)

label(s, M, 116, 'Toekomstbestendig onderwijs')
kop(s, 122, 'Docenten leren werken met AI, studenten leren AI goed gebruiken')
KW2 = (BREED - 5) / 2
blokken = [
    ('docent', 'AI-geletterdheid in het dagelijkse werk',
     'Docenten werken bij elke beoordeling met AI. Ze zien hoe een voorstel tot stand komt, sturen het bij en '
     'houden het laatste woord. Zo leren ze wat AI wel en niet kan.'),
    ('student', 'Werken met AI, en toch het leerresultaat halen',
     'Studenten mogen AI gebruiken bij het schrijven. Elke opdracht wordt inhoudelijk en kritisch beoordeeld op de '
     'leerdoelen. Aannames zonder onderbouwing en wollige alinea\'s, waar AI om bekend staat, komen daardoor niet '
     'ongemerkt door.'),
]
for i, (ic, h3, p) in enumerate(blokken):
    x = M + i * (KW2 + 5)
    kaart(s, x, 145, KW2, 72)
    icoon(s, x + 5, 150, ic)
    tekst(s, x + 5, 165, KW2 - 10, 11, h3, size=10.5, bold=True, regel=1.05)
    tekst(s, x + 5, 178, KW2 - 10, 36, p, size=9.5, regel=1.25)
voet(s, 4)

# ================= 7 en 8. Ervaring en inbegrepen =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'Ervaring')
kop(s, 24, 'Eduface draait al bij vier hogescholen en universiteiten in Nederland')
tekst(s, M, 44, BREED, 6, 'Wij zijn niet de eerste. Het model is ontwikkeld met hulp van de Radboud Universiteit.',
      size=10.5, color=ZACHT)
vlak(s, M, 54, BREED, 0.3, LIJN)
for i, (naam, h) in enumerate([('hr', 9), ('hhs', 6.5), ('tilburg', 8), ('radboud', 9)]):
    cx = M + (i + 0.5) * BREED / 4
    from PIL import Image
    iw, ih = Image.open(A / f'logo-{naam}.png').size
    w = h * iw / ih
    logo(s, naam, cx - w / 2, 62 - h / 2, h=h)
tekst(s, M, 68, BREED / 4, 5, 'lerarenopleiding', size=8, color=ZACHT, align=PP_ALIGN.CENTER)
vlak(s, M, 76, BREED, 0.3, LIJN)

label(s, M, 90, 'Inbegrepen in de licentie')
tegels = [
    ('koppeling', 'LMS-integratie', 'Eduface werkt binnen NEO. Studenten leveren in zoals nu, cijfer en feedback gaan '
     'terug naar NEO en daarna naar Progress.'),
    ('training', 'Training', 'Elke nakijker krijgt een training in het werken met Eduface naast NEO. Per opdracht '
     'leggen we de opdracht, de rubric en de feedbackinstructies samen vast.'),
]
for i, (ic, h3, p) in enumerate(tegels):
    x = M + i * (KW2 + 5)
    kaart(s, x, 97, KW2, 52)
    icoon(s, x + 5, 102, ic)
    tekst(s, x + 5, 117, KW2 - 10, 6, h3, size=10.5, bold=True)
    tekst(s, x + 5, 124, KW2 - 10, 24, p, size=9.5, regel=1.25)
aanname(s, 152, 'Inbegrepen in de prijs, geen losse kosten.', h=5)
voet(s, 5)

# ================= 9 en 10. Privacy en licentiemodel =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'Privacy')
punten = [
    'Academica blijft eigenaar van al het studentenwerk en alle data.',
    'Studentenwerk wordt niet gebruikt om AI-modellen te trainen.',
    'Studentdata gaat niet naar externe AI-aanbieders.',
    'Verwerking alleen voor het afgesproken onderwijsdoel.',
    'Versleuteld tijdens transport, bewaartermijn volgens afspraak.',
    'De docent ziet en keurt alles goed voordat de student het ziet.',
    'Verwerkersovereenkomst afgesloten (bijlage: "Verwerkersovereenkomst Eduface", versie voor onbekostigde instellingen).',
]
y = 25
for i, pt in enumerate(punten):
    h = 12 if len(pt) > 95 else 8
    icoon(s, M - 1.5, y + 0.6, 'check', d=7, rond=False)
    tekst(s, M + 8, y + 1.5, BREED - 8, h - 2, pt, size=10)
    if i < len(punten) - 1: vlak(s, M, y + h, BREED, 0.3, LIJN)
    y += h
aanname(s, y + 3, 'De verwerkersovereenkomst ligt ter beoordeling bij onze AVG-functionaris.', h=5)

label(s, M, 112, 'Licentiemodel')
kaart(s, M, 119, BREED, 26)
som = [('400', 'studenten (minimum)'), '×', ('€ 3,75', 'per student per maand'), '×', ('12', 'maanden'), '=',
       ('€ 18.000', 'per jaar')]
breedtes = [34, 8, 40, 8, 26, 8, 40]
x = M + 5
for deel, b in zip(som, breedtes):
    if isinstance(deel, str):
        tekst(s, x, 119, b, 26, deel, size=14, color=ZACHT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    else:
        if deel[0] == '€ 18.000': kaart(s, x, 122, b, 20, fill=WIT)
        tekst(s, x, 119, b, 26, [[(deel[0], {'size': 18, 'bold': True, 'color': KLANT})],
                                  [(deel[1], {'size': 8.5, 'color': ZACHT})]],
              align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ruimte=1)
    x += b
tekst(s, M, 150, 165, 10, 'Dit is de vaste licentieprijs, ook tijdens de proof of value. De koppeling met NEO, de '
      'inrichting per opdracht en de training zitten in de prijs.', size=10, regel=1.25)
tekst(s, M, 162, BREED, 20, [
    'Wij starten met ongeveer 350 actieve studenten. Tot 400 studenten blijft de prijs gelijk.',
    [('Boven de 400 studenten: ', {}), open_()],
    'Looptijd: 1 jaar, met de mogelijkheid om na 90 dagen op te zeggen.',
], size=10, bullet=True, ruimte=3)
voet(s, 6)

# ================= 11. ROI =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, 'ROI')
tekst(s, M, 24, BREED, 6, 'De prijs is opgebouwd uit drie onderdelen', size=11, bold=True)
for i, (ic, naam) in enumerate([('ai', 'AI-capaciteit'), ('tool', 'Toolfee'), ('training', 'Training')]):
    x = M + i * (KW + 5)
    kaart(s, x, 32, KW, 14)
    icoon(s, x + 3.5, 33.5, ic)
    tekst(s, x + 17, 32, KW - 20, 14, naam, size=10, bold=True, anchor=MSO_ANCHOR.MIDDLE)
mn = [open_(), (' min', {})]
tabel(s, M, 54, [40, 22, 28, 32, 52], [
    ['Opdrachttype', 'Aantal per jaar', 'Feedbacktijd nu', 'Controletijd met Eduface', 'Besparing per jaar'],
    ['Kort (KC)', '350', mn, mn, [open_(), (' uur', {})]],
    ['Paper (module-opdracht)', '748', mn, mn, [open_(), (' uur', {})]],
    ['Thesis (twee examinatoren)', '10 × 2', mn, mn, [open_(), (' uur', {})]],
    ['Totaal', '', '', '', [open_(), (' uur × normbedrag = € ', {'bold': True}), open_()]],
], num=(1, 2, 3, 4), totaal=True, rijhoogte=9)
aanname(s, 113, 'Leestijd niet meegerekend. Besparing = (feedbacktijd nu − controletijd met Eduface) × aantal × '
        'uurtarief. Voorzichtig scenario; het verwachte scenario volgt na de proof of value.')
tabel(s, M, 130, [74, 50, 50], [
    ['', 'Jaar 1', 'Jaar 2'],
    ['Licentie', '€ 18.000', [('€ 18.000 (', {}), open_(), (')', {})]],
    ['Baten (tabel hierboven)', [('€ ', {}), open_()], [('€ ', {}), open_()]],
    ['ROI', [open_()], [open_()]],
], num=(1, 2), totaal=True, rijhoogte=8)
aanname(s, 168, 'Aannames: geklokte tijden van onze docenten, te bevestigen in de proof of value. In jaar 2 tellen de '
        'Pabo, de theses vanaf jaar 2 en de groei van de MET mee. De prijs in jaar 2 hangt af van het aantal '
        'studenten boven de 400.')
vlak(s, M, 184, BREED, 16, TINT)
vlak(s, M, 184, 1.2, 16, KLANT)
tekst(s, M + 6, 184, BREED - 10, 16, [[('Ons risico is beperkt. ', {'bold': True}),
      ('Opzeggen kan na 90 dagen. Het maximale bedrag dat we inzetten om te zien of het werkt, is € 4.500.', {})]],
      size=10, anchor=MSO_ANCHOR.MIDDLE)
voet(s, 7)

# ================= 12 en 13. Risico's en scope =================
s = prs.slides.add_slide(LEEG)
label(s, M, 18, "Mogelijke risico's")
kaart(s, M, 25, BREED, 14, fill=None, lijn=LIJN, streep=True, lw=1.25)
tekst(s, M + 6, 25, BREED - 12, 14, 'Dit onderdeel vullen we samen in.', size=10, color=ZACHT, anchor=MSO_ANCHOR.MIDDLE)

label(s, M, 52, 'Scope')
kop(s, 58, 'We starten klein, en rollen uit na een geslaagde proof of value')
BW = 76
kaart(s, M, 82, BW, 64)
tekst(s, M + 5, 86, BW - 10, 6, 'Proof of value (2 weken)', size=10.5, bold=True)
tekst(s, M + 5, 94, BW - 10, 50, [
    [('Opleiding: ', {}), open_()],
    [('Echte opdrachten met onze eigen rubrics (aantal: ', {}), open_(), (')', {})],
    'We meten dezelfde stappen als in deze business case: lezen, feedback formuleren, cijfer invoeren.',
    'Plus kwaliteit: aandeel studenten met feedback per criterium, doorlooptijd, consistentie tussen beoordelaars.',
], size=9.5, bullet=True, ruimte=3)
icoon(s, M + BW + 5.5, 108, 'pijl', d=11, rond=False)
xr = M + BREED - BW
kaart(s, xr, 82, BW, 64, fill=WIT, lijn=TINT2, lw=1.25)
tekst(s, xr + 5, 86, BW - 10, 6, 'Uitrol', size=10.5, bold=True)
tekst(s, xr + 5, 94, BW - 10, 50, [
    'Alle geaccrediteerde opleidingen: SO, MILE, AD-DEP, PMKC, PHKC, MET en MBA',
    'Later de Pabo, na de accreditatie',
    'Formatieve feedback bij elke module',
], size=9.5, bullet=True, ruimte=3)
vlak(s, M, 151, BREED, 15, TINT)
vlak(s, M, 151, 1.2, 15, KLANT)
tekst(s, M + 6, 151, BREED - 10, 15, [[('Door als: ', {'bold': True}),
      ('de koppeling met NEO werkt, inclusief de cijferterugkoppeling, en de beoordeling van ons praktijkgerichte '
       'werk voldoet aan de vooraf vastgelegde criteria.', {})]], size=9.5, anchor=MSO_ANCHOR.MIDDLE)
voet(s, 8)

prs.save(UIT)
print('opgeslagen:', UIT)
