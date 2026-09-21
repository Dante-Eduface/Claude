"""Vervolgstappen. Navy, want hij sluit het deck af.

Vijf stappen zijn een volgorde, geen rijtje losse kaarten. De as staat
rechtop: de lijn loopt verticaal door alle vijf de tegels, zodat je ziet dat
stap 2 pas komt na stap 1. De volgorde zit in de nummering, niet in extra
woorden als "eerst". Stap 1 staat op een groene tegel omdat dat de enige stap
is die nu gevraagd wordt; de rest is het pad daarna.

Liggend paste dit niet meer. Met vijf stappen wordt een kolom 298px breed en
dan zou de langste stap acht regels worden en door de voetlijn lopen; kleiner
zetten dan 32px mag niet. Rechtop krijgt de tekst een baan van 1100px en
wordt diezelfde stap twee regels.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, \
    GREEN, WHITE, INV_SOFT, INV_RULE, INK900, HEAD, BODY, \
    M, W, TITLE, TEXT, CAPTION

els = []

els += [text(M, 88, W - 2 * M, TITLE * 1.3, 'Proposed Next Steps',
             font=HEAD, size=TITLE, bold=True, color=WHITE, align='left', ls=1.04)]

STEPS = [
    ('mensen', 'Confirm Priority\nand Budget',
     'Gauge with the Executive Board whether this is a priority now.'),
    ('globe', 'Validate\nin the U.S.',
     'On-site with instructors, students, and leadership. Legal and IT '
     'validation, approximately one month or more.'),
    ('vlag', 'Pilot the\nStart Group',
     'Launch with a self-scaling license. On-site instructor training support '
     'from the Eduface team at pilot start. Target launch December 2026.'),
    ('route', 'Programmatic\nExpansion',
     'Roll out to additional programs following pilot success.'),
    ('kalender', 'Full Institutional\nIntegration',
     'Roll out institution-wide from next academic year.'),
]

ROW_Y0, ROW_H, TILE = 262, 128, 80
NUM_X, TILE_X = M, M + 72
HEAD_X, HEAD_W = TILE_X + TILE + 40, 340
BODY_X = HEAD_X + HEAD_W + 48
BODY_W = W - M - BODY_X
TILE_DY = (ROW_H - TILE) / 2

# De as eerst, zodat de tegels erop liggen in plaats van eronder.
AXIS_X = TILE_X + TILE / 2
els += [rect(AXIS_X - 1, ROW_Y0 + ROW_H / 2, 2,
             (len(STEPS) - 1) * ROW_H, INV_RULE)]

for i, (icon, head, body) in enumerate(STEPS):
    y = ROW_Y0 + i * ROW_H
    first = i == 0
    els += tile(TILE_X, y + TILE_DY, icon, tone='navy' if first else 'green',
                fill=GREEN if first else INK900, size=TILE, r=18, ic=40)
    els += [text(NUM_X, y + TILE_DY + 22, 56, 36, f'0{i+1}', font=HEAD,
                 size=CAPTION, color=GREEN if first else INV_SOFT,
                 align='left', ls=1.0),
            text(HEAD_X, y + 16, HEAD_W, TEXT * 2.6, head, font=HEAD, size=TEXT,
                 bold=True, color=WHITE, align='left', ls=1.2),
            text(BODY_X, y + 16, BODY_W, TEXT * 2.6, body, font=BODY, size=TEXT,
                 color=INV_SOFT, align='left', ls=1.45)]

els += foot(dark=True, page=16, source='Concept, for discussion.')

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-16.html', dark=DARK), 'preview/slide-16.png')
    print('preview/slide-16.png')
