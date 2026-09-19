"""Vergelijkbare dataset: het verschil in trainingsdata als beeld, met het
citaat uit de AI Act eronder als onderbouwing."""
import random
from deckbuild import (rect, text, title, foot, cols, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G,
                       INK50, INK100, INK200, INK500, WHITE, HEAD, M)

els = title('Vergelijkbare dataset')

c2, w2 = cols(2)
KOL, RIJ, CEL, GAT = 12, 7, 24, 9
GRID_W = KOL * (CEL + GAT) - GAT
GRID_H = RIJ * (CEL + GAT) - GAT

# vaste "willekeurige" plekken, zodat de slide elke build hetzelfde is
random.seed(7)
raak = set(random.sample(range(KOL * RIJ), 6))

PANELEN = [
    (M, TINT_A, AMBER, 'Algemeen model', 'Getraind op alles.', False),
    (M + w2 + 72, TINT_G, GREEN_DEEP, 'Ons model', 'Getraind op beoordeeld studentwerk.', True),
]
for px, tint, kleur, kop, regel, alles_groen in PANELEN:
    els += [rect(px, 268, w2, 400, tint, r=28),
            text(px + 48, 306, w2 - 96, 56, kop, font=HEAD, size=44, bold=True,
                 color=kleur, align='left')]
    gx = px + (w2 - GRID_W) / 2
    for i in range(KOL * RIJ):
        x = gx + (i % KOL) * (CEL + GAT)
        y = 388 + (i // KOL) * (CEL + GAT)
        vol = alles_groen or i in raak
        els += [rect(x, y, CEL, CEL, GREEN if vol else INK200, r=7)]
    els += [text(px + 48, 606, w2 - 96, 44, regel, size=30, align='left')]

els += [text(M, 688, 1920 - 2 * M, 40,
             'Groen is data waarin een docent werk van een student heeft beoordeeld.',
             size=28, color=INK500)]

# --- het citaat als onderbouwing ----------------------------------------
els += [rect(M, 730, 8, 100, GREEN, r=4),
        text(M + 40, 730, 1520, 80,
             '“Datasets voor training, validatie en tests zijn relevant, voldoende representatief, '
             'en zoveel mogelijk foutenvrij en volledig met het oog op het beoogde doel.”',
             size=30, align='left', ls=1.3),
        text(M + 40, 816, 1520, 34, 'EU AI Act, verordening 2024/1689, artikel 10 lid 3',
             size=23, color=INK500, align='left')]
els += foot(page=None)

shoot(render_html(els, 'preview/dataset.html'), 'preview/dataset.png')
print('preview/dataset.png')
