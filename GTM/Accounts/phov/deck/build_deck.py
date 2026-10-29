"""PHOV-deck, oktober 2026. Zie deckbuild.py voor de renderers.

Op de slide staat alleen waar de kijker naar kijkt. Dante's volledige tekst staat
per slide in de notities en komt als sprekersnotitie in de pptx.

    python3 build_deck.py            # alle slides, preview + pptx
    python3 build_deck.py 03-nu      # alleen deze preview
"""
import sys
from deckbuild import (rect, pic, text, title, tile, foot, cols,
                       render_pptx, render_html, shoot,
                       NAVY, GREEN, INK50, INK100, INK500, WHITE, HEAD, M)

S = []
# Titels aan of uit voor het hele deck. Dante wil ze (29-10-2026).
TITELS = True

# Ritme: navy en wit om en om (Dante, 29-10-2026), zodat de slides niet op
# elkaar lijken. Oneven slides navy, even slides wit.
VLAK = '0E3546'               # vlak op navy
LIJN_D = '1E4656'             # lijn op navy
MUTED_D = '8FA9B4'            # tweede tekstkleur op navy, ruim boven 4,5:1

def thema(dark):
    return dict(fg=WHITE if dark else NAVY, muted=MUTED_D if dark else INK500,
                lijn=LIJN_D if dark else INK100, ic='mint' if dark else 'navy')

def slidetitel(t, dark=False): return title(t, dark) if TITELS else []

def add(naam, els, notes='', dark=False):
    # De pptx kent geen achtergrondkleur per slide, dus een navy vlak onderop.
    if dark:
        els = [rect(0, 0, 1920, 1080, NAVY)] + els
    S.append((naam, els, notes, dark))

# ---------------------------------------------------------------- 1 aanleiding, navy
# De vraag aan het bureau, en het advies dat ze al kenden. Het verschil met
# "Al bekend." zit in het gewicht, niet in de kleur.
D = True; T = thema(D)
els = slidetitel('Aanleiding', D)
els += [text(M, 330, 1920 - 2 * M, 140, 'Hoe zetten we AI in ons onderwijs in,\n'
             'en hoe helpen we docenten daarbij?', font=HEAD, size=56, bold=True,
             color=T['fg'], ls=1.2)]
PILLEN = [('Toetstermen aanpassen', 450), ('Docenten meenemen', 400)]
x = (1920 - (sum(w for _, w in PILLEN) + 28 * len(PILLEN) + 200)) / 2
for lbl, w in PILLEN:
    els += [rect(x, 590, w, 76, VLAK, r=38),
            text(x, 609, w, 40, lbl, size=34, color=WHITE, ls=1.0)]
    x += w + 28
els += [text(x + 12, 609, 200, 40, 'Al bekend.', size=34, bold=True, color=GREEN,
             align='left', ls=1.0)]
els += foot(dark=D, page=1)
add('01-aanleiding', els, dark=D, notes="""Anderhalf jaar geleden heeft PHOV een bureau ingehuurd. De vraag was hoe ze AI in hun onderwijs kunnen inzetten en hoe ze docenten daarbij helpen.
Het advies was "toetstermen aanpassen" en "docenten meenemen". Dat wisten ze al.""")

# ---------------------------------------------------------------- 2 doel, wit
c3, w3 = cols(3)
D = False
els = slidetitel('Doel', D)
for cx, (ic, kop) in zip(c3, [('lesgeven', 'Docenten met AI'), ('boek', 'Open boek'),
                              ('lagen', 'Curriculum')]):
    els += tile(cx, 380, ic, 'green', 180)
    els += [text(cx - w3 / 2 - 30, 600, w3 + 60, 60, kop, font=HEAD, size=52, bold=True, ls=1.0)]
els += foot(page=2)
add('02-doel', els, notes="""Wat ze wilden:
1. Docenten die AI in hun vakgebied gebruiken, met een pragmatische partner ernaast
2. Open-boek tentamens behouden (AI-detectie)
3. Curriculumontwikkeling""")

# ---------------------------------------------------------------- 3 huidige situatie, navy
# Per stap wie en wat er gebeurt. Zes kolommen, zodat moduleleider en "cijfer
# vastgesteld" recht onder elkaar staan, net als de twee cursusbureaus.
# Alles neutraal: dit beschrijft, het oordeel komt op de probleemslide.
c6, w6 = cols(6)
TS = 96
D = True; T = thema(D)

def strook(y, label, stappen):
    out = [text(M, y, 600, 40, label, font=HEAD, size=36, bold=True, color=T['muted'],
                align='left', ls=1.0)]
    ty = y + 58
    out.append(rect(c6[0], ty + TS / 2 - 2, c6[len(stappen) - 1] - c6[0], 4, T['lijn']))
    for cx, (ic, rol, wat) in zip(c6, stappen):
        out += [rect(cx - 70, ty - 6, 140, TS + 12, NAVY)]
        out += tile(cx, ty, ic, 'navy', TS)
        out += [text(cx - 146, ty + TS + 14, 292, 40, rol, font=HEAD, size=34,
                     bold=True, color=T['fg'], ls=1.0),
                text(cx - 170, ty + TS + 56, 340, 90, wat, size=32, color=T['muted'], ls=1.2)]
    return out

