"""Board deck Q3 2026 — alle 14 slides. Cover is al goedgekeurd (slide-01-cover.py),
hier opnieuw gedefinieerd zodat de pptx in één keer uit één bron komt."""
from deckbuild import (rect, pic, text, title, cols, render_html, render_pptx, shoot,
                        NAVY, AMBER, GREEN_DEEP, TINT_A, TINT_G, INK50, INK100, INK500, HEAD, BODY, M)
from common import board_foot, LOGO_WIT, LOGO_NAVY


def slide_01_cover():
    els = [rect(0, 0, 1920, 1080, NAVY)]
    els += title('Board Update — Q3 2026', dark=True)
    els += [text(M, 232, 1680, 60, 'ROM  ·  Tjarko Kwee  ·  Imec',
                 font=BODY, size=40, color='FFFFFFB3', align='left')]
    els += [pic(LOGO_WIT, M, 928, 214, 58)]
    return els


def slide_02_agenda():
    els = title('Update, geen consultatie.')
    items = [
        'Bath Spa: het nieuws',
        'Waar we nu staan — financiën, pipeline, key accounts',
        'Van publiek naar privaat',
        'Hoe we tractie genereren',
        'Milestones tot de volgende board',
        'Vragen',
    ]
    y, row_h = 270, 92
    for i, label in enumerate(items, start=1):
        cy = y + (i - 1) * row_h
        els += [rect(M, cy, 56, 56, TINT_A, r=14)]
        els += [text(M, cy + 4, 56, 48, str(i), font=HEAD, size=28, bold=True, color=AMBER, align='center')]
        els += [text(M + 80, cy + 4, 1500, 50, label, font=BODY, size=34, color=NAVY, align='left')]
    els += board_foot(src='Board meeting Q3 2026.', page=2)
    return els


def slide_03_bathspa():
    els = title('Bath Spa stopt')
    bullets = [
        'Pilot afgerond: succescriteria maar deels gehaald, oordeel van hun AI Programme Board.',
        'Reden is institutionele AI-gereedheid en governance, niet onze productkwaliteit.',
        'Geen vervolg "at this stage" — pilotfee van £3.280 incl. btw volgt nog.',
    ]
    y, row_h = 300, 150
    for b in bullets:
        els += [rect(M, y + 14, 14, 14, AMBER, r=7)]
        els += [text(M + 50, y, 1500, 130, b, font=BODY, size=38, color=NAVY, align='left', ls=1.35)]
        y += row_h
    els += board_foot(src='Mail Helen King, Bath Spa University, 21-09-2026.', page=3)
    return els


def slide_04_financien():
    els = title('Runway: 3,5 maanden')
    els += [text(M, 235, 1680, 50,
                 'Cash in bank €51.000 · tot half januari 2027 · nieuwe tranche nodig in december',
                 font=BODY, size=32, color=INK500, align='left')]
    rows = [
        ('Salarissen', '6.447,57', '42,7%'),
        ('Management fees (excl. btw)', '3.400,00', '22,5%'),
        ('Loonheffing', '1.820,00', '12,1%'),
        ('Huisvesting', '1.383,03', '9,2%'),
        ('Overig (7 posten)', '2.034,20', '13,5%'),
    ]
    y0 = 330
    els += [text(M, y0, 900, 40, 'Post', font=BODY, size=24, bold=True, color=INK500, align='left')]
    els += [text(1250, y0, 260, 40, 'Per maand', font=BODY, size=24, bold=True, color=INK500, align='right')]
    els += [text(1560, y0, 220, 40, '%', font=BODY, size=24, bold=True, color=INK500, align='right')]
    els += [rect(M, y0 + 48, 1920 - 2 * M, 2, INK100)]
    y, rh = y0 + 68, 62
    for label, bedrag, pct in rows:
        els += [text(M, y, 1100, 50, label, font=BODY, size=32, color=NAVY, align='left')]
        els += [text(1250, y, 260, 50, bedrag, font=BODY, size=32, color=NAVY, align='right')]
        els += [text(1560, y, 220, 50, pct, font=BODY, size=32, color=NAVY, align='right')]
        y += rh
    els += [rect(M, y + 2, 1920 - 2 * M, 2, NAVY)]
    y += 22
    els += [text(M, y, 1100, 50, 'Totaal', font=BODY, size=32, bold=True, color=NAVY, align='left')]
    els += [text(1250, y, 260, 50, '15.084,80', font=BODY, size=32, bold=True, color=NAVY, align='right')]
    els += [text(1560, y, 220, 50, '100%', font=BODY, size=32, bold=True, color=NAVY, align='right')]
    els += board_foot(src='Eduface financieel model, Q3 board knowledge doc, sep 2026.', page=4)
    return els


