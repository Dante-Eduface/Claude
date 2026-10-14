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
JISC_LOGO = 'assets/logo_jisc.png' if os.path.exists('assets/logo_jisc.png') else 'assets/logo_jisc_placeholder.png'
from PIL import Image as _Img
JISC_R = _Img.open(JISC_LOGO).size[0] / _Img.open(JISC_LOGO).size[1]   # breedte/hoogte


def shoot(html_path, png_path):
    # Headless Chromium hier snijdt de onderkant af bij 1920x1080; ruimer schieten en bijknippen.
    import subprocess
    from PIL import Image
    subprocess.run([D.CHROME, '--headless', '--disable-gpu', f'--screenshot={png_path}',
                    '--window-size=1920,1300', '--hide-scrollbars',
                    '--virtual-time-budget=4000', html_path], capture_output=True)
    Image.open(png_path).crop((0, 0, W, H)).save(png_path)


# ---------------------------------------------------------------- iconen
sys.path.insert(0, '/home/user/Claude/.claude/skills/pitch-deck')
import icons as I
I.ICONS.update({
    'maan': '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/>',
    'deur': '<path d="M3 21h18"/><path d="M6 21V3h12v18"/><path d="M14.5 12h.01"/>',
    'slot': '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    'krant': '<path d="M4 4h13v16H6a2 2 0 0 1-2-2Z"/><path d="M17 8h3v10a2 2 0 0 1-2 2"/><path d="M7 8h7M7 12h7M7 16h4"/>',
    'vlag': '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
})


def icon(naam, tint='navy'):
    """Rendert een icoon (transparant) naar assets/; ruim geschoten en bijgeknipt."""
    import subprocess
    from PIL import Image
    uit = f'assets/icon-{naam}-{tint}.png'
    if os.path.exists(uit):
        return uit
    tmp = os.path.abspath(f'assets/_{naam}.html')
    open(tmp, 'w').write(
        "<!DOCTYPE html><html><head><style>html,body{margin:0;background:transparent}"
        "svg{display:block;width:296px;height:296px}</style></head><body>"
        f"<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg' fill='none' "
        f"stroke='#{I.TINTS[tint]}' stroke-width='1.9' stroke-linecap='round' "
        f"stroke-linejoin='round'>{I.ICONS[naam]}</svg></body></html>")
    subprocess.run([D.CHROME, '--headless', '--disable-gpu', f'--screenshot={uit}',
                    '--window-size=600,600', '--default-background-color=00000000',
                    '--hide-scrollbars', tmp], capture_output=True)
    os.remove(tmp)
    Image.open(uit).crop((0, 0, 296, 296)).save(uit)
    return uit


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
        out.append(text(M, 1000, 1180, 36, src, size=22,
                        color='8FA9B4' if dark else INK500, align='left'))
    out += logopaar(dark)
    return out


def logopaar(dark=False, y=986):
    """Eduface en Jisc rechtsonder. Op navy op een wit vlak, anders valt het Jisc-logo weg."""
    jh = 56; jw = jh * JISC_R   # vierkant Jisc-blok iets groter dan het woordmerk, anders oogt het klein
    x_jisc = 1800 - jw
    x_lijn = x_jisc - 24
    x_edu = x_lijn - 24 - 148
    out = []
    if dark:
        out.append(rect(x_edu - 24, y - 14, 1800 - x_edu + 48, jh + 28, WHITE, r=18))
    out += [pic('assets/logo_navy_c.png', x_edu, y + 8, 148, 40),
            rect(x_lijn, y, 2, jh, INK200),
            pic(JISC_LOGO, x_jisc, y, jw, jh)]
    return out


