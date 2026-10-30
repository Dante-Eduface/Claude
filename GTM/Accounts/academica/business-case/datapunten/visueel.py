"""Optie 2, visueel: twee uitwerkingen als SVG in HTML. Deterministisch (vaste seed)."""
import random, math
random.seed(7)
NAVY, I700, I500, I300, I200, I100, I50 = '#002333', '#2C4A57', '#5B7480', '#A9BCC4', '#CDD9DE', '#E7EEF0', '#F3F7F8'
ICON = {k: open(f'../assets/icon-{k}.png', 'rb') and f'../assets/icon-{k}.png' for k in ['file', 'users', 'feedback']}

def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u**3*a + 3*u*u*t*b + 3*u*t*t*c + t**3*d for a, b, c, d in zip(p0, p1, p2, p3))

# ---------------------------------------------------------------- A: stromen
def stromen():
    W, H = 1048, 500
    px, pw = 712, 336                      # paneel rechts
    tx, ty = px, H / 2                     # waar de stromen binnenkomen
    bronnen = [(80, 'Wetenschappelijke publicaties', 'file', 260, 'rect'),
               (250, 'Onderzoek naar hoe docenten beoordelen', 'users', 260, 'circle'),
               (420, 'Feedbackvoorbeelden uit het onderwijs', 'feedback', 1400, 'circle')]
    els = []
    for y, label, ic, n, vorm in bronnen:
        p0, p3 = (318, y), (tx, ty + (y - 250) * 0.18)
        p1, p2 = (480, y), (560, p3[1])
        for _ in range(n):
            t = random.random() ** 0.85
            x, yy = bez(p0, p1, p2, p3, t)
            spread = (1 - t) * (34 if n > 500 else 22) + 3
            yy += random.gauss(0, spread / 2)
            x += random.uniform(-4, 4)
            c = random.choice([NAVY, I700, I500, I300]) if n > 500 else random.choice([I500, I300, I200])
            o = 0.35 + 0.6 * t
            if vorm == 'rect':
                els.append(f'<rect x="{x-2.5:.1f}" y="{yy-3.2:.1f}" width="5" height="6.4" rx="1" fill="{c}" opacity="{o:.2f}"/>')
            else:
                r = 2.1 if n > 500 else 3
                els.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="{r}" fill="{c}" opacity="{o:.2f}"/>')
    labels = ''.join(
        f'<div style="position:absolute;left:0;top:{y-30}px;width:300px;display:flex;gap:16px;align-items:center">'
        f'<div class="ic"><img src="{ICON[ic]}"></div><div class="t">{label}</div></div>'
        for y, label, ic, n, v in bronnen)
    paneel = (f'<div style="position:absolute;left:{px}px;top:70px;width:{pw}px;height:360px;background:{NAVY};border-radius:20px;padding:44px 36px">'
              f'<img src="../assets/logo_white.png" style="height:36px">'
              f'<div class="num" style="font-size:70px;color:#fff;margin:64px 0 14px">250.000</div>'
              f'<div class="s" style="color:#fff">onderwijsspecifieke feedbackvoorbeelden</div></div>')
    svg = f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0">{"".join(els)}</svg>'
    return f'<div style="position:relative;width:{W}px;height:{H}px">{svg}{labels}{paneel}</div>'

# ---------------------------------------------------------------- B: fundament
def fundament():
    W, H = 1048, 550
    els = []
    # lagen van onder naar boven: breed en dicht -> smal
    lagen = [(430, 110, 1048, 2600, 2.0, 'Feedbackvoorbeelden uit het onderwijs', 'feedback', [NAVY, I700, I500]),
             (310, 100, 800, 700, 2.6, 'Onderzoek naar hoe docenten beoordelen', 'users', [I700, I500, I300]),
             (200, 90, 560, 300, 3.2, 'Wetenschappelijke publicaties', 'file', [I500, I300, I200])]
    cx = 524
    labels = ''
    for y, h, w, n, r, label, ic, kleuren in lagen:
        x0 = cx - w / 2
        els.append(f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" rx="20" fill="{I50}"/>')
        for _ in range(n):
            x = random.uniform(x0 + 14, x0 + w - 14); yy = random.uniform(y + 12, y + h - 12)
            els.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="{r}" fill="{random.choice(kleuren)}" opacity="{random.uniform(.45,.95):.2f}"/>')
        labels += (f'<div style="position:absolute;left:{cx-w/2+24 if w<1048 else 24}px;top:{y+h/2-22}px;display:flex;gap:12px;align-items:center;'
                   f'background:#fff;border-radius:999px;padding:6px 18px 6px 6px;box-shadow:0 1px 2px rgba(0,35,51,.06)">'
                   f'<div class="ic" style="width:32px;height:32px"><img src="{ICON[ic]}" style="width:18px;height:18px"></div>'
                   f'<div style="font-size:17px;font-weight:700;color:{NAVY}">{label}</div></div>')
    # model bovenop
    model = (f'<div style="position:absolute;left:{cx-200}px;top:26px;width:400px;height:150px;background:{NAVY};border-radius:20px;'
             f'display:flex;flex-direction:column;align-items:center;justify-content:center">'
             f'<img src="../assets/logo_white.png" style="height:40px;margin-bottom:18px">'
             f'<div class="eb" style="color:#9EABB1">Een eigen model</div></div>')
    getal = (f'<div style="position:absolute;right:24px;top:{500+110+24}px"></div>')
    svg = f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0">{"".join(els)}</svg>'
    return f'<div style="position:relative;width:{W}px;height:{H}px">{svg}{labels}{model}</div>'

CSS = """@font-face{font-family:'League Spartan';font-weight:700;src:url('../../../../../Design/Merk/fonts/LeagueSpartan-Bold.ttf')}
*{margin:0;padding:0;box-sizing:border-box}body{background:#fff;font-family:Inter,sans-serif;color:#002333}
.v{width:1144px;padding:48px}.eb{font-size:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#5B7480}
.h2{font-family:'League Spartan';font-weight:700;font-size:46px;line-height:1.1;margin:12px 0 32px}
.num{font-family:'League Spartan';font-weight:700;line-height:1}.t{font-size:21px;font-weight:700;line-height:1.25}
.s{font-size:20px;line-height:1.4;color:#2C4A57}
.ic{flex:none;width:56px;height:56px;border-radius:50%;background:#F3F7F8;display:flex;align-items:center;justify-content:center}.ic img{width:26px;height:26px}"""

kop = '<div class="eb">Hoe het model getraind is</div><div class="h2">Een eigen model, getraind op onderwijskennis</div>'
B_onder = ('<div style="display:flex;align-items:baseline;gap:20px;margin-top:28px">'
           '<div class="num" style="font-size:96px">250.000</div><div class="s" style="font-size:22px;white-space:nowrap">onderwijsspecifieke feedbackvoorbeelden vormen het fundament</div></div>')
open('visueel.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
    f'<div class="v" id="A">{kop}{stromen()}</div><div class="v" id="B">{kop}{fundament()}{B_onder}</div></body></html>')
