"""Openingsslide (layouts.md type 1): navy vlak, de claim groot, verder niets.

De titel is hier het enige leesmoment, dus hij krijgt HERO over twee regels en
breekt op de komma: 'Scaling Consistent' en 'Timely Feedback at UTI' lezen dan
als twee ademhalingen in plaats van als één lange balk. Eronder één contextregel
op SUB in de zachte inverse kleur, dicht op de titel zodat ze samen één blok
vormen. Onderaan de lockup in plaats van foot(): een openingsslide draagt geen
paginanummer en geen scheidingslijn, en de lockup zakt tot precies op de
veilige marge zodat het blok erboven lucht houdt.
"""
from deckbuild import text, lockup, render_html, shoot, \
    WHITE, INV_SOFT, HEAD, BODY, M, W, HERO, SUB

els = []

TITLE_Y = 336

els += [text(M, TITLE_Y, W - 2 * M, HERO * 2.2,
             'Scaling Consistent,\nTimely Feedback at UTI',
             font=HEAD, size=HERO, bold=True, color=WHITE, align='left', ls=0.98)]

# Contextregel dicht onder de kop: samen één blok, optisch gecentreerd in het
# veld boven de lockup.
els += [text(M, TITLE_Y + 292, W - 2 * M, SUB * 1.6,
             'Eduface for Universal Technical Institute',
             font=BODY, size=SUB, color=INV_SOFT, align='left', ls=1.3)]

# Geen foot() op de opening: alleen de merk-lockup, onderaan op de marge.
els += lockup(M, 920, dark=True)

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-01.html', dark=DARK), 'preview/slide-01.png')
    print('preview/slide-01.png')