# ---------------------------------------------------------------- slides
def s_opening():
    els = [rect(0, 0, W, H, NAVY)]
    # groen accentvlak rechts, rustig
    els += [oval(1380, 260, 760, '0A3A47', '0A3A47', 0),
            oval(1520, 400, 480, '0F4C57', '0F4C57', 0),
            oval(1660, 540, 200, GREEN, GREEN, 0)]
    els += eyebrow('Jisc  ×  Eduface  ·  Webinar', y=300, dark=True)
    els += [text(M, 360, 1200, 330, 'The business outcomes of\nAI marking and feedback',
                 font=HEAD, size=96, bold=True, color=WHITE, align='left', ls=1.05)]
    els += [text(M, 600, 1100, 60, 'Lessons from 20+ pilots and implementations',
                 size=36, color='B9CBD2', align='left')]
    els += [rect(M - 28, 904, 222 + 50 + 80 * JISC_R + 56, 132, WHITE, r=22),
            pic('assets/logo_navy_c.png', M, 940, 222, 60),
            rect(M + 222 + 24, 934, 2, 72, INK200),
            pic(JISC_LOGO, M + 222 + 50, 930, 80 * JISC_R, 80)]
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
    els += kop('Consistency is more than\nthe same grade', w=1300)
    lagen = [('1', 'Same mark', 'Run the same assignment twice, get the same grade', INK50, INK500),
             ('2', 'Same focus', 'The feedback addresses the same parts of the work', TINT_G, GREEN_DEEP),
             ('3', 'Same style', 'The feedback is written the same way, every time', TINT_G, GREEN_DEEP)]
    x0, bw = M + 300, 1380
    for i, (nr, t, sub, fill, kleur) in enumerate(lagen):
        y = 350 + i * 170
        els += [rect(x0, y, bw, 140, fill, r=24),
                text(x0 + 40, y + 34, 80, 80, nr, font=HEAD, size=64, bold=True, color=kleur, align='left'),
                text(x0 + 140, y + 30, 420, 60, t, font=HEAD, size=46, bold=True, color=NAVY, align='left'),
                text(x0 + 560, y + 46, 780, 50, sub, size=30, color=NAVY, align='left')]
    # haken links: wat de meesten toetsen, wat wij ook toetsen
    els += [rect(M + 250, 360, 4, 120, INK200),
            text(M, 380, 230, 90, 'What most\npeople check', size=26, bold=True, color=INK500, align='right', ls=1.2),
            rect(M + 250, 530, 4, 290, GREEN),
            text(M, 630, 230, 90, 'What we\nalso check', size=26, bold=True, color=GREEN_DEEP, align='right', ls=1.2)]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- herbruikbaar
TONE = {'amber': TINT_A, 'green': TINT_G, 'navy': INK50}
PLACE = 'F9E3C2'   # amber vlak: alles wat Jeroen/Dante nog moeten invullen


def itile(cx, y, naam, tone='green', size=140):
    ic = int(size * 0.5)
    return [rect(cx - size / 2, y, size, size, TONE[tone], r=size * 0.24),
            pic(icon(naam, tone), cx - ic / 2, y + (size - ic) / 2, ic, ic)]


def statement(t, sub=None, dark=True, size=88):
    els = [rect(0, 0, W, H, NAVY)] if dark else []
    els += [text(M, 330, 1680, 320, t, font=HEAD, size=size, bold=True,
                 color=WHITE if dark else NAVY, align='left', ls=1.08)]
    if sub:
        els += [text(M, 700, 1500, 60, sub, size=36, color='B9CBD2' if dark else INK500, align='left')]
    els += voet(0, dark=dark)
    return els, dark


def section(nr, t, sub):
    els = [rect(0, 0, W, H, NAVY)]
    els += [text(M, 250, 600, 260, nr, font=HEAD, size=240, bold=True, color=GREEN, align='left', ls=1.0),
            text(M, 540, 1600, 120, t, font=HEAD, size=104, bold=True, color=WHITE, align='left', ls=1.0),
            text(M, 690, 1500, 60, sub, size=36, color='B9CBD2', align='left')]
    els += voet(0, dark=True)
    return els, True


def card(x, y, w, h, fill=INK50):
    return [rect(x, y, w, h, fill, r=28)]


# ---------------------------------------------------------------- deel 0 en 1
def s_agenda():
    els = eyebrow('Today')
    els += kop('Four parts')
    stappen = [('gesprek', 'In conversation\nwith Jisc'), ('lamp', 'What we learned\nin 20+ implementations'),
               ('deur', 'Breakout rooms:\nyou choose'), ('check', 'Wrap-up\ntogether')]
    xs, w = D.cols(4)
    els += [rect(xs[0], 520, xs[-1] - xs[0], 4, INK100)]
    for i, (ic, t) in enumerate(stappen):
        tone = 'amber' if i == 2 else 'green'
        els += itile(xs[i], 450, ic, tone)
        els += [text(xs[i] - w / 2, 630, w, 120, t, size=34, bold=i == 2, color=NAVY, ls=1.25)]
    els += [text(xs[2] - w / 2, 760, w, 50, 'Consistency  or  Efficiency', size=26, color=AMBER, bold=True)]
    els += voet(2)
    return els, False


