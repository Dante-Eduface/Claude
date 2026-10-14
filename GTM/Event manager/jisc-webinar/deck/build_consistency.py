"""Breakout-deck Consistency (Dante). Hergebruikt de bouwstenen van build.py.

Draaien vanuit deze map:  python3 build_consistency.py
"""
import os
import build as B
import deckbuild as D
from deckbuild import rect, oval, pic, text, NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G, \
    INK50, INK100, INK200, INK500, WHITE, HEAD, BODY, M

W, H = B.W, B.H
eyebrow, kop, voet, card, itile, icon = B.eyebrow, B.kop, B.voet, B.card, B.itile, B.icon


# ---------------------------------------------------------------- opening en uitleg
def s_opening():
    els = [rect(0, 0, W, H, NAVY)]
    els += [oval(1380, 260, 760, '0A3A47', '0A3A47', 0),
            oval(1520, 400, 480, '0F4C57', '0F4C57', 0),
            oval(1660, 540, 200, GREEN, GREEN, 0)]
    els += eyebrow('Breakout room  ·  Consistency', y=300, dark=True)
    els += [text(M, 360, 1200, 330, 'Consistency without\nshowing AI grades',
                 font=HEAD, size=96, bold=True, color=WHITE, align='left', ls=1.05),
            text(M, 600, 1100, 60, 'with Dante Torbed, Eduface', size=36, color='B9CBD2', align='left')]
    els += B.logopaar(dark=True)
    return els, True


def s_how():
    els = eyebrow('This room')
    els += kop('Three parts')
    stappen = [('check', 'Vote on\nfive statements'), ('oogdicht', 'A short demo:\nthe consistency check'),
               ('gesprek', 'Discussion')]
    xs, w = D.cols(3)
    els += [rect(xs[0], 520, xs[-1] - xs[0], 4, INK100)]
    for i, (ic, t) in enumerate(stappen):
        els += itile(xs[i], 450, ic, 'amber' if i == 1 else 'green')
        els += [text(xs[i] - w / 2, 630, w, 120, t, size=36, bold=i == 1, color=NAVY, ls=1.25)]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- stellingen, één per slide
STELLINGEN = [
    ('choice', 'In the short term, AI will have an impact at my institution on…',
     ['Formative feedback only', 'Formative and summative feedback']),
    ('agree', 'Two markers on the same module would give the same assignment a different mark.', None),
    ('agree', 'Our current moderation catches most inconsistent marking.', None),
    ('agree', 'Students notice when feedback differs between markers.', None),
    ('agree', 'I would trust an AI that flags marks more than an AI that proposes them.', None),
]


def stelling(n):
    soort, t, opties = STELLINGEN[n - 1]

    def slide():
        els = eyebrow(f'Statement {n} of {len(STELLINGEN)}')
        els += [text(M, 260, 1560, 340, t, font=HEAD, size=80, bold=True, color=NAVY, align='left', ls=1.1)]
        if soort == 'choice':
            labels = [(f'A   {opties[0]}', TINT_G, GREEN_DEEP), (f'B   {opties[1]}', TINT_A, AMBER)]
            bw = 700
        else:
            labels = [('Agree', TINT_G, GREEN_DEEP), ('Disagree', TINT_A, AMBER)]
            bw = 320
        x = M
        for lab, fill, kleur in labels:
            els += [rect(x, 660, bw, 100, fill, r=50),
                    text(x, 688, bw, 50, lab, size=34, bold=True, color=kleur)]
            x += bw + 32
        # voortgang
        x = M
        for i in range(1, len(STELLINGEN) + 1):
            w = 64 if i == n else 20
            kleur = GREEN if i == n else (GREEN_DEEP if i < n else INK100)
            els.append(rect(x, 850, w, 20, kleur, r=10))
            x += w + 14
        els += voet(0)
        return els, False
    slide.__name__ = f's_stelling{n}'
    return slide


# ---------------------------------------------------------------- de consistency check
def s_sec_check():
    return B.section('Demo', 'The consistency check', 'AI that checks marking, without grading')


def s_does_doesnt():
    els = eyebrow('The consistency check')
    els += kop('It reads every paper.\nIt never shows a grade.', w=1400)
    xs, w = D.cols(2)
    kolommen = [('It does', TINT_G, GREEN_DEEP, '✓',
                 ['Analyses each paper in the background', 'Flags marks outside the expected range',
                  'Adds comments, if you want them']),
                ('It doesn’t', INK50, INK500, '×',
                 ['Show an AI grade', 'Change the lecturer’s mark', 'Make any decision'])]
    for i, (t, fill, kleur, teken, items) in enumerate(kolommen):
        x = xs[i] - w / 2
        els += card(x, 360, w, 470, fill)
        els += [text(x + 48, 396, w - 96, 60, t, font=HEAD, size=48, bold=True, color=NAVY, align='left')]
        for j, it in enumerate(items):
            y = 500 + j * 100
            els += [text(x + 48, y, 50, 50, teken, font=HEAD, size=44, bold=True, color=kleur, align='left'),
                    text(x + 110, y + 6, w - 160, 50, it, size=32, color=NAVY, align='left')]
    els += voet(0)
    return els, False


