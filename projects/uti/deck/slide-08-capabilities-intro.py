"""Opener van het capability-blok: vier capabilities als inhoudsopgave.

Layout-type 3 (kop + inhoud). De vier items zijn echte gelijken — elk krijgt
hierna zijn eigen slide — dus mogen ze identieke geometrie delen. Iconen,
volgorde en nummering zijn exact die van de nav-rail op slide 9 tot en met 12,
zodat de kijker daar hetzelfde rijtje herkent.

Geen kaartjes: één haarlijn bakent het rijtje af en de kolommen hangen eraan.
Nummers blijven gedempt (geen groen), want hier is nog geen item actief; groen
markeert vanaf slide 9 waar je bent.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, INK500, INK200, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION

els = []

# --- kop: bewering, geen label ---------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 1.4,
             'Getting There Takes Four Capabilities',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

els += [text(M, 210, 1010, TEXT * 3.2,
             "Drawn from our conversations with UTI, and from what we've seen "
             "work (and not work) for other customers solving the same problem.",
             font=BODY, size=TEXT, color=INK500, align='left', ls=1.45)]

# --- de vier capabilities ---------------------------------------------------
RULE_Y, TILE_Y = 436, 488
NUM_Y, LABEL_Y = 658, 698

els += [rect(M, RULE_Y, W - 2 * M, 1, INK200)]

c4, w4 = cols(4)
CAPS = [
    ('01', 'doel',       'Accuracy &\nConsistency'),
    ('02', 'sleutel',    'Technical\nDomain Fit'),
    # afbreken op het koppelteken: zo staan alle vier de labels op twee regels
    # en delen ze dezelfde basislijnen
    ('03', 'instelling', 'Institution-\nWide'),
    ('04', 'schuifjes',  'Self-\nConfiguring'),
]

for cx, (num, icon, label) in zip(c4, CAPS):
    x = cx - w4 / 2
    els += tile(x, TILE_Y, icon, tone='navy', fill=INK50, size=132, r=20, ic=64)
    els += [text(x, NUM_Y, w4, 32, num, font=HEAD, size=CAPTION,
                 color=INK500, align='left', ls=1.0),
            text(x, LABEL_Y, w4, SUB * 2.4, label, font=HEAD, size=SUB,
                 bold=True, color=NAVY, align='left', ls=1.16)]

# --- wegwijzer naar het blok dat volgt --------------------------------------
els += [text(M, 856, 900, 36, 'The next four slides walk through each capability.',
             font=BODY, size=CAPTION, color=INK500, align='left', ls=1.2)]

els += foot(dark=False, page=8)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-08.html', dark=DARK), 'preview/slide-08.png')
    print('preview/slide-08.png')
