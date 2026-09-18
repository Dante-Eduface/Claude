"""Proefslide (Gate 2, stuk 2/2): Bath Spa-bewijs.

De kern is een magnitude-vergelijking, dus die krijgt de geometrie die daarbij
hoort: twee bereiken op één gedeelde schaal met nulpunt, niet twee losse
cijfers met een pijl ertussen (dat codeert grootte in lettergrootte).
Grijs voor de oude situatie, groen voor waar de slide over gaat — de
chart-regel uit slides/layouts.md. De drie ondersteunende cijfers staan als
compacte, gebronde bewijsregel eronder, niet als drie gelijke kaarten."""
from deckbuild import rect, text, foot, render_html, shoot, cols, \
    NAVY, GREEN, INK700, INK500, INK200, INK100, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION

els = []

# --- kop: bewering, geen label ---------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.2,
             'Marking Time Drops 6–10x at Bath Spa University',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- dominante vergelijking: twee bereiken op één schaal van 0 tot 30 min ---
LANE_X, LANE_W = 560, 1000          # plotbaan
SCALE_MAX = 30                       # minuten, nulpunt zichtbaar
PXM = LANE_W / SCALE_MAX             # px per minuut
ROW_Y, ROW_H, ROW_GAP = 330, 76, 40

def x_at(minutes):
    return LANE_X + minutes * PXM

ROWS = [
    ('Traditional marking', 15, 30, INK200, INK700, '15–30 min'),
    ('With Eduface', 1.5, 5, GREEN, NAVY, '1.5–5 min'),
]

for i, (label, lo, hi, bar, label_color, value) in enumerate(ROWS):
    y = ROW_Y + i * (ROW_H + ROW_GAP)
    els += [text(M, y + 18, LANE_X - M - 40, 48, label, font=BODY, size=TEXT,
                 color=label_color, align='right', ls=1.2),
            rect(LANE_X, y, LANE_W, ROW_H, INK50),
            rect(x_at(lo), y, x_at(hi) - x_at(lo), ROW_H, bar),
            text(LANE_X + LANE_W + 40, y + 14, 260, 56, value, font=HEAD, size=SUB,
                 bold=True, color=NAVY, align='left', ls=1.0)]

# nulpunt en schaal-einde: de as die de vergelijking eerlijk houdt
AXIS_TOP, AXIS_BOT = ROW_Y, ROW_Y + 2 * ROW_H + ROW_GAP
els += [rect(LANE_X, AXIS_TOP, 1, AXIS_BOT - AXIS_TOP, INK200),
        text(LANE_X - 40, AXIS_BOT + 16, 80, 36, '0', size=CAPTION, color=INK500,
             align='right', ls=1.2),
        text(LANE_X + LANE_W - 200, AXIS_BOT + 16, 200, 36, '30',
             size=CAPTION, color=INK500, align='right', ls=1.2),
        text(LANE_X, AXIS_BOT + 16, LANE_W, 36, 'minutes per submission',
             size=CAPTION, color=INK500, align='center', ls=1.2)]

# --- ondersteunende bewijsregel: drie cijfers, geen drie gelijke kaarten ---
c3, w3 = cols(3)
EVIDENCE = [
    ('~94%', 'AI grading accuracy'),
    ('2,300+', 'feedback items across 435 submissions'),
    ('15–20 hrs', 'saved per 60-student cohort, every cycle'),
]
ROW2_Y = 700
els += [rect(M, ROW2_Y - 40, W - 2 * M, 1, INK100)]
for i, (cx, (val, lbl)) in enumerate(zip(c3, EVIDENCE)):
    if i:
        els += [rect(cx - w3 / 2 - 24, ROW2_Y, 1, 140, INK100)]
    els += [text(cx - w3 / 2, ROW2_Y, w3, 60, val, font=HEAD, size=SUB, bold=True,
                 color=NAVY, align='center', ls=1.0),
            text(cx - w3 / 2, ROW2_Y + 72, w3, 70, lbl, font=BODY, size=CAPTION,
                 color=INK500, align='center', ls=1.3)]

els += foot(page=13, source='Source: Bath Spa University · Eduface pilot data.')

shoot(render_html(els, 'preview/slide-13.html'), 'preview/slide-13.png')
print('preview/slide-13.png')
