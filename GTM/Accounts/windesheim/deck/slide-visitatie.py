"""Visitatie-slide: per opleiding wanneer het bezoek was en het scherpste woord
uit dat rapport. De uitkomst vertelt Dante er zelf bij."""
from deckbuild import (rect, oval, text, title, tile, foot, cols,
                       render_html, shoot, NAVY, INK100, INK200, INK500, WHITE, HEAD, M)

c3, w3 = cols(3)
els = title('Visitatie') + [rect(M, 392, 1920 - 2 * M, 4, INK100)]

BEZOEK = [
    ('november 2021', 'schoolbord', 'Van rubriek naar cijfer', 'Lerarenopleiding Nederlands'),
    ('april 2024',    'microfoon',  'Wijze en omvang',         'Journalistiek'),
    ('november 2024', 'winkel',     'Toelichting leeg',        'Ondernemerschap & Retail'),
]
for cx, (datum, ic, kern, opleiding) in zip(c3, BEZOEK):
    els += [text(cx - w3 / 2, 300, w3, 48, datum, font=HEAD, size=32, bold=True, color=INK500, ls=1.0),
            oval(cx - 12, 382, 24, WHITE, NAVY, 6),
            rect(cx - 2, 406, 4, 46, INK200)]
    els += tile(cx, 460, ic, 'amber')
    els += [text(cx - w3 / 2, 630, w3, 110, kern, font=HEAD, size=46, bold=True, ls=1.1),
            text(cx - w3 / 2, 748, w3, 70, opleiding, size=28, color=INK500, ls=1.25)]

els += foot(quote='“De narratieve feedback is niet altijd helemaal passend bij de rubric.”',
            src='Visitatierapporten NQA en Hobéon. Citaat: NQA, Ad E-commerce, november 2024, p. 24.',
            page=None)

shoot(render_html(els, 'preview/visitatie.html'), 'preview/visitatie.png')
print('preview/visitatie.png')