els = slidetitel('Huidige situatie', D)
els += strook(236, 'Tentamens', [
    ('pen', 'Student', 'maakt toets'),
    ('cijfers', 'Docent', 'punten, feedback'),
    ('usercheck', 'Moduleleider', 'stelt cijfer vast'),
    ('data', 'Cursusbureau', 'krijgt eindcijfer'),
])
els += strook(570, 'Schrijfopdrachten', [
    ('inleveren', 'Student', 'levert in'),
    ('filepen', 'Docent', 'wisselend format'),
    ('aftekenen', 'Cijfer', 'vastgesteld'),
    ('check', 'Cursusbureau', 'checkt taal'),
    ('mail', 'Secretariaat', 'zet het open'),
    ('studenten', 'Student', 'ziet resultaat'),
])
els += foot(dark=D, page=3)
add('03-nu', els, dark=D, notes="""Tentamens
1. Studenten maken het tentamen
2. Het antwoord van de student gaat terug naar de docent, die punten en feedback geeft
3. De moduleleider controleert en stelt het cijfer vast
4. Daarna gaat het naar het cursusbureau

Schrijfopdrachten
1. De student levert in via de leeromgeving (individueel, duo of groep)
2. De docent krijgt een melding dat hij kan nakijken
3. Elke docent geeft feedback in zijn eigen format, en elke opdracht heeft weer een ander format. Dat uploadt hij.
4. Het cijfer wordt vastgesteld
5. Het cursusbureau kijkt het nog na op taal en rariteiten
6. Het secretariaat zet het open en de student ziet zijn cijfer en feedback""")

# ---------------------------------------------------------------- 4 probleem, wit
# Twee open kolommen, geen vlakken: een lijst pijnpunten met een icoon per regel.
# Oplossing krijgt bewust een andere vorm (kaarten met vinkjes op navy).
D = False
els = slidetitel('Probleem', D)
GELD = [('klok', 'Betaald per beoordelingsuur'), ('pen', 'Feedback is een eis')]
CONS = [('verschillen', 'Oordelen lopen uiteen'), ('weegschaal', 'Nieuwe rubric ongetest'),
        ('aftekenen', 'Gesprek over het formulier'), ('groep', 'Directie als breekijzer')]
for x0, kop, punten in [(M, 'Geld', GELD), (1000, 'Consistentie', CONS)]:
    els += [text(x0, 270, 700, 52, kop, font=HEAD, size=52, bold=True, align='left', ls=1.0),
            rect(x0, 344, 680, 4, NAVY)]
    for i, (ic, lbl) in enumerate(punten):
        y = 400 + i * 100
        els += [pic(f'assets/icon-{ic}-navy.png', x0, y, 56, 56),
                text(x0 + 84, y + 9, 620, 44, lbl, size=36, color=NAVY, align='left', ls=1.0)]
els += foot(page=4)
add('04-probleem', els, notes="""Geld
- PHOV betaalt docenten voor elk uur dat ze beoordelen ("wij betalen voor de tijd die ze beoordelen")
- En PHOV eist dat ze feedback geven ("wij eisen dat ze feedback geven")

Consistentie
- Vooraf liggen de oordelen van beoordelaars ver uit elkaar, pas na overleg komen ze dichter bij elkaar ("dan zie je dat de bandbreedte groot is, dan gaan ze overleggen met elkaar")
- Daarom kalibreren ze scripties minstens een keer per twee jaar. De nieuwe rubric is nog niet getest.
- Kalibratie hoort over de inhoud te gaan ("Het gaat om de inhoud. Je moet challengen."), maar gaat soms over handtekeningen op een formulier
- De directie schuift zelf aan om mensen scherp te houden, als breekijzertje.""")

# ---------------------------------------------------------------- 5 oplossing, navy
# Zelfde volgorde als het probleem (geld links, consistentie rechts), maar als
# twee kaarten met groene vinkjes, zodat je het verschil ziet bij het doorklikken.
D = True; T = thema(D)
els = slidetitel('Oplossing', D)
GELD = ['Start met een eerste versie', 'Minder beoordelingsuren', 'Eerder een cijfer']
CONS = ['Dezelfde rubric voor elke opdracht', 'Cijferopbouw per criterium',
        'Kalibreren begint bij de inhoud']
