"""Twee opties voor de dataset-slide: A grote blokjes, B de roos."""
import math
from deckbuild import (rect, oval, text, title, foot, cols, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G,
                       INK50, INK100, INK200, INK500, WHITE, HEAD, M)

c2, w2 = cols(2)
CITAAT = ('“Datasets voor training, validatie en tests zijn relevant, voldoende representatief, '
          'en zoveel mogelijk foutenvrij en volledig met het oog op het beoogde doel.”')
BRON = 'EU AI Act, verordening 2024/1689, artikel 10 lid 3'

def citaatblok(y):
    return [rect(M, y, 8, 100, GREEN, r=4),
            text(M + 40, y, 1520, 80, CITAAT, size=30, align='left', ls=1.3),
            text(M + 40, y + 86, 1520, 34, BRON, size=23, color=INK500, align='left')]

# ============================================================ A: tien blokken
els = title('Vergelijkbare dataset')
KOL, CEL, GAT = 5, 96, 18
GW = KOL * (CEL + GAT) - GAT
for px, tint, kleur, kop, groen, regel in [
        (M, TINT_A, AMBER, 'Algemeen model', 1, 'Eén op de tien is beoordeeld werk.'),
        (M + w2 + 72, TINT_G, GREEN_DEEP, 'Ons model', 10, 'Alles is beoordeeld werk.')]:
    els += [rect(px, 268, w2, 382, tint, r=28),
            text(px + 48, 298, w2 - 96, 56, kop, font=HEAD, size=44, bold=True,
                 color=kleur, align='left'),
            text(px + 48, 356, w2 - 96, 44, regel, size=30, align='left')]
    gx = px + (w2 - GW) / 2
    for i in range(10):
        els += [rect(gx + (i % KOL) * (CEL + GAT), 408 + (i // KOL) * (CEL + GAT),
                     CEL, CEL, GREEN if i < groen else INK200, r=22)]
    
els += [text(M, 672, 1920 - 2 * M, 40,
             'Elk blokje is trainingsdata. Groen is werk van een student dat een docent heeft beoordeeld.',
             size=28, color=INK500)]
els += citaatblok(726) + foot(page=None)
shoot(render_html(els, 'preview/dataset-a.html'), 'preview/dataset-a.png')

# ============================================================ B: de roos
els = title('Beoogd doel')
for cx, tint, kleur, kop, raak in [
        (M + w2 / 2, TINT_A, AMBER, 'Algemeen model', False),
        (M + w2 + 72 + w2 / 2, TINT_G, GREEN_DEEP, 'Ons model', True)]:
    cy = 470
    els += [oval(cx - 175, cy - 175, 350, INK100, INK100, 0),
            oval(cx - 115, cy - 115, 230, INK50, INK200, 1),
            oval(cx - 58, cy - 58, 116, GREEN, GREEN, 0),
            text(cx - 200, 240, 400, 56, kop, font=HEAD, size=44, bold=True, color=kleur)]
    if raak:
        plekken = [(0, -28), (26, 12), (-26, 10), (8, 34), (-34, -12), (40, -20),
                   (-8, -46), (52, 26), (-52, 30), (18, -12)]
    else:
        plekken = [(-150, -95), (140, -110), (-205, 40), (190, 70), (-95, 160),
                   (120, 155), (-140, -160), (165, -35), (-30, 195), (10, -20)]
    for dx, dy in plekken:
        els += [oval(cx + dx - 13, cy + dy - 13, 26, NAVY, WHITE, 2)]
els += [text(M, 672, 1920 - 2 * M, 40,
             'Elke stip is trainingsdata. De roos is het beoogde doel: werk van studenten beoordelen.',
             size=28, color=INK500)]
els += citaatblok(726) + foot(page=None)
shoot(render_html(els, 'preview/dataset-b.html'), 'preview/dataset-b.png')
print('a + b klaar')
