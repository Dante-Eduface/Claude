"""Proefslide (Gate 2, stuk 2/2): Bath Spa-bewijs.

De kern is een magnitude-vergelijking, dus die krijgt de geometrie die daarbij
hoort: twee bereiken op één gedeelde schaal met nulpunt, niet twee losse
cijfers met een pijl ertussen (dat codeert grootte in lettergrootte).
Grijs voor de oude situatie, groen voor waar de slide over gaat — de
chart-regel uit slides/layouts.md. De drie ondersteunende cijfers staan in
een bewijsbalk eronder, elk met eigen icoon, niet als drie gelijke kaarten.

Deze slide blijft licht: bewijs leest het beste op wit, en hij staat direct
na het navy capability-blok — twee donkere slides achter elkaar zou het
ritme platslaan.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, GREEN, GREEN_DEEP, INK700, INK500, INK200, INK50, WHITE, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION

els = []

# --- kop: bewering, geen label ---------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 2.2,
             'Marking Time Drops 6–10x at Bath Spa University',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- dominante vergelijking: twee bereiken op één schaal van 0 tot 30 min ---
LANE_X, LANE_W = 560, 1000
SCALE_MAX = 30
PXM = LANE_W / SCALE_MAX
ROW_Y, ROW_H, ROW_GAP = 306, 88, 40

x_at = lambda minutes: LANE_X + minutes * PXM

ROWS = [
    ('Traditional marking', 15, 30, INK200, INK700, '15–30 min'),
    ('With Eduface', 1.5, 5, GREEN, NAVY, '1.5–5 min'),
]

for i, (label, lo, hi, bar, label_color, value) in enumerate(ROWS):
    y = ROW_Y + i * (ROW_H + ROW_GAP)
    els += [text(M, y + 24, LANE_X - M - 40, 48, label, font=BODY, size=TEXT,
                 color=label_color, align='right', ls=1.2),
            rect(LANE_X, y, LANE_W, ROW_H, INK50),
            rect(x_at(lo), y, x_at(hi) - x_at(lo), ROW_H, bar),
            text(LANE_X + LANE_W + 40, y + 20, 260, 56, value, font=HEAD, size=SUB,
                 bold=True, color=NAVY, align='left', ls=1.0)]

AXIS_TOP, AXIS_BOT = ROW_Y, ROW_Y + 2 * ROW_H + ROW_GAP
els += [rect(LANE_X, AXIS_TOP, 1, AXIS_BOT - AXIS_TOP, INK200),
        text(LANE_X - 40, AXIS_BOT + 16, 80, 36, '0', size=CAPTION, color=INK500,
             align='right', ls=1.2),
        text(LANE_X + LANE_W - 200, AXIS_BOT + 16, 200, 36, '30',
             size=CAPTION, color=INK500, align='right', ls=1.2),
        text(LANE_X, AXIS_BOT + 16, LANE_W, 36, 'minutes per submission',
             size=CAPTION, color=INK500, align='center', ls=1.2)]

# --- bewijsbalk: drie cijfers, elk met eigen icoon -------------------------
BAND_Y, BAND_H = 660, 228
els += [rect(M, BAND_Y, W - 2 * M, BAND_H, INK50, r=20)]

c3, w3 = cols(3)
EVIDENCE = [
    ('doel', '~94%', 'AI grading accuracy'),
    ('bestand', '2,300+', 'feedback items across\n435 submissions'),
    ('klok', '15–20 hrs', 'saved per 60-student cohort,\nevery cycle'),
]
for i, (cx, (icon, val, lbl)) in enumerate(zip(c3, EVIDENCE)):
    if i:
        els += [rect(cx - w3 / 2 - 24, BAND_Y + 40, 1, BAND_H - 80, INK200)]
    els += tile(cx - w3 / 2 + 24, BAND_Y + 52, icon, tone='greendeep',
                fill=WHITE, size=96, r=16, ic=48)
    els += [text(cx - w3 / 2 + 144, BAND_Y + 46, w3 - 144, 64, val, font=HEAD,
                 size=SUB, bold=True, color=NAVY, align='left', ls=1.0),
            text(cx - w3 / 2 + 144, BAND_Y + 112, w3 - 144, 90, lbl, font=BODY,
                 size=CAPTION, color=INK500, align='left', ls=1.35)]

els += foot(page=13, source='Source: Bath Spa University · Eduface pilot data.')

shoot(render_html(els, 'preview/slide-13.html'), 'preview/slide-13.png')
print('preview/slide-13.png')
