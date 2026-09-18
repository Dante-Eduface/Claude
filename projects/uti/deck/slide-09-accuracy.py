"""Proefslide (Gate 2, stuk 1/2): capability-slide met navigatie-rail links.
Vier vaste capabilities, het huidige item onderscheiden door gewicht en kleur
(navy/bold vs. ink-500), niet door contrast te verlagen op de andere drie."""
from deckbuild import rect, pic, text, foot, render_html, shoot, \
    NAVY, INK500, HEAD, BODY, M, TITLE, TEXT, CAPTION

CAPS = ['Accuracy & Consistency', 'Technical Domain Fit',
        'Institution-Wide', 'Self-Configuring']
ACTIVE = 0

els = []

# --- nav-rail: links, vier capabilities, huidige actief -------------------
NAV_X, NAV_W, ROW_H, NAV_Y0 = M, 400, 132, 300
NAV_H = ROW_H * len(CAPS)
for i, label in enumerate(CAPS):
    y = NAV_Y0 + i * ROW_H
    active = i == ACTIVE
    els += [text(NAV_X, y, 56, 40, f'0{i+1}', font=HEAD, size=CAPTION, bold=active,
                 color=NAVY if active else INK500, align='left', ls=1.0),
            text(NAV_X + 64, y - 6, NAV_W - 64, 96, label, font=HEAD,
                 size=TEXT, bold=active, color=NAVY if active else INK500,
                 align='left', ls=1.2)]

els += [rect(NAV_X + NAV_W + 40, NAV_Y0, 1, NAV_H - 26, 'E7EEF0')]

# --- inhoud: claim + toelichting + ondersteunend icoon ---------------------
# Optisch gecentreerd tegen de nav-rail, anders valt de onderkant leeg.
CONTENT_X = NAV_X + NAV_W + 40 + 80
CONTENT_W = 1920 - M - CONTENT_X
CONTENT_H = 132 + 56 + 2 * TEXT * 1.45
CONTENT_Y = NAV_Y0 + (NAV_H - 26 - CONTENT_H) / 2

els += [rect(CONTENT_X, CONTENT_Y, 132, 132, 'F3F7F8', r=20),
        pic('assets/icon-check-navy.png', CONTENT_X + 34, CONTENT_Y + 34, 64, 64)]

els += [text(CONTENT_X + 172, CONTENT_Y, CONTENT_W - 172, TITLE * 2.2,
             'Trained for Accuracy\nand Consistency', font=HEAD, size=TITLE,
             bold=True, color=NAVY, align='left', ls=1.04)]

els += [text(CONTENT_X, CONTENT_Y + 132 + 56, min(CONTENT_W, 980), 140,
             'The model is trained specifically to grade and give feedback '
             'with accuracy and consistency at the core.',
             font=BODY, size=TEXT, color=NAVY, align='left', ls=1.45)]

els += foot(page=9)

shoot(render_html(els, 'preview/slide-09.html'), 'preview/slide-09.png')
print('preview/slide-09.png')
