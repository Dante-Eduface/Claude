"""Spreiding: hetzelfde dashboard, maar met beoordelaars die uiteenlopen."""
from deckbuild import (rect, text, title, foot, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G,
                       INK50, INK100, INK200, INK500, WHITE, HEAD, M)

els = title('Spreiding')

CX, CY, CW, CH = M, 276, 1920 - 2 * M, 470
els += [rect(CX, CY, CW, CH, INK50, r=28),
        text(CX + 56, CY + 44, 900, 46, 'Model accuracy per grader',
             font=HEAD, size=38, bold=True, align='left'),
        text(CX + 56, CY + 100, 900, 40, 'Hoe dicht elke beoordelaar bij het voorstel bleef',
             size=28, color=INK500, align='left')]

RIJEN = [('Beoordelaar A', 98, 'Excellent', True),
         ('Beoordelaar B', 94, 'Excellent', True),
         ('Beoordelaar C', 87, 'Wisselend', False),
         ('Beoordelaar D', 79, 'Wisselend', False),
         ('Beoordelaar E', 71, 'Wijkt af',  False),
         ('Beoordelaar F', 66, 'Wijkt af',  False)]

BAR_X, BAR_W, BAR_H = CX + 380, 760, 26
for i, (naam, pct, label, goed) in enumerate(RIJEN):
    y = CY + 170 + i * 48
    kleur, tint = (GREEN_DEEP, TINT_G) if goed else (AMBER, TINT_A)
    els += [text(CX + 56, y - 4, 300, 36, naam, size=28, bold=True, align='left'),
            rect(BAR_X, y, BAR_W, BAR_H, INK200, r=13),
            rect(BAR_X, y, BAR_W * pct / 100, BAR_H, kleur, r=13),
            text(BAR_X + BAR_W + 28, y - 6, 130, 40, f'{pct}%',
                 font=HEAD, size=32, bold=True, align='left'),
            rect(BAR_X + BAR_W + 180, y - 6, 210, 40, tint, r=20),
            text(BAR_X + BAR_W + 180, y + 1, 210, 30, label, size=24, color=kleur)]

els += [text(M, 790, 1920 - 2 * M, 60,
             '32 punten verschil tussen de strengste en de mildste beoordelaar.',
             font=HEAD, size=48, bold=True)]
els += foot(src='Voorbeeld met fictieve data, ter illustratie van wat het dashboard laat zien.',
            page=None)

shoot(render_html(els, 'preview/spreiding.html'), 'preview/spreiding.png')
print('preview/spreiding.png')
