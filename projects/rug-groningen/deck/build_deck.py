"""RUG-deck, skeleton overgenomen van het écht gepresenteerde Windesheim-deck
(PDF 'Windesheim_presentaties_2.pdf', 14 sep 2026 — 11 slides, niet de
14-slide build-script-versie in projects/windesheim/deck/). Content vervangen
door RUG-materiaal uit projects/rug-groningen/.

Productcategorie: Exam Grader — nakijken van OPEN VRAGEN, geen schrijfopdrachten.

Eén slide is een 1-op-1 hergebruikte, echte afbeelding uit dat PDF (niet
Windesheim-specifiek): de datalek-krantenkoppen. De webinar-screenshot-slide
uit de PDF is er op Dantes verzoek uitgehaald; in die plek staat nu de kale
Demo-titelslide uit het Windesheim-script.

Render eerst naar PNG (preview), pas na akkoord naar bewerkbare pptx.
"""
import os
from deckbuild import (rect, oval, pic, text, cols, title, tile, foot,
                        full_bleed, render_html, render_pptx, shoot,
                        NAVY, AMBER, GREEN, GREEN_DEEP, TINT_A, TINT_G,
                        INK50, INK100, INK200, INK500, WHITE, HEAD, BODY, M)

SLIDES = []  # (naam, elementen, dark)

def add(name, els, dark=False):
    SLIDES.append((name, els, dark))


# ---------------------------------------------------------------- 1. Titel
els = []
card_w, card_h = 900, 220
card_x, card_y = (1920 - card_w) / 2, 460
els.append(rect(card_x, card_y, card_w, card_h, WHITE, r=28))
els.append(pic('logo_navy.png', card_x + 60, card_y + card_h / 2 - 27, 200, 54))
sep_x = card_x + 60 + 200 + 50
els.append(rect(sep_x, card_y + 44, 1, card_h - 88, INK200))
els.append(text(sep_x + 36, card_y + card_h / 2 - 42, card_w - (sep_x + 36 - card_x) - 40, 84,
                 'Rijksuniversiteit\nGroningen', font=HEAD, size=30, bold=True,
                 color=NAVY, align='left', ls=1.15))
els.append(text(0, card_y + card_h + 56, 1920, 50,
                 'AI-nakijken van open vragen  ·  21 september 2026', size=32, color='8FA9B4', align='center'))
els.append(text(0, card_y + card_h + 104, 1920, 40,
                 'Dante Torbed en Jeroen van Gessel, Eduface', size=22, color='5B7480', align='center'))
add('01-titel', els, dark=True)


# ---------------------------------------------------------- 2. Waarschuwing
# Hergebruikte, echte krantenkoppen (HAN-datalek, Fontys, algemene waarschuwing)
# uit het daadwerkelijk gebruikte Windesheim-deck. Niet instelling-specifiek,
# dus 1-op-1 herbruikbaar als bewijs voor de RUG-situatie.
add('02-waarschuwing', full_bleed('assets/waarschuwing-datalek.png'), dark=True)


# ----------------------------------------------------------- 3. Het model
els = title('Het model')
els.append(text(0, 232, 1920, 50, 'Per vakgebied apart getraind', size=34, color=INK500, align='center'))
labels = [('weegschaal', 'Recht'), ('trend', 'Economie'), ('groep', 'Sociale\nwetenschappen'),
          ('kolf', 'Techniek'), ('boek', 'Geestes-\nwetenschappen'), ('zorg', 'Gezondheid')]
xs, w = cols(6)
for cx, (icon, label) in zip(xs, labels):
    els.append(rect(cx - w / 2, 330, w, 210, INK50, r=18))
    els += tile(cx, 330 + 24, icon, tone='navy', size=110)
    els.append(text(cx - w / 2 + 16, 330 + 150, w - 32, 50, label, size=27, bold=True, color=NAVY, ls=1.15))
