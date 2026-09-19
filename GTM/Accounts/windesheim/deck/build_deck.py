"""Windesheim-deck, 14 september 2026. Zie deckbuild.py voor de renderers."""
import math, os
from deckbuild import (rect, oval, pic, text, title, tile, foot, cols,
                       render_pptx, render_html, shoot,
                       NAVY, AMBER, GREEN, GREEN_DEEP, TINT_G, INK50, INK100,
                       INK200, INK500, WHITE, HEAD, BODY, M)

S = []
def add(naam, els, dark=False): S.append((naam, els, dark))

c2, w2 = cols(2)
c3, w3 = cols(3)
c4, w4 = cols(4)

# ---------------------------------------------------------------- 1 eigen model
els = title('Eigen model')
for cx, (ic, lbl) in zip(c3, [('data', '250.000 opdrachten'),
                              ('pen', 'Docentfeedback erop'),
                              ('boek', 'Domeinkennis per vak')]):
    els += tile(cx, 380, ic, 'green')
    els += [text(cx - w3 / 2, 570, w3, 120, lbl, font=HEAD, size=46, bold=True, ls=1.1)]
els += [text(M, 706, 1920 - 2 * M, 40, 'Gebouwd met', size=28, color=INK500),
        pic('assets/leiden.png', 674, 748, 180, 76),
        pic('assets/radboud.png', 914, 748, 333, 76)]
els += foot(src='Demo en gesprek, 14 september 2026.', page=1)
add('01-eigen-model', els)

# ---------------------------------------------------------------- 2 het model
# Fundament onderaan, de vakgebieden daar bovenop getraind.
els = title('Het model')
els += [text(M, 246, 1920 - 2 * M, 40, 'Per vakgebied apart getraind', size=28, color=INK500)]
VAK = [('weegschaal', 'Recht'), ('trend', 'Economie'), ('groep', 'Sociale\nwetenschappen'),
       ('kolf', 'Techniek'), ('boek', 'Geestes\nwetenschappen'), ('zorg', 'Gezondheid')]
CW, VGAP = 260, 24
for i, (ic, lbl) in enumerate(VAK):
    x = M + i * (CW + VGAP)
    els += [rect(x, 300, CW, 200, INK50, r=24),
            pic(f'assets/icon-{ic}-navy.png', x + CW / 2 - 34, 330, 68, 68),
            text(x + 12, 414, CW - 24, 86, lbl, font=HEAD, size=28, bold=True, ls=1.15)]
els += [rect(M, 528, 1920 - 2 * M, 48, INK100, r=24),
        text(M, 540, 1920 - 2 * M, 34, 'RAG, toegang tot vakliteratuur', size=26, color=INK500)]
els += [rect(M, 604, 1920 - 2 * M, 216, NAVY, r=28),
        text(160, 634, 600, 36, 'FUNDAMENT', size=26, bold=True, color=GREEN, align='left')]
for x, lbl in [(230, '250.000 datapunten'), (990, 'Didactiek en onderwijskunde')]:
    els += [rect(x, 690, 700, 100, GREEN, r=22),
            text(x, 716, 700, 60, lbl, font=HEAD, size=40, bold=True, color=NAVY)]
els += foot(src='Getraind met de Universiteit Leiden en de Radboud Universiteit.', page=2)
add('02-het-model', els)

# ---------------------------------------------------------------- 2 waarom
els = title('Waarom') + [
    text(M, 440, 1920 - 2 * M, 300, 'Eerst het probleem.\nDan pas de tool.',
         font=HEAD, size=88, bold=True, ls=1.15)] + foot(page=3)
add('03-waarom', els)

# ---------------------------------------------------------------- 3 voldoet
els = title('Voldoet') + tile(960, 400, 'check', 'green', 200) + [
    text(M, 660, 1920 - 2 * M, 120, 'Alle standaarden, vijf visitatierapporten.',
         font=HEAD, size=56, bold=True)] + foot(
    src='NQA en Hobéon, visitatierapporten Hogeschool Windesheim, 2021-2025. '
        'Standaard 3 Toetsing en standaard 4 Gerealiseerde leerresultaten.', page=4)
add('04-voldoet', els)

