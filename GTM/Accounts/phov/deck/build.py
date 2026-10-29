"""PHOV-deck in Eduface-stijl.

Gebouwd op de pitch-deck-skill (deckbuild.py). Geen slidetitels: de content draagt
de slide (Dante, 29-10-2026). Draai vanuit deze map: python3 build.py [slidenummers]
"""
import subprocess, sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
sys.dont_write_bytecode = True
import deckbuild as D
from deckbuild import (rect, text, foot, render_html, render_pptx,
                       NAVY, GREEN, GREEN_DEEP, INK50, INK500, WHITE, HEAD, M)

# PHOV-logo is vierkant
D.KLANT_W, D.KLANT_H = 60, 60


def label(x, y, t, color=NAVY, w=800):
    return text(x, y, w, 64, t, font=HEAD, size=52, bold=True, color=color, align='left', ls=1.0)


def bullets(x, y, w, items, *, size=34, gap=32, color=NAVY, dot=GREEN_DEEP, lines=None):
    """Elk item een eigen tekstvak met een blokje ervoor.
    lines: aantal regels per item, want er is geen auto-layout (reference.md)."""
    out, lh = [], size * 1.35
    for t, n in zip(items, lines or [2] * len(items)):
        out.append(rect(x, y + lh / 2 - 6, 12, 12, dot, r=3))
        out.append(text(x + 36, y, w - 36, n * lh, t, size=size, color=color,
                        align='left', ls=1.35))
        y += n * lh + gap
    return out


def shoot(pages):
    """Screenshot plus overloopcheck via Playwright (node), zie shoot.js."""
    subprocess.run(['node', 'shoot.js'] + [f for pair in pages for f in pair], check=True)


# ---------------------------------------------------------------- slides
def s3():
    els = [rect(M, 150, 620, 620, NAVY, r=20),
           label(M + 64, 214, 'Geld', color=GREEN, w=500)]
    els += bullets(M + 64, 314, 500, [
        'PHOV betaalt docenten voor elk uur dat ze beoordelen',
        'En PHOV eist dat ze feedback geven',
    ], color=WHITE, dot=GREEN, lines=[2, 2], gap=40)
    x = M + 620 + 96
    els += [label(x, 214, 'Consistentie')]
    els += bullets(x, 314, 1920 - M - x, [
        'Vooraf liggen de oordelen van beoordelaars ver uit elkaar, pas na overleg komen ze dichter bij elkaar',
        'Daarom kalibreren jullie scripties minstens één keer per twee jaar. De nieuwe rubric is nog niet getest.',
        'Kalibratie hoort over de inhoud te gaan, maar gaat soms over handtekeningen op een formulier',
        'De directie schuift zelf aan om mensen scherp te houden',
    ], lines=[2, 2, 2, 1])
    els += foot(page=3)
    return els


SLIDES = {3: s3}

if __name__ == '__main__':
    nums = [int(a) for a in sys.argv[1:]] or sorted(SLIDES)
    built = {n: SLIDES[n]() for n in nums}
    shoot([(render_html(els, f'preview/slide-{n}.html'), f'preview/slide-{n}.png')
           for n, els in built.items()])
    render_pptx([built[n] for n in sorted(built)], 'phov-deck-bewerkbaar.pptx')