def s_jisc():
    els = [rect(0, 0, W, H, NAVY)]
    els += eyebrow('In conversation', y=300, dark=True)
    els += [text(M, 350, 1100, 120, 'Hannah Lawrence', font=HEAD, size=110, bold=True, color=WHITE, align='left'),
            text(M, 490, 1100, 60, 'Licence Manager, Jisc', size=40, color='B9CBD2', align='left')]
    els += [oval(1260, 250, 520, '0F4C57', '0F4C57', 0),
            text(1260, 490, 520, 40, 'photo', size=28, color='8FA9B4')]
    els += [text(M, 640, 1000, 120, 'What does the sector expect from AI feedback,\nand what is actually working?',
                 size=34, color=GREEN, align='left', ls=1.3)]
    els += voet(0, dark=True)
    return els, True


def s_jisc_pilot():
    els = eyebrow('Context')
    els += [text(M, 250, 900, 260, '38', font=HEAD, size=260, bold=True, color=GREEN_DEEP, align='left', ls=1.0),
            text(M, 540, 820, 140, "colleges and universities in Jisc's\nAI in marking and feedback pilot",
                 size=40, color=NAVY, align='left', ls=1.25),
            text(M, 700, 820, 50, 'September 2025 to August 2026', size=30, color=INK500, align='left')]
    els += card(1060, 250, 740, 520, INK50)
    els += [text(1120, 300, 640, 50, '“', font=HEAD, size=120, bold=True, color=GREEN, align='left', ls=1.0),
            text(1120, 390, 640, 260, "These tools shouldn't be used as a final marker. Humans should always be reviewing the feedback.",
                 size=38, color=NAVY, align='left', ls=1.3),
            text(1120, 680, 640, 40, 'Tom Moule, Jisc', size=28, bold=True, color=NAVY, align='left')]
    els += voet(0, src='Jisc National Centre for AI, May 2026 · Times Higher Education, 27 March 2026')
    return els, False


JISC_VRAGEN = [
    'What do you see institutions struggling with most right now when it comes to AI?',
    'What made Jisc decide to start the AI in marking and feedback pilot?',
    'The pilot points towards formative feedback. What makes AI so valuable there?',
    'Where do institutions tend to get stuck when they try it?',
    "What's one piece of advice you'd give an institution starting next term?",
]


def jisc_vraag(n):
    """Eén vraag per slide, zodat niemand vooruit leest."""
    def slide():
        els = eyebrow(f'In conversation with Jisc  ·  {n} of {len(JISC_VRAGEN)}')
        els += [text(M, 300, 1500, 420, JISC_VRAGEN[n - 1], font=HEAD, size=88, bold=True,
                     color=NAVY, align='left', ls=1.1)]
        # voortgang: vijf stippen, de huidige groen en breder
        x = M
        for i in range(1, len(JISC_VRAGEN) + 1):
            w = 64 if i == n else 20
            kleur = GREEN if i == n else (GREEN_DEEP if i < n else INK100)
            els.append(rect(x, 800, w, 20, kleur, r=10))
            x += w + 14
        els += voet(0)
        return els, False
    slide.__name__ = f's_jisc_q{n}'
    return slide


# ---------------------------------------------------------------- deel 2
def s_not_a_demo():
    return statement('This is not a product demo.\nThese are the patterns we saw.')


def s_three_reasons():
    els = eyebrow('Why institutions bring us in')
    els += kop('Three reasons')
    items = [('slot', 'amber', 'Data risk', 'Staff already use AI to mark,\noutside policy'),
             ('weegschaal', 'green', 'Consistency', 'Grading and feedback,\nformative and summative'),
             ('klok', 'navy', 'Efficiency', 'Time back for\nlecturers')]
    xs, w = D.cols(3)
    for i, (ic, tone, t, sub) in enumerate(items):
        els += card(xs[i] - w / 2, 320, w, 520, TONE[tone])
        els += [text(xs[i] - w / 2 + 48, 360, 120, 80, str(i + 1), font=HEAD, size=64, bold=True,
                     color=INK500, align='left')]
        els += [pic(icon(ic, tone), xs[i] - 60, 440, 120, 120)]
        els += [text(xs[i] - w / 2, 610, w, 70, t, font=HEAD, size=56, bold=True, color=NAVY),
                text(xs[i] - w / 2, 700, w, 100, sub, size=30, color=INK500, ls=1.3)]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- datarisico
