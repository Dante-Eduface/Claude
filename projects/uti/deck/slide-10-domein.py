"""Capability 2/4: technische vakinhoud.

Structureel een kopie van slide-09: dezelfde nav-rail links, dezelfde vier
capabilities, dezelfde geometrie. Alleen het actieve item verschuift naar 02 en
de claim rechts wisselt. Die herhaling is het punt — vier slides die exact
hetzelfde silhouet hebben laten de kijker zien dat hij door één blok loopt en
alleen de rij eronder opschuift. De claim staat op vier regels omdat hij op
HERO anders buiten de rechterkolom valt.
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
ACTIVE = 1

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

els += [text(CONTENT_X, NAV_Y0 - 14, CONTENT_W, HERO * 4.2,
             'Built for\ntechnical fields\nand domain\nknowledge',
             font=HEAD, size=HERO, bold=True, color=WHITE, align='left', ls=0.98)]

# Vier regels claim in plaats van drie, dus de body schuift één regelhoogte mee.
# 540 houdt de kop-naar-body afstand exact gelijk aan slide 09.
els += [text(CONTENT_X, NAV_Y0 + 540, min(CONTENT_W, 860), 160,
             'Purpose-built for technical, vocational subject matter, '
             'not a generic writing tool.',
             font=BODY, size=TEXT, color=INV_SOFT, align='left', ls=1.45)]

els += foot(dark=True, page=10)

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-10.html', dark=DARK), 'preview/slide-10.png')
    print('preview/slide-10.png')