def s_signal():
    els = eyebrow('What the marker sees')
    els += kop('A signal, not a score')
    # nagebouwd scherm, fictieve data
    x0, y0, bw = M, 300, 1680
    els += [rect(x0, y0, bw, 600, WHITE, r=24), rect(x0, y0, bw, 600, INK50, r=24),
            rect(x0 + 2, y0 + 2, bw - 4, 596, WHITE, r=22),
            text(x0 + 40, y0 + 28, 1200, 40, 'Essay 2  ·  Module EDU201  ·  your marking', size=26, bold=True,
                 color=INK500, align='left')]
    kol = [(x0 + 40, 'Submission'), (x0 + 480, 'Your mark'), (x0 + 820, 'AI grade'), (x0 + 1160, 'Consistency signal')]
    for x, t in kol:
        els += [text(x, y0 + 90, 340, 36, t.upper(), size=22, bold=True, color=INK500, align='left')]
    rijen = [('#1042', '65', None), ('#1043', '58', None), ('#1044', '72', None),
             ('#1045', '41', 'Outside expected range'), ('#1046', '67', None)]
    for i, (sub, cijfer, sig) in enumerate(rijen):
        y = y0 + 140 + i * 88
        if sig:
            els += [rect(x0 + 20, y - 14, bw - 40, 76, TINT_A, r=14)]
        els += [rect(x0 + 40, y - 18, bw - 80, 1, INK100),
                text(kol[0][0], y + 4, 300, 40, sub, size=30, color=NAVY, align='left'),
                text(kol[1][0], y + 4, 200, 40, cijfer, font=HEAD, size=34, bold=True, color=NAVY, align='left'),
                pic(icon('oogdicht', 'navy'), kol[2][0], y + 2, 36, 36),
                text(kol[2][0] + 50, y + 6, 200, 36, 'Hidden', size=26, color=INK500, align='left')]
        if sig:
            els += [pic(icon('vlag', 'amber'), kol[3][0], y + 2, 36, 36),
                    text(kol[3][0] + 50, y + 4, 400, 40, sig, size=28, bold=True, color=AMBER, align='left')]
        else:
            els += [text(kol[3][0], y + 4, 400, 40, '—', size=28, color=INK200, align='left')]
    els += voet(0, src='Illustrative screen, fictional data.')
    return els, False


def s_live():
    return B.statement('Live demo', sub='Same marking, one signal, no AI grade.')


# ---------------------------------------------------------------- discussie
def s_topic():
    els = [rect(0, 0, W, H, NAVY)]
    els += eyebrow('Discussion', y=300, dark=True)
    els += [text(M, 350, 1600, 320, 'Is consistency without\nAI grades enough?', font=HEAD, size=104,
                 bold=True, color=WHITE, align='left', ls=1.05),
            text(M, 640, 1500, 50, 'Or is it a first step towards something more?', size=36,
                 color='B9CBD2', align='left')]
    els += B.logopaar(dark=True)
    return els, True


VRAGEN = [
    'Where would a signal like this have helped you last year?',
    'Who should receive the signal: the marker, the module leader or the moderator?',
    'What would need to be true before you trust a flag?',
    'How would you explain this to your students?',
]


def vraag(n):
    def slide():
        els = eyebrow(f'Discussion  ·  {n} of {len(VRAGEN)}')
        els += [text(M, 300, 1500, 420, VRAGEN[n - 1], font=HEAD, size=88, bold=True,
                     color=NAVY, align='left', ls=1.1)]
        x = M
        for i in range(1, len(VRAGEN) + 1):
            w = 64 if i == n else 20
            kleur = GREEN if i == n else (GREEN_DEEP if i < n else INK100)
            els.append(rect(x, 800, w, 20, kleur, r=10))
            x += w + 14
        els += voet(0)
        return els, False
    slide.__name__ = f's_vraag{n}'
    return slide


def s_close():
    els = [rect(0, 0, W, H, NAVY)]
    els += [text(M, 330, 1500, 260, 'Back to the\nmain room', font=HEAD, size=104, bold=True,
                 color=WHITE, align='left', ls=1.05),
            text(M, 620, 1500, 50, 'Bring one thing you heard here.', size=36, color='B9CBD2', align='left')]
    els += B.logopaar(dark=True)
    return els, True


DECK = ([s_opening, s_how] + [stelling(i) for i in range(1, len(STELLINGEN) + 1)]
        + [s_sec_check, s_does_doesnt, s_signal, s_live, s_topic]
        + [vraag(i) for i in range(1, len(VRAGEN) + 1)] + [s_close])


def build(fns, naam, map_='preview-consistency'):
    os.makedirs(map_, exist_ok=True)
    slides = []
    for i, fn in enumerate(fns, 1):
        els, dark = fn()
        if 1 < i < len(fns):
            els = els + [text(1330, 1004, 60, 30, str(i), size=22,
                              color='8FA9B4' if dark else '9AAFB8', align='right')]
        h = D.render_html(els, f'{map_}/{i:02d}-{fn.__name__[2:]}.html', dark=dark)
        B.shoot(os.path.abspath(h), h[:-5] + '.png')
        os.remove(h)
        slides.append(els)
    D.render_pptx(slides, f'{naam}-bewerkbaar.pptx')


if __name__ == '__main__':
    build(DECK, 'breakout-consistency')
