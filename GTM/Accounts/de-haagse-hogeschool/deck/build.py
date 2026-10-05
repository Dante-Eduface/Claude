"""Leerprofiel-deck voor Piet Willems, De Haagse Hogeschool. Drie slides.

    python3 build.py            # alle slides naar preview/
    python3 build.py 1          # alleen slide 1
    python3 build.py --pptx     # plus leerprofiel-bewerkbaar.pptx

Bouwt op de pitch-deck-skill. CHROME in de omgeving overschrijft het Mac-pad.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../.claude/skills/pitch-deck'))
import deckbuild as D
from deckbuild import (rect, pic, text, title, foot, render_html, render_pptx, shoot,
                       NAVY, GREEN, GREEN_DEEP, INK50, INK100, INK200, INK500, WHITE,
                       HEAD, M)
import icons

if os.environ.get('CHROME'):
    D.CHROME = icons.CHROME = os.environ['CHROME']

# Het HHS-logo is breed (4,7:1). Op 130 px breed wordt "HOGESCHOOL" onleesbaar,
# dus het logopaar schuift 40 px naar links en het HHS-logo krijgt 170 px.
D.KLANT_W, D.KLANT_H = 170, 36

INK300, INK700 = 'A9BCC4', '2C4A57'
LIJN = 3


def voet(**kw):
    """foot() met het logopaar 40 px naar links, zodat het brede HHS-logo past."""
    out = foot(**kw)
    for el in out:
        if el['k'] == 'pic' or (el['k'] == 'rect' and el['w'] == 1 and el['h'] == 52):
            el['x'] -= 40
    return out


# ------------------------------------------------------------------ slide 1
def slide_bronnen():
    els = title('Elke opdracht is een datapunt')

    TOP, BOT = 340, 816              # inhoudsband onder de kolomkoppen
    KOP_Y = 256

    # -- A: bronnen ---------------------------------------------------------
    AX, A_END = M, 650
    BRONNEN = [
        ('filepen',   'Schrijfopdrachten en papers'),
        ('pen',       'Open vragen'),
        ('microfoon', 'Audio: mondeling, presentaties'),
        ('iama',      'Formatieve oefententamens'),
        ('historie',  'Wekelijkse formatieve vragen'),
        ('gesprek',   'Ontvangen feedback'),
    ]
    for naam, _ in BRONNEN:
        icons.render(naam, 'navy')
    els += [text(AX, KOP_Y, 500, 52, 'Bronnen', font=HEAD, size=44, bold=True, align='left')]
    pitch = (BOT - TOP) / len(BRONNEN)
    midden = [TOP + pitch / 2 + i * pitch for i in range(len(BRONNEN))]
    for (naam, label), cy in zip(BRONNEN, midden):
        els += [pic(f'assets/icon-{naam}-navy.png', AX, cy - 20, 40, 40),
                text(AX + 60, cy - 20, 520, 40, label, size=32, align='left')]

    # -- B: wat er per datapunt wordt vastgelegd ----------------------------
    BX, BW = 790, 420
    els += [text(BX, KOP_Y, BW, 52, 'Elk datapunt', font=HEAD, size=44, bold=True, align='left')]
    els += [rect(BX, TOP, BW, BOT - TOP, INK50, r=20)]
    VELDEN = [('Score', 'per rubriccriterium'),
              ('Leerdoel', 'van het vak'),
              ('Skill', 'van de opleiding'),
              ('Moment', 'in de tijd')]
    rij, gat = 88, 20
    y = TOP + ((BOT - TOP) - (len(VELDEN) * rij + (len(VELDEN) - 1) * gat)) / 2
    for kop, detail in VELDEN:
        els += [text(BX + 40, y, BW - 80, 44, kop, font=HEAD, size=40, bold=True, align='left'),
                text(BX + 40, y + 48, BW - 80, 40, detail, size=32, color=INK500, align='left')]
        y += rij + gat

    # -- A naar B: elke bron landt in hetzelfde datapunt --------------------
    VERZAMEL = 740
    els += [rect(A_END + 24, cy - LIJN / 2, VERZAMEL - A_END - 24, LIJN, INK200) for cy in midden]
    els += [rect(VERZAMEL, midden[0], LIJN, midden[-1] - midden[0], INK200),
            rect(VERZAMEL, (TOP + BOT) / 2 - LIJN / 2, BX - VERZAMEL, LIJN, INK200)]

    # -- C: het leerprofiel van één student ---------------------------------
    CX, CW = 1310, 490
    els += [text(CX, KOP_Y, CW, 52, 'Leerprofiel', font=HEAD, size=44, bold=True, align='left')]
    els += [rect(CX, TOP, CW, BOT - TOP, NAVY, r=20),
            rect(BX + BW, (TOP + BOT) / 2 - LIJN / 2, CX - BX - BW, LIJN, INK200)]
    els += [text(CX + 40, TOP + 36, CW - 80, 40, 'Eén student, over tijd',
                 size=32, color=INK300, align='left')]

    # Groei per skill: elke staaf is een moment, de hoogte de stand op die skill.
    SKILLS = [('Kritisch denken', [.30, .42, .40, .55, .62, .76]),
              ('Onderzoeken',     [.50, .47, .52, .49, .50, .52]),
              ('Presenteren',     [.20, .28, .46, .42, .60, .68])]
    SH, SW, SG = 76, 14, 10                       # staafhoogte max, breedte, gat
    blok_w = len(SKILLS[0][1]) * (SW + SG) - SG
    bx = CX + CW - 40 - blok_w
    y = TOP + 104
    for naam, reeks in SKILLS:
        els += [text(CX + 40, y + SH / 2 - 20, bx - CX - 56, 40, naam,
                     size=32, color=WHITE, align='left')]
        for i, v in enumerate(reeks):
            x = bx + i * (SW + SG)
            els += [rect(x, y, SW, SH, INK700, r=4),
                    rect(x, y + SH * (1 - v), SW, SH * v, GREEN, r=4)]
        y += SH + 36
    els += [text(bx, y - 24, blok_w, 32, 'tijd  →', size=24, color=INK300, align='right')]

    els += voet(src='Het leerprofiel is een concept. De skills zijn voorbeelden: '
                    'een instelling werkt met haar eigen skills.', page=1)
    return els


SLIDES = {1: ('01-bronnen', slide_bronnen)}


if __name__ == '__main__':
    kies = [int(a) for a in sys.argv[1:] if a.isdigit()] or sorted(SLIDES)
    alle = []
    for n in kies:
        naam, bouw = SLIDES[n]
        els = bouw()
        alle.append(els)
        print(shoot(render_html(els, f'preview/{naam}.html'), f'preview/{naam}.png'))
    if '--pptx' in sys.argv:
        print(render_pptx(alle, 'leerprofiel-bewerkbaar.pptx'))
