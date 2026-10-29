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

# ---------------------------------------------------------------- 2 hoe het nu werkt
# Twee stroken op hetzelfde zes-kolommenraster, zodat je ziet dat een
# schrijfopdracht twee keer zoveel stappen heeft als een tentamen.
# De stappen waar de docent uren maakt staan in amber: dat is slide 3.
c6, w6 = cols(6)

def strook(y, label, stappen):
    out = [text(M, y, 600, 44, label, font=HEAD, size=40, bold=True, align='left', ls=1.0)]
    cy = y + 104
    out.append(rect(c6[0], cy - 2, c6[len(stappen) - 1] - c6[0], 4, INK100))
    for i, (cx, (lbl, docent)) in enumerate(zip(c6, stappen), 1):
        kleur = AMBER if docent else NAVY
        out += [oval(cx - 30, cy - 30, 60, TINT_A if docent else INK50, kleur, 0),
                text(cx - 30, cy - 19, 60, 40, str(i), font=HEAD, size=34, bold=True,
                     color=kleur, ls=1.0),
                text(cx - (w6 + 60) / 2, cy + 52, w6 + 60, 84, lbl, size=32, bold=docent,
                     color=NAVY, ls=1.25)]
    return out

els = title('Hoe het nu werkt')
els += strook(244, 'Tentamens', [
    ('Student maakt\nhet tentamen', False),
    ('Docent: punten\nen feedback', True),
    ('Moduleleider\nstelt cijfer vast', False),
])
els += strook(572, 'Schrijfopdrachten', [
    ('Student levert in', False),
    ('Docent krijgt\neen melding', False),
    ('Feedback in\neigen format', True),
    ('Cijfer wordt\nvastgesteld', False),
    ('Cursusbureau\ncheckt taal', False),
    ('Secretariaat\nzet het open', False),
])
els += foot(src='Gesprek met PHOV.', page=2)
add('02-nu', els, notes="""Tentamens
1. Studenten maken het tentamen
2. Het antwoord van de student gaat terug naar de docent, die punten en feedback geeft
3. De moduleleider controleert en stelt het cijfer vast, daarna gaat het naar het cursusbureau

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
