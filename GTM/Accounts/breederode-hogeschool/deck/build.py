# -*- coding: utf-8 -*-
"""Deck testochtend Breederode, 23-09-2026.
Opening, agenda, per onderwerp een titelslide plus een lege slide voor de screenshot,
en een afsluiter. Bron: deckbuild.py uit de pitch-deck skill.
"""
import os
import deckbuild as D
from deckbuild import rect, pic, text, render_html, render_pptx, NAVY, WHITE, INK100, INK500, HEAD, BODY

D.CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

def shoot(html_path, png_path):
    import subprocess
    subprocess.run([D.CHROME, '--headless', '--no-sandbox', '--disable-gpu',
                    f'--screenshot={png_path}', '--window-size=1920,1080',
                    '--hide-scrollbars', '--virtual-time-budget=2500', html_path],
                   capture_output=True)
    return png_path
D.shoot = shoot
M = 120
SOFT = '8FA9B4'          # zachte witte tekst op navy
AMBER = D.AMBER

def bg_navy():
    return [rect(0, 0, 1920, 1080, NAVY)]

def voet(dark=False, page=None):
    """Voet zonder klantlogo: er is geen Breederode-logo in Design/Merk."""
    out = [rect(M, 868, 1920 - 2 * M, 1, 'FFFFFF33' if dark else INK100)]
    out.append(pic('assets/logo_white.png' if dark else 'assets/logo_navy.png', M, 907, 170, 46))
    if page:
        out.append(text(1700, 1004, 100, 36, str(page), size=23,
                        color='FFFFFF73' if dark else '9AAFB8', align='right'))
    return out

# ---------------------------------------------------------------- slides
def opening():
    els = bg_navy()
    els += [text(M, 300, 1400, 40, '23 september 2026  ·  9:00 tot 12:30  ·  Rotterdam',
                 font=BODY, size=24, color=SOFT, align='left')]
    els += [text(M, 372, 1680, 160, 'Testochtend', font=HEAD, size=132, bold=True,
                 color=WHITE, align='left', ls=0.98)]
    els += [text(M, 556, 1400, 70, 'Eduface bij Breederode Hogeschool',
                 font=BODY, size=44, color=SOFT, align='left')]
    els += voet(dark=True)
    return els

AGENDA = [
    'Waar we staan',
    'Navolgbaarheid in beeld',
    'Modelinstructies',
    'Beoordelingsformulier en beoordelingsstijlen',
    'Snelle opmerkingen',
    'Zelf aan de slag, en de afspraken daarna',
]

def agenda():
    els = [text(M, 120, 1680, 100, 'Vanochtend', font=HEAD, size=76, bold=True,
                color=NAVY, align='left', ls=1.04)]
    y = 300
    for i, regel in enumerate(AGENDA, 1):
        els += [text(M, y, 70, 60, str(i), font=HEAD, size=44, bold=True,
                     color=AMBER, align='left')]
        els += [text(M + 96, y - 2, 1500, 60, regel, font=BODY, size=44,
                     color=NAVY, align='left')]
        y += 96
    els += voet(page=2)
    return els

def sectie(titel, onder, page):
    els = bg_navy()
    els += [text(M, 380, 1680, 140, titel, font=HEAD, size=110, bold=True,
                 color=WHITE, align='left', ls=1.0)]
    els += [text(M, 546, 1500, 80, onder, font=BODY, size=44, color=SOFT,
                 align='left', ls=1.15)]
    els += voet(dark=True, page=page)
    return els

def leeg():
    return []

def afsluiter(page):
    els = bg_navy()
    els += [text(M, 180, 1680, 100, 'En dan', font=HEAD, size=76, bold=True,
                 color=WHITE, align='left', ls=1.04)]
    regels = [
        'Twee weken testen op opdrachten die jullie al hebben nagekeken',
        'We toetsen aan jullie maat: 92% accuraatheid, 3,5 van 5 op bruikbaarheid',
        'Daarna twee weken voor de koppeling met itslearning',
    ]
    y = 360
    for r in regels:
        els += [rect(M, y + 16, 40, 4, AMBER)]
        els += [text(M + 80, y - 6, 1540, 90, r, font=BODY, size=44, color=WHITE,
                     align='left', ls=1.2)]
        y += 130
    els += voet(dark=True, page=page)
    return els

SECTIES = [
    ('Navolgbaarheid in beeld', 'Waar examinatoren uit elkaar lopen, in een overzicht'),
    ('Modelinstructies',        'Wat het model meekrijgt voordat het een woord schrijft'),
    ('Beoordelingsformulier',   'Jullie eigen formulier, een op een overgenomen'),
    ('Beoordelingsstijlen',     'Dezelfde opdracht, verschillende manieren van beoordelen'),
    ('Snelle opmerkingen',      'Vooraf ingevulde opmerkingen in de tekst, in uniforme woorden'),
]

slides, namen, donker = [], [], []
slides.append(opening());  namen.append('01-opening');  donker.append(True)
slides.append(agenda());   namen.append('02-agenda');   donker.append(False)

p = 3
for i, (t, o) in enumerate(SECTIES, 1):
    slides.append(sectie(t, o, p)); namen.append(f'{p:02d}-sectie-{i}'); donker.append(True); p += 1
    slides.append(leeg());          namen.append(f'{p:02d}-leeg-{i}');   donker.append(False); p += 1
slides.append(afsluiter(p)); namen.append(f'{p:02d}-afsluiter'); donker.append(False)

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
for els, naam, dk in zip(slides, namen, donker):
    h = render_html(els, f'preview/{naam}.html', dark=dk)
    D.shoot(h, f'preview/{naam}.png')
render_pptx(slides, 'breederode-testochtend-bewerkbaar.pptx')
print('slides:', len(slides))