def slide_05_pipeline():
    els = title('De pijplijn draait op privé')
    chip_w = 780
    els += [rect(M, 250, chip_w, 110, TINT_G, r=20)]
    els += [text(M + 40, 268, 200, 60, '69%', font=HEAD, size=44, bold=True, color=GREEN_DEEP, align='left')]
    els += [text(M + 240, 280, chip_w - 280, 60, 'van de gewogen pipeline is particulier',
                 font=BODY, size=25, color=GREEN_DEEP, align='left', ls=1.2)]
    x2 = M + chip_w + 40
    els += [rect(x2, 250, chip_w, 110, INK50, r=20)]
    els += [text(x2 + 40, 268, 220, 60, '30,5%', font=HEAD, size=44, bold=True, color=INK500, align='left')]
    els += [text(x2 + 260, 280, chip_w - 300, 60, 'is publiek bekostigd',
                 font=BODY, size=25, color=INK500, align='left', ls=1.2)]
    rows = [
        ('UTI', '€400.000', '50%'), ('BPP', '€400.000', '10%'),
        ('Rijksuniversiteit Groningen', '€300.000', '20%'), ('UADE', '€250.000', '20%'),
        ('Windesheim', '€200.000', '10%'), ('Bristol University', '€200.000', '10%'),
        ('Concorde Career College', '€200.000', '15%'), ('12 overige deals', '€207.500', '—'),
    ]
    y0 = 420
    els += [text(M, y0, 900, 36, 'Instelling', font=BODY, size=22, bold=True, color=INK500, align='left')]
    els += [text(1350, y0, 220, 36, 'Dealsize', font=BODY, size=22, bold=True, color=INK500, align='right')]
    els += [text(1600, y0, 200, 36, 'Kans', font=BODY, size=22, bold=True, color=INK500, align='right')]
    els += [rect(M, y0 + 42, 1920 - 2 * M, 2, INK100)]
    y, rh = y0 + 58, 44
    for label, bedrag, pct in rows:
        els += [text(M, y, 1300, 38, label, font=BODY, size=27, color=NAVY, align='left')]
        els += [text(1350, y, 220, 38, bedrag, font=BODY, size=27, color=NAVY, align='right')]
        els += [text(1600, y, 200, 38, pct, font=BODY, size=27, color=NAVY, align='right')]
        y += rh
    els += board_foot(src='Q3 board knowledge doc, sep 2026. Volledige lijst van 19 deals in Close (zie B4, open-vragen.md).', page=5)
    return els


def _key_accounts_slide(kop, data, page):
    els = title(kop)
    xs, w = cols(2)
    y0 = 270
    for cx, (name, lines, next_step) in zip(xs, data):
        x = cx - w / 2
        els += [text(x, y0, w, 60, name, font=HEAD, size=38, bold=True, color=NAVY, align='left')]
        ly = y0 + 90
        for line in lines:
            els += [text(x, ly, w, 90, line, font=BODY, size=28, color=INK500, align='left', ls=1.35)]
            ly += 110
        els += [rect(x, ly + 16, w, 2, INK100)]
        els += [text(x, ly + 40, w, 100, next_step, font=BODY, size=29, bold=True, color=NAVY, align='left', ls=1.3)]
    els += board_foot(src='Close, geverifieerd 23-09-2026.', page=page)
    return els


