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

# ---------------------------------------------------------------- 2 nu
# Wie raakt het werk aan, in volgorde. Beide stroken op hetzelfde raster, zodat
# student, docent en cursusbureau recht onder elkaar staan. De docent staat in
# amber: daar zitten de uren, dat is slide 3. De rest vertelt Dante erbij.
c4, w4 = cols(4)
TS = 128

def strook(y, label, stappen):
    out = [text(M, y, 600, 44, label, font=HEAD, size=40, bold=True, align='left', ls=1.0)]
    ty = y + 86
    out.append(rect(c4[0], ty + TS / 2 - 2, c4[len(stappen) - 1] - c4[0], 4, INK100))
    for cx, (ic, rol) in zip(c4, stappen):
        tone = 'amber' if rol == 'Docent' else 'navy'
        out += [rect(cx - 80, ty - 6, 160, TS + 12, WHITE)]
        out += tile(cx, ty, ic, tone, TS)
        out += [text(cx - w4 / 2, ty + TS + 18, w4, 40, rol, font=HEAD, size=34,
                     bold=True, color=NAVY, ls=1.0)]
    return out

els = title('Nu')
els += strook(250, 'Tentamens', [('pen', 'Student'), ('cijfers', 'Docent'),
                                  ('instelling', 'Cursusbureau')])
# De moduleleider zit niet in de lijn maar kijkt mee over de schouder van de docent.
PW, PY = 470, 236
els += [rect(c4[1] - PW / 2, PY, PW, 64, INK50, r=32),
        pic('assets/icon-usercheck-navy.png', c4[1] - PW / 2 + 22, PY + 12, 40, 40),
        text(c4[1] - PW / 2 + 74, PY + 15, PW - 84, 40, 'Moduleleider kijkt mee',
             size=32, color=NAVY, align='left', ls=1.0),
        rect(c4[1] - 1.5, PY + 64, 3, 336 - PY - 64 - 8, INK200)]
els += strook(560, 'Schrijfopdrachten', [('inleveren', 'Student'), ('gesprek', 'Docent'),
                                         ('instelling', 'Cursusbureau'), ('mail', 'Secretariaat')])
els += foot(page=2)
add('02-nu', els, notes="""Tentamens
1. Studenten maken het tentamen
2. Het antwoord gaat terug naar de docent, die punten en feedback geeft
3. Daarna gaat het naar het cursusbureau
De moduleleider kijkt mee: controleert en stelt het cijfer vast.

Schrijfopdrachten
1. De student levert in via de leeromgeving (individueel, duo of groep)
2. Elke docent geeft feedback in zijn eigen format, en elke opdracht heeft weer een ander format. Dat uploadt hij.
3. Het cursusbureau kijkt het nog na op taal en rariteiten
4. Het secretariaat zet het open en de student ziet zijn cijfer en feedback""")

# ---------------------------------------------------------------- render
alleen = sys.argv[1:]
for naam, els, notes, dark in S:
    if alleen and naam not in alleen:
        continue
    print(shoot(render_html(els, f'preview/{naam}.html', dark=dark), f'preview/{naam}.png'))
if not alleen:
    print(render_pptx([e for _, e, _, _ in S], 'phov-deck-bewerkbaar.pptx',
                      notes=[n for _, _, n, _ in S]))