els.append(rect(M, 600, 1920 - 2 * M, 190, NAVY, r=18))
els.append(text(160, 626, 400, 34, 'FUNDAMENT', size=22, bold=True, color=GREEN, align='left'))
els.append(rect(160, 672, 780, 78, GREEN, r=16))
els.append(text(160, 696, 780, 40, '250.000+ datapunten', size=30, bold=True, color=NAVY))
els.append(rect(980, 672, 780, 78, GREEN, r=16))
els.append(text(980, 696, 780, 40, 'Didactiek en onderwijskunde', size=30, bold=True, color=NAVY))
els.append(text(0, 826, 1920, 34, 'Gebouwd met', size=22, color=INK500, align='center'))
els.append(pic('assets/leiden.png', 640, 862, 220, 70))
els.append(pic('assets/radboud.png', 1060, 862, 220, 70))
add('03-het-model', els)


# ------------------------------------------------------------- 4. Feedback
els = title('Feedback')
tiles = [('filepen', 'Open vragen'),
         ('lagen', 'Formatief'),
         ('usercheck', 'Human in the loop +\nconsistentie')]
xs, w = cols(3)
for cx, (icon, label) in zip(xs, tiles):
    els += tile(cx, 420, icon, tone='green', size=148)
    els.append(text(cx - w / 2, 600, w, 90, label, font=HEAD, size=34, bold=True, color=NAVY, ls=1.25))
els.append(text(120, 760, 300, 34, 'Werkt in', size=24, color=INK500, align='left'))
els.append(pic('assets/brightspace.png', 120, 796, 280, 60))
els += foot(page=4)
add('04-feedback', els)


# ---------------------------------------------------------- 5. Consistentie
els = title('Consistentie')
els.append(rect(120, 260, 1680, 560, INK50, r=22))
els.append(text(160, 296, 900, 40, 'Modelnauwkeurigheid per beoordelaar', size=30, bold=True, color=NAVY, align='left'))
els.append(text(160, 340, 900, 34, 'Hoe dicht elke beoordelaar bij het voorstel bleef', size=22, color=INK500, align='left'))
rows = [('Beoordelaar A', 98, 'Excellent', GREEN_DEEP), ('Beoordelaar B', 94, 'Excellent', GREEN_DEEP),
        ('Beoordelaar C', 87, 'Wisselend', AMBER), ('Beoordelaar D', 79, 'Wisselend', AMBER),
        ('Beoordelaar E', 71, 'Wijkt af', AMBER), ('Beoordelaar F', 66, 'Wijkt af', AMBER)]
y0 = 404
for i, (name, pct, label, color) in enumerate(rows):
    y = y0 + i * 66
    els.append(text(160, y, 260, 40, name, size=24, bold=True, color=NAVY, align='left'))
    bar_x, bar_w = 440, 780
    els.append(rect(bar_x, y + 6, bar_w, 26, INK100, r=13))
    els.append(rect(bar_x, y + 6, bar_w * pct / 100, 26, color, r=13))
    els.append(text(bar_x + bar_w + 20, y, 100, 40, f'{pct}%', size=26, bold=True, color=NAVY, align='left'))
    els.append(rect(bar_x + bar_w + 140, y + 2, 190, 34, TINT_G if color == GREEN_DEEP else TINT_A, r=17))
    els.append(text(bar_x + bar_w + 140, y + 8, 190, 26, label, size=20, color=(GREEN_DEEP if color == GREEN_DEEP else AMBER)))
els.append(text(120, 852, 1680, 32,
                 'Voorbeeld met fictieve data, ter illustratie van wat een consistentie-dashboard laat zien — geen RUG- of gemeten Eduface-cijfers.',
                 size=19, color=INK500, align='left'))
add('05-consistentie', els)


# ------------------------------------------------------- 6. Vacaturestop
els = title('Vacaturestop')
els += tile(960, 300, 'klok', tone='amber', size=148)
els.append(text(0, 500, 1920, 170, '9 maart\n2026', font=HEAD, size=110, bold=True, color=AMBER, ls=1.0))
els.append(text(0, 700, 1920, 50, 'Geen nieuwe externe inhuur meer toegestaan, op een paar uitzonderingen na',
                 size=30, color=NAVY, align='center'))
els += foot(src='UKrant / OOG, maart 2026. Uitzonderingen: kritieke functies met CvB-goedkeuring, en procedures die al vóór 9 maart liepen.',
            page=6)
add('06-vacaturestop', els)


