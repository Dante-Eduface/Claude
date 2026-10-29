"""PHOV-deck, oktober 2026. Zie deckbuild.py voor de renderers.

Op de slide staat alleen waar de kijker naar kijkt. Dante's volledige tekst staat
per slide in NOTES en komt als sprekersnotitie in de pptx.

    python3 build_deck.py            # alle slides, preview + pptx
    python3 build_deck.py 02-nu      # alleen deze preview
"""
import sys
from deckbuild import (rect, oval, pic, text, title, tile, foot, cols,
                       render_pptx, render_html, shoot,
                       NAVY, AMBER, GREEN, GREEN_DEEP, TINT_A, TINT_G, INK50, INK100,
                       INK200, INK500, WHITE, HEAD, BODY, M)

S = []
# Titels aan of uit voor het hele deck. Dante wil ze (29-10-2026), het briefing
# voor slide 4 tot en met 7 niet. Eén schakelaar, zodat het consistent blijft.
TITELS = True
def slidetitel(t, dark=False): return title(t, dark) if TITELS else []
def add(naam, els, notes='', dark=False): S.append((naam, els, notes, dark))

# Elke slide begint met een korte titel (Dante, 29-10-2026). Daaronder alleen
# wat het publiek moet zien; wat Dante vertelt staat in de notities.

# ---------------------------------------------------------------- 1 aanleiding
# De vraag aan het bureau, en het advies dat ze al kenden. Advies in navy:
# het verschil met "Al bekend." zit in het gewicht, niet in de kleur.
els = slidetitel('Aanleiding')
els += [text(M, 330, 1920 - 2 * M, 140, 'Hoe zetten we AI in ons onderwijs in,\n'
             'en hoe helpen we docenten daarbij?', font=HEAD, size=56, bold=True, ls=1.2)]
PILLEN = [('Toetstermen aanpassen', 450), ('Docenten meenemen', 400)]
AB = 'Al bekend.'
x = (1920 - (sum(w for _, w in PILLEN) + 28 * len(PILLEN) + 200)) / 2
for lbl, w in PILLEN:
    els += [rect(x, 590, w, 76, INK50, r=38),
            text(x, 609, w, 40, lbl, size=34, color=NAVY, ls=1.0)]
    x += w + 28
els += [text(x + 12, 609, 200, 40, AB, size=34, bold=True, color=NAVY, align='left', ls=1.0)]
els += foot(page=1)
add('01-aanleiding', els, notes="""Anderhalf jaar geleden heeft PHOV een bureau ingehuurd. De vraag was hoe ze AI in hun onderwijs kunnen inzetten en hoe ze docenten daarbij helpen.
Het advies was "toetstermen aanpassen" en "docenten meenemen". Dat wisten ze al.""")

# ---------------------------------------------------------------- 2 doel
c3, w3 = cols(3)
els = slidetitel('Doel')
for cx, (ic, kop) in zip(c3, [('lesgeven', 'Docenten met AI'), ('boek', 'Open boek'),
                              ('lagen', 'Curriculum')]):
    els += tile(cx, 380, ic, 'green', 180)
    els += [text(cx - w3 / 2 - 30, 600, w3 + 60, 60, kop, font=HEAD, size=52, bold=True, ls=1.0)]
els += foot(page=2)
add('02-doel', els, notes="""Wat ze wilden:
1. Docenten die AI in hun vakgebied gebruiken, met een pragmatische partner ernaast
2. Open-boek tentamens behouden (AI-detectie)
3. Curriculumontwikkeling""")

# ---------------------------------------------------------------- 3 huidige situatie
# Per stap wie en wat er gebeurt.
# Zes kolommen, zodat moduleleider en "cijfer vastgesteld" recht onder elkaar
# staan, net als de twee cursusbureaus. Alles neutraal: dit beschrijft, het
# oordeel komt op de probleemslide.
c6, w6 = cols(6)
TS = 96

def strook(y, label, stappen):
    out = [text(M, y, 600, 40, label, font=HEAD, size=36, bold=True, color=INK500,
                align='left', ls=1.0)]
    ty = y + 58
    out.append(rect(c6[0], ty + TS / 2 - 2, c6[len(stappen) - 1] - c6[0], 4, INK100))
    for cx, (ic, rol, wat) in zip(c6, stappen):
        out += [rect(cx - 70, ty - 6, 140, TS + 12, WHITE)]
        out += tile(cx, ty, ic, 'navy', TS)
        out += [text(cx - 146, ty + TS + 14, 292, 40, rol, font=HEAD, size=34,
                     bold=True, ls=1.0),
                text(cx - 170, ty + TS + 56, 340, 90, wat, size=32, color=INK500,
                     ls=1.2)]
    return out