def s_data_risk():
    els = eyebrow('1 · Data risk', y=96)
    els += kop('Staff already use AI,\noutside policy', w=760)
    # twee nieuwskoppen als kaartjes, licht gedraaid kan niet in pptx, dus verspringend
    koppen = [(980, 200, 'The Guardian · 20 November 2025',
               "'We could have asked ChatGPT': students fight back over course taught by AI",
               'University of Staffordshire'),
              (1060, 560, 'Omroep Brabant (NL) · early 2026',
               'Docent bouwt AI-tool die studentgegevens naar ChatGPT stuurt',
               'Lecturer builds AI tool that sends student data to ChatGPT')]
    for x, y, bron, kop_, vert in koppen:
        els += [rect(x + 12, y + 14, 740, 300, INK100, r=20), rect(x, y, 740, 300, WHITE, r=20),
                rect(x, y, 740, 300, 'FFFFFF', r=20)]
        els += [rect(x, y, 740, 6, AMBER),
                text(x + 40, y + 36, 660, 40, bron.upper(), size=22, bold=True, color=INK500, align='left'),
                text(x + 40, y + 84, 660, 160, kop_, font=HEAD, size=40, bold=True, color=NAVY, align='left', ls=1.15)]
        if vert:
            els += [text(x + 40, y + 236, 660, 40, vert, size=24, color=INK500, align='left')]
    els += [text(M, 560, 760, 200, 'When it reaches the press,\nit is no longer an IT issue.',
                 size=36, color=NAVY, align='left', ls=1.3)]
    els += voet(0, src='theguardian.com/education/2025/nov/20 · omroepbrabant.nl/nieuws/6002910')
    return els, False


def s_ban():
    return statement("Banning it doesn't stop it.\nA safe alternative does.")


# ---------------------------------------------------------------- consistentie
def s_sec_consistency():
    return section('01', 'Consistency', 'Grading and feedback, formative and summative')


def s_nine_of_twenty():
    els = eyebrow('The problem is old')
    els += [text(M, 220, 1100, 300, '9 of 20', font=HEAD, size=240, bold=True, color=NAVY, align='left', ls=1.0)]
    els += [text(M, 500, 1000, 160, 'assignments were ranked both best and worst\nby different experienced examiners',
                 size=42, color=NAVY, align='left', ls=1.3)]
    # 20 stippen, 9 ervan amber
    for i in range(20):
        r_, c_ = divmod(i, 5)
        fill = AMBER if i in (0, 2, 3, 6, 9, 11, 14, 15, 18) else INK100
        els.append(oval(1300 + c_ * 92, 260 + r_ * 92, 64, fill, fill, 0))
    els += [text(1300, 650, 460, 40, 'Same work, opposite rankings', size=28, color=INK500, align='left')]
    els += voet(0, src='Bloxham et al., Assessment & Evaluation in Higher Education, 2016 · 24 examiners, 20 UK universities')
    return els, False


def s_where_it_hurts():
    els = eyebrow('Consistency')
    els += kop('Where inconsistency hurts')
    items = [('groep', 'Many markers,\none module'), ('historie', 'Paper 80 is marked\ndifferently from paper 5'),
             ('ongelijk', 'Students compare,\nthen appeal'), ('oogdicht', 'Moderation only\nsees a sample')]
    xs, w = D.cols(4)
    for i, (ic, t) in enumerate(items):
        els += card(xs[i] - w / 2, 360, w, 400, INK50)
        els += itile(xs[i], 430, ic, 'amber' if i else 'green')
        els += [text(xs[i] - w / 2 + 20, 620, w - 40, 140, t, size=32, color=NAVY, bold=True, ls=1.3)]
    els += voet(0)
    return els, False


def s_builds():
    els = eyebrow('Why it matters to us')
    els += kop('Consistent feedback\ncan build on itself', w=1100)
    stappen = ['Draft 1', 'Draft 2', 'Final']
    crit = ['Argument', 'Evidence', 'Structure']
    xs, w = D.cols(3)
    for i, st in enumerate(stappen):
        els += card(xs[i] - w / 2, 420, w, 400, INK50)
        els += [text(xs[i] - w / 2 + 40, 450, w, 50, st, font=HEAD, size=40, bold=True, color=NAVY, align='left')]
        for j, c in enumerate(crit):
            on = j <= i
            els += [rect(xs[i] - w / 2 + 40, 530 + j * 86, w - 80, 66, TINT_G if on else WHITE, r=33),
                    text(xs[i] - w / 2 + 70, 548 + j * 86, 300, 36, c, size=28, color=GREEN_DEEP if on else INK500, align='left'),
                    text(xs[i] + w / 2 - 140, 548 + j * 86, 70, 36, '✓' if on else '·', size=30, bold=True,
                         color=GREEN_DEEP if on else INK200, align='right')]
        if i < 2:
            els += [text(xs[i] + w / 2 - 10, 600, 92, 60, '→', font=HEAD, size=56, bold=True, color=INK200)]
    els += voet(0)
    return els, False


