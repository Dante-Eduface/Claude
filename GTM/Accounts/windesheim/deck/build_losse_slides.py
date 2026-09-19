"""Bouwt de drie losse slides: één pptx per slide plus één gecombineerde."""
from deckbuild import render_pptx, render_html, shoot

def laad(pad):
    """Voert een slide-script uit en geeft de elementenlijst terug."""
    bron = open(pad, encoding='utf-8').read()
    bron = '\n'.join(r for r in bron.split('\n')
                     if not r.startswith(('shoot(', 'print(')))
    ruimte = {}
    exec(compile(bron, pad, 'exec'), ruimte)
    return ruimte['els']

SLIDES = [('spreiding', 'slide-spreiding.py'),
          ('vergelijkbare-dataset', 'slide-eentaak.py'),
          ('aanzetten', 'slide-aanzetten.py')]

alle = []
for naam, pad in SLIDES:
    els = laad(pad)
    alle.append(els)
    render_pptx([els], f'slide-{naam}-bewerkbaar.pptx')
    shoot(render_html(els, f'preview/{naam}.html'), f'preview/{naam}.png')

render_pptx(alle, 'windesheim-losse-slides.pptx')
print(f'{len(alle)} losse pptx + windesheim-losse-slides.pptx')
