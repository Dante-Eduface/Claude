"""Slide: consistent beoordelen. Bron voor preview en bewerkbare pptx."""
import sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
from deckbuild import rect, text, render_html, render_pptx, NAVY, AMBER, INK50, INK100, INK200, INK500, WHITE, HEAD, BODY

MUTED_INV, PANEL, TRACK = 'A9BCC4', '0A2C3B', '1B3B4A'
els = []

# 1. Belangrijkst: groot navy blok
els += [rect(120, 96, 1104, 664, NAVY, r=32),
        text(184, 160, 976, 160, 'Beoordelaars oordelen\nconsistent', font=HEAD, size=72, bold=True, color=WHITE, align='left', ls=1.05),
        text(184, 336, 976, 44, 'Zie in één overzicht wie afwijkt van het team.', size=34, color=MUTED_INV, align='left'),
        rect(184, 420, 976, 276, PANEL, r=16),
        text(224, 452, 560, 40, 'Voorbeeld, cijfer per docent', size=32, color=MUTED_INV, align='left'),
        text(840, 452, 280, 40, 'Gemiddelde 7,1', size=32, color=MUTED_INV, align='right')]
TX, TW = 400, 600
for i, (naam, cijfer, af) in enumerate([('Docent A', 7.2, False), ('Docent B', 7.0, False), ('Docent C', 5.6, True)]):
    y = 512 + i * 56
    els += [text(224, y, 160, 40, naam, size=32, bold=af, color=WHITE if af else MUTED_INV, align='left'),
            rect(TX, y + 10, TW, 20, TRACK, r=10),
            rect(TX, y + 10, TW * cijfer / 10, 20, AMBER if af else WHITE, r=10),
            text(1030, y, 90, 40, f'{cijfer:.1f}'.replace('.', ','), size=32, bold=True, color=AMBER if af else WHITE, align='right')]
els += [rect(TX + TW * 0.71 - 1.5, 500, 3, 168, '8FA9B4')]

# 2. Tweede: wit met rand
els += [rect(1256, 96, 544, 340, INK200, r=24),
        rect(1258, 98, 540, 336, WHITE, r=22),
        text(1304, 136, 448, 100, 'Elk cijfer is\nnavolgbaar', font=HEAD, size=48, bold=True, align='left', ls=1.05),
        text(1304, 252, 448, 80, 'Onderbouwing per rubriccriterium.', size=32, color=INK500, align='left', ls=1.25),
        rect(1304, 348, 340, 52, INK50, r=26),
        text(1304, 357, 340, 36, 'AI Act audit trail', size=32, bold=True, align='center')]

# 3. Derde: getint vlak
els += [rect(1256, 468, 544, 292, INK100, r=24),
        text(1304, 516, 448, 92, 'De examencommissie\nborgt de kwaliteit', font=HEAD, size=40, bold=True, align='left', ls=1.1),
        text(1304, 628, 448, 80, 'Elke onderbouwing direct in te zien.', size=32, color=INK500, align='left', ls=1.25)]

# Callout onder de kaarten
els += [rect(120, 792, 1680, 200, INK50, r=16),
        rect(120, 792, 10, 200, NAVY),
        text(176, 828, 1580, 140,
             'Consistent beoordelen is een speerpunt van dit project. Daarmee helpt het om de eisen van de '
             'accreditatiepartij hierboven steviger te borgen, en dat kan een positieve impact hebben op de pabo, '
             'die nu in de accreditatie zit.', size=34, bold=True, align='left', ls=1.35)]

render_html(els, 'preview/consistent-beoordelen.html')
render_pptx([els], 'consistent-beoordelen-bewerkbaar.pptx')
