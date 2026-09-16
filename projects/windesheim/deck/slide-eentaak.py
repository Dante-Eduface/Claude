"""Eén taak: een algemeen model kan van alles, ons model doet één ding."""
from deckbuild import (rect, pic, text, title, foot, cols, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G,
                       INK50, INK100, INK200, INK500, WHITE, HEAD, M)

els = title('Eén taak')
c2, w2 = cols(2)

# --- links: het algemene model kan van alles ----------------------------
els += [rect(M, 268, w2, 392, TINT_A, r=28),
        text(M + 48, 300, w2 - 96, 56, 'Algemeen model', font=HEAD, size=44,
             bold=True, color=AMBER, align='left')]
TAKEN = [('kar', 'Boodschappen'), ('pan', 'Recept'), ('vliegtuig', 'Vakantie'),
         ('mail', 'Mail'), ('code', 'Code'), ('globe', 'Vertalen')]
CW, CH, CG = 222, 116, 21
for i, (ic, lbl) in enumerate(TAKEN):
    x = M + 48 + (i % 3) * (CW + CG)
    y = 374 + (i // 3) * (CH + CG)
    els += [rect(x, y, CW, CH, WHITE, r=18),
            pic(f'assets/icon-{ic}-navy.png', x + CW / 2 - 20, y + 18, 40, 40),
            text(x, y + 68, CW, 34, lbl, size=24, color=INK500)]
els += [text(M + 48, 632, w2 - 96, 36, 'en duizend andere dingen', size=26,
             color=AMBER, align='left')]

# --- rechts: ons model doet er één -------------------------------------
RX = M + w2 + 72
els += [rect(RX, 268, w2, 392, TINT_G, r=28),
        text(RX + 48, 300, w2 - 96, 56, 'Ons model', font=HEAD, size=44,
             bold=True, color=GREEN_DEEP, align='left'),
        rect(RX + w2 / 2 - 90, 382, 180, 180, WHITE, r=40),
        pic('assets/icon-filepen-green.png', RX + w2 / 2 - 45, 427, 90, 90),
        text(RX + 48, 588, w2 - 96, 60, 'Feedback op schrijfopdrachten',
             font=HEAD, size=38, bold=True)]

els += [text(M, 684, 1920 - 2 * M, 40,
             'Waar een model op getraind is, bepaalt waar het voor mag worden ingezet.',
             size=28, color=INK500)]
els += [rect(M, 726, 8, 100, GREEN, r=4),
        text(M + 40, 726, 1520, 80,
             '“Datasets voor training, validatie en tests zijn relevant, voldoende '
             'representatief (…) met het oog op het beoogde doel.”',
             size=30, align='left', ls=1.3),
        text(M + 40, 812, 1520, 34, 'EU AI Act, verordening 2024/1689, artikel 10 lid 3',
             size=23, color=INK500, align='left')]
els += foot(page=None)

shoot(render_html(els, 'preview/eentaak.html'), 'preview/eentaak.png')
print('preview/eentaak.png')
