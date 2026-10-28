"""Slide: consistent beoordelen. Bron voor preview en bewerkbare pptx."""
import sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
from deckbuild import rect, text, render_html, render_pptx, NAVY, INK50, INK100, INK200, INK500, WHITE, HEAD

MUTED_INV, PANEL, TRACK = 'A9BCC4', '0A2C3B', '1B3B4A'
els = []

# Titel
els += [text(120, 72, 1680, 96, 'Accreditatie', font=HEAD, size=80, bold=True, align='left', ls=1.0)]

# 1. Belangrijkst: navy blok over de volle breedte, tekst links, voorbeeld rechts
els += [rect(120, 200, 1680, 340, NAVY, r=32),
        text(184, 248, 720, 140, 'Beoordelaars oordelen\nconsistent', font=HEAD, size=64, bold=True, color=WHITE, align='left', ls=1.05),
        text(184, 404, 700, 84, 'Zie in één overzicht wie afwijkt van het team.', size=32, color=MUTED_INV, align='left', ls=1.3),
        rect(960, 248, 776, 244, PANEL, r=16),
        text(1000, 272, 420, 40, 'Voorbeeld per docent', size=32, color=MUTED_INV, align='left'),
        text(1424, 272, 280, 40, 'Gemiddelde 7,1', size=32, color=MUTED_INV, align='right')]
TX, TW = 1160, 450
for i, (naam, cijfer, af) in enumerate([('Docent A', 7.2, False), ('Docent B', 7.0, False), ('Docent C', 5.6, True)]):
    y = 324 + i * 52
    els += [text(1000, y, 150, 40, naam, size=32, bold=af, color=WHITE if af else MUTED_INV, align='left'),
            rect(TX, y + 10, TW, 20, TRACK, r=10),
            rect(TX, y + 10, TW * cijfer / 10, 20, WHITE if af else '5B7480', r=10),
            text(1630, y, 74, 40, f'{cijfer:.1f}'.replace('.', ','), size=32, bold=True, color=WHITE if af else MUTED_INV, align='right')]
els += [rect(TX + TW * 0.71 - 1.5, 316, 3, 160, MUTED_INV)]

# 2. Tweede: wit met rand, breder dan de derde
els += [rect(120, 572, 900, 236, INK200, r=24),
        rect(122, 574, 896, 232, WHITE, r=22),
        text(168, 612, 800, 56, 'Elk cijfer is navolgbaar', font=HEAD, size=48, bold=True, align='left', ls=1.05),
        text(168, 676, 800, 40, 'Onderbouwing per rubriccriterium.', size=32, color=INK500, align='left'),
        rect(168, 728, 340, 48, INK50, r=24),
        text(168, 734, 340, 36, 'AI Act audit trail', size=32, bold=True, align='center')]

# 3. Derde: getint vlak, kleinere kop
els += [rect(1052, 572, 748, 236, INK100, r=24),
        text(1100, 612, 652, 92, 'De examencommissie borgt\nde kwaliteit', font=HEAD, size=40, bold=True, align='left', ls=1.1),
        text(1100, 720, 652, 40, 'Elke onderbouwing direct in te zien.', size=32, color=INK500, align='left')]

# Aanvulling: geen vlak, regular gewicht, dunne balk. Ondergeschikt aan alle drie de kaarten.
els += [rect(120, 840, 4, 136, INK200),
        text(160, 840, 1640, 136,
             'Consistent beoordelen is een speerpunt van dit project. Daarmee helpt het om de eisen van de '
             'accreditatiepartij hierboven steviger te borgen, en dat kan een positieve impact hebben op de pabo, '
             'die nu in de accreditatie zit.', size=32, color=NAVY, align='left', ls=1.4)]

render_html(els, 'preview/consistent-beoordelen.html')
render_pptx([els], 'consistent-beoordelen-bewerkbaar.pptx')
