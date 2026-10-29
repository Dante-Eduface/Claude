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
def add(naam, els, notes='', dark=False): S.append((naam, els, notes, dark))

# ---------------------------------------------------------------- 1 aanleiding
# Boven het advies dat ze al kenden, grijs. Onder wat ze echt wilden, groen.
c3, w3 = cols(3)
els = title('Aanleiding')
els += [text(M, 262, 400, 44, 'Advies', font=HEAD, size=40, bold=True, align='left', ls=1.0)]
for x, w, lbl in [(420, 470, 'Toetstermen aanpassen'), (920, 430, 'Docenten meenemen')]:
    els += [rect(x, 248, w, 72, INK50, r=36),
            text(x, 266, w, 40, lbl, size=32, color=INK500, ls=1.0)]
els += [rect(M, 384, 1920 - 2 * M, 2, INK100),
        text(M, 430, 400, 44, 'Wens', font=HEAD, size=40, bold=True, align='left', ls=1.0)]
for cx, (ic, lbl) in zip(c3, [('docenten', 'AI in het vak'), ('boek', 'Open boek blijft'),
                              ('lagen', 'Curriculum')]):
    els += tile(cx, 520, ic, 'green')
    els += [text(cx - w3 / 2, 694, w3, 50, lbl, font=HEAD, size=46, bold=True, ls=1.0)]
els += foot(page=1)
add('01-aanleiding', els, notes="""Anderhalf jaar geleden heeft PHOV een bureau ingehuurd. De vraag was hoe ze AI in hun onderwijs kunnen inzetten en hoe ze docenten daarbij helpen.
Het advies was "toetstermen aanpassen" en "docenten meenemen". Dat wisten ze al.

Wat ze wilden:
1. Docenten die AI in hun vakgebied gebruiken, met een pragmatische partner ernaast
2. Open-boek tentamens behouden (AI-detectie)
3. Curriculumontwikkeling""")

# ---------------------------------------------------------------- 2 huidige situatie
# Geen kop: de twee stromen dragen de slide. Per stap wie en wat er gebeurt.
# Zes kolommen, zodat moduleleider en "cijfer vastgesteld" recht onder elkaar
# staan, net als de twee cursusbureaus. Alles neutraal: dit beschrijft, het
# oordeel komt op slide 3.
c6, w6 = cols(6)
TS = 112

def strook(y, label, stappen):
    out = [text(M, y, 600, 40, label, font=HEAD, size=36, bold=True, color=INK500,
                align='left', ls=1.0)]
    ty = y + 72
    out.append(rect(c6[0], ty + TS / 2 - 2, c6[len(stappen) - 1] - c6[0], 4, INK100))
    for cx, (ic, rol, wat) in zip(c6, stappen):
        out += [rect(cx - 70, ty - 6, 140, TS + 12, WHITE)]
        out += tile(cx, ty, ic, 'navy', TS)
        out += [text(cx - 146, ty + TS + 16, 292, 40, rol, font=HEAD, size=34,
                     bold=True, ls=1.0),
                text(cx - 146, ty + TS + 62, 292, 120, wat, size=32, color=INK500,
                     ls=1.2)]
    return out

els = strook(96, 'Tentamens', [
    ('pen', 'Student', 'maakt het\ntentamen'),
    ('cijfers', 'Docent', 'geeft punten\nen feedback'),
    ('usercheck', 'Moduleleider', 'controleert en\nstelt cijfer vast'),
    ('data', 'Cursusbureau', 'ontvangt het\neindcijfer'),
])
els += strook(480, 'Schrijfopdrachten', [
    ('inleveren', 'Student', 'levert in: solo,\nduo of groep'),
    ('filepen', 'Docent', 'feedback in eigen\nformat, elke\nopdracht anders'),
    ('aftekenen', 'Cijfer', 'wordt\nvastgesteld'),
    ('check', 'Cursusbureau', 'checkt taal en\nrariteiten'),
    ('mail', 'Secretariaat', 'zet het open'),
    ('studenten', 'Student', 'ziet cijfer\nen feedback'),
])
els += foot(page=2)
add('02-nu', els, notes="""Tentamens
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

# ---------------------------------------------------------------- render
alleen = sys.argv[1:]
for naam, els, notes, dark in S:
    if alleen and naam not in alleen:
        continue
    print(shoot(render_html(els, f'preview/{naam}.html', dark=dark), f'preview/{naam}.png'))
if not alleen:
    print(render_pptx([e for _, e, _, _ in S], 'phov-deck-bewerkbaar.pptx',
                      notes=[n for _, _, n, _ in S]))
