"""Breakout-deck Operational efficiency: de docent in the loop bij summatieve feedback.

Draaien vanuit deze map:  python3 build_efficiency.py
"""
import build as B
import build_consistency as C
import deckbuild as D
from deckbuild import rect, oval, pic, text, NAVY, GREEN, GREEN_DEEP, AMBER, TINT_A, TINT_G, \
    INK50, INK100, INK200, INK500, WHITE, HEAD, BODY, M

W, H = B.W, B.H
eyebrow, kop, voet, card, itile, icon = B.eyebrow, B.kop, B.voet, B.card, B.itile, B.icon


def voortgang(n, totaal, y):
    out, x = [], M
    for i in range(1, totaal + 1):
        w = 64 if i == n else 20
        kleur = GREEN if i == n else (GREEN_DEEP if i < n else INK100)
        out.append(rect(x, y, w, 20, kleur, r=10))
        x += w + 14
    return out


# ---------------------------------------------------------------- opening en uitleg
def s_opening():
    els = [rect(0, 0, W, H, NAVY)]
    els += [oval(1380, 260, 760, '0A3A47', '0A3A47', 0),
            oval(1520, 400, 480, '0F4C57', '0F4C57', 0),
            oval(1660, 540, 200, GREEN, GREEN, 0)]
    els += eyebrow('Breakout room  ·  Operational efficiency', y=300, dark=True)
    els += [text(M, 360, 1200, 330, 'Keeping the lecturer\nin the loop',
                 font=HEAD, size=96, bold=True, color=WHITE, align='left', ls=1.05),
            text(M, 600, 1100, 60, 'with [name], Eduface', size=36, color='B9CBD2', align='left')]
    els += B.logopaar(dark=True)
    return els, True


def s_how():
    els = eyebrow('This room')
    els += kop('Three parts')
    stappen = [('check', 'Vote on\nfive statements'), ('usercheck', 'How we keep the lecturer\nin the loop'),
               ('gesprek', 'Discussion')]
    xs, w = D.cols(3)
    els += [rect(xs[0], 520, xs[-1] - xs[0], 4, INK100)]
    for i, (ic, t) in enumerate(stappen):
        els += itile(xs[i], 450, ic, 'amber' if i == 1 else 'green')
        els += [text(xs[i] - w / 2, 630, w, 120, t, size=36, bold=i == 1, color=NAVY, ls=1.25)]
    els += voet(0)
    return els, False


# ---------------------------------------------------------------- stellingen
STELLINGEN = [
    'Formative feedback that no lecturer has read first is acceptable.',
    'Time saved on marking would go back into teaching at my institution.',
    'Most lecturers would accept AI feedback without changing it.',
    'Students care whether a person wrote their feedback.',
    'Summative feedback should always be signed off by a lecturer.',
]


def stelling(n):
    def slide():
        els = eyebrow(f'Statement {n} of {len(STELLINGEN)}')
        els += [text(M, 260, 1560, 340, STELLINGEN[n - 1], font=HEAD, size=80, bold=True,
                     color=NAVY, align='left', ls=1.1)]
        x = M
        for lab, fill, kleur in [('Agree', TINT_G, GREEN_DEEP), ('Disagree', TINT_A, AMBER)]:
            els += [rect(x, 660, 320, 100, fill, r=50), text(x, 688, 320, 50, lab, size=34, bold=True, color=kleur)]
            x += 352
        els += voortgang(n, len(STELLINGEN), 850)
        els += voet(0)
        return els, False
    slide.__name__ = f's_stelling{n}'
    return slide


# ---------------------------------------------------------------- human in the loop
def s_sec():
    return B.section('Demo', 'Human in the loop', 'How the lecturer stays in charge of summative feedback')


def s_flow():
    els = eyebrow('Summative feedback')
    els += kop('The AI drafts.\nThe lecturer decides.', w=1400)
    stappen = [('rubric', 'navy', 'AI drafts a comment\nper rubric criterion'),
               ('filepen', 'navy', 'Lecturer reads,\nedits and adds'),
               ('usercheck', 'green', 'Only approved feedback\nreaches the student')]
    xs, w = D.cols(3)
    for i, (ic, tone, t) in enumerate(stappen):
        els += itile(xs[i], 450, ic, tone, size=150)
        els += [text(xs[i] - w / 2, 640, w, 110, t, size=32, color=NAVY, bold=i == 2, ls=1.3)]
        if i < 2:
            els += [text(xs[i] + 90, 490, w - 180 + 72, 70, '→', font=HEAD, size=60, bold=True, color=INK200)]
    els += [rect(M, 820, 300, 60, TINT_G, r=30),
            text(M, 834, 300, 36, 'Lecturer + AI', size=28, bold=True, color=GREEN_DEEP),
            text(M + 330, 834, 1200, 36, 'Every comment is reviewed before the student sees it.',
                 size=28, color=INK500, align='left')]
    els += voet(0)
    return els, False


