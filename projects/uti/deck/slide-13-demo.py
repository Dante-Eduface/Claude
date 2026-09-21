"""Demo: de overgang van vertellen naar laten zien.

Statement-slide uit slides/layouts.md: één woord, veel lucht, verder niets. Dit
is het moment waarop de kijker moet stoppen met meelezen en naar het scherm moet
kijken, en dat werkt alleen als er niets anders op de slide staat om te lezen.

Navy, omdat hij het capability-blok afsluit en het bewijs erna inleidt. Links
uitgelijnd op dezelfde marge als de rest van de deck, zodat de pauze een pauze
is en geen ander deck.
"""
from deckbuild import text, foot, render_html, shoot, \
    WHITE, HEAD, M, W, HERO

els = []

# Optisch gecentreerd in de band tussen kop en voetlijn (236 tot 896).
els += [text(M, 500, W - 2 * M, HERO * 1.4, 'Demo',
             font=HEAD, size=HERO, bold=True, color=WHITE, align='left', ls=0.98)]

els += foot(dark=True, page=13)

DARK = True

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-13.html', dark=DARK), 'preview/slide-13.png')
    print('preview/slide-13.png')
