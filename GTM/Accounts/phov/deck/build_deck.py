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
# Geen kop. Boven het advies van het bureau, grijs, want dat wisten ze al.
# Onder wat PHOV echt wilde, in groen: daar gaat de rest van het deck over.
c3, w3 = cols(3)
els = [text(M, 96, 1400, 40, 'Aan een bureau, anderhalf jaar geleden', font=HEAD,
            size=36, bold=True, color=INK500, align='left', ls=1.0),
       text(M, 152, 1680, 46, 'Vraag: hoe zetten we AI in ons onderwijs in, '
            'en hoe helpen we docenten daarbij?', size=36, color=NAVY, align='left', ls=1.0)]
# Advies in navy, net zo leesbaar als de rest. Het verschil met "Al bekend."
# zit in het gewicht, niet in de kleur (core/regels.md).
els += [text(M, 241, 160, 40, 'Advies:', size=34, color=NAVY, align='left', ls=1.0)]
x = M + 150
for lbl, w in [('Toetstermen aanpassen', 450), ('Docenten meenemen', 400)]:
    els += [rect(x, 222, w, 76, INK50, r=38),
            text(x, 241, w, 40, lbl, size=34, color=NAVY, ls=1.0)]
    x += w + 28
els += [text(x + 20, 241, 400, 40, 'Al bekend.', size=34, bold=True, color=NAVY,
             align='left', ls=1.0),
        rect(M, 350, 1920 - 2 * M, 2, INK100),
        text(M, 396, 1200, 40, 'Wat PHOV wil', font=HEAD, size=36, bold=True,
             color=INK500, align='left', ls=1.0)]
for cx, (ic, kop, wat) in zip(c3, [
        ('lesgeven', 'Docenten met AI', 'in hun eigen vak, met een\npragmatische partner ernaast'),
        ('boek', 'Open boek', 'tentamens behouden,\nmet AI-detectie'),
        ('lagen', 'Curriculum', 'ontwikkelen')]):
    els += tile(cx, 470, ic, 'green')
    els += [text(cx - w3 / 2 - 30, 640, w3 + 60, 50, kop, font=HEAD, size=46, bold=True, ls=1.0),
            text(cx - w3 / 2 - 30, 702, w3 + 60, 90, wat, size=32, color=INK500, ls=1.2)]
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