# ---------------------------------------------------------------- 4 visitatie
# Per opleiding: wanneer de visitatie was, welk vak, en het scherpste woord
# uit dat rapport. De uitkomst vertelt Dante er zelf bij.
els = title('Visitatie') + [rect(M, 392, 1920 - 2 * M, 4, INK100)]
BEZOEK = [
    ('januari 2021',  'zorg',       'Kwaliteitsverschil',     'Gezondheid, deeltijd'),
    ('november 2021', 'schoolbord', 'Van rubriek naar cijfer', 'Lerarenopleiding Nederlands'),
    ('april 2024',    'microfoon',  'Wijze en omvang',        'Journalistiek'),
    ('november 2024', 'winkel',     'Toelichting leeg',       'Ondernemerschap & Retail'),
]
for cx, (datum, ic, kern, opleiding) in zip(c4, BEZOEK):
    els += [text(cx - w4 / 2, 300, w4, 48, datum, font=HEAD, size=32, bold=True, color=INK500, ls=1.0),
            oval(cx - 12, 382, 24, WHITE, NAVY, 6),
            rect(cx - 2, 406, 4, 46, INK200)]
    els += tile(cx, 460, ic, 'amber')
    els += [text(cx - w4 / 2, 630, w4, 110, kern, font=HEAD, size=46, bold=True, ls=1.1),
            text(cx - w4 / 2, 748, w4, 70, opleiding, size=28, color=INK500, ls=1.25)]
els += foot(quote='“De narratieve feedback is niet altijd helemaal passend bij de rubric.”',
            src='Visitatierapporten NQA en Hobéon. Citaat: NQA, Ad E-commerce, november 2024, p. 24.', page=5)
add('05-visitatie', els)

# ---------------------------------------------------------------- 5 eigen leerroute
BASE, BARW = 780, 160
els = title('Eigen leerroute') + [rect(560, BASE, 800, 3, INK200)]
for i, (v, lab, h, kleur) in enumerate([('900', '2023', 39, INK100),
                                        ('2.700', '2024', 116, INK100),
                                        ('7.000', '2025', 300, GREEN)]):
    x = 600 + i * (BARW + 120)
    els += [rect(x, BASE - h, BARW, h, kleur, r=12),
            text(x - 40, BASE - h - 78, BARW + 80, 70, v, font=HEAD, size=58, bold=True),
            text(x - 40, BASE + 24, BARW + 80, 50, lab, size=32, color=INK500)]
els += [text(M, 320, 1920 - 2 * M, 60, 'studenten in de eigen leerroute, per september',
             size=36, color=INK500)]
els += foot(src='Jaarverantwoording 2025 Hogeschool Windesheim, p. 14 en '
                'Jaarverantwoording 2024, p. 20.', page=6)
add('06-eigen-leerroute', els)

# ---------------------------------------------------------------- 6 krimp
els = title('Krimp')
for cx, (ic, tone, stat, kleur, lab) in zip(c2, [
        ('studenten', 'navy', '-9%', NAVY, 'Studenten'),
        ('docenten', 'amber', '-21%', AMBER, 'Docenten')]):
    els += tile(cx, 380, ic, tone)
    els += [text(cx - w2 / 2, 560, w2, 180, stat, font=HEAD, size=150, bold=True, color=kleur, ls=1.0),
            text(cx - w2 / 2, 730, w2, 70, lab, font=HEAD, size=48, bold=True)]
els += foot(src='Jaarverantwoording Hogeschool Windesheim, meerjarenraming tot 2028. '
                'Onderwijsformatie van 1.302 naar 1.032 fte.', page=7)
add('07-krimp', els)

# ---------------------------------------------------------------- 7 herkenbaar
# Rond de tafel: één tafel, acht stoelen, één stoel groen. Dat is de uitnodiging.
els = title('Herkenbaar?', dark=True)
CX, CY, R, SEAT = 960, 610, 150, 40
els += [oval(CX - R, CY - R, R * 2, NAVY, 'FFFFFF', 4)]
for i in range(8):
    a = math.radians(-90 + i * 45)
    sx, sy = CX + math.cos(a) * 230 - SEAT / 2, CY + math.sin(a) * 230 - SEAT / 2
    groen = (i == 3)
    els += [oval(sx, sy, SEAT, GREEN if groen else NAVY,
                 GREEN if groen else 'FFFFFF', 4)]