# --------------------------------------------------------------- 7. Demo
# Kale titelslide, 1-op-1 uit het Windesheim-script — vervangt op Dantes
# verzoek de webinar-screenshot-slide die in de echte PDF stond.
add('07-demo', title('Demo', dark=True) + foot(dark=True, page=7), dark=True)


# ----------------------------------------------------------- 8. Aanzetten
els = title('Aanzetten')
els.append(rect(120, 300, 780, 460, INK50, r=20))
els.append(rect(120, 300, 780, 70, INK100, r=20))
els.append(oval(150, 328, 14, 'E05A4F', 'E05A4F', 0))
els.append(text(200, 320, 300, 30, 'D2L Brightspace', font=HEAD, size=22, bold=True, color=NAVY, align='left'))
rows = ['Course slides', 'Assessment brief', 'Rubric', 'Studentenhandboek']
for i, r in enumerate(rows):
    y = 400 + i * 82
    els.append(rect(150, y, 720, 60, WHITE, r=14))
    els.append(text(174, y + 14, 300, 34, r, size=24, bold=True, color=NAVY, align='left'))
    els.append(rect(700, y + 12, 140, 36, TINT_G, r=18))
    els.append(text(700, y + 18, 140, 26, 'gesynct', size=18, color=GREEN_DEEP))
els.append(rect(940, 480, 140, 100, GREEN, r=20))
els.append(text(940, 512, 140, 40, 'Sync', font=HEAD, size=30, bold=True, color=NAVY))
els.append(rect(1120, 300, 680, 460, NAVY, r=20))
els.append(text(1160, 330, 400, 40, 'Eduface', font=HEAD, size=32, bold=True, color=WHITE, align='left'))
els.append(rect(1560, 330, 200, 44, GREEN, r=22))
els.append(text(1560, 340, 200, 28, 'Alle courses klaar', size=17, bold=True, color=NAVY))
steps = ['Leest het vak', 'Bouwt de instructies', 'Vult aan met domeinkennis']
for i, s in enumerate(steps):
    y = 420 + i * 90
    els.append(oval(1160, y, 44, GREEN, GREEN, 0))
    els.append(text(1160, y + 8, 44, 30, str(i + 1), font=HEAD, size=26, bold=True, color=NAVY))
    els.append(text(1220, y + 4, 540, 40, s, size=26, bold=True, color=WHITE, align='left'))
els.append(text(0, 800, 1920, 50, 'De docent zet niets op.', font=HEAD, size=40, bold=True, color=NAVY, align='center'))
els += foot(page=8)
add('08-aanzetten', els)


# --------------------------------------------------------------- 9. AI Act
els = title('AI Act')
tiles = [('lamp', 'Explainability &\nTraceability'), ('aanbieder', 'Human oversight')]
xs, w = cols(2)
for cx, (icon, label) in zip(xs, tiles):
    els += tile(cx, 420, icon, tone='navy', size=148)
    els.append(text(cx - w / 2, 600, w, 90, label, font=HEAD, size=34, bold=True, color=NAVY, ls=1.25))
els += foot(src=('EU AI Act: assessment-AI = hoog-risico (Annex III), verplichtingen vanaf 2 aug 2026. '
                  "RUG's eigen AI-beleid (dec 2023): Rule 6 verwerkersovereenkomst + AVG, Rule 8 human-in-the-loop verplicht — Eduface voldoet 1-op-1."),
            page=9)
add('09-ai-act', els)


# ------------------------------------------------------ 10. Vergelijkbare dataset
els = title('Vergelijkbare dataset')
els.append(rect(120, 260, 860, 460, TINT_A, r=22))
els.append(text(160, 296, 500, 40, 'Algemeen model', font=HEAD, size=30, bold=True, color=AMBER, align='left'))
mini = [('kar', 'Boodschappen'), ('pan', 'Recept'), ('vliegtuig', 'Vakantie'),
        ('mail', 'Mail'), ('code', 'Code'), ('globe', 'Vertalen')]