def s_97():
    els = eyebrow('What we see')
    els += [text(M, 220, 900, 300, '97%', font=HEAD, size=280, bold=True, color=GREEN_DEEP, align='left', ls=1.0),
            text(M, 530, 860, 160, 'of summative assignments get\nextra feedback from the lecturer,\non top of the AI draft',
                 size=40, color=NAVY, align='left', ls=1.3)]
    els += card(1100, 250, 700, 500, NAVY)
    els += [text(1160, 310, 600, 380, 'Lecturers don’t outsource their judgement.\n\nThey work with the AI to give the student better feedback.',
                 font=HEAD, size=44, bold=True, color=WHITE, align='left', ls=1.2)]
    els += voet(0, src='Eduface platform data, summative assessments.')
    return els, False


def s_screen():
    els = eyebrow('What the lecturer sees')
    els += kop('Every comment waits\nfor approval', w=900)
    # productbeeld van eduface.me
    els += [rect(840, 230, 980, 470, INK50, r=24),
            pic('assets/prod_review.png', 870, 260, 920, 920 * 1010 / 2160)]
    els += [text(M, 520, 640, 200, 'Approve, edit or add.\nNothing goes to the student\nwithout the lecturer.',
                 size=34, color=NAVY, align='left', ls=1.35)]
    els += voet(0, src='Product screen from eduface.me')
    return els, False


def s_idea():
    els = eyebrow('An idea we’d like your view on')
    els += kop('A nudge against\nrubber-stamping', w=1100)
    # rij goedkeuringen zonder wijziging, dan een duwtje
    for i in range(10):
        x = M + i * 92
        els += [oval(x, 470, 68, TINT_G, TINT_G, 0),
                text(x, 482, 68, 44, '✓', font=HEAD, size=36, bold=True, color=GREEN_DEEP)]
    els += [oval(M + 10 * 92, 470, 68, TINT_A, TINT_A, 0),
            text(M + 10 * 92, 480, 68, 44, '?', font=HEAD, size=40, bold=True, color=AMBER)]
    bx = M + 11 * 92 + 30
    els += [rect(bx, 440, 1800 - bx, 130, AMBER, r=24),
            text(bx + 36, 466, 1800 - bx - 72, 100,
                 '10 approved without a single change.\nTake a closer look at this one?',
                 size=30, bold=True, color=WHITE, align='left', ls=1.3)]
    els += [text(M, 680, 1500, 100, 'When a lecturer approves a long run of drafts untouched,\nthe platform asks them to look again.',
                 size=34, color=NAVY, align='left', ls=1.35)]
    els += voet(0, src='Concept for discussion, not a current feature.')
    return els, False


def s_live():
    return B.statement('Live demo', sub='One assignment, from AI draft to approved feedback.')


# ---------------------------------------------------------------- discussie
def s_topic():
    els = [rect(0, 0, W, H, NAVY)]
    els += eyebrow('Discussion', y=300, dark=True)
    els += [text(M, 350, 1600, 320, 'What should a lecturer\nalways add that AI can’t?', font=HEAD, size=104,
                 bold=True, color=WHITE, align='left', ls=1.05),
            text(M, 640, 1500, 50, 'The 97% says lecturers already know.', size=36,
                 color='B9CBD2', align='left')]
    els += B.logopaar(dark=True)
    return els, True


VRAGEN = [
    'What does “human in the loop” mean at your institution in practice?',
    'When is approving without edits fine, and when is it a warning sign?',
    'Who is accountable for summative feedback: the lecturer, the module lead or the institution?',
    'Where would you spend the time you get back?',
]


def vraag(n):
    def slide():
        els = eyebrow(f'Discussion  ·  {n} of {len(VRAGEN)}')
        els += [text(M, 300, 1500, 420, VRAGEN[n - 1], font=HEAD, size=88, bold=True,
                     color=NAVY, align='left', ls=1.1)]
        els += voortgang(n, len(VRAGEN), 800)
        els += voet(0)
        return els, False
    slide.__name__ = f's_vraag{n}'
    return slide


DECK = ([s_opening, s_how] + [stelling(i) for i in range(1, len(STELLINGEN) + 1)]
        + [s_sec, s_flow, s_97, s_screen, s_idea, s_live, s_topic]
        + [vraag(i) for i in range(1, len(VRAGEN) + 1)] + [C.s_close])


if __name__ == '__main__':
    C.build(DECK, 'breakout-efficiency', map_='preview-efficiency')