els += foot(dark=True, page=8)
add('08-herkenbaar', els, dark=True)

# ---------------------------------------------------------------- 8 feedback
els = title('Feedback')
for cx, (ic, lbl) in zip(c3, [('filepen', 'Schrijfopdrachten'),
                              ('lagen', 'Concept voor concept'),
                              ('usercheck', 'Human in the loop')]):
    els += tile(cx, 380, ic, 'green')
    els += [text(cx - w3 / 2, 570, w3, 130, lbl, font=HEAD, size=46, bold=True, ls=1.1)]
els += [text(M, 726, 400, 36, 'Werkt in', size=24, color=INK500, align='left'),
        pic('assets/brightspace.png', M, 766, 248, 64)]
els += foot(page=9)
add('09-feedback', els)

# ---------------------------------------------------------------- 9 demo
add('10-demo', title('Demo', dark=True) + foot(dark=True, page=10), dark=True)

# ---------------------------------------------------------------- 10 bewijs
els = title('Bewijs') + [pic('assets/bath-spa.png', 900, 254, 120, 120)]
for cx, (stat, lab) in zip(c4, [('435', 'inzendingen'), ('13', 'nakijkers'),
                                ('2-3', 'minuten per review'), ('94%', 'accuraatheid')]):
    els += [text(cx - w4 / 2, 430, w4, 160, stat, font=HEAD, size=130, bold=True, ls=1.0),
            text(cx - w4 / 2, 600, w4, 90, lab, size=34, color=INK500, ls=1.3)]
els += foot(src='Bath Spa University, pilot juni 2026. Accuraatheid is het verschil tussen ons '
                'cijfervoorstel en dat van de docent, geen overeenstemmingspercentage. '
                'Bij docenten die het model hadden afgestemd 98 procent.', page=11)
add('11-bewijs', els)

# ---------------------------------------------------------------- 11 ai act
els = title('AI Act')
for cx, (ic, lbl) in zip(c3, [('lamp', 'Explainability'),
                              ('historie', 'Traceability'),
                              ('aanbieder', 'Human oversight')]):
    els += tile(cx, 390, ic, 'navy')
    els += [text(cx - w3 / 2, 580, w3, 120, lbl, font=HEAD, size=46, bold=True, ls=1.1)]
els += foot(src='EU AI Act, verplichtingen voor hoog-risico toepassingen in het onderwijs.', page=12)
add('12-ai-act', els)

# ---------------------------------------------------------------- 12 twee routes
els = title('Twee routes') + [
    rect(M, 360, w2, 260, INK50, r=32),
    text(M + 48, 424, w2 - 96, 160, 'Een beoordelingsfunctie\nbovenop een algemeen model',
         font=HEAD, size=44, bold=True, color=INK500, ls=1.15),
    rect(M + w2 + 72, 360, w2, 260, TINT_G, r=32),
    text(M + w2 + 120, 424, w2 - 96, 160, 'Een model dat alleen\nbeoordelen doet',
         font=HEAD, size=44, bold=True, ls=1.15),
    text(M + w2 + 72, 680, w2, 70, 'Data   ·   Omvang   ·   Knoppen',
         font=HEAD, size=42, bold=True, color=GREEN_DEEP)]
els += foot(page=13)
add('13-twee-routes', els)

# ---------------------------------------------------------------- 13 vervolg
els = title('Vervolg')
for cx, (ic, lbl) in zip(c3, [('klok', 'Een half uur'),
                              ('cijfers', 'De getallen'),
                              ('pilot', 'Eén opleiding')]):
    els += tile(cx, 390, ic, 'navy')
    els += [text(cx - w3 / 2, 580, w3, 120, lbl, font=HEAD, size=46, bold=True, ls=1.1)]
els += foot(page=14)
add('14-vervolg', els)

# ---------------------------------------------------------------- bouwen
if __name__ == '__main__':
    os.makedirs('preview', exist_ok=True)
    render_pptx([e for _, e, _ in S], 'windesheim-deck-bewerkbaar.pptx')
    for naam, els, dark in S:
        shoot(render_html(els, f'preview/{naam}.html', dark), f'preview/{naam}.png')
    print(f'{len(S)} slides gebouwd')
