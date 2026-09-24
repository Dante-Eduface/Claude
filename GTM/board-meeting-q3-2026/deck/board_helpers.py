"""Board-memo stijl i.p.v. pitch-stijl: kleinere kop, meer en dichtere inhoud per
slide. Board leest en slaat na, kijkt niet vanaf een podium mee."""
from deckbuild import rect, text, NAVY, INK500, INK100, HEAD, BODY, M


def board_title(t, size=60):
    return [text(M, 84, 1760, 84, t, font=HEAD, size=size, bold=True, color=NAVY, align='left')]


def subline(t, y=180, size=27, color=INK500):
    return [text(M, y, 1760, 44, t, font=BODY, size=size, color=color, align='left')]


def bullets(items, x, y, w, row_h, size=26, color=NAVY, dot_color=None, ls=1.3):
    """items: lijst van strings, of (tekst, kleur) tuples voor losse kleur per regel."""
    els = []
    cy = y
    for it in items:
        txt, col = it if isinstance(it, tuple) else (it, color)
        if dot_color:
            els += [rect(x, cy + 10, 10, 10, dot_color, r=5)]
            tx = x + 30
        else:
            tx = x
        els += [text(tx, cy, w - (tx - x), row_h - 8, txt, font=BODY, size=size, color=col, align='left', ls=ls)]
        cy += row_h
    return els


def table(headers, rows, x, y, col_x, col_w, aligns, row_h=34, header_size=19, body_size=21,
          header_color=INK500, body_color=NAVY, line_color=INK100, bold_last=False):
    """col_x/col_w/aligns: lijst per kolom. rows: lijst van tuples met evenveel velden als col_x."""
    els = []
    for cx, cw, al, h in zip(col_x, col_w, aligns, headers):
        els += [text(cx, y, cw, 30, h, font=BODY, size=header_size, bold=True, color=header_color, align=al)]
    table_w = (col_x[-1] + col_w[-1]) - x
    els += [rect(x, y + 30, table_w, 2, line_color)]
    cy = y + 30 + 14
    n = len(rows)
    for i, row in enumerate(rows):
        bold = bold_last and i == n - 1
        if bold:
            els += [rect(x, cy - 6, (col_x[-1] + col_w[-1]) - x, 2, NAVY)]
            cy += 14
        for cx, cw, al, val in zip(col_x, col_w, aligns, row):
            els += [text(cx, cy, cw, row_h - 6, str(val), font=BODY, size=body_size, bold=bold,
                         color=body_color, align=al)]
        cy += row_h
    return els, cy
