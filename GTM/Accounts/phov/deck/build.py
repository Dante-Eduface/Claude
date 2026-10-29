"""PHOV-deck in PHOV-huisstijl (phov.nl, oktober 2026).

Hergebruikt de elementen en de pptx-renderer van de pitch-deck-skill, met eigen
kleuren, fonts en voet. Draai vanuit deze map: python3 build.py [slidenummers]
"""
import html as H, sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
from deckbuild import rect, pic, render_pptx

# Uit phov.nl/css/style.css
NAVY, BLUE = '112E65', '00539B'
GREEN, GREEN_DK, GREEN_LT = '8CC63F', '69AA13', 'D4E9C2'
BLUE_LT, INK = 'EEF3F7', '333333'
WHITE, MUTED, LINE = 'FFFFFF', '6B7A90', 'C1D5E6'
# Site: Helvetica Rounded Condensed Bold (koppen) en Meta Plus (tekst).
# Vrij beschikbare evenknieën, ook in Canva: Barlow Condensed en Fira Sans (Meta-familie).
HEAD, BODY = 'Barlow Condensed', 'Fira Sans'
M = 120


def text(x, y, w, h, t, *, font=BODY, size=34, bold=False, color=NAVY, align='left', ls=1.3):
    return dict(k='text', x=x, y=y, w=w, h=h, t=t, font=font, size=size,
                bold=bold, color=color, align=align, ls=ls)


def label(x, y, t, color=GREEN_DK, w=800):
    return text(x, y, w, 60, t.upper(), font=HEAD, size=48, bold=True, color=color, ls=1.0)


def bullets(x, y, w, items, *, size=34, gap=30, color=NAVY, dot=GREEN, lines=None):
    """Elk item een eigen tekstvak met een groen blokje ervoor.
    lines: aantal regels per item (geen auto-layout, zie reference.md)."""
    out, lh = [], size * 1.3
    lines = lines or [2] * len(items)
    for t, n in zip(items, lines):
        out.append(rect(x, y + lh / 2 - 7, 14, 14, dot, r=3))
        out.append(text(x + 40, y, w - 40, n * lh, t, size=size, color=color))
        y += n * lh + gap
    return out


def frame(page):
    """Groene balk boven zoals op phov.nl, voet met logo's en paginanummer."""
    return [rect(0, 0, 1920, 22, GREEN), rect(0, 22, 1920, 10, GREEN_LT),
            rect(M, 900, 1920 - 2 * M, 3, '91B5D4'),
            pic('assets/klant.png', M, 930, 90, 90),
            pic('assets/logo_navy.png', 1560, 958, 130, 35),
            text(1720, 960, 80, 36, str(page), size=26, color=MUTED, align='right')]


def render_html(els, path, prefix='../'):
    parts = []
    for el in els:
        st = (f"left:{el['x']:.1f}px;top:{el['y']:.1f}px;"
              f"width:{el['w']:.1f}px;height:{el['h']:.1f}px;")
        if el['k'] == 'rect':
            parts.append(f'<div style="position:absolute;{st}background:#{el["fill"]};'
                         f'border-radius:{el.get("r",0):.1f}px"></div>')
        elif el['k'] == 'pic':
            parts.append(f'<img src="{prefix}{el["p"]}" style="position:absolute;{st}object-fit:contain">')
        elif el['k'] == 'text':
            parts.append(
                f'<div style="position:absolute;{st}font-family:\'{el["font"]}\',sans-serif;'
                f'font-size:{el["size"]}px;font-weight:{700 if el["bold"] else 400};'
                f'color:#{el["color"]};text-align:{el["align"]};line-height:{el["ls"]};'
                f'white-space:pre-line;outline:var(--dbg)">{H.escape(el["t"])}</div>')
    open(path, 'w', encoding='utf-8').write(
        '<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;700'
        '&family=Fira+Sans:wght@400;700&display=swap" rel="stylesheet">'
        '<style>*{margin:0;padding:0;box-sizing:border-box}'
        '.slide{position:relative;width:1920px;height:1080px;overflow:hidden;background:#fff}'
        '</style></head><body><div class="slide">' + ''.join(parts) + '</div></body></html>')
    return path


def shoot(pages):
    """pages: [(html, png)]. Meldt tekst die buiten zijn kader loopt."""
    import subprocess
    subprocess.run(['node', 'shoot.js'] + [f for pair in pages for f in pair], check=True)


# ---------------------------------------------------------------- slides
def s3():
    els = frame(3)
    # Links: geld, op navy vlak zoals het nieuwsbriefblok op phov.nl
    els += [rect(M, 150, 620, 620, NAVY)]
    els += [label(M + 56, 206, 'Geld', color=GREEN, w=520)]
    els += bullets(M + 56, 300, 520, [
        'PHOV betaalt docenten voor elk uur dat ze beoordelen',
        'En PHOV eist dat ze feedback geven',
    ], color=WHITE, lines=[2, 2], gap=40)
    x = M + 620 + 96
    els += [label(x, 206, 'Consistentie')]
    els += bullets(x, 300, 1920 - M - x, [
        'Vooraf liggen de oordelen van beoordelaars ver uit elkaar, pas na overleg komen ze dichter bij elkaar',
        'Daarom kalibreren jullie scripties minstens één keer per twee jaar. De nieuwe rubric is nog niet getest.',
        'Kalibratie hoort over de inhoud te gaan, maar gaat soms over handtekeningen op een formulier',
        'De directie schuift zelf aan om mensen scherp te houden',
    ], lines=[2, 2, 2, 1])
    return els


SLIDES = {3: s3}

if __name__ == '__main__':
    nums = [int(a) for a in sys.argv[1:]] or sorted(SLIDES)
    built = {n: SLIDES[n]() for n in nums}
    shoot([(render_html(els, f'preview/slide-{n}.html'), f'preview/slide-{n}.png')
           for n, els in built.items()])
    render_pptx([built[n] for n in sorted(built)], 'phov-deck-bewerkbaar.pptx')