els = slidetitel('Huidige situatie')
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
els += foot(page=3)
add('03-nu', els, notes="""Tentamens
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

# ---------------------------------------------------------------- 4 en 5, twee blokken
# Probleem en oplossing in dezelfde twee blokken, in dezelfde volgorde: links
# geld in navy, rechts consistentie licht. Per punt een icoon en een regel.
# Woorden van PHOV: beoordelen, eisen, beoordelaars, kalibreren.
TOP = 250 if TITELS else 120
LW = 720                      # breedte geldblok
RX = M + LW + 40              # start consistentieblok

def blok(x, w, label, punten, dark):
    fg = WHITE if dark else NAVY
    out = [rect(x, TOP, w, 820 - TOP, NAVY if dark else INK50, r=32),
           text(x + 56, TOP + 48, w - 112, 48, label, font=HEAD, size=44, bold=True,
                color=GREEN if dark else NAVY, align='left', ls=1.0)]
    stap = (820 - TOP - 170) / 4
    for i, (ic, lbl) in enumerate(punten):
        y = TOP + 150 + i * stap
        out += [pic(f'assets/icon-{ic}-{"mint" if dark else "navy"}.png', x + 56, y, 56, 56),
                text(x + 140, y + 9, w - 180, 44, lbl, size=36, color=fg, align='left', ls=1.0)]
    return out

def tweeluik(titel, geld, cons, page):
    els = slidetitel(titel)
    els += blok(M, LW, geld[0], geld[1], True)
    els += blok(RX, 1920 - M - RX, cons[0], cons[1], False)
    return els + foot(page=page)

els = tweeluik('Probleem',
    ('Geld', [('klok', 'Betaald per beoordelingsuur'),
              ('pen', 'Feedback is een eis')]),
    ('Consistentie', [('verschillen', 'Oordelen van beoordelaars lopen uiteen'),
                      ('weegschaal', 'Kalibreren, nieuwe rubric ongetest'),
                      ('aftekenen', 'Gesprek over het formulier'),
                      ('groep', 'Directie als breekijzer')]), 4)
add('04-probleem', els, notes="""Geld
- PHOV betaalt docenten voor elk uur dat ze beoordelen ("wij betalen voor de tijd die ze beoordelen")
- En PHOV eist dat ze feedback geven ("wij eisen dat ze feedback geven")

Consistentie
- Vooraf liggen de oordelen van beoordelaars ver uit elkaar, pas na overleg komen ze dichter bij elkaar ("dan zie je dat de bandbreedte groot is, dan gaan ze overleggen met elkaar")
- Daarom kalibreren ze scripties minstens een keer per twee jaar. De nieuwe rubric is nog niet getest.
- Kalibratie hoort over de inhoud te gaan ("Het gaat om de inhoud. Je moet challengen."), maar gaat soms over handtekeningen op een formulier
- De directie schuift zelf aan om mensen scherp te houden, als breekijzertje.""")

els = tweeluik('Oplossing',
    ('Geld besparen', [('filepen', 'Start met een eerste versie'),
                       ('klok', 'Minder beoordelingsuren'),
                       ('historie', 'Eerder een cijfer')]),
    ('Consistentie', [('rubric', 'Dezelfde rubric voor elke opdracht'),
                      ('cijfers', 'Uitlegbare cijferopbouw per criterium'),
                      ('gesprek', 'Kalibreren begint bij de inhoud')]), 5)
add('05-oplossing', els, notes="""Geld besparen
- De docent begint niet met een leeg vel maar met een eerste versie van feedback en cijfer. Hij kijkt dus sneller na en PHOV betaalt minder beoordelingsuren.
- Bijkomstigheid: de doorlooptijd van zes weken wordt korter. Studenten krijgen eerder hun cijfer.

Consistentie
- Elke opdracht wordt op dezelfde rubric gescoord, met een uitlegbare cijferopbouw per criterium. Zo leggen alle beoordelaars dezelfde maat aan.
- De kalibratie begint bij een beoordeling per criterium. Het gesprek gaat dan over de inhoud, niet over het formulier. (Eigen redenering, geen belofte.)

Koppeling met de huidige situatie: de AI Exam Grader hoort bij Tentamens, de AI Paper Grader bij Schrijfopdrachten. Allebei live.""")

# ---------------------------------------------------------------- 6 prijs
# Twee getallen in navy, geen groen: een prijs is geen goed nieuws-getal.
# Achter de 1.500 bewust geen periode tot Dante die bevestigt.
c2, w2 = cols(2)
PT = 300 if TITELS else 220
els = slidetitel('Prijs')
for cx, (bedrag, r1, r2) in zip(c2, [('€10', 'per student per maand', 'minimaal 150 studenten'),
                                     ('€1.500', 'minimaal', 'voor het reserveren van AI-capaciteit')]):
    els += [text(cx - w2 / 2, PT, w2, 190, bedrag, font=HEAD, size=180, bold=True, ls=1.0),
            text(cx - w2 / 2, PT + 230, w2, 50, r1, font=HEAD, size=44, bold=True, ls=1.0),
            text(cx - w2 / 2, PT + 298, w2, 44, r2, size=34, color=INK500, ls=1.0)]
els += [rect(959, PT, 2, 340, INK100)] + foot(page=6)
add('06-prijs', els, notes="""- 10 euro per student per maand, minimaal 150 studenten
- Minimaal 1.500 euro voor het reserveren van AI-capaciteit""")

# ---------------------------------------------------------------- 7 demo
# Leeg kader voor de screenshot, 16:9. Het deck eindigt hier.
DT = 250 if TITELS else 120
DH = 820 - DT
DW = DH * 16 / 9
els = slidetitel('Demo')
els += [rect((1920 - DW) / 2, DT, DW, DH, INK50, r=28),
        text((1920 - DW) / 2, DT + DH / 2 - 22, DW, 44, 'Screenshot volgt', size=36,
             color=NAVY, ls=1.0)]
els += foot(page=7)
add('07-demo', els)

# ---------------------------------------------------------------- render
alleen = sys.argv[1:]
for naam, els, notes, dark in S:
    if alleen and naam not in alleen:
        continue
    print(shoot(render_html(els, f'preview/{naam}.html', dark=dark), f'preview/{naam}.png'))
if not alleen:
    print(render_pptx([e for _, e, _, _ in S], 'phov-deck-bewerkbaar.pptx',
                      notes=[n for _, _, n, _ in S]))
