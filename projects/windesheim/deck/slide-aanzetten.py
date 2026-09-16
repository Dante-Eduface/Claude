"""Aanzetten: Brightspace links, sync in het midden, Eduface klaar rechts."""
from deckbuild import (rect, pic, text, title, foot, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, TINT_G, INK50, INK100, INK200,
                       INK500, WHITE, HEAD, M)

els = title('Aanzetten')

# --- links: het LMS dat ze al hebben -------------------------------------
PX, PY, PW, PH = M, 300, 700, 440
els += [rect(PX, PY, PW, PH, INK50, r=28),
        rect(PX, PY, PW, 76, INK100, r=28),
        rect(PX, PY + 48, PW, 28, INK100)]
for i, kleur in enumerate(['E06C5A', 'E8B84B', GREEN]):
    els += [rect(PX + 32 + i * 34, PY + 28, 20, 20, kleur, r=10)]
els += [pic('assets/brightspace.png', PX + 330, PY + 22, 248, 32)]

RIJ = ['Course slides', 'Assessment brief', 'Rubric', 'Studentenhandboek']
for i, naam in enumerate(RIJ):
    y = PY + 104 + i * 82
    els += [rect(PX + 28, y, PW - 56, 66, WHITE, r=16),
            text(PX + 56, y + 16, 420, 40, naam, font=HEAD, size=30, bold=True, align='left'),
            rect(PX + PW - 190, y + 14, 134, 38, TINT_G, r=19),
            text(PX + PW - 190, y + 21, 134, 30, 'gesynct', size=22, color=GREEN_DEEP)]

# --- midden: de knop -----------------------------------------------------
els += [rect(880, 478, 160, 88, GREEN, r=22),
        text(880, 502, 160, 44, 'Sync', font=HEAD, size=38, bold=True, color=NAVY)]

# --- rechts: Eduface staat klaar ----------------------------------------
EX, EW = 1100, 700
els += [rect(EX, PY, EW, PH, NAVY, r=28),
        text(EX + 40, PY + 40, 300, 50, 'Eduface', font=HEAD, size=40, bold=True, color=WHITE, align='left'),
        rect(EX + EW - 320, PY + 38, 280, 54, GREEN, r=27),
        text(EX + EW - 320, PY + 50, 280, 34, 'Alle courses klaar', font=HEAD, size=26, bold=True, color=NAVY)]
for i, stap in enumerate(['Leest het vak', 'Bouwt de instructies', 'Vult aan met domeinkennis']):
    y = PY + 140 + i * 92
    els += [rect(EX + 40, y, 52, 52, GREEN, r=26),
            text(EX + 40, y + 10, 52, 34, str(i + 1), font=HEAD, size=28, bold=True, color=NAVY),
            text(EX + 112, y + 6, 540, 50, stap, font=HEAD, size=34, bold=True, color=WHITE, align='left')]

els += [text(M, 790, 1920 - 2 * M, 60, 'De docent zet niets op.',
             font=HEAD, size=52, bold=True)]
els += foot(page=None)

shoot(render_html(els, 'preview/aanzetten.html'), 'preview/aanzetten.png')
print('preview/aanzetten.png')
