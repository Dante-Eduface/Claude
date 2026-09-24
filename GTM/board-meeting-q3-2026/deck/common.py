"""Gedeelde hulpjes voor dit deck. Geen klantlogo (intern deck), dus een eigen
lichte voet i.p.v. deckbuild.foot(), die een klant.png verwacht."""
from deckbuild import rect, text, pic, M, NAVY, INK100, INK500, BODY

LOGO_NAVY = 'assets/logo_navy.png'
LOGO_WIT = 'assets/logo_white.png'


def board_foot(src=None, page=None, dark=False):
    out = [rect(M, 868, 1920 - 2 * M, 1, 'FFFFFF33' if dark else INK100)]
    if src:
        out.append(text(M, 894, 1500, 60, src, font=BODY, size=23,
                         color='8FA9B4' if dark else INK500, align='left', ls=1.3))
    out.append(pic(LOGO_WIT if dark else LOGO_NAVY, 1680, 902, 120, 33))
    if page:
        out.append(text(1660, 950, 140, 34, str(page), font=BODY, size=20,
                         color='FFFFFF73' if dark else '9AAFB8', align='right'))
    return out