for x0, kop, punten in [(M, 'Geld besparen', GELD), (980, 'Consistentie', CONS)]:
    els += [rect(x0, 250, 820, 570, VLAK, r=32),
            text(x0 + 56, 300, 700, 48, kop, font=HEAD, size=48, bold=True, color=GREEN,
                 align='left', ls=1.0)]
    for i, lbl in enumerate(punten):
        y = 420 + i * 110
        els += [rect(x0 + 56, y, 56, 56, NAVY, r=14),
                pic('assets/icon-check-mint.png', x0 + 70, y + 14, 28, 28),
                text(x0 + 140, y + 9, 640, 44, lbl, size=36, color=WHITE, align='left', ls=1.0)]
els += foot(dark=D, page=5)
add('05-oplossing', els, dark=D, notes="""Geld besparen
- De docent begint niet met een leeg vel maar met een eerste versie van feedback en cijfer. Hij kijkt dus sneller na en PHOV betaalt minder beoordelingsuren.
- Bijkomstigheid: de doorlooptijd van zes weken wordt korter. Studenten krijgen eerder hun cijfer.

Consistentie
- Elke opdracht wordt op dezelfde rubric gescoord, met een uitlegbare cijferopbouw per criterium. Zo leggen alle beoordelaars dezelfde maat aan.
- De kalibratie begint bij een beoordeling per criterium. Het gesprek gaat dan over de inhoud, niet over het formulier. (Eigen redenering, geen belofte.)

Koppeling met de huidige situatie: de AI Exam Grader hoort bij Tentamens, de AI Paper Grader bij Schrijfopdrachten. Allebei live.""")

# ---------------------------------------------------------------- 6 prijs, wit
# Naar het UTI-voorbeeld van Dante: navy vlak met het getal links en de
# voorwaarden met vinkjes rechts, eronder wat het dekt. Achter de 1.500 bewust
# geen periode tot Dante die bevestigt. Wat het dekt staat in Platform/product.md.
D = False
els = slidetitel('Prijs', D)
els += [rect(M, 250, 1920 - 2 * M, 380, NAVY, r=32),
        text(190, 312, 420, 230, '€10', font=HEAD, size=230, bold=True, color=WHITE,
             align='left', ls=1.0),
        text(600, 350, 380, 150, 'per student,\nper maand', font=HEAD, size=56, bold=True,
             color=WHITE, align='left', ls=1.15),
        rect(1000, 300, 2, 280, LIJN_D)]
for i, lbl in enumerate(['Minimaal 150 studenten',
                         'Minimaal €1.500 voor het\nreserveren van AI-capaciteit']):
    y = 330 + i * 120
    els += [rect(1060, y, 56, 56, VLAK, r=14),
            pic('assets/icon-check-mint.png', 1074, y + 14, 28, 28),
            text(1140, y + 9, 640, 100, lbl, size=36, color=WHITE, align='left', ls=1.25)]
els += [rect(M, 670, 1920 - 2 * M, 2, INK100),
        text(M, 700, 600, 40, 'Wat dat dekt', size=32, color=INK500, align='left', ls=1.0)]
c4, w4 = cols(4)
for i, (ic, lbl) in enumerate([('filepen', 'AI Paper Grader'), ('cijfers', 'AI Exam Grader'),
                               ('rubric', 'Rubric-scoring'), ('usercheck', 'Docent beslist')]):
    x0 = M + i * (w4 + 72)
    els += [rect(x0, 760, 72, 72, INK50, r=18),
            pic(f'assets/icon-{ic}-navy.png', x0 + 18, 778, 36, 36),
            text(x0 + 96, 776, w4 - 96, 40, lbl, size=32, color=NAVY, align='left', ls=1.0)]
els += foot(page=6)
add('06-prijs', els, notes="""- 10 euro per student per maand, minimaal 150 studenten
- Minimaal 1.500 euro voor het reserveren van AI-capaciteit

Wat het dekt: AI Paper Grader (schrijfopdrachten) en AI Exam Grader (tentamens), allebei live. Rubric-scoring met uitlegbare cijferopbouw. De docent keurt elke opmerking en elk cijfer goed voordat de student iets ziet.""")

# ---------------------------------------------------------------- 7 demo, navy
# Leeg kader voor de screenshot, 16:9. Het deck eindigt hier.
D = True
DT = 250 if TITELS else 120
DH = 820 - DT
DW = DH * 16 / 9
els = slidetitel('Demo', D)
els += [rect((1920 - DW) / 2, DT, DW, DH, VLAK, r=28),
        text((1920 - DW) / 2, DT + DH / 2 - 22, DW, 44, 'Screenshot volgt', size=36,
             color=WHITE, ls=1.0)]
els += foot(dark=D, page=7)
add('07-demo', els, dark=D)

# ---------------------------------------------------------------- render
alleen = sys.argv[1:]
for naam, els, notes, dark in S:
    if alleen and naam not in alleen:
        continue
    print(shoot(render_html(els, f'preview/{naam}.html', dark=dark), f'preview/{naam}.png'))
if not alleen:
    print(render_pptx([e for _, e, _, _ in S], 'phov-deck-bewerkbaar.pptx',
                      notes=[n for _, _, n, _ in S]))
