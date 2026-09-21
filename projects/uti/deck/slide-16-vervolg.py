"""Vervolgstappen. Navy, want hij sluit het deck af.

Drie stappen zijn een volgorde, geen rijtje losse kaarten. De as staat rechtop:
de lijn loopt verticaal door alle drie de tegels, zodat je ziet dat stap 2 pas
komt na stap 1. De volgorde zit in de nummering, niet in extra woorden.

Het waren er vijf; de twee stappen vóór de pilot zijn eruit op verzoek van
Dante. Met drie rijen komt er ruimte vrij, en die gaat naar formaat: grotere
tegels, koppen op SUB in plaats van TEXT, en meer lucht tussen de rijen. Geen
groene tegel meer op stap 1: in de gevraagde opzet is de pilot niet langer het
enige dat nu gevraagd wordt, dus er is niets om als enige te markeren.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, \
    WHITE, INV_SOFT, INV_RULE, INK900, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT

els = []

els += [text(M, 88, W - 2 * M, TITLE * 1.3, 'Proposed Next Steps',
             font=HEAD, size=TITLE, bold=True, color=WHITE, align='left', ls=1.04)]

STEPS = [
    ('vlag', 'Pilot the\nStart Group',
     'Launch with a self-scaling license. On-site instructor training support '
     'from the Eduface team at pilot start. Target launch December 2026.'),
    ('route', 'Programmatic\nExpansion',
     'Roll out to additional program(s) following pilot success.'),
    ('kalender', 'Full Institutional\nIntegration',
     'Roll out institution-wide from next academic year.'),
]

ROW_Y0, ROW_H, TILE = 300, 200, 112
NUM_X, TILE_X = M, M + 80
HEAD_X, HEAD_W = TILE_X + TILE + 40, 440
BODY_X = HEAD_X + HEAD_W + 48
BODY_W = W - M - BODY_X
TILE_DY = (ROW_H - TILE) / 2

# De as eerst, zodat de tegels erop liggen in plaats van eronder.
AXIS_X = TILE_X + TILE / 2
els += [rect(AXIS_X - 1, ROW_Y0 + ROW_H / 2, 2,
             (len(STEPS) - 1) * ROW_H, INV_RULE)]

for i, (icon, head, body) in enumerate(STEPS):
    y = ROW_Y0 + i * ROW_H
    els += tile(TILE_X, y + TILE_DY, icon, tone='green', fill=INK900,
                size=TILE, r=22, ic=56)
    els += [text(NUM_X, y + TILE_DY + 34, 64, 44, f'0{i+1}', font=HEAD,
                 size=TEXT, color=INV_SOFT, align='left', ls=1.0),
            text(HEAD_X, y + 30, HEAD_W, SUB * 2.6, head, font=HEAD, size=SUB,
                 bold=True, color=WHITE, align='left', ls=1.18),
            text(BODY_X, y + 34, BODY_W, TEXT * 3.2, body, font=BODY, size=TEXT,
                 color=INV_SOFT, align='left', ls=1.45)]

els += foot(dark=True, page=16, source='Concept, for discussion.')

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-16.html', dark=DARK), 'preview/slide-16.png')
    print('preview/slide-16.png')
