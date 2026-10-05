"""Deck: nieuwe designer voorstellen aan Jeroen en Menno (oktober 2026).

Draaien vanuit deze map:  python3 build.py
Bouwt per slide een PNG-preview in preview/ en een bewerkbare pptx voor Canva.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../.claude/skills/pitch-deck'))
import deckbuild as D
from deckbuild import rect, oval, pic, text, title, tile, render_html, render_pptx
import subprocess
from deckbuild import NAVY, WHITE, INK50, INK100, INK200, INK500, HEAD, BODY, M

if not os.path.exists(D.CHROME):
    D.CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

W = 1920 - 2 * M


def shoot(html_path, png_path):
    subprocess.run([D.CHROME, '--headless', '--no-sandbox', '--disable-gpu',
                    f'--screenshot={png_path}', '--window-size=1920,1300',
                    '--hide-scrollbars', '--virtual-time-budget=4000', html_path],
                   capture_output=True)
    from PIL import Image
    Image.open(png_path).crop((0, 0, 1920, 1080)).save(png_path)
    return png_path


SOFT = '9EABB1'          # foreground-inverse-soft (wit op 62%) op navy, plat gemaakt voor pptx


def voet(quote=None, src=None, page=None, dark=False):
    """Voet zonder klantlogo: dit deck is intern."""
    out = [rect(M, 868, W, 1, '24475A' if dark else INK100)]
    if quote:
        out.append(text(M, 900, 1320, 56, quote, size=34, color=NAVY, align='left', ls=1.3))
    if src:
        out.append(text(M, 912, 1320, 40, src, size=23, color=SOFT if dark else INK500,
                        align='left', ls=1.3))
    out.append(pic(D.LOGO_WIT if dark else D.LOGO_NAVY, 1800 - 170, 907, 170, 46))
    if page:
        out.append(text(1700, 1004, 100, 36, str(page), size=23,
                        color='5E7A88' if dark else '9AAFB8', align='right'))
    return out


def navy():
    return [rect(0, 0, 1920, 1080, NAVY)]


# ---------------------------------------------------------------- slide 1: wie
def wie():
    els = navy()
    els.append(text(M, 250, 960, 40, 'Voorstel, oktober 2026', size=30, color=SOFT, align='left'))
    els.append(text(M, 320, 960, 140, '[Naam]', font=HEAD, size=132, bold=True,
                    color=WHITE, align='left', ls=0.98))
    els.append(text(M, 500, 900, 120, 'Product designer die ook zelf bouwt, van Figma tot live app.',
                    size=44, color=SOFT, align='left', ls=1.15))
    els.append(text(M, 700, 900, 40, '[Opleiding]  ·  woont in Den Haag  ·  30 uur per week',
                    size=30, color=SOFT, align='left'))
    # Fotovlak: in Canva vervangen door de echte foto
    els.append(rect(1240, 200, 560, 560, '163B4C', r=20))
    els.append(text(1240, 455, 560, 50, 'Foto', size=40, color=SOFT))
    els += voet(page=1, dark=True)
    return els


# ---------------------------------------------------------------- slide 2: waarom
def waarom():
    els = title('Ontwerpt het en bouwt het zelf')
    blokken = [
        ('code', 'Eigen app, live',
         'In Figma ontworpen met een eigen design system, gebouwd met een echte login. Draait nu op de telefoon.'),
        ('trend', 'Website in Framer',
         'Voor een detailingstudio, ontworpen en gebouwd. Volgens de kandidaat 30 tot 40% meer omzet.'),
        ('groep', 'Scouting',
         'Organiseerde evenementen tot 30.000 bezoekers. Deed ook sponsoring, video en social.'),
    ]
    cw = (W - 2 * 72) / 3
    for i, (ic, kop, body) in enumerate(blokken):
        x = M + i * (cw + 72)
        els += tile(x + 64, 280, ic, 'navy', size=128)
        els.append(text(x, 452, cw, 52, kop, font=HEAD, size=44, bold=True, align='left'))
        els.append(text(x, 524, cw, 230, body, size=32, align='left', ls=1.4))
    els += voet(src='Omzetcijfer: eigen opgave van de kandidaat, niet gecontroleerd.', page=2)
    return els


# ---------------------------------------------------------------- slide 4: wat
def wat():
    els = title('Eerst de Paper Grader')
    lw = 800
    els.append(text(M, 280, lw, 52, 'Focus', font=HEAD, size=44, bold=True, align='left'))
    els.append(text(M, 352, lw, 240,
                    'De beoordelingsflow van AI Paper Grader en AI Exam Grader. Dat is wat we verkopen. '
                    'Dante begeleidt, Samuel bouwt na de overdracht.',
                    size=32, align='left', ls=1.4))
    rx = 1000
    els.append(text(rx, 280, 800, 52, 'Als er tijd over is', font=HEAD, size=44, bold=True, align='left'))
    for i, punt in enumerate(['Waarom gratis gebruikers (PLG) afhaken',
                              'Mailtool kiezen en de mailflow bouwen',
                              'Banners voor beurzen']):
        y = 352 + i * 68
        els.append(rect(rx, y + 16, 12, 12, INK200, r=3))
        els.append(text(rx + 36, y, 760, 44, punt, size=32, align='left'))
    # Pluspunt
    els.append(rect(M, 640, W, 168, INK50, r=20))
    els.append(text(M + 48, 676, W - 96, 100,
                    'Pluspunt: elke woensdag feedback van docenten op de eigen opleiding. '
                    'Gratis gebruikersonderzoek bij precies onze doelgroep.',
                    size=32, align='left', ls=1.4))
    els += voet(page=4)
    return els


# ---------------------------------------------------------------- slide 5: beslissen
def beslissen():
    els = navy()
    els += title('Beslissen voor woensdag', dark=True)
    rijen = [
        ('Gaan we het doen?', 'Akkoord nodig uiterlijk wo 7 oktober, anders kan het sprintvoorstel niet op tijd in.'),
        ('Vergoeding', 'Nog open. De kandidaat staat open voor een lager begin, bijstellen op basis van het werk.'),
        ('Tweede gesprek', 'Met Jeroen en Menno, online of in Leiden.'),
        ('Geheimhouding', 'Werkt met echte inleveringen van studenten. Afspraak nodig, ligt bij Jeroen.'),
    ]
    for i, (kop, body) in enumerate(rijen):
        y = 290 + i * 136
        if i:
            els.append(rect(M, y - 28, W, 1, '24475A'))
        els.append(text(M, y, 560, 52, kop, font=HEAD, size=44, bold=True, color=WHITE, align='left'))
        els.append(text(720, y + 4, 1080, 96, body, size=32, color=SOFT, align='left', ls=1.35))
    els += voet(page=5, dark=True)
    return els


# ---------------------------------------------------------------- slide 3: de sprint
def sprint():
    els = title('Drie dagen per week bij Eduface')

    # Weekstrip: welke dag waar naartoe gaat
    dagen = [('Ma', 'Eduface', True), ('Di', 'Eduface', True), ('Wo', 'Les', False),
             ('Do', 'Eduface', True), ('Vr', 'Vrij', False),
             ('Za', 'Bijbaan', False), ('Zo', 'Bijbaan', False)]
    gap = 24
    tw = (W - 6 * gap) / 7
    y = 272
    for i, (dag, wat, edu) in enumerate(dagen):
        x = M + i * (tw + gap)
        els.append(rect(x, y, tw, 176, NAVY if edu else INK50, r=20))
        els.append(text(x, y + 36, tw, 44, dag, font=HEAD, size=40, bold=True,
                        color=WHITE if edu else NAVY))
        els.append(text(x, y + 100, tw, 40, wat, size=30,
                        color=WHITE if edu else INK500))
    els.append(text(M, y + 208, W, 40,
                    'De sprint telt 40 uur per week. Ongeveer 30 gaan naar Eduface, de rest naar les en verslag.',
                    size=30, color=INK500, align='left'))

    # Tijdlijn: drie momenten
    ly = 600
    els.append(rect(M, ly + 11, W, 2, INK200))
    momenten = [
        ('Deze week', 'Leerdoel en deliverables inleveren, uiterlijk wo 7 okt.'),
        ('Elke woensdag', 'Les van 13:00 tot 15:15 en een feedbacksessie met docenten.'),
        ('Einde sprint', 'Technische verantwoording, reflectie en het ontwerp zelf.'),
    ]
    cw = (W - 2 * 72) / 3
    for i, (kop, body) in enumerate(momenten):
        x = M + i * (cw + 72)
        els.append(oval(x, ly, 24, NAVY if i == 0 else WHITE, NAVY, 4))
        els.append(text(x, ly + 52, cw, 48, kop, font=HEAD, size=44, bold=True, align='left'))
        els.append(text(x, ly + 112, cw, 140, body, size=32, color=NAVY, align='left', ls=1.3))

    els += voet('Leerdoel: herontwerp van de beoordelingsflow van AI Paper Grader.', page=3)
    return els


SLIDES = {'01-wie': wie, '02-waarom': waarom, '03-sprint': sprint,
          '04-wat': wat, '05-beslissen': beslissen}

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    wie = sys.argv[1:] or list(SLIDES)
    built = []
    for naam in wie:
        els = SLIDES[naam]()
        shoot(os.path.abspath(render_html(els, f'preview/{naam}.html')), f'preview/{naam}.png')
        built.append(els)
        print('preview', naam)
    if len(wie) == len(SLIDES):
        render_pptx(built, 'designer-voorstellen-bewerkbaar.pptx')
        print('pptx klaar')
