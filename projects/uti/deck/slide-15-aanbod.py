"""Het aanbod. De prijs is het dominante object, niet de capabilities.

Het bedrag zit in een navy vlak over de volle breedte: dat is het enige
zware object op een witte slide, dus het oog landt erop voor het de titel
naleest. De twee voorwaarden staan in datzelfde vlak, achter een dunne
scheidingslijn, want ze horen bij de prijs en zijn geen losse punten.

De vier capabilities keren onderaan klein terug, zelfde iconen en zelfde
volgorde als slides 8 tot 12, zodat het als terugverwijzing leest en niet
als een nieuw rijtje.
"""
from deckbuild import rect, text, tile, foot, render_html, shoot, cols, \
    NAVY, WHITE, INV_SOFT, INV_RULE, INK900, INK500, INK100, INK50, HEAD, BODY, \
    M, W, TITLE, SUB, TEXT, CAPTION, STAT

els = []

# --- kop: bewering die het aanbod draagt, plus één regel context -----------
els += [text(M, 88, W - 2 * M, TITLE * 1.3,
             'Institution-wide feedback, priced per student',
             font=HEAD, size=TITLE, bold=True, color=NAVY, align='left', ls=1.04),
        text(M, 200, W - 2 * M, 48, 'Delivered by Eduface, mapped to what UTI needs.',
             font=BODY, size=TEXT, color=INK500, align='left', ls=1.3)]

# --- het aanbod: navy vlak, prijs links, voorwaarden rechts ----------------
PAN_Y, PAN_H, PAD = 300, 356, 72
els += [rect(M, PAN_Y, W - 2 * M, PAN_H, NAVY, r=24)]

PRICE_X = M + PAD
els += [text(PRICE_X, 372, 300, 210, '$3', font=HEAD, size=STAT, bold=True,
             color=WHITE, align='left', ls=0.9),
        text(PRICE_X + 236, 400, 420, 112, 'per student,\nper month',
             font=HEAD, size=SUB, bold=True, color=WHITE, align='left', ls=1.15),
        text(PRICE_X, 540, 520, 44, 'billed annually',
             font=BODY, size=TEXT, color=INV_SOFT, align='left', ls=1.2)]

# De voorwaarden horen bij de prijs, dus binnen hetzelfde vlak; de lijn
# scheidt ze zonder er een tweede kaartje omheen te zetten. Het vinkje is het
# enige groen op de slide: deze twee zitten in de prijs inbegrepen.
RULE_X, TERM_X, LBL_X = 900, 964, 964 + 84
TERM_W = W - M - PAD - LBL_X
els += [rect(RULE_X, PAN_Y + 40, 1, PAN_H - 80, INV_RULE)]
for i, t in enumerate(['Discount for multi-year commitment',
                       'Scales with growing students & instructors']):
    y = 402 + i * 96
    els += tile(TERM_X, y, 'check', tone='green', fill=INK900, size=56, r=14, ic=28)
    els += [text(LBL_X, y + 6, TERM_W, 48, t,
                 font=BODY, size=TEXT, color=WHITE, align='left', ls=1.35)]

# --- stille herhaling van de vier capabilities ----------------------------
RECAP_Y = 736
els += [rect(M, RECAP_Y, W - 2 * M, 1, INK100),
        text(M, RECAP_Y + 24, 600, 34, 'What that covers', font=BODY,
             size=CAPTION, color=INK500, align='left', ls=1.2)]

c4, w4 = cols(4)
RECAP = [('doel', 'Accuracy & Consistency'), ('sleutel', 'Technical Domain Fit'),
         ('instelling', 'Institution-Wide'), ('schuifjes', 'Self-Configuring')]
for cx, (icon, label) in zip(c4, RECAP):
    x = cx - w4 / 2
    els += tile(x, 820, icon, tone='navy', fill=INK50, size=72, r=16, ic=36)
    els += [text(x + 92, 840, w4 - 92, 40, label, font=BODY, size=CAPTION,
                 color=INK500, align='left', ls=1.3)]

els += foot(dark=False, page=15)

DARK = False

if __name__ == '__main__':
    shoot(render_html(els, 'preview/slide-15.html', dark=DARK), 'preview/slide-15.png')
    print('preview/slide-15.png')
