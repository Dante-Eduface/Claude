"""Het voorgestelde model: twee eigenschappen die samen één uitkomst opleveren.

Layout-type 3 (kop + inhoud) met twee gelijke kolommen eronder. De twee
concepten zijn echte gelijken, dus krijgen ze identieke geometrie. Het cijfer
is geen derde kolom maar de uitkomst van de twee erboven: daarom een groene
balk over de volle inhoudsbreedte, navy tekst erop (groen vlak + navy tekst
is de enige plek waar fel groen mag dragen). Getal en label staan op één
basislijn, zodat het als één zin leest en niet als losse tegel.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, GREEN, INK500, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, HERO

els = []

# --- kop: bewering, geen label ---------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.4,
             'Feedback Lands on Every Submission,\nat the Same Quality',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- twee concepten, identiek opgebouwd ------------------------------------
c2, w2 = cols(2)
CONCEPTS = [
    ('bericht', 'Feedback, Delivered\non the Assignment',
     'Automated feedback goes straight to the student, tied to their submission.'),
    ('weegschaal', 'Consistent,\nAccurate Feedback',
     'The same quality of feedback, regardless of which instructor grades it.'),
]

ROW_Y = 296
for cx, (icon, head, body) in zip(c2, CONCEPTS):
    x = cx - w2 / 2
    els += tile(x, ROW_Y, icon, tone='navy', fill=INK50, size=112, r=20, ic=56)
    els += [text(x, ROW_Y + 152, w2, SUB * 2.4, head, font=HEAD, size=SUB,
                 bold=True, color=NAVY, align='left', ls=1.16),
            text(x, ROW_Y + 288, w2 - 40, TEXT * 3, body, font=BODY, size=TEXT,
                 color=INK500, align='left', ls=1.45)]

# --- de uitkomst: groen vlak, navy tekst, volle inhoudsbreedte -------------
BAND_Y, BAND_H = 736, 164
els += [rect(M, BAND_Y, W - 2 * M, BAND_H, GREEN, r=20),
        text(M + 72, BAND_Y + 10, 460, HERO * 1.1, '48.5%', font=HEAD, size=HERO,
             bold=True, color=NAVY, align='left', ls=1.0),
        # label op de basislijn van het cijfer, zodat het als één zin leest
        text(M + 532, BAND_Y + 78, W - 2 * M - 532 - 72, SUB * 1.6,
             'of grading time saved', font=BODY, size=SUB,
             color=NAVY, align='left', ls=1.1)]

els += foot(dark=False, page=6)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-06.html', dark=DARK), 'preview/slide-06.png')
    print('preview/slide-06.png')
