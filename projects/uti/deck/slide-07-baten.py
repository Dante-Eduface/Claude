"""Wat het model oplevert: drie gevolgen van dezelfde ontkoppeling.

Layout-type 4 (drie kolommen). De drie baten zijn echte gelijken, dus krijgen
ze identieke geometrie: icoontegel, kopje, twee regels. Ongelijk gewicht zou
hier suggereren dat er een rangorde is die het materiaal niet geeft.

Dezelfde kolom-DNA als slide 6 (tegel, SUB-kop, TEXT-body), maar zonder het
groene uitkomstvlak: slide 6 loopt uit op één cijfer, deze slide loopt uit op
een veld van drie. De kopregel doet de samenvatting, niet een vierde blok.

De North Star-clausule staat in de voetregel, niet in kolom 3: het is de
herkomst van de claim, geen onderdeel van de baat zelf.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, INK500, INK100, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT

els = []

# --- kop: bewering, geen label ---------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.2,
             'Capacity Grows Without Hiring to Match',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# Haarlijn: geeft de drie kolommen een bovenrand om aan te hangen, zodat de
# ruimte onder de kop een veld wordt in plaats van een gat.
els += [rect(M, 252, W - 2 * M, 1, INK100)]

# --- drie baten, identiek opgebouwd ----------------------------------------
c3, w3 = cols(3)
BENEFITS = [
    ('ontkoppeld', 'Grading Capacity,\nDecoupled from Headcount',
     'Output no longer rises and falls with instructor headcount.'),
    ('klok', 'More Time to Teach,\nLess Evening Work',
     'Supports instructor retention.'),
    ('trend', 'Scales Without\nProportional Cost',
     'New campuses and programs, without headcount growing 1:1.'),
]

ROW_Y = 378
# Vaste y voor kop en body, zodat de drie kolommen op dezelfde regels landen
# ook als één kop een regel langer wordt.
HEAD_Y, BODY_Y = ROW_Y + 178, ROW_Y + 350

for cx, (icon, head, body) in zip(c3, BENEFITS):
    x = cx - w3 / 2
    els += tile(x, ROW_Y, icon, tone='navy', fill=INK50, size=132, r=20, ic=64)
    els += [text(x, HEAD_Y, w3, SUB * 3.4, head, font=HEAD, size=SUB,
                 bold=True, color=NAVY, align='left', ls=1.16),
            text(x, BODY_Y, w3 - 32, TEXT * 3.2, body, font=BODY, size=TEXT,
                 color=INK500, align='left', ls=1.45)]

els += foot(dark=False, page=7,
            source="Aligned with North Star Phase II's efficiency "
                   "and optimization pillar.")

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-07.html', dark=DARK), 'preview/slide-07.png')
    print('preview/slide-07.png')