def s_endgoal_consistency():
    els = [rect(0, 0, W, H, NAVY)]
    els += eyebrow('Where we want to get to', dark=True)
    els += kop('A student sees their own\ngrowth across the degree', dark=True, w=1300)
    # groeilijn, illustratief
    pts = [(220, 840), (520, 790), (820, 720), (1120, 640), (1420, 560), (1700, 470)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        n = 24
        for k in range(n):
            t = k / n
            els.append(oval(x1 + (x2 - x1) * t - 4, y1 + (y2 - y1) * t - 4, 8, '2D6470', '2D6470', 0))
    for i, (x, y) in enumerate(pts):
        d = 34 + i * 8
        els.append(oval(x - d / 2, y - d / 2, d, GREEN, GREEN, 0))
    for x, t in [(220, 'Year 1'), (820, 'Year 2'), (1420, 'Year 3')]:
        els += [text(x - 100, 890, 200, 40, t, size=28, color='B9CBD2')]
    els += [text(M, 960, 1200, 36, 'Illustration', size=22, color='8FA9B4', align='left')]
    els += logopaar(dark=True)
    return els, True


def s_llm_vs_model():
    import random
    random.seed(7)
    els = eyebrow('Our lesson')
    els += kop('We started with general LLMs.\nThen we built our own model.', size=72)
    for i, (cx, spread, kleur, t, sub) in enumerate([
            (560, 260, INK200, 'General LLM', 'Same paper, different focus each run'),
            (1360, 110, GREEN_DEEP, 'Purpose-built model', 'Same paper, same criteria, same voice')]):
        els += card(cx - 380, 360, 760, 480, INK50 if i == 0 else TINT_G)
        for _ in range(26):
            x = cx + random.gauss(0, spread * 0.5); y = 560 + random.gauss(0, spread * 0.35)
            x = max(cx - 330, min(cx + 310, x)); y = max(390, min(700, y))
            els.append(oval(x, y, 22, kleur, kleur, 0))
        els += [text(cx - 380, 730, 760, 50, t, font=HEAD, size=42, bold=True, color=NAVY),
                text(cx - 380, 786, 760, 40, sub, size=28, color=INK500)]
    els += voet(0, src='Illustration, not a measurement. Model trained on 250,000 education-specific feedback examples.')
    return els, False


def s_cases_consistency():
    els = eyebrow('What institutions learned')
    els += kop('Two lessons on consistency')
    cases = [('rubric', 'green', 'The gap was in the rubric,\nnot in the markers',
              'Six markers, one module. One marked\n“critical analysis” lower every time:\nthey read the descriptor differently.'),
             ('studenten', 'amber', 'Students act on feedback\nthey recognise',
              'Three formative rounds, a different\nfocus each time: students ignored it.\nSame criteria every round: they used it.')]
    xs, w = D.cols(2)
    for i, (ic, tone, t, sub) in enumerate(cases):
        x = xs[i] - w / 2
        els += card(x, 320, w, 520, TONE[tone])
        els += [pic(icon(ic, tone), x + 56, 370, 96, 96),
                text(x + 56, 500, w - 112, 130, t, font=HEAD, size=46, bold=True, color=NAVY, align='left', ls=1.1),
                text(x + 56, 650, w - 112, 160, sub, size=30, color=NAVY, align='left', ls=1.35)]
    els += voet(0, src='Typical scenarios from our implementations, institutions not named.')
    return els, False


def s_policy_objection():
    return statement('“AI grading isn’t aligned\nwith our policy.”', sub='An objection we hear often.')


def s_moderation():
    els = eyebrow('When AI grading is a step too far')
    els += kop('Not ready for AI grades?\nUse it to moderate.', w=1300)
    # verdeling van cijfers, één uitschieter gemarkeerd
    import math
    base_y = 800
    for i in range(28):
        x = 220 + i * 54
        hgt = 60 + 200 * math.exp(-((i - 13) ** 2) / 40)
        out = i == 23
        if out:
            hgt = 330
        els.append(rect(x, base_y - hgt, 36, hgt, AMBER if out else INK100, r=8))
    els += [pic(icon('vlag', 'amber'), 220 + 23 * 54 - 12, base_y - 330 - 80, 60, 60),
            text(220 + 23 * 54 + 70, base_y - 400, 300, 100, 'Flagged:\nfar from expected', size=30,
                 bold=True, color=AMBER, align='left', ls=1.25)]
    els += [rect(M, base_y + 2, 1680, 3, INK200),
            text(M, base_y + 30, 1680, 40, 'AI grade stays hidden. Only large deviations reach the moderator.',
                 size=30, color=INK500, align='left')]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- efficiency
def s_sec_efficiency():
    return section('02', 'Operational efficiency', 'Time saved on marking and feedback')


def s_two_flavours():
    els = eyebrow('Efficiency')
    els += kop('Two flavours')
    xs, w = D.cols(2)
    data = [('maan', 'navy', 'Formative', '03:00', 'Student asks for feedback\nwhen it suits them',
             'No human in the loop'),
            ('usercheck', 'green', 'Summative', 'Lecturer + AI', 'Time saved on writing,\nnot on reading',
             'Human in the loop')]
    for i, (ic, tone, t, big, sub, tag) in enumerate(data):
        x = xs[i] - w / 2
        bg = NAVY if i == 0 else TINT_G
        fg = WHITE if i == 0 else NAVY
        els += card(x, 300, w, 560, bg)
        els += [pic(icon(ic, 'mint' if i == 0 else 'green'), x + 56, 350, 80, 80),
                text(x + 160, 362, 500, 60, t, font=HEAD, size=48, bold=True, color=fg, align='left'),
                text(x + 56, 480, w - 112, 140, big, font=HEAD, size=120 if i == 0 else 96, bold=True,
                     color=GREEN if i == 0 else GREEN_DEEP, align='left', ls=1.0),
                text(x + 56, 640, w - 112, 110, sub, size=32, color=fg, align='left', ls=1.3),
                rect(x + 56, 778, 360, 52, '0F4C57' if i == 0 else WHITE, r=26),
                text(x + 56, 788, 360, 36, tag, size=24, bold=True, color=GREEN if i == 0 else GREEN_DEEP)]
    els += voet(0)
    return els, False


def s_hours():
    els = eyebrow('Where the time goes')
    els += kop('Academics already work\nfar beyond contract', w=1300)
    rows = [('Contract', 37.5, INK200), ('Actual average', 50.9, AMBER)]
    for i, (t, v, kleur) in enumerate(rows):
        y = 470 + i * 170
        bw = v / 52 * 1280
        els += [text(M, y + 20, 360, 50, t, size=32, color=NAVY, bold=i == 1, align='left'),
                rect(M + 380, y, bw, 100, kleur, r=14),
                text(M + 380 + bw - 260, y + 22, 230, 60, f'{v:g} h', font=HEAD, size=52, bold=True,
                     color=NAVY if i == 0 else WHITE, align='right')]
    els += [text(M + 380, 820, 1200, 40, '+13.4 hours a week beyond contract', size=32, bold=True, color=AMBER, align='left')]
    els += voet(0, src='UCU workload survey, 2016, n ≈ 12,100 (older data)')
    return els, False


def s_pains():
    els = eyebrow('What we hear from institutions')
    els += kop('The cost of no time')
    groepen = [('For lecturers', 'green', [('schoolbord', 'Marking instead of mentoring'), ('klok', 'Structural overtime')]),
               ('For institutions', 'amber', [('pen', 'No formative feedback at all'), ('prijs', 'Paying external markers'),
                                              ('studenten', 'Fewer staff, more students')])]
    xs, w = D.cols(2)
    for i, (t, tone, items) in enumerate(groepen):
        x = xs[i] - w / 2
        els += [text(x, 320, w, 50, t.upper(), size=26, bold=True, color=GREEN_DEEP if i == 0 else AMBER, align='left')]
        for j, (ic, it) in enumerate(items):
            y = 390 + j * 150
            els += card(x, y, w, 126, TONE[tone])
            els += [pic(icon(ic, tone), x + 36, y + 31, 64, 64),
                    text(x + 130, y + 40, w - 160, 50, it, size=34, bold=True, color=NAVY, align='left')]
    els += voet(0)
    return els, False


def s_editing_cost():
    els = eyebrow('Our lesson')
    els += kop('Editing AI feedback can cost more\ntime than writing it yourself', size=72, w=1600)
    rows = [('Writing feedback yourself', 0.55, INK200, NAVY),
            ('Fixing inaccurate AI feedback', 0.85, AMBER, WHITE),
            ('Approving accurate AI feedback', 0.22, GREEN, NAVY)]
    for i, (t, frac, kleur, tk) in enumerate(rows):
        y = 420 + i * 150
        els += [text(M, y + 28, 520, 50, t, size=32, bold=i == 1, color=NAVY, align='left'),
                rect(M + 560, y, 1120 * frac, 104, kleur, r=14)]
    els += voet(0, src='Illustration of time per assignment, not a measurement.')
    return els, False


def s_accuracy():
    els = eyebrow('Therefore')
    els += kop('Accuracy is the most\nimportant factor', w=1300)
    stappen = [('rubric', 'Your rubric and\ninstructions'), ('model', 'The model\nfollows them'),
               ('filepen', 'Feedback you\nwould give'), ('check', 'Approve,\ndon\'t rewrite')]
    xs, w = D.cols(4)
    for i, (ic, t) in enumerate(stappen):
        tone = 'green' if i == 3 else 'navy'
        els += itile(xs[i], 470, ic, tone, size=150)
        els += [text(xs[i] - w / 2, 650, w, 110, t, size=32, color=NAVY, bold=i == 3, ls=1.3)]
        if i < 3:
            els += [text(xs[i] + 90, 510, w - 180 + 72, 70, '→', font=HEAD, size=60, bold=True, color=INK200)]
    els += voet(0)
    return els, False


def s_tuning():
    els = eyebrow('Our lessons')
    els += kop('Tuning is the investment', w=1300)
    xs, w = D.cols(3)
    stats = [('94%', 'accuracy on average', INK500),
             ('98%', 'accuracy for lecturers\nwho tuned the model', GREEN_DEEP),
             ('−85%', 'time spent typing feedback,\nup to 20 min per assignment', NAVY)]
    for i, (n, t, kleur) in enumerate(stats):
        els += card(xs[i] - w / 2, 330, w, 460, TINT_G if i == 1 else INK50)
        els += [text(xs[i] - w / 2, 390, w, 220, n, font=HEAD, size=150, bold=True, color=kleur, ls=1.0),
                text(xs[i] - w / 2 + 30, 620, w - 60, 110, t, size=32, color=NAVY, ls=1.3)]
    els += voet(0, src='Accuracy: Bath Spa pilot, June 2026 (435 submissions, 13 markers). Typing time: Eduface implementations.')
    return els, False


def s_endgoal_efficiency():
    els = eyebrow('Where we want to get to')
    els += kop('Lecturer time moves from\ntyping to teaching', w=1300)
    rows = [('Today', [(0.62, AMBER, 'Writing feedback'), (0.38, INK200, 'Teaching & mentoring')]),
            ('With AI', [(0.25, AMBER, 'Checking'), (0.75, GREEN, 'Teaching & mentoring')])]
    for i, (t, parts) in enumerate(rows):
        y = 480 + i * 180
        els += [text(M, y + 30, 240, 50, t, size=34, bold=True, color=NAVY, align='left')]
        x = M + 260
        for frac, kleur, lab in parts:
            bw = 1420 * frac
            els += [rect(x, y, bw - 8, 110, kleur, r=14),
                    text(x + 28, y + 34, bw - 50, 44, lab, size=30, bold=True,
                         color=NAVY if kleur != AMBER else WHITE, align='left')]
            x += bw
    els += voet(0, src='Illustration, not a measurement.')
    return els, False


def s_objection():
    return statement('“Won’t lecturers just\nclick approve?”', sub='The question we always get.')


def s_objection_answer():
    els = eyebrow('Our answer')
    els += kop('Approving is still judging')
    items = [('wisselend', 'amber', 'The alternative today is\noften no feedback at all'),
             ('rubric', 'green', 'It gives the feedback\nthe lecturer set up'),
             ('historie', 'navy', 'Every edit is logged\nin the audit trail')]
    xs, w = D.cols(3)
    for i, (ic, tone, t) in enumerate(items):
        els += card(xs[i] - w / 2, 330, w, 400, TONE[tone])
        els += [pic(icon(ic, tone), xs[i] - 50, 390, 100, 100),
                text(xs[i] - w / 2 + 30, 540, w - 60, 140, t, size=32, bold=True, color=NAVY, ls=1.3)]
    els += [text(M, 790, 1680, 60, 'The AI assists. The academic decides.', font=HEAD, size=48, bold=True,
                 color=GREEN_DEEP, align='left')]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- breakouts en afsluiting
def s_choose_room():
    els = eyebrow('Breakout rooms')
    els += kop('Choose your room')
    xs, w = D.cols(2)
    data = [('weegschaal', 'green', 'Consistency', 'with Dante'), ('klok', 'navy', 'Operational efficiency', 'with [name]')]
    for i, (ic, tone, t, who) in enumerate(data):
        x = xs[i] - w / 2
        els += [rect(x, 320, w, 540, TONE[tone], r=28)]
        els += [pic(icon('deur', tone), x + w / 2 - 70, 470, 140, 140),
                text(x, 650, w, 60, t, font=HEAD, size=46, bold=True, color=NAVY),
                text(x, 720, w, 40, who, size=30, color=INK500)]
    els += [text(M, 900, 1680, 40, 'Statements · vote · discuss · short talk · questions', size=28, color=INK500, align='left')]
    els += voet(0)
    return els, False


def statements(room, items):
    els = eyebrow(f'Room · {room}')
    els += kop('Agree or disagree?')
    for i, t in enumerate(items):
        y = 330 + i * 190
        els += card(M, y, 1680, 160, INK50)
        els += [text(M + 40, y + 40, 80, 80, str(i + 1), font=HEAD, size=64, bold=True, color=GREEN_DEEP, align='left'),
                text(M + 140, y + 50, 1150, 70, t, size=36, bold=True, color=NAVY, align='left', ls=1.2),
                rect(M + 1330, y + 50, 140, 60, TINT_G, r=30),
                text(M + 1330, y + 62, 140, 36, 'Agree', size=26, bold=True, color=GREEN_DEEP),
                rect(M + 1490, y + 50, 160, 60, TINT_A, r=30),
                text(M + 1490, y + 62, 160, 36, 'Disagree', size=26, bold=True, color=AMBER)]
    els += voet(0)
    return els, False


def s_room_consistency():
    return statements('Consistency', [
        'Same grade with different feedback is consistent enough.',
        'Students care more about fair grades than consistent feedback.',
        'AI should flag unusual marks, not propose them.'])


def s_room_efficiency():
    return statements('Operational efficiency', [
        'Formative feedback no lecturer has read first is acceptable.',
        'Time saved on marking will be cut, not given back to students.',
        'Approving AI feedback with small edits is still my feedback.'])


def s_what_we_heard():
    els = eyebrow('Back together')
    els += kop('What we heard')
    xs, w = D.cols(2)
    for i, t in enumerate(['Consistency', 'Operational efficiency']):
        x = xs[i] - w / 2
        els += card(x, 320, w, 540, TINT_G if i == 0 else INK50)
        els += [text(x + 48, 360, w - 96, 60, t, font=HEAD, size=44, bold=True, color=NAVY, align='left')]
        for j in range(3):
            els += [rect(x + 48, 470 + j * 120, w - 96, 3, INK200)]
    els += voet(0)
    return els, False


def s_close():
    els = [rect(0, 0, W, H, NAVY)]
    els += [text(M, 330, 1500, 260, 'Which of these would\nyou test first?', font=HEAD, size=96, bold=True,
                 color=WHITE, align='left', ls=1.05),
            text(M, 620, 1500, 50, 'Slides and sources follow by email.', size=36, color='B9CBD2', align='left'),
            text(M, 700, 1500, 50, 'info@eduface.me  ·  eduface.me', size=32, color=GREEN, align='left')]
    els += logopaar(dark=True)
    return els, True


DECK = [s_opening, s_agenda, s_jisc, jisc_vraag(1), jisc_vraag(2), s_jisc_pilot,
        jisc_vraag(3), jisc_vraag(4), jisc_vraag(5), s_logos, s_not_a_demo, s_three_reasons,
        s_data_risk, s_ban,
        s_sec_consistency, s_consistency_layers, s_nine_of_twenty, s_where_it_hurts, s_builds,
        s_endgoal_consistency, s_llm_vs_model, s_cases_consistency, s_policy_objection, s_moderation,
        s_sec_efficiency, s_two_flavours, s_pains, s_editing_cost, s_accuracy, s_tuning,
        s_endgoal_efficiency, s_objection, s_objection_answer,
        s_choose_room, s_what_we_heard, s_close]


def build(fns, naam):
    os.makedirs('preview', exist_ok=True)
    slides = []
    for i, fn in enumerate(fns, 1):
        els, dark = fn()
        if 1 < i < len(fns):   # paginanummer links van het logo
            els = els + [text(1330, 1004, 60, 30, str(i), size=22,
                              color='8FA9B4' if dark else '9AAFB8', align='right')]
        h = D.render_html(els, f'preview/{i:02d}-{fn.__name__[2:]}.html', dark=dark)
        shoot(os.path.abspath(h), h[:-5] + '.png')
        os.remove(h)
        slides.append(els)
    D.render_pptx(slides, f'{naam}-bewerkbaar.pptx')


if __name__ == '__main__':
    build(DECK, 'jisc-webinar')
