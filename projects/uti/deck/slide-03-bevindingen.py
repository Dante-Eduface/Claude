"""Bevindingen-slide: drie beperkingen die we bij UTI vonden (layout 4).

Drie gelijkwaardige bevindingen, dus drie echte gelijken naast elkaar: één
icoontegel, één kopje, één body per kolom, allemaal op dezelfde rasterlijnen.
Geen kaartjes eromheen — de kolomruimte doet het groeperen al, en drie
vlakken naast elkaar zou de slide luid maken zonder iets toe te voegen.

De kop vat de drie bevindingen samen als bewering; de kolommen zijn het
bewijs eronder. Licht, omdat dit de probleemstelling is die de kijker moet
kunnen narekenen, niet een statement-moment.
"""
from deckbuild import text, tile, foot, render_html, shoot, cols, \
    NAVY, INK700, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT

els = []

# --- kop: bewering, drie bijvoeglijke naamwoorden = drie kolommen -----------
els += [text(M, 88, W - 2 * M, TITLE * 2.4,
             'Assessment Today Is Rigid,\nCostly and Invisible',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- drie bevindingen op één raster ----------------------------------------
c3, w3 = cols(3)

TILE_Y, TILE = 388, 120
HEAD_Y, HEAD_H = 556, 116      # vaste kophoogte: koppen wrappen ongelijk,
BODY_Y = 684                   # de bodies moeten toch op één lijn beginnen
BODY_W = w3 - 28               # body iets smaller: de rechterkolom raakt anders
                               # exact de veilige marge

FINDINGS = [
    ('exact', 'Exact-Match\nGrading Only',
     'Blackboard can only auto-grade answers with an exact match.'),
    ('trend', "Grading Time\nDoesn't Scale",
     'New locations and programs scale instructors proportionally, '
     'and squeeze profitability.'),
    ('onzichtbaar', 'Feedback Is\na Black Box',
     "It isn't visible, so it can't be measured or influenced as a "
     'driver of retention.'),
]

for cx, (icon, head, body) in zip(c3, FINDINGS):
    x = cx - w3 / 2
    els += tile(x, TILE_Y, icon, tone='navy', fill=INK50, size=TILE, r=20, ic=56)
    els += [text(x, HEAD_Y, w3, HEAD_H, head, font=HEAD, size=SUB, bold=True,
                 color=NAVY, align='left', ls=1.08),
            text(x, BODY_Y, BODY_W, 200, body, font=BODY, size=TEXT,
                 color=INK700, align='left', ls=1.45)]

els += foot(dark=False, page=3)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-03.html', dark=DARK), 'preview/slide-03.png')
    print('preview/slide-03.png')
