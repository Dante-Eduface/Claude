"""Proefslide 1/12: Cover. Opening-layout uit Design/System/slides/layouts.md:
navy vlak, witte tekst, titel + één regel context, logo linksonder, verder niks."""
from deckbuild import rect, pic, text, title, render_html, render_pptx, shoot, NAVY, BODY, M

els = [rect(0, 0, 1920, 1080, NAVY)]
els += title('Board Update — Q3 2026', dark=True)
els += [text(M, 232, 1680, 60, 'ROM  ·  Tjarko Kwee  ·  Imec',
             font=BODY, size=40, color='FFFFFFB3', align='left')]
els += [pic('assets/logo_white.png', M, 928, 214, 58)]

shoot(render_html(els, 'preview/01-cover.html', dark=True), 'preview/01-cover.png')
print('preview klaar: preview/01-cover.png')
