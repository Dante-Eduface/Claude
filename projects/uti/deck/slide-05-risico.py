"""Risico: de kantelslide van het deck, van 'zo is het nu' naar 'dit breekt'.

Navy, omdat dit de toonwissel markeert (kleurritme uit slides/layouts.md).
Twee items, maar geen twee gelijke vakjes: links het mechanisme in proza,
rechts de twee groeicijfers als cijferregels. Ongelijke bevindingen krijgen
ongelijke vorm (compositie.md 5), en de kolommen worden gescheiden door een
brede goot in plaats van een lijn — een rand zou hier alleen zwakke
hierarchie repareren (compositie.md 11).

De bron van de groeicijfers staat in de voettekst, niet in de bodytekst, zodat
de cijfers zelf de rechterkolom kunnen dragen.
"""
from deckbuild import text, tile, foot, render_html, shoot, cols, \
    WHITE, INV_SOFT, INK900, GREEN, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT

els = []

# --- kop: bewering die beide items samenbindt ------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.2,
             'UTI Needs More Instructors\nThan the Market Can Supply',
             font=HEAD, size=TITLE, bold=True, color=WHITE, align='left', ls=1.04)]

(c1, c2), CW = cols(2, gap=96)
X1, X2 = c1 - CW / 2, c2 - CW / 2

# blok optisch gecentreerd tussen kop en voetlijn: gelijke lucht boven en onder
TILE_Y, TILE, IC = 356, 120, 56
HEAD_Y = TILE_Y + 168

# --- item 1: het mechanisme, in proza --------------------------------------
els += tile(X1, TILE_Y, 'mensen', tone='green', fill=INK900, size=TILE, r=20, ic=IC)
els += [text(X1, HEAD_Y, CW, SUB * 2.6, 'Instructor Hiring\nIs Getting Harder',
             font=HEAD, size=SUB, bold=True, color=WHITE, align='left', ls=1.15),
        text(X1, HEAD_Y + 140, CW, TEXT * 5,
             'The same skilled-trades shortage driving '
             "UTI's enrollment also limits the supply of "
             'qualified instructors.',
             font=BODY, size=TEXT, color=INV_SOFT, align='left', ls=1.45)]

# --- item 2: dezelfde start, maar cijfers in plaats van proza --------------
els += tile(X2, TILE_Y, 'instelling', tone='green', fill=INK900, size=TILE, r=20, ic=IC)
els += [text(X2, HEAD_Y, CW, SUB * 2.6, 'Growth Plans\nWiden the Gap',
             font=HEAD, size=SUB, bold=True, color=WHITE, align='left', ls=1.15)]

NUMS = [('2', 'new campuses per year')]
# NUM_W volgt de breedte van het getal zelf: bij één cijfer zou de oude 264
# (gemeten op '12–16') een gat van twee tekens tussen cijfer en label laten.
NUM_Y, NUM_STEP, NUM_W, NUM_GAP = HEAD_Y + 132, 104, 72, 28
for i, (val, label) in enumerate(NUMS):
    y = NUM_Y + i * NUM_STEP
    # getal en label op één regel: samen één feit, niet twee kolommen
    els += [text(X2, y, NUM_W, TITLE * 1.2, val, font=HEAD, size=TITLE,
                 bold=True, color=WHITE, align='left', ls=1.0),
            text(X2 + NUM_W + NUM_GAP, y + 30, CW - NUM_W - NUM_GAP, TEXT * 1.6,
                 label, font=BODY, size=TEXT, color=INV_SOFT, align='left', ls=1.2)]

els += foot(dark=True, page=5, source='North Star strategy target.')

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-05.html', dark=DARK), 'preview/slide-05.png')
    print('preview/slide-05.png')
