"""Het aanbod. De prijs is hier het dominante object, niet de capabilities.

De vier capabilities staan er nog wel, maar klein en stil onderaan als
herhaling van slides 8 tot 12. Wie deze slide ziet moet eerst het bedrag zien
en pas daarna waar het voor is. Zelfde iconen en zelfde volgorde als in het
capability-blok, zodat het als terugverwijzing leest en niet als nieuw rijtje.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, GREEN, GREEN_DEEP, INK500, INK100, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION

els = []

els += [text(M, 88, W - 2 * M, TITLE * 1.3,
             'Institution-wide feedback for $3 per student',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04),
        text(M, 196, W - 2 * M, 50, 'Delivered by Eduface, mapped to what UTI needs.',
             font=BODY, size=TEXT, color=INK500, align='left', ls=1.3)]

# --- de prijs: het zwaarste object op de slide ----------------------------
PRICE_Y = 300
els += [text(M, PRICE_Y, 420, 200, '$3', font=HEAD, size=180, bold=True,
             color=NAVY, align='left', ls=0.9),
        text(M + 300, PRICE_Y + 44, 520, 60, 'per student,\nper month',
             font=HEAD, size=SUB, bold=True, color=NAVY, align='left', ls=1.15),
        text(M, PRICE_Y + 208, 700, 44, 'billed annually',
             font=BODY, size=TEXT, color=INK500, align='left', ls=1.2)]

# twee voorwaarden, rechts naast de prijs
TERMS_X = 1020
for i, t in enumerate(['Discount for multi-year commitment',
                       'Scales with growing students & instructors']):
    y = PRICE_Y + 30 + i * 108
    els += [rect(TERMS_X, y, 8, 56, GREEN),
            text(TERMS_X + 40, y + 4, W - M - TERMS_X - 40, 100, t,
                 font=BODY, size=TEXT, color=NAVY, align='left', ls=1.35)]

# --- stille herhaling van de vier capabilities ----------------------------
RECAP_Y = 664
els += [rect(M, RECAP_Y - 40, W - 2 * M, 1, INK100),
        text(M, RECAP_Y - 24, 600, 36, 'What that covers', size=CAPTION,
             color=INK500, align='left', ls=1.2)]

c4, w4 = cols(4)
RECAP = [('doel', 'Accuracy & Consistency'), ('sleutel', 'Technical Domain Fit'),
         ('instelling', 'Institution-Wide'), ('schuifjes', 'Self-Configuring')]
for cx, (icon, label) in zip(c4, RECAP):
    els += tile(cx - w4 / 2, RECAP_Y + 28, icon, tone='navy', fill=INK50,
                size=72, r=16, ic=36)
    els += [text(cx - w4 / 2 + 92, RECAP_Y + 46, w4 - 92, 70, label,
                 font=BODY, size=CAPTION, color=INK500, align='left', ls=1.3)]

els += foot(page=14)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-14.html', dark=DARK), 'preview/slide-14.png')
    print('preview/slide-14.png')
