"""Vervolgstappen. Navy, want hij sluit het deck af.

Vier stappen zijn een volgorde, geen rijtje losse kaarten, dus ze staan op één
as met een lijn ertussen: je ziet dat stap 2 pas komt na stap 1. De laatste
stap krijgt een groene stip omdat dat het punt is waar dit heen loopt.
"""
from deckbuild import rect, oval, text, tile, foot, render_html, shoot, cols, \
    NAVY, GREEN, WHITE, INV_SOFT, INV_RULE, INK900, HEAD, BODY, \
    M, W, TITLE, TEXT, CAPTION

els = []

els += [text(M, 88, W - 2 * M, TITLE * 1.3, 'Proposed Next Steps',
             font=HEAD, size=TITLE, bold=True, color=WHITE, align='left', ls=1.04)]

STEPS = [
    ('mensen', 'Confirm Priority\nand Budget',
     'Gauge with the Executive Board whether this is a priority now.'),
    ('globe', 'Validate in the U.S.',
     'On-site with instructors, students, and leadership.'),
    ('vlag', 'Pilot the Start Group',
     'Launch with a self-scaling license.'),
    ('kalender', 'Full Institutional\nIntegration',
     'Roll out institution-wide from next academic year.'),
]

c4, w4 = cols(4)
AXIS_Y, TILE = 380, 88

# de as die de vier stappen tot één volgorde maakt
els += [rect(c4[0], AXIS_Y + TILE / 2, c4[-1] - c4[0], 2, INV_RULE)]

for i, (cx, (icon, head, body)) in enumerate(zip(c4, STEPS)):
    last = i == len(STEPS) - 1
    els += tile(cx - TILE / 2, AXIS_Y, icon, tone='navy' if last else 'green',
                fill=GREEN if last else INK900, size=TILE, r=18, ic=44)
    els += [text(cx - w4 / 2, AXIS_Y - 76, w4, 44, f'0{i+1}', font=HEAD,
                 size=CAPTION, color=GREEN if last else INV_SOFT,
                 align='center', ls=1.0),
            text(cx - w4 / 2, AXIS_Y + TILE + 44, w4, 120, head, font=HEAD,
                 size=TEXT, bold=True, color=WHITE, align='center', ls=1.2),
            text(cx - w4 / 2, AXIS_Y + TILE + 176, w4, 160, body, font=BODY,
                 size=CAPTION, color=INV_SOFT, align='center', ls=1.4)]

els += foot(dark=True, page=15, source='Concept, for discussion.')

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-15.html', dark=DARK), 'preview/slide-15.png')
    print('preview/slide-15.png')
