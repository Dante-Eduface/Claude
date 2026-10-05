"""Deck: nieuwe designer voorstellen aan Jeroen en Menno (oktober 2026).

Draaien vanuit deze map:  python3 build.py
Bouwt per slide een PNG-preview in preview/ en een bewerkbare pptx voor Canva.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../.claude/skills/pitch-deck'))
import deckbuild as D
from deckbuild import rect, oval, pic, text, title, render_html, render_pptx
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


def voet(quote=None, page=None):
    """Voet zonder klantlogo: dit deck is intern."""
    out = [rect(M, 868, W, 1, INK100)]
    if quote:
        out.append(text(M, 900, 1320, 56, quote, size=34, color=NAVY, align='left', ls=1.3))
    out.append(pic(D.LOGO_NAVY, 1800 - 170, 907, 170, 46))
    if page:
        out.append(text(1700, 1004, 100, 36, str(page), size=23, color='9AAFB8', align='right'))
    return out


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


SLIDES = {'03-sprint': sprint}

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
