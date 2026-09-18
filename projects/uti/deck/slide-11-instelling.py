"""Capability 3/4: instellingsbreed.

Structureel een kopie van slide-09: dezelfde nav-rail, dezelfde geometrie,
alleen het actieve item schuift naar 03 en de claim wisselt. Die herhaling is
het punt: vier slides met hetzelfde silhouet laten zien dat je door één blok
loopt. Dus ook dezelfde afstand kop-naar-body als op 09, anders springt het
blok.

De claim staat op drie regels omdat 'course-by-course' op HERO niet naast
'Institution-wide,' past; de afbreking valt op een koppelteken dat er toch al
stond.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, \
    NAVY, GREEN, WHITE, INV_SOFT, INV_RULE, INK900, HEAD, BODY, \
    M, W, HERO, TEXT, CAPTION

CAPS = [
    ('Accuracy & Consistency', 'doel'),
    ('Technical Domain Fit', 'sleutel'),
    ('Institution-Wide', 'instelling'),
    ('Self-Configuring', 'schuifjes'),
]
ACTIVE = 2

els = []

# --- nav-rail: vier capabilities, elk met eigen icoon ----------------------
NAV_X, NAV_W, ROW_H, NAV_Y0, TILE = M, 520, 156, 208, 96
LABEL_X = NAV_X + TILE + 32
LABEL_W = NAV_W - TILE - 32
for i, (label, icon) in enumerate(CAPS):
    y = NAV_Y0 + i * ROW_H
    on = i == ACTIVE
    els += tile(NAV_X, y, icon, tone='navy' if on else 'green',
                fill=GREEN if on else INK900, size=TILE, r=20, ic=48)
    els += [text(LABEL_X, y + 6, LABEL_W, 34, f'0{i+1}', font=HEAD, size=CAPTION,
                 color=GREEN if on else INV_SOFT, align='left', ls=1.0),
            text(LABEL_X, y + 42, LABEL_W, 88, label, font=HEAD, size=TEXT,
                 bold=on, color=WHITE if on else INV_SOFT, align='left', ls=1.2)]

els += [rect(NAV_X + NAV_W + 60, NAV_Y0, 1, ROW_H * len(CAPS) - 26, INV_RULE)]

# --- de claim zelf: dit is het statement van de slide ----------------------
CONTENT_X = NAV_X + NAV_W + 60 + 80
CONTENT_W = W - M - CONTENT_X

els += [text(CONTENT_X, NAV_Y0 - 14, CONTENT_W, HERO * 3.2,
             'Institution-wide,\nnot course-\nby-course',
             font=HEAD, size=HERO, bold=True, color=WHITE, align='left', ls=0.98)]

els += [text(CONTENT_X, NAV_Y0 + 412, min(CONTENT_W, 860), 160,
             'Works at the institutional level, so it scales across every '
             'program and campus.',
             font=BODY, size=TEXT, color=INV_SOFT, align='left', ls=1.45)]

els += foot(dark=True, page=11)

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-11.html', dark=DARK), 'preview/slide-11.png')
    print('preview/slide-11.png')