def slide_06_keyaccounts1():
    return _key_accounts_slide('Twee publieke accounts', [
        ('Haagse Hogeschool', [
            'Piet en Mario willen door, Theo adviseerde de tool voor het hele jaar te kopen.',
            'Lectoraat neutraal, wil wel verder.',
        ], 'Evaluatiemeeting 2 okt — mogelijk Go Live Plan.'),
        ('Hogeschool Rotterdam', [
            'Business case en voorstel goedgekeurd, procurement gestart.',
            'IT staat geen Brightspace-integratie toe voor één opleiding.',
        ], 'Gesprek met IT over de integratiescope.'),
    ], 6)


def slide_07_keyaccounts2():
    return _key_accounts_slide('Van test naar contract', [
        ('Breederode Hogeschool', [
            'Testochtend 23 sep. Zelfde dag al: concept licentieovereenkomst gestuurd.',
            'Irma en Marcel keken hem na, kwamen terug met kleine wijzigingen.',
        ], 'Wijzigingen verwerken, overeenkomst afronden.'),
        ('UTI', [
            'Technische validatie rond: Canvas- en Blackboard-quizzes, Discussions.',
            'Business case (instructeursverloop, retentie) in opbouw.',
        ], 'Demo voor campus leadership, 25 sep.'),
    ], 7)


def slide_08_patroon():
    els = title('Publiek: traag en onzeker')
    bullets = [
        'Pilots van 6 maanden, met moeite bijeengesprokkeld budget.',
        'Lastig committeren aan een vervolgstap, ook als we de succesfactoren halen.',
        'Trage besluitvorming, in commissies.',
        'Pijn is moeilijk te kwantificeren — dus is ons prijspunt moeilijk te verdedigen.',
    ]
    y, row_h = 300, 135
    for b in bullets:
        els += [rect(M, y + 14, 14, 14, AMBER, r=7)]
        els += [text(M + 50, y, 1650, 110, b, font=BODY, size=36, color=NAVY, align='left', ls=1.35)]
        y += row_h
    els += board_foot(src='Patroon over de actieve publieke deals, sep 2026.', page=8)
    return els


def slide_09_beslissing():
    els = [rect(0, 0, 1920, 1080, NAVY)]
    els += [text(M, 410, 1920 - 2 * M, 220,
                 'Dus focussen we volledig op particuliere instellingen.',
                 font=HEAD, size=74, bold=True, color='FFFFFF', align='center', ls=1.2)]
    els += [text(M, 660, 1920 - 2 * M, 60,
                 'Sneller besluit, meer budget, kleinere implementatie.',
                 font=BODY, size=34, color='FFFFFFB3', align='center')]
    return els


def slide_10_markt():
    els = [text(M, 260, 1920 - 2 * M, 220, '€28 mln', font=HEAD, size=170, bold=True, color=NAVY, align='center')]
    els += [text(M, 490, 1920 - 2 * M, 60, 'ARR-potentie particulier onderwijs, Europa excl. Turkije',
                 font=BODY, size=36, color=INK500, align='center')]
    els += board_foot(
        src='Interne eerste inschatting o.b.v. Eurostat 2023, niet extern gevalideerd. '
            'NL €1,0 mln · VK-apprenticeships 761.480 lerenden, 1.305 providers.', page=10)
    return els


def slide_11_product():
    els = title('Feedback, in jouw toon')
    els += [text(M, 235, 1680, 90,
                 'Grootste uitdaging was de feedbacktoon laten klinken als de docent zelf. Dat is nu eenvoudig geworden.',
                 font=BODY, size=32, color=INK500, align='left', ls=1.3)]
    img_h = 430
    img_w = int(img_h * (2048 / 1116))
    img_x = (1920 - img_w) / 2
    els += [rect(img_x - 4, 356 - 4, img_w + 8, img_h + 8, INK100, r=12)]
    els += [pic('assets/feedback-style-screenshot.png', img_x, 356, img_w, img_h)]
    els += board_foot(src='Product-UI, sep 2026.', page=11)
    return els


