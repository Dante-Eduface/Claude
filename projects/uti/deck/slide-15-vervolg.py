"""Vervolgstappen. Navy, want hij sluit het deck af.

Vier stappen zijn een volgorde, geen rijtje losse kaarten. Daarom staan ze op
één horizontale as: de lijn loopt door alle vier de tegels, zodat je ziet dat
stap 2 pas komt na stap 1. De volgorde zit in de nummering, niet in extra
woorden als "eerst". Stap 1 staat op een groene tegel omdat dat de enige stap
is die nu gevraagd wordt; de andere drie zijn het pad daarna.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    GREEN, WHITE, INV_SOFT, INV_RULE, INK900, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION

els = []

els += [text(M, 88, W - 2 * M, TITLE * 1.3, 'Proposed Next Steps',
             font=HEAD, size=TITLE, bold=True, color=WHITE, align='left', ls=1.04)]

# Regelafbrekingen staan vast: zo houden alle vier de koppen twee regels en
# loopt de bodytekst overal op dezelfde hoogte door.
STEPS = [
    ('mensen', 'Confirm Priority\nand Budget',
     'Gauge with the Executive\nBoard whether this is\na priority now.'),
    ('globe', 'Validate\nin the U.S.',
     'On-site with instructors,\nstudents, and leadership.'),
    ('vlag', 'Pilot the\nStart Group',
     'Launch with a\nself-scaling license.'),
    ('kalender', 'Full Institutional\nIntegration',
     'Roll out institution-wide\nfrom next academic year.'),
]

c4, w4 = cols(4)
NUM_Y, TILE_Y, TILE = 320, 372, 112
HEAD_Y, BODY_Y = 536, 672

# de as die de vier stappen tot één volgorde maakt
els += [rect(c4[0], TILE_Y + TILE / 2, c4[-1] - c4[0], 2, INV_RULE)]

for i, (cx, (icon, head, body)) in enumerate(zip(c4, STEPS)):
    first = i == 0
    els += tile(cx - TILE / 2, TILE_Y, icon, tone='navy' if first else 'green',
                fill=GREEN if first else INK900, size=TILE, r=22, ic=56)
    els += [text(cx - w4 / 2, NUM_Y, w4, 36, f'0{i+1}', font=HEAD, size=CAPTION,
                 color=GREEN if first else INV_SOFT, align='center', ls=1.0),
            text(cx - w4 / 2, HEAD_Y, w4, 116, head, font=HEAD, size=SUB,
                 bold=True, color=WHITE, align='center', ls=1.18),
            text(cx - w4 / 2, BODY_Y, w4, 150, body, font=BODY, size=TEXT,
                 color=INV_SOFT, align='center', ls=1.4)]

els += foot(dark=True, page=15, source='Concept, for discussion.')

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-15.html', dark=DARK), 'preview/slide-15.png')
    print('preview/slide-15.png')
