"""Jisc x Eduface webinar, slides. Bron voor preview (PNG) en pptx.

Draaien vanuit deze map:  python3 build.py [proef|alles]
"""
import sys, os
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
import deckbuild as D
from deckbuild import rect, oval, pic, text, NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G, \
    INK50, INK100, INK200, INK500, WHITE, HEAD, BODY, M

# Chrome staat in deze omgeving ergens anders dan op de Mac.
D.CHROME = os.environ.get('CHROME', '/tmp/claude-0/-home-user-Claude/'
                          '20e016e8-029a-5cf3-abfb-844a148874f6/scratchpad/chrome.sh')

W, H = 1920, 1080


def shoot(html_path, png_path):
    # Headless Chromium hier snijdt de onderkant af bij 1920x1080; ruimer schieten en bijknippen.
    import subprocess
    from PIL import Image
    subprocess.run([D.CHROME, '--headless', '--disable-gpu', f'--screenshot={png_path}',
                    '--window-size=1920,1300', '--hide-scrollbars',
                    '--virtual-time-budget=4000', html_path], capture_output=True)
    Image.open(png_path).crop((0, 0, W, H)).save(png_path)


# ---------------------------------------------------------------- bouwstenen
def eyebrow(t, y=96, dark=False):
    return [text(M, y, 1200, 40, t.upper(), font=BODY, size=26, bold=True,
                 color=GREEN if dark else GREEN_DEEP, align='left', ls=1.0)]

def kop(t, y=140, dark=False, size=80, w=1680):
    return [text(M, y, w, 200, t, font=HEAD, size=size, bold=True,
                 color=WHITE if dark else NAVY, align='left', ls=1.05)]

def voet(page, dark=False, src=None):
    out = []
    if src:
        out.append(text(M, 1000, 1400, 36, src, size=22,
                        color='8FA9B4' if dark else INK500, align='left'))
    lg = 'assets/logo_white_c.png' if dark else 'assets/logo_navy_c.png'
    out.append(pic(lg, 1800 - 148, 996, 148, 40))
    return out


# ---------------------------------------------------------------- slides
def s_opening():
    els = [rect(0, 0, W, H, NAVY)]
    # groen accentvlak rechts, rustig
    els += [oval(1380, 260, 760, '0A3A47', '0A3A47', 0),
            oval(1520, 400, 480, '0F4C57', '0F4C57', 0),
            oval(1660, 540, 200, GREEN, GREEN, 0)]
    els += eyebrow('Jisc  ×  Eduface  ·  Webinar', y=300, dark=True)
    els += [text(M, 360, 1200, 330, 'What 20+ AI feedback\nimplementations taught us',
                 font=HEAD, size=96, bold=True, color=WHITE, align='left', ls=1.05)]
    els += [text(M, 600, 1100, 60, 'Consistency, efficiency and the risk nobody planned for',
                 size=36, color='B9CBD2', align='left')]
    els += [pic('assets/logo_white_c.png', M, 940, 222, 60)]
    return els, True


def s_logos():
    els = eyebrow('What we learned')
    els += kop('Lessons from 20+ pilots\nand implementations', size=80)
    # 7 logo's in twee rijen + groot +20-rondje rechts
    logos = [('assets/l_hr.png', 1478 / 379), ('assets/l_hhs_en.png', 1127 / 401),
             ('assets/l_tu.png', 1152 / 292), ('assets/l_ru.png', 1477 / 336),
             ('assets/l_ul.png', 1488 / 627), (None, 'Bath Spa'), (None, '7th logo')]
    tw, th, gap = 262, 150, 28
    x0, y0 = M, 430
    for i, (p, r) in enumerate(logos):
        row, col = divmod(i, 4)
        x = x0 + col * (tw + gap) + (row * (tw + gap) / 2)
        y = y0 + row * (th + gap)
        els.append(rect(x, y, tw, th, INK50, r=24))
        if p:
            bw, bh = 196, 80
            lw, lh = (bw, bw / r) if bw / r <= bh else (bh * r, bh)
            els.append(pic(p, x + (tw - lw) / 2, y + (th - lh) / 2, lw, lh))
        else:
            els.append(text(x, y + th / 2 - 20, tw, 40, r, size=28, color=INK500))
    # +20
    cx, cy, d = 1560, 590, 280
    els += [oval(cx - d / 2, cy - d / 2, d, GREEN, GREEN, 0),
            text(cx - d / 2, cy - 70, d, 120, '+20', font=HEAD, size=120, bold=True, color=NAVY),
            text(cx - 170, cy + d / 2 + 24, 340, 40, 'pilots & implementations', size=30,
                 color=INK500)]
    els += voet(5)
    return els, False


def s_consistency_layers():
    els = eyebrow('Consistency')
    els += kop('Consistency is more than\nthe same grade', size=80, w=900)
    # drie concentrische cirkels, rechts
    cx, cy = 1360, 580
    rings = [(740, INK50, 'Same voice', 'Feedback in the same style, every time'),
             (500, TINT_G, 'Same criteria', 'The same parts of the work get comment'),
             (270, NAVY, 'Same grade', None)]
    for d, fill, *_ in rings:
        els.append(oval(cx - d / 2, cy - d / 2, d, fill, fill, 0))
    els += [text(cx - 135, cy - 26, 270, 52, 'Same grade', font=HEAD, size=44, bold=True, color=WHITE),
            text(cx - 250, cy - 215, 500, 52, 'Same criteria', font=HEAD, size=44, bold=True, color=GREEN_DEEP),
            text(cx - 370, cy - 330, 740, 52, 'Same voice', font=HEAD, size=44, bold=True, color=NAVY)]
    # aantekening links: waar de meeste evaluaties stoppen
    els += [rect(M + 640, 634, cx - 135 - M - 640 - 20, 3, AMBER),
            oval(cx - 135 - 26, 626, 18, AMBER, AMBER, 0),
            rect(M, 560, 6, 150, AMBER),
            text(M + 36, 560, 640, 150, 'Where most evaluations stop:\nrun it twice, compare the mark.',
                 size=34, color=NAVY, align='left', ls=1.3)]
    els += voet(8)
    return els, False


PROEF = [s_opening, s_logos, s_consistency_layers]


def build(fns, naam):
    os.makedirs('preview', exist_ok=True)
    slides = []
    for i, fn in enumerate(fns, 1):
        els, dark = fn()
        h = D.render_html(els, f'preview/{fn.__name__}.html', dark=dark)
        shoot(os.path.abspath(h), f'preview/{fn.__name__}.png')
        slides.append(els)
    D.render_pptx(slides, f'{naam}-bewerkbaar.pptx')


if __name__ == '__main__':
    build(PROEF, 'jisc-webinar-proef')