mx0, my0 = 160, 370
for i, (icon, label) in enumerate(mini):
    cx = mx0 + (i % 3) * 240 + 90
    cy = my0 + (i // 3) * 170
    els.append(rect(cx - 90, cy, 180, 130, WHITE, r=14))
    els.append(pic(f'assets/icon-{icon}-navy.png', cx - 20, cy + 14, 40, 40))
    els.append(text(cx - 90, cy + 70, 180, 40, label, size=18, color=INK500))
els.append(text(160, 676, 700, 34, 'en duizend andere dingen', size=22, color=AMBER, align='left'))
els.append(rect(1020, 260, 780, 460, TINT_G, r=22))
els.append(text(1060, 296, 500, 40, 'Ons model', font=HEAD, size=30, bold=True, color=GREEN_DEEP, align='left'))
els += tile(1410, 400, 'filepen', tone='green', size=140)
els.append(text(1060, 560, 700, 90, 'Nakijken van\nopen vragen', font=HEAD, size=30, bold=True, color=NAVY, ls=1.25))
els.append(rect(120, 780, 6, 80, GREEN))
els.append(text(150, 780, 1650, 50,
                 '"Datasets voor training, validatie en tests zijn relevant, voldoende representatief, en zoveel mogelijk foutenvrij en volledig met het oog op het beoogde doel."',
                 size=24, color=NAVY, align='left', ls=1.3))
els.append(text(150, 838, 1650, 30, 'EU AI Act, verordening 2024/1689, artikel 10 lid 3', size=19, color=INK500, align='left'))
add('10-vergelijkbare-dataset', els)


# ------------------------------------------------------ 11. Zelf bouwen of Eduface
els = title('Zelf bouwen of Eduface')
els.append(rect(120, 250, 1680, 330, INK50, r=20))
pts = [
    ('UG Grader is handmatig', 'Geen AI-feedback. Het nakijken van open vragen blijft volledig bij de docent.'),
    ('Zelf bouwen = nieuw product', '€350.000–500.000/jaar en 12-18 maanden (schatting), plus de volledige EU AI Act-last — midden in een €45M-bezuiniging.'),
    ('Eduface: bewezen, direct', 'RUG koopt al extern in waar dat sneller is (FeedbackFruits) — buy is geen taboe.'),
]
for i, (h, p) in enumerate(pts):
    y = 280 + i * 100
    els.append(oval(160, y + 6, 16, GREEN, GREEN, 0))
    els.append(text(200, y - 6, 500, 36, h, font=HEAD, size=25, bold=True, color=NAVY, align='left'))
    els.append(text(720, y - 6, 1040, 60, p, size=21, color=INK500, align='left', ls=1.3))
els.append(rect(120, 610, 1680, 210, TINT_A, r=20))
els.append(text(160, 632, 900, 32, 'Illustratief voorbeeld — niet een geverifieerde klantcase', size=19, bold=True, color=AMBER, align='left'))
els.append(text(160, 668, 900, 30, '"Een instelling bouwde zelf een AI-feedbacktool"', size=22, bold=True, color=NAVY, align='left'))
case_pts = ['Onderhoud slokte alles op', 'De workflow liep vast', 'Geen ruimte voor innovatie', 'Alsnog afhankelijk van Big Tech']
xs, w = cols(4)
for i, (cx, p) in enumerate(zip(xs, case_pts)):
    els.append(text(cx - w / 2, 710, w, 80, p, size=19, bold=True, color=NAVY, ls=1.25))
els += foot(page=11)
add('11-zelf-bouwen', els)


# --------------------------------------------------------------------- build
if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)
    prev_dir = os.path.join(base, 'preview')
    os.makedirs(prev_dir, exist_ok=True)
    pptx_slides = []
    for i, (name, els, dark) in enumerate(SLIDES, 1):
        html_path = os.path.join(prev_dir, f'{name}.html')
        png_path = os.path.join(prev_dir, f'{name}.png')
        render_html(els, html_path, dark=dark, prefix='../')
        shoot(html_path, png_path)
        pptx_slides.append(els)
        print(f'{i:02d}. {name} -> {png_path}')
    render_pptx(pptx_slides, os.path.join(base, 'rug-deck-bewerkbaar.pptx'))
    print('PPTX:', os.path.join(base, 'rug-deck-bewerkbaar.pptx'))
