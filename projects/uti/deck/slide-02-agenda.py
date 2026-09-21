"""Agenda: wegwijzer, geen betoog.

Negen items passen niet in één leesbare kolom, dus twee kolommen van 5 en 4,
gelezen van boven naar beneden en dan naar rechts. Het nummer staat links in de
rij op caption-formaat in muted, het label draagt de rij op body-formaat in
navy: zo scant het oog de labels en niet de cijfers. Onder elke rij één
haarlijn, want zonder die lijn zweven negen korte labels los in een breed vlak;
de lijn geeft de kolom een rechterrand die op de marge uitkomt. Geen
accentkleur, want er is hier niets actiefs om te markeren.
"""
from deckbuild import rect, text, foot, render_html, shoot, \
    NAVY, INK500, INK100, HEAD, BODY, \
    M, W, TITLE, TEXT, CAPTION

els = []

# --- kop -------------------------------------------------------------------
els += [text(M, 88, W - 2 * M, TITLE * 1.3, 'Agenda',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04)]

# --- twee kolommen: 5 links, 4 rechts --------------------------------------
ITEMS = [
    'Key Findings',
    'Current State',
    'Risks Ahead',
    'The Proposed Model',
    'Benefits',
    'Required Capabilities',
    'Proven Results',
    'Our Solution',
    'Next Steps',
]
LEFT_N = 5

COL_W, COL_GAP = 700, 280
COL_X = [M, M + COL_W + COL_GAP]          # rechterkolom eindigt precies op de marge
NUM_W, LABEL_DX = 60, 72
ROW_H, Y0, RULE_DY = 124, 282, 74

for i, label in enumerate(ITEMS):
    col, row = (0, i) if i < LEFT_N else (1, i - LEFT_N)
    x, y = COL_X[col], Y0 + row * ROW_H
    # nummer iets lager zodat de kleine cijfers optisch op de lijn van het label staan
    els += [text(x, y + 9, NUM_W, 34, f'{i + 1:02d}', font=HEAD, size=CAPTION,
                 color=INK500, align='left', ls=1.0),
            text(x + LABEL_DX, y, COL_W - LABEL_DX, 48, label, font=BODY,
                 size=TEXT, color=NAVY, align='left', ls=1.2)]
    # lijn staat tussen items, niet onder het laatste: anders loopt de kolom
    # dood tegen de voettekstlijn
    if i not in (LEFT_N - 1, len(ITEMS) - 1):
        els += [rect(x, y + RULE_DY, COL_W, 1, INK100)]

els += foot(dark=False, page=2)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-02.html', dark=DARK), 'preview/slide-02.png')
    print('preview/slide-02.png')
