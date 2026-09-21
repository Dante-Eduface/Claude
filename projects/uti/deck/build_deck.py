"""Zet het hele UTI-deck samen tot één bewerkbare pptx.

Elke slide is een eigen bestand met een lijst `els` en een vlag `DARK`. Dit
script laadt ze op paginavolgorde en rendert ze twee keer: als pptx met echte
tekstvakken en vormen (zo blijft hij bewerkbaar in PowerPoint, Keynote en
Canva) en als PNG-preview per slide.
"""
import importlib.util, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

from deckbuild import render_pptx, render_html, shoot, rect, NAVY, WHITE, W, H_


def canvas(dark):
    """De HTML-preview krijgt zijn achtergrond uit CSS, de pptx niet. Zonder dit
    vlak exporteert een navy slide als witte tekst op wit papier."""
    return [rect(0, 0, W, H_, NAVY if dark else WHITE)]

SLIDES = [
    (1,  'slide-01-opening.py'),
    (2,  'slide-02-agenda.py'),
    (3,  'slide-03-bevindingen.py'),
    (4,  'slide-04-huidige-situatie.py'),
    (5,  'slide-05-risico.py'),
    (6,  'slide-06-model.py'),
    (7,  'slide-07-baten.py'),
    (8,  'slide-08-capabilities-intro.py'),
    (9,  'slide-09-accuracy.py'),
    (10, 'slide-10-domein.py'),
    (11, 'slide-11-instelling.py'),
    (12, 'slide-12-configuratie.py'),
    (13, 'slide-13-demo.py'),
    (14, 'slide-14-bathspa.py'),
    (15, 'slide-15-aanbod.py'),
    (16, 'slide-16-vervolg.py'),
]

OUT = 'UTI-Eduface-deck.pptx'


def load(path):
    spec = importlib.util.spec_from_file_location(f'_slide_{path}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(preview=True, alleen=None, uit=None):
    """alleen: lijst paginanummers voor een losse export, bijvoorbeeld [2, 13]."""
    doel = uit or OUT
    built, missing = [], []
    for page, fname in SLIDES:
        if alleen and page not in alleen:
            continue
        if not os.path.exists(fname):
            missing.append((page, fname))
            continue
        mod = load(fname)
        built.append((page, fname, mod.els, getattr(mod, 'DARK', False)))

    if missing:
        print('ONTBREKEND:', ', '.join(f'{p}:{f}' for p, f in missing))

    render_pptx([canvas(dark) + els for _, _, els, dark in built], doel)
    print(f'{len(built)} slides -> {doel}')

    if preview:
        os.makedirs('preview', exist_ok=True)
        for page, _, els, dark in built:
            n = f'slide-{page:02d}'
            shoot(render_html(els, f'preview/{n}.html', dark=dark), f'preview/{n}.png')
        print(f'{len(built)} previews -> preview/')


if __name__ == '__main__':
    # python3 build_deck.py                       het hele deck
    # python3 build_deck.py --only 2,13 --out x.pptx   losse slides als eigen bestand
    alleen = uit = None
    if '--only' in sys.argv:
        alleen = [int(n) for n in sys.argv[sys.argv.index('--only') + 1].split(',')]
    if '--out' in sys.argv:
        uit = sys.argv[sys.argv.index('--out') + 1]
    main(preview='--no-preview' not in sys.argv, alleen=alleen, uit=uit)