def slide_12_gtm():
    els = title('Van beurzen naar bellen')
    xs, w = cols(2)
    x0, x1 = xs[0] - w / 2, xs[1] - w / 2
    els += [text(x0, 260, w, 50, 'TOEN', font=BODY, size=26, bold=True, color=INK500, align='left')]
    els += [text(x0, 320, w, 140, 'Introducties, dure beurzen en evenementen, webinars.',
                 font=BODY, size=34, color=NAVY, align='left', ls=1.35)]
    els += [rect(x0, 500, w, 2, INK100)]
    els += [text(x0, 540, w, 200, 'Eén-op-één, duur per lead, niet herhaalbaar zonder het volgende evenement.',
                 font=BODY, size=28, color=INK500, align='left', ls=1.4)]

    els += [text(x1, 260, w, 50, 'NU', font=BODY, size=26, bold=True, color=GREEN_DEEP, align='left')]
    els += [text(x1, 320, w, 140, 'LinkedIn-berichten → mail → warm bellen. De SHIFT-pijplijn.',
                 font=BODY, size=34, color=NAVY, align='left', ls=1.35)]
    els += [rect(x1, 500, w, 2, INK100)]
    els += [text(x1, 540, w, 60, '466', font=HEAD, size=52, bold=True, color=GREEN_DEEP, align='left')]
    els += [text(x1, 604, w, 50, 'organisaties gescreend, 340 contactpersonen', font=BODY, size=25,
                 color=INK500, align='left', ls=1.3)]

    els += [text(960 - 40, 300, 80, 100, '→', font=HEAD, size=64, bold=True, color=AMBER, align='center')]
    els += board_foot(src='SHIFT-pijplijn, sinds vorige board meeting.', page=12)
    return els


def slide_13_milestones():
    els = title('Op weg naar de tranche')
    rows = [
        ('1', '2 betaalde UK-pilots via Jisc/CHEST, elk ≥ £4.000', 'Kandidaten: Bristol, Goldsmiths'),
        ('2', '1 institutionele licentie ≥ €40.000/jaar', 'UTI'),
        ('3', '1 institutionele licentie ≥ €10.000/jaar',
         'Breederode · Hogeschool Rotterdam · Haagse Hogeschool'),
    ]
    y, row_h = 280, 190
    for num, cond, cand in rows:
        els += [rect(M, y, 64, 64, TINT_A, r=16)]
        els += [text(M, y + 6, 64, 52, num, font=HEAD, size=34, bold=True, color=AMBER, align='center')]
        els += [text(M + 90, y, 1500, 60, cond, font=BODY, size=34, color=NAVY, align='left', ls=1.3)]
        els += [text(M + 90, y + 66, 1500, 60, cand, font=BODY, size=28, bold=True, color=GREEN_DEEP, align='left')]
        y += row_h
    els += board_foot(
        src='CLA-tranche milestones, Q3 board knowledge doc. Koppeling aan deals is een voorstel, nog te bevestigen.',
        page=13)
    return els


def slide_14_vragen():
    els = [rect(0, 0, 1920, 1080, NAVY)]
    els += [text(M, 460, 1920 - 2 * M, 160, 'Wat willen jullie weten?',
                 font=HEAD, size=88, bold=True, color='FFFFFF', align='center')]
    els += [pic(LOGO_WIT, M, 928, 214, 58)]
    return els


SLIDES = [
    ('01-cover', slide_01_cover), ('02-agenda', slide_02_agenda), ('03-bathspa', slide_03_bathspa),
    ('04-financien', slide_04_financien), ('05-pipeline', slide_05_pipeline),
    ('06-keyaccounts1', slide_06_keyaccounts1), ('07-keyaccounts2', slide_07_keyaccounts2),
    ('08-patroon', slide_08_patroon), ('09-beslissing', slide_09_beslissing),
    ('10-markt', slide_10_markt), ('11-product', slide_11_product), ('12-gtm', slide_12_gtm),
    ('13-milestones', slide_13_milestones), ('14-vragen', slide_14_vragen),
]

if __name__ == '__main__':
    all_els = []
    for name, fn in SLIDES:
        els = fn()
        all_els.append(els)
        shoot(render_html(els, f'preview/{name}.html'), f'preview/{name}.png')
        print('gerenderd:', name)
    render_pptx(all_els, 'eduface-board-q3-2026-bewerkbaar.pptx')
    print('pptx klaar:', len(all_els), 'slides')
