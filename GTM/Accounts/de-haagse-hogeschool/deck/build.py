"""Leerprofiel-deck voor Piet Willems, De Haagse Hogeschool. Drie slides.

    python3 build.py            # alle slides naar preview/
    python3 build.py 2          # alleen slide 2
    python3 build.py --pptx     # plus leerprofiel-bewerkbaar.pptx

Bouwt op de pitch-deck-skill. CHROME in de omgeving overschrijft het Mac-pad.

Wat het leerprofiel wel en niet volgt staat in Platform/product.md (05-10-2026):
invoer is alleen schrijfopdrachten, open vragen en docentfeedback in Eduface, en
het profiel volgt de leerdoelen van het vak, niet de skills van de opleiding.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../.claude/skills/pitch-deck'))
import deckbuild as D
from deckbuild import (rect, pic, text, title, foot, render_html, render_pptx, shoot,
                       NAVY, GREEN, TINT_A, INK50, INK100, INK200, INK500, WHITE, HEAD, M)
import icons

if os.environ.get('CHROME'):
    D.CHROME = icons.CHROME = os.environ['CHROME']

# Het HHS-logo is breed (4,7:1). Op 130 px breed wordt "HOGESCHOOL" onleesbaar,
# dus het logopaar schuift 40 px naar links en het HHS-logo krijgt 170 px.
D.KLANT_W, D.KLANT_H = 170, 36

INK300, INK700 = 'A9BCC4', '2C4A57'
LIJN = 3
TOP, BOT, KOP_Y = 340, 816, 256      # inhoudsband en kolomkoppen, gelijk op elke slide

CONCEPT = 'Het leerprofiel is een concept'


def voet(**kw):
    """foot() met het logopaar 40 px naar links, zodat het brede HHS-logo past."""
    out = foot(**kw)
    for el in out:
        if el['k'] == 'pic' or (el['k'] == 'rect' and el['w'] == 1 and el['h'] == 52):
            el['x'] -= 40
    return out


def kolomkop(x, w, t):
    return [text(x, KOP_Y, w, 52, t, font=HEAD, size=44, bold=True, align='left')]


def punt(x, y, w, kop, detail, dark=False):
    """Vetgedrukt kernwoord met een regel uitleg eronder. 88 px hoog."""
    return [text(x, y, w, 44, kop, font=HEAD, size=40, bold=True,
                 color=WHITE if dark else NAVY, align='left'),
            text(x, y + 48, w, 40, detail, size=32,
                 color=INK300 if dark else INK500, align='left')]


def staven(x, y, reeks, h, w, gat, spoor, kies=None):
    """Eén staaf per datapunt, de hoogte is de stand op dat leerdoel.
    Het gekozen datapunt wordt navy, de rest groen."""
    out = []
    for i, v in enumerate(reeks):
        sx = x + i * (w + gat)
        out += [rect(sx, y, w, h, spoor, r=4),
                rect(sx, y + h * (1 - v), w, h * v, NAVY if i == kies else GREEN, r=4)]
    return out


# ------------------------------------------------------------------ slide 1
def slide_bronnen():
    els = title('Elke opdracht is een datapunt')
    mid = (TOP + BOT) / 2

    # -- A: bronnen ---------------------------------------------------------
    AX, A_END = M, 650
    BRONNEN = [('filepen', 'Schrijfopdrachten en papers'),
               ('pen',     'Open vragen'),
               ('gesprek', 'Docentfeedback in Eduface')]
    els += kolomkop(AX, 500, 'Bronnen')
    midden = [mid + (i - 1) * 120 for i in range(len(BRONNEN))]
    for (naam, label), cy in zip(BRONNEN, midden):
        icons.render(naam, 'navy')
        els += [pic(f'assets/icon-{naam}-navy.png', AX, cy - 20, 40, 40),
                text(AX + 60, cy - 20, 520, 40, label, size=32, align='left')]

    # -- B: wat er per datapunt wordt vastgelegd ----------------------------
    BX, BW = 790, 420
    els += kolomkop(BX, BW, 'Elk datapunt')
    els += [rect(BX, TOP, BW, BOT - TOP, INK50, r=20)]
    VELDEN = [('Score', 'per rubriccriterium'),
              ('Leerdoel', 'van het vak'),
              ('Moment', 'in de tijd')]
    rij, gat = 88, 48
    y = mid - (len(VELDEN) * rij + (len(VELDEN) - 1) * gat) / 2
    for kop, detail in VELDEN:
        els += punt(BX + 40, y, BW - 80, kop, detail)
        y += rij + gat

    # -- A naar B: elke bron landt in hetzelfde datapunt --------------------
    VERZAMEL = 740
    els += [rect(A_END + 24, cy - LIJN / 2, VERZAMEL - A_END - 24, LIJN, INK200) for cy in midden]
    els += [rect(VERZAMEL, midden[0], LIJN, midden[-1] - midden[0], INK200),
            rect(VERZAMEL, mid - LIJN / 2, BX - VERZAMEL, LIJN, INK200)]

    # -- C: het leerprofiel van één student ---------------------------------
    CX, CW = 1310, 490
    els += kolomkop(CX, CW, 'Leerprofiel')
    els += [rect(CX, TOP, CW, BOT - TOP, NAVY, r=20),
            rect(BX + BW, mid - LIJN / 2, CX - BX - BW, LIJN, INK200)]
    els += [text(CX + 40, TOP + 36, CW - 80, 40, 'Eén student, over tijd',
                 size=32, color=INK300, align='left')]
    LEERDOELEN = [('Analyseren',     [.30, .42, .40, .55, .62, .76]),
                  ('Bronnengebruik', [.48, .46, .50, .47, .49, .50]),
                  ('Argumenteren',   [.25, .34, .48, .36, .58, .68])]
    SH, SW, SG = 76, 14, 10
    blok_w = 6 * (SW + SG) - SG
    bx = CX + CW - 40 - blok_w
    y = TOP + 104
    for naam, reeks in LEERDOELEN:
        els += [text(CX + 40, y + SH / 2 - 20, bx - CX - 56, 40, naam,
                     size=32, color=WHITE, align='left')]
        els += staven(bx, y, reeks, SH, SW, SG, INK700)
        y += SH + 36
    els += [text(bx - 40, y - 24, blok_w + 40, 32, 'tijd  →', size=24, color=INK300, align='right')]

    els += voet(src=f'{CONCEPT}. De leerdoelen zijn voorbeelden: '
                    'elk vak werkt met zijn eigen leerdoelen.', page=1)
    return els


# ------------------------------------------------------------------ slide 2
def slide_docent():
    els = title('Wie ligt op schema, en waarom')

    # Het scherm: een kader met een kopregel en twee panelen.
    FX, FY, FW, FH = M, 236, 1920 - 2 * M, 600
    PAD = 24
    els += [rect(FX, FY, FW, FH, INK50, r=20),
            text(FX + 32, FY + 22, 900, 36, 'Docentweergave  ·  Onderzoeksmethoden 2',
                 size=26, bold=True, align='left')]
    # Het label hoort in het scherm zelf: dit is geen bestaand product.
    LW = 452
    els += [rect(FX + FW - PAD - LW, FY + 16, LW, 44, TINT_A, r=22),
            text(FX + FW - PAD - LW, FY + 25, LW, 30, 'Illustratief voorbeeld, fictieve data',
                 size=24, bold=True, align='center')]

    PY = FY + 80
    PH = FY + FH - PAD - PY

    # -- links: één student, groei per leerdoel ----------------------------
    LX, LWD = FX + PAD, 960
    els += [rect(LX, PY, LWD, PH, WHITE, r=8),
            text(LX + 32, PY + 26, 600, 40, 'Learning Evidence Timeline',
                 font=HEAD, size=34, bold=True, align='left'),
            text(LX + 32, PY + 72, 600, 32, 'Sanne de Vries, per leerdoel',
                 size=26, color=INK500, align='left'),
            text(LX + LWD - 232, PY + 72, 200, 32, 'tijd  →',
                 size=24, color=INK500, align='right')]
    RIJEN = [('Analyseren',     [.28, .36, .41, .48, .55, .60, .66, .72], None),
             ('Bronnengebruik', [.45, .47, .44, .46, .48, .45, .47, .46], None),
             ('Argumenteren',   [.30, .38, .46, .52, .34, .55, .62, .68], 4)]
    bx, SW, SG, SH = LX + 300, 28, 56, 56
    y = PY + 130
    for naam, reeks, kies in RIJEN:
        els += [text(LX + 32, y + SH / 2 - 18, 250, 36, naam, size=28, align='left')]
        els += staven(bx, y, reeks, SH, SW, SG, INK100, kies)
        if kies is not None:
            sel_x, sel_y = bx + kies * (SW + SG) + SW / 2, y + SH
        y += SH + 20
    # Het bewijs achter één punt: welke opdracht, welke score, wat de docent schreef.
    CY = y + 4
    els += [rect(sel_x - LIJN / 2, sel_y, LIJN, CY - sel_y, NAVY),
            rect(LX + 32, CY, LWD - 64, PY + PH - 24 - CY, INK50, r=8),
            text(LX + 56, CY + 16, LWD - 112, 34,
                 'Paper 2, week 6  ·  Argumenteren 2 van 4', size=28, bold=True, align='left'),
            text(LX + 56, CY + 56, LWD - 112, 34,
                 'Feedback docent: “Je conclusie volgt niet uit je eigen data.”',
                 size=28, color=INK500, align='left')]

    # -- rechts: de groep ---------------------------------------------------
    RX = LX + LWD + PAD
    RW = FX + FW - PAD - RX
    els += [rect(RX, PY, RW, PH, WHITE, r=8),
            text(RX + 32, PY + 26, RW - 64, 40, 'Groep 2B', font=HEAD, size=34, bold=True, align='left'),
            text(RX + 32, PY + 72, RW - 64, 32, '28 studenten', size=26, color=INK500, align='left')]
    GROEP = [('check', 'green',     '22', 'op schema',            'op alle leerdoelen'),
             ('wisselend', 'amber', '6',  'extra aandacht nodig', 'op Bronnengebruik'),
             ('groep', 'navy',      '9',  'maken dezelfde fout',  'correlatie gelezen als causaliteit')]
    y = PY + 140
    for icoon, tint, n, label, detail in GROEP:
        icons.render(icoon, tint)
        els += [pic(f'assets/icon-{icoon}-{tint}.png', RX + 32, y + 6, 36, 36),
                text(RX + 84, y, 76, 48, n, font=HEAD, size=44, bold=True, align='left'),
                text(RX + 164, y + 4, RW - 196, 34, label, size=28, bold=True, align='left'),
                text(RX + 164, y + 42, RW - 196, 32, detail, size=26, color=INK500, align='left')]
        y += 108

    els += voet(src='Illustratief voorbeeld met fictieve namen en cijfers. '
                    f'{CONCEPT}, dit is geen bestaand scherm.', page=2)
    return els


# ------------------------------------------------------------------ slide 3
def slide_actie():
    els = title('Van inzicht naar actie')

    DOCENT = [('Vroeg signaleren',               'wie achterloopt'),
              ('Gericht instructie geven',       'aan groepen die dezelfde les nodig hebben'),
              ('Gesprekken op basis van bewijs', 'met de student, in plaats van op gevoel'),
              ('Onderwijs bijsturen',            'op wat veel studenten lastig vinden')]
    INSTELLING = [('Draagt bij aan minder uitstroom',     'behoud van studenten, collegegeld en financiering'),
                  ('Betere voortgang van studenten',      'achterstand is eerder zichtbaar en bij te sturen'),
                  ('Onderbouwing van onderwijskwaliteit', 'met bewijs per leerdoel, over alle studenten heen'),
                  ('Inzicht dat nakijken niet geeft',     'groei per leerdoel over tijd, niet één cijfer')]

    LX, LW = M, 720
    CX = 912
    CW = 1920 - M - CX
    # Vier punten per kant hebben meer hoogte nodig dan de band op slide 1 en 2,
    # dus koppen en kaart staan hier 16 px hoger en lopen 12 px verder door.
    top, bot, pad = TOP - 16, BOT + 12, 30
    els += [text(LX, KOP_Y - 8, LW, 52, 'Wat de docent doet', font=HEAD, size=44, bold=True, align='left'),
            text(CX, KOP_Y - 8, CW, 52, 'Wat de instelling wint', font=HEAD, size=44, bold=True, align='left')]
    els += [rect(CX, top, CW, bot - top, NAVY, r=20)]

    rij = 88
    gat = (bot - top - 2 * pad - len(DOCENT) * rij) / (len(DOCENT) - 1)
    y = top + pad
    for (k1, d1), (k2, d2) in zip(DOCENT, INSTELLING):
        els += punt(LX, y, LW, k1, d1)
        els += punt(CX + 44, y, CW - 88, k2, d2, dark=True)
        y += rij + gat

    els += voet(src='Effecten op uitstroom en voortgang zijn verwachtingen, nog niet gemeten. '
                    f'{CONCEPT}.', page=3)
    return els


SLIDES = {1: ('01-bronnen', slide_bronnen),
          2: ('02-docent', slide_docent),
          3: ('03-actie', slide_actie)}


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
