"""Huidige situatie: twee kosten die instructeurs nu dragen, naast elkaar.

De twee items zijn geen gelijken, dus krijgen ze geen gelijke vakjes. Het
getal 2-4 hrs is de claim van de slide en staat op HERO; de black box is de
tweede post en staat op SUB. Ranking dus via type, niet via twee identieke
kaarten (compositie.md 5). Ruimte scheidt de kolommen, geen lijn: een rand
zou hier alleen zwakke hierarchie repareren (compositie.md 11).

De kolommen delen drie horizontale lijnen (icoon, kop, body), zodat de
ongelijke hoogtes als rangorde lezen en niet als scheve uitlijning. De
eenheid staat naast het getal, niet eronder, anders krijgt links een vierde
regel die de gedeelde bodylijn breekt.
"""
from deckbuild import text, tile, foot, render_html, shoot, cols, \
    NAVY, INK700, INK500, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, HERO

els = []

# --- kop: bewering die de twee items samenvat ------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.2,
             'Grading Consumes Evenings,\nand the Feedback Cannot Be Measured',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- twee kolommen met ruime goot, zodat er geen scheidingslijn nodig is ---
(c1, c2), CW = cols(2, gap=96)
X1, X2 = c1 - CW / 2, c2 - CW / 2

ROW_ICON, ROW_HEAD, ROW_BODY = 352, 532, 756
TILE, IC = 120, 56

# item 1: het getal draagt de slide
els += tile(X1, ROW_ICON, 'klok', tone='navy', fill=INK50, size=TILE, r=20, ic=IC)
els += [text(X1, ROW_HEAD, CW, HERO * 1.15, '2–4 hrs', font=HEAD, size=HERO,
             bold=True, color=NAVY, align='left', ls=0.98),
        # eenheid hangt op de basislijn van het getal, niet eronder
        text(X1 + 508, ROW_HEAD + 65, 284, SUB * 1.3, 'per day', font=HEAD,
             size=SUB, color=INK500, align='left', ls=1.0),
        text(X1, ROW_BODY, CW, TEXT * 4, 'Spent grading, per instructor, often in '
             'the evening. One of the leading drivers of instructor attrition.',
             font=BODY, size=TEXT, color=INK700, align='left', ls=1.45)]

# item 2: zelfde drie lijnen, lichter gewicht
els += tile(X2, ROW_ICON, 'onzichtbaar', tone='navy', fill=INK50,
            size=TILE, r=20, ic=IC)
els += [text(X2, ROW_HEAD + 44, CW, SUB * 1.3, 'A Black Box', font=HEAD,
             size=SUB, bold=True, color=NAVY, align='left', ls=1.0),
        text(X2, ROW_BODY, CW, TEXT * 4, "Verbal feedback isn't visible, "
             "so it can't be measured or influenced as a retention driver.",
             font=BODY, size=TEXT, color=INK700, align='left', ls=1.45)]

els += foot(dark=False, page=4)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-04.html', dark=DARK), 'preview/slide-04.png')
    print('preview/slide-04.png')
