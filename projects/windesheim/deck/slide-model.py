"""Losse proefslide: hoe het model is opgebouwd. Fundament onder, vakgebieden erop."""
from deckbuild import (rect, pic, text, title, foot, render_html, shoot,
                       NAVY, GREEN, GREEN_DEEP, TINT_G, INK50, INK100, INK500,
                       WHITE, HEAD, M)

els = title('Het model')

# --- vakgebieden, bovenop het fundament getraind -------------------------
els += [text(M, 246, 1920 - 2 * M, 40, 'Per vakgebied apart getraind', size=28, color=INK500)]
VAK = [('weegschaal', 'Recht'), ('trend', 'Economie'), ('groep', 'Sociale\nwetenschappen'),
       ('kolf', 'Techniek'), ('boek', 'Geestes\nwetenschappen'), ('zorg', 'Gezondheid')]
CW, GAP = 260, 24
for i, (ic, lbl) in enumerate(VAK):
    x = M + i * (CW + GAP)
    els += [rect(x, 300, CW, 200, INK50, r=24),
            pic(f'assets/icon-{ic}-navy.png', x + CW / 2 - 34, 330, 68, 68),
            text(x + 12, 414, CW - 24, 86, lbl,
                 font=HEAD, size=28, bold=True, ls=1.15)]

# --- de laag ertussen ----------------------------------------------------
els += [rect(M, 528, 1920 - 2 * M, 48, INK100, r=24),
        text(M, 540, 1920 - 2 * M, 34, 'RAG, toegang tot vakliteratuur', size=26, color=INK500)]

# --- het fundament -------------------------------------------------------
els += [rect(M, 604, 1920 - 2 * M, 216, NAVY, r=28),
        text(160, 634, 600, 36, 'FUNDAMENT', size=26, bold=True, color=GREEN, align='left')]
for x, lbl in [(230, '250.000 datapunten'), (990, 'Didactiek en onderwijskunde')]:
    els += [rect(x, 690, 700, 100, GREEN, r=22),
            text(x, 716, 700, 60, lbl, font=HEAD, size=40, bold=True, color=NAVY)]

els += foot(src='Getraind met de Universiteit Leiden en de Radboud Universiteit.', page=None)

shoot(render_html(els, 'preview/model.html'), 'preview/model.png')
print('preview/model.png')
