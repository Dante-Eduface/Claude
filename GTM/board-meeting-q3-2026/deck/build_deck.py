"""Board deck Q3 2026 — v2, board-memo stijl.
Feedback van Jeroen: titels = de echte agendapunten/sectienamen, niet een bedachte
claim. En veel meer inhoud per slide: dit wordt gelezen en nageslagen, niet vanaf
een podium gepresenteerd. Zie .claude/skills/pitch-deck/reference.md voor waarom
dat een andere stijl is dan de pitch-deck-skill standaard aanhoudt."""
from deckbuild import (rect, pic, text, cols, render_html, render_pptx, shoot,
                        NAVY, AMBER, GREEN_DEEP, TINT_A, TINT_G, INK50, INK100, INK500, HEAD, BODY, M)
from common import board_foot, LOGO_WIT, LOGO_NAVY
from board_helpers import board_title, subline, bullets, table


def slide_01_cover():
    els = [rect(0, 0, 1920, 1080, NAVY)]
    els += [text(M, 88, 1920 - 2 * M, 120, 'Board Update — Q3 2026',
                 font=HEAD, size=96, bold=True, color='FFFFFF', align='center', ls=1.0)]
    els += [text(M, 232, 1680, 60, 'ROM  ·  Tjarko Kwee  ·  Imec',
                 font=BODY, size=40, color='FFFFFFB3', align='left')]
    els += [pic(LOGO_WIT, M, 928, 214, 58)]
    return els


def slide_02_agenda():
    els = board_title('Agenda')
    els += subline('Dit is een update, geen consultatie.')
    items = [
        ('1', 'Bath Spa', 'Het nieuws: waarom de deal stopt en wat dat niet betekent.'),
        ('2', 'Financiën', 'Cash, burn, runway en de tranche-deadline.'),
        ('3', 'Pipeline', 'Alle 19 actieve deals, gewogen, publiek vs. particulier.'),
        ('4', 'Key accounts', 'HHS, Hogeschool Rotterdam, Breederode, UTI.'),
        ('5', 'Het patroon', 'Waarom publieke deals vastlopen.'),
        ('6', 'De Beslissing', 'Volledige focus op particuliere instellingen, en de markt erachter.'),
        ('7', 'Het product', 'Wat er dit kwartaal is bijgebouwd.'),
        ('8', 'GTM', 'De nieuwe aanpak, van beurzen naar SHIFT.'),
        ('9', 'Milestones', 'De drie voorwaarden voor de volgende CLA-tranche.'),
        ('10', 'Vragen', ''),
    ]
    y, row_h = 250, 63
    for num, kop, sub in items:
        els += [text(M, y, 50, 40, num, font=HEAD, size=24, bold=True, color=AMBER, align='left')]
        els += [text(M + 60, y, 380, 40, kop, font=HEAD, size=26, bold=True, color=NAVY, align='left')]
        els += [text(M + 460, y + 2, 1300, 40, sub, font=BODY, size=23, color=INK500, align='left')]
        y += row_h
    els += board_foot(src='Board meeting Q3 2026.', page=2)
    return els


def slide_03_bathspa():
    els = board_title('Bath Spa')
    els += subline('Ze gaan niet door met Eduface. Reden: institutionele AI-gereedheid, niet productkwaliteit.')
    y = 230
    els += bullets([
        'Susanna heeft de pilotdata verzameld en geanalyseerd: Eduface-gebruiksstatistieken, interviews en surveys onder deelnemers.',
        'Een samenvattend rapport is vorige week besproken door hun AI Programme Board (AIPB).',
        'Hun conclusie, letterlijk: "we found that the measures of success were only partially met."',
        '"We are not yet ready to implement an AI assistant tool for assessment and feedback. We won’t be proceeding with Eduface, or other similar product, at this stage."',
        'Helen King (Director of Learning Innovation, Development & Skills) was oprecht positief: "It has been good working with you and I wish you all the best for the further development of the Eduface tool."',
    ], M, y, 1680, 92, size=27, dot_color=AMBER, ls=1.3)
    y2 = y + 5 * 92 + 20
    els += [rect(M, y2, 1680, 2, INK100)]
    y2 += 26
    els += bullets([
        ('Financieel: Bath Spa betaalt de afgesproken pilotfee van £3.280 incl. btw. Factuur moet nog verstuurd worden.', NAVY),
        ('Voor ons: de 94% accuraatheidsmeting (435 inzendingen, 13 nakijkers, juni 2026) komt uit deze pilot en blijft feitelijk overeind. Dat cijfer wordt door Bath Spa niet betwist.', GREEN_DEEP),
    ], M, y2, 1680, 60, size=25, ls=1.3)
    els += board_foot(src='Mail Helen King, Bath Spa University, 21-09-2026.', page=3)
    return els


def slide_04_financien():
    els = board_title('Financiën')
    els += subline('Cash in bank €51.000 · runway 3,5 maanden, tot half januari 2027 · nieuwe tranche nodig in december.',
                    color=NAVY, size=27)
    rows = [
        ('Salarissen', '6.447,57', '42,7%'),
        ('Management fees (excl. btw)', '3.400,00', '22,5%'),
        ('Loonheffing', '1.820,00', '12,1%'),
        ('Huisvesting (Dotslash)', '1.383,03', '9,2%'),
        ('Software', '899,11', '6,0%'),
        ('Reiskosten (NS Menno)', '399,95', '2,7%'),
        ('Administratie', '320,86', '2,1%'),
        ('Google Ads (stopgezet)', '182,20', '1,2%'),
        ('Rente pre-seed ELF', '132,24', '0,9%'),
        ('Representatie en attenties', '67,77', '0,4%'),
        ('Bank en verzekering', '32,07', '0,2%'),
        ('Totaal', '15.084,80', '100%'),
    ]
    tbl, _ = table(
        ['Post', 'Per maand', '%'], rows,
        x=M, y=250, col_x=[M, 1300, 1650], col_w=[1100, 300, 170],
        aligns=['left', 'right', 'right'], row_h=44, header_size=21, body_size=26, bold_last=True)
    els += tbl
    els += board_foot(src='Eduface financieel model, Q3 board knowledge doc, sep 2026.', page=4)
    return els


def slide_05_pipeline():
    els = board_title('Pipeline')
    els += subline('€2.157.500 totaal, €489.000 gewogen. 69% van het gewogen bedrag is particulier, 30,5% publiek, 0,5% overig (Noordhoff, uitgever).',
                    size=22)

    # (naam, land, privaat, noot voor twijfelgevallen, in Q3 aangemaakt (True/False/None=onbekend), dealsize, kans)
    rows = [
        ('UTI', 'US', True, None, True, '€400.000', '50%'),
        ('BPP', 'UK', True, None, True, '€400.000', '10%'),
        ('Rijksuniversiteit Groningen', 'NL', False, None, True, '€300.000', '20%'),
        ('UADE', 'AR', True, None, True, '€250.000', '20%'),
        ('Windesheim', 'NL', False, None, True, '€200.000', '10%'),
        ('Bristol University', 'UK', False, None, True, '€200.000', '10%'),
        ('Concorde Career College', 'US', True, None, True, '€200.000', '15%'),
        ('Goldsmiths', 'UK', False, None, True, '€60.000', '30%'),
        ('Haagse Hogeschool', 'NL', False, None, False, '€20.000', '50%'),
        ('Breederode Hogeschool', 'NL', True, None, True, '€20.000', '70%'),
        ('Tilburg University', 'NL', False, None, False, '€20.000', '15%'),
        ('UMCG', 'NL', False, None, False, '€15.000', '50%'),
        ('Radboud Universiteit', 'NL', False, None, False, '€15.000', '15%'),
        ('Hogeschool Rotterdam', 'NL', False, None, False, '€10.000', '85%'),
        ('Notenboom', 'NL', True, None, True, '€10.000', '20%'),
        ('CMI', 'IE', True, None, True, '€10.000', '10%'),
        ('HBMSU', 'AE', False, 'quasi-publiek', True, '€10.000', '10%'),
        ('Noordhoff', '—', False, 'uitgever', True, '€10.000', '10%'),
        ('Academica', 'NL', True, None, True, '€7.500', '10%'),
    ]

    IX, IW = M, 480
    LX, LW = 620, 70
    PX, PW = 710, 130
    QX, QW = 860, 90
    DX, DW = 1350, 230
    KX, KW = 1610, 190

    y0 = 258
    for h, x, w, al in [('Instelling', IX, IW, 'left'), ('Land', LX, LW, 'left'), ('Privaat', PX, PW, 'left'),
                        ('Q3', QX, QW, 'left'), ('Dealsize', DX, DW, 'right'), ('Kans', KX, KW, 'right')]:
        els += [text(x, y0, w, 28, h, font=BODY, size=17, bold=True, color=INK500, align=al)]
    els += [rect(M, y0 + 28, 1680, 2, INK100)]

    y, row_h = y0 + 40, 26
    for name, land, priv, noot, q3, dealsize, kans in rows:
        els += [text(IX, y, IW, 24, name, font=BODY, size=19, color=NAVY, align='left')]
        els += [text(LX, y, LW, 24, land, font=BODY, size=19, color=INK500, align='left')]
        if priv:
            els += [rect(PX, y - 1, 98, 22, TINT_G, r=6)]
            els += [text(PX, y + 1, 98, 18, 'PRIVAAT', font=BODY, size=13, bold=True, color=GREEN_DEEP, align='center')]
        elif noot:
            els += [text(PX, y, PW, 24, noot, font=BODY, size=16, color=INK500, align='left')]
        if q3 is True:
            els += [rect(QX, y - 1, 52, 22, TINT_A, r=6)]
            els += [text(QX, y + 1, 52, 18, 'Q3', font=BODY, size=13, bold=True, color=AMBER, align='center')]
        elif q3 is None:
            els += [text(QX, y, QW, 24, 'n.b.', font=BODY, size=16, color=INK500, align='left')]
        els += [text(DX, y, DW, 24, dealsize, font=BODY, size=19, color=NAVY, align='right')]
        els += [text(KX, y, KW, 24, kans, font=BODY, size=19, color=NAVY, align='right')]
        y += row_h

    els += [rect(M, y - 4, 1680, 2, NAVY)]
    y += 12
    els += [text(IX, y, IW, 26, 'Totaal', font=BODY, size=19, bold=True, color=NAVY, align='left')]
    els += [text(DX, y, DW, 26, '€2.157.500', font=BODY, size=19, bold=True, color=NAVY, align='right')]
    els += [text(KX, y, KW, 26, '€489.000 gewogen', font=BODY, size=16, bold=True, color=NAVY, align='right')]

    els += board_foot(
        src='Q3 board knowledge doc, sep 2026. Afwijkende waarden op enkele regels t.o.v. Close (zie B4, open-vragen.md). '
            'BPP en Concorde staan niet in Close, Q3-aanmaak bevestigd door Jeroen. Aanmaakdatum overige regels uit Close, 24-09-2026.',
        page=5)
    return els


def _key_accounts_slide(kop, sub, accounts, page):
    els = board_title(kop)
    els += subline(sub, size=24)
    xs, w = cols(2)
    y0 = 230
    for cx, (name, meddpicc, next_step) in zip(xs, accounts):
        x = cx - w / 2
        els += [text(x, y0, w, 46, name, font=HEAD, size=34, bold=True, color=NAVY, align='left')]
        y = y0 + 60
        for label, val in meddpicc:
            els += [text(x, y, w, 30, label, font=BODY, size=18, bold=True, color=INK500, align='left')]
            els += [text(x, y + 26, w, 70, val, font=BODY, size=21, color=NAVY, align='left', ls=1.25)]
            y += 26 + 22 * ((len(val) // 62) + 1) + 14
        els += [rect(x, y + 6, w, 2, INK100)]
        els += [text(x, y + 26, w, 30, 'VOLGENDE STAP', font=BODY, size=16, bold=True, color=AMBER, align='left')]
        els += [text(x, y + 52, w, 60, next_step, font=BODY, size=23, bold=True, color=NAVY, align='left', ls=1.25)]
    els += board_foot(src='Close, geverifieerd 23-09-2026.', page=page)
    return els


def slide_06_keyaccounts1():
    return _key_accounts_slide(
        'Key accounts', 'De twee publieke accounts die het dichtst bij een besluit zitten (1/2).', [
            ('Haagse Hogeschool', [
                ('STATUS', 'Theo adviseerde Piet de tool voor het hele jaar te kopen, dan kan het onderzoek een vervolg krijgen. Lectoraat: niet positief, niet negatief, wil wel verder.'),
                ('BETROKKENEN', 'Piet en Mario (opleidingsmanagers IVK), Marcel (lectoraat), Marco (curriculumcommissie, kan Eduface breder trekken dan taalopleidingen). Faculteitsdirecteur Willem tekent uiteindelijk.'),
                ('BUDGET', 'Er is een intern potje voor het inkopen van AI-tools beschikbaar.'),
            ], 'Evaluatiemeeting 2 okt, 14:00-15:00: uitvoering pilot, uitdagingen, onderwijsuitkomsten, analysegegevens lectoraat, vervolgstappen en mogelijk Go Live Plan voor dit studiejaar.'),
            ('Hogeschool Rotterdam', [
                ('STATUS', 'Business case en voorstel goedgekeurd (call met Paul, 16 sep), procurement is gestart. Nick (opleidingsdirecteur) houdt Mark Boot hiervoor verantwoordelijk.'),
                ('BLOKKADE', 'IT staat geen Brightspace-integratie toe voor één losse opleiding. Optie 1: meer opleidingen erbij (duurt lang). Optie 2: standalone werken tot volgend studiejaar.'),
                ('TROEF', 'Aangeven dat de tool breder gebruikt gaat worden en dit een testcasus is; andere opleidingen kunnen een LOI tekenen.'),
            ], 'Mark zet ons aan tafel met Marije/Marijke en Sytse van der Zwan (IT). Concept licentieovereenkomst ligt al klaar.'),
        ], 6)


def slide_07_keyaccounts2():
    return _key_accounts_slide(
        'Key accounts', 'De twee accounts die momenteel het hardst versnellen (2/2).', [
            ('Breederode Hogeschool', [
                ('STATUS', 'Testochtend 23 sep. Dezelfde dag al concept licentieovereenkomst gestuurd (22 sep, vooruitlopend). Irma en Marcel keken hem zorgvuldig na, kwamen 23 sep terug met kleine wijzigingen.'),
                ('SUCCESCRITERIA', 'Boven 92% accuraatheid tegenover het docentcijfer, 3,5 van 5 sterren op gebruiksvriendelijkheid (bevestigd 3 sep).'),
                ('PAD', '2 weken testen op bestaande opdrachten, dan 2 weken itslearning-integratie, dan pilotscope en contract via Marcel (Calder).'),
            ], 'Wijzigingen in de licentieovereenkomst verwerken en afronden.'),
            ('UTI', [
                ('STATUS', 'Technische validatie rond: Canvas-quizzes bevestigd, Blackboard-quizzes bevestigd (al operationeel), Blackboard Discussions ook ondersteund via onze API.'),
                ('BETROKKENEN', 'Robert Jordan (AVP Instructional Design) vroeg de slides om te delen met campus leaders begin oktober. Bas Schotsman (AVP Academic Operations) enthousiast, ziet ook kans in het beoordelen van Discussions.'),
                ('BUSINESS CASE', 'Nog nodig: kosten instructeursverloop, gemiddeld uurloon, gemiddelde retentietijd, aantal actieve en vertrokken instructeurs (12 mnd). Go-Live Plan is een gedeeld Google Doc.'),
            ], 'Demo voor bredere groep campus leadership op 25 sep, daarna richting go/no-go.'),
        ], 7)


def slide_08_patroon():
    els = board_title('Het patroon')
    els += subline('Wat we zien bij elke publieke deal in de pipeline.', size=27)
    y = 230
    els += bullets([
        'Publieke instellingen eisen een pilot van 6 maanden, waarvoor ze met moeite budget bijeensprokkelen.',
        'Ze vinden het lastiger om te committeren aan een duidelijke vervolgstap, ook als we de afgesproken succesfactoren halen.',
        'Beslissingen gaan in commissies die vaak heel lang duren.',
        'We hebben op dit moment vooral moeite met het kwantificeren van pijn, waardoor de waarde van de tool lastiger in te schatten is en het moeilijker is om ons prijspunt te verdedigen.',
    ], M, y, 1680, 96, size=29, dot_color=AMBER, ls=1.3)
    y2 = y + 4 * 96 + 30
    els += [rect(M, y2, 1680, 2, INK100)]
    y2 += 28
    els += [text(M, y2, 200, 34, 'IN DE PRAKTIJK', font=BODY, size=19, bold=True, color=INK500, align='left')]
    els += bullets([
        'RUG: het eigen ontwikkelteam van de universiteit is de concurrent, geen budgethouder in beeld.',
        'Windesheim: aanbestedingsplicht boven €80k, wacht op een hoog-risico-AI-kader dat er nog niet is.',
        'Bath Spa: net gestopt na maanden AIPB-proces, ondanks een positieve pilot.',
    ], M, y2 + 40, 1680, 52, size=24, color=INK500)
    els += board_foot(src='Patroon over de actieve publieke deals, sep 2026.', page=8)
    return els


def slide_09_beslissing():
    els = board_title('De Beslissing')
    els += subline('Volledige focus op particuliere instellingen: for-profit en non-profit, geen staatsgesubsidieerd.',
                    size=27, color=NAVY)
    y = 230
    els += bullets([
        ('Bij private instellingen gaan keuzes een stuk sneller en is er meer budget beschikbaar voor een veel kleinere implementatie.', NAVY),
    ], M, y, 1680, 70, size=29, dot_color=GREEN_DEEP, ls=1.3)
    y2 = y + 90
    els += [rect(M, y2, 1680, 2, INK100)]
    y2 += 30
    els += [text(M, y2, 400, 34, 'DE MARKT ERACHTER', font=BODY, size=19, bold=True, color=INK500, align='left')]
    rows = [
        ('Nederland, hoger onderwijs', '46.000-80.000', '€1,7-2,9 mln'),
        ('VK, hoger onderwijs (AP)', '≥71.050', '≥£2,6 mln'),
        ('VK, apprenticeships (ITP)', '~520.000', '~£18,7 mln'),
        ('VK, franchise-laag', '167.440', '~£6,0 mln'),
        ('Verenigde Staten, particulier', '~4,2 mln', '~$150,8 mln'),
        ('Europa, overig (niet herzien)', '3,6 mln', '~€129,6 mln'),
    ]
    tbl, ty = table(
        ['Markt', 'Omvang', 'ARR-potentie'], rows,
        x=M, y=y2 + 40, col_x=[M, 700, 1400], col_w=[560, 680, 400],
        aligns=['left', 'left', 'right'], row_h=42, header_size=19, body_size=25)
    els += tbl
    els += [text(M, ty + 6, 1680, 60,
                 'Hoger door het juiste prijsmodel (36/jaar, niet 7,88), niet door een grotere markt: NL en VK hoger '
                 'onderwijs kwamen bij hercontrole juist lager uit. 0 particuliere deals gewonnen tot nu toe (Tio, '
                 'ICM, CMS Vocational alle Lost); dit is TAM, geen omzet.',
                 font=BODY, size=19, color=INK500, align='left', ls=1.3)]
    els += board_foot(
        src='Marktomvang herzien 24-09-2026: DUO/NRTO, HESA, NCES, eigen pijplijn. HESA/NCES/Eurostat/DUO waren '
            'geblokkeerd in de sessie, cijfers zijn kruislings gezocht, niet uit brontabellen.',
        page=9)
    return els


def slide_10_product():
    els = board_title('Het product')
    els += subline('Feedback verder configureerbaar gemaakt.', size=27)
    els += bullets([
        'Grootste uitdaging was de feedback kunnen aanpassen naar hoe de docent het zelf zou zeggen. Dat is nu heel makkelijk gemaakt.',
    ], M, 230, 1680, 60, size=27)
    img_h = 480
    img_w = int(img_h * (2048 / 1116))
    img_x = (1920 - img_w) / 2
    img_y = 320
    els += [rect(img_x - 4, img_y - 4, img_w + 8, img_h + 8, INK100, r=12)]
    els += [pic('assets/feedback-style-screenshot.png', img_x, img_y, img_w, img_h)]
    els += board_foot(src='Product-UI, sep 2026.', page=10)
    return els


def slide_11_gtm():
    els = board_title('GTM')
    els += subline('De aanpak is sinds vorige board meeting fundamenteel veranderd.', size=27)
    xs, w = cols(2)
    x0, x1 = xs[0] - w / 2, xs[1] - w / 2
    y0 = 260
    els += [text(x0, y0, w, 40, 'TOEN', font=BODY, size=22, bold=True, color=INK500, align='left')]
    els += bullets([
        'Introducties via het netwerk.',
        'Dure beurzen en evenementen.',
        'Webinars.',
        'Eén-op-één, duur per lead, niet herhaalbaar zonder het volgende evenement.',
    ], x0, y0 + 50, w, 66, size=25, dot_color=INK500)

    els += [text(x1, y0, w, 40, 'NU: DE SHIFT-PIJPLIJN', font=BODY, size=22, bold=True, color=GREEN_DEEP, align='left')]
    els += bullets([
        'LinkedIn-bericht → mail → warm bellen, geautomatiseerd van sourcing tot bericht.',
        '5 stappen: lead sourcing → contact sourcing → onderzoek → outreach → import in Lemlist.',
        '466 organisaties gescreend, 340 contactpersonen, 231 dossiers met bewijscitaat.',
    ], x1, y0 + 50, w, 76, size=25, dot_color=GREEN_DEEP)
    els += [text(960 - 30, y0 + 200, 60, 60, '→', font=HEAD, size=56, bold=True, color=AMBER, align='center')]
    els += board_foot(src='SHIFT-pijplijn, sinds vorige board meeting.', page=11)
    return els


def slide_12_milestones():
    els = board_title('Milestones')
    els += subline('Drie voorwaarden voor de volgende CLA-tranche, nodig in december.', size=27)
    rows = [
        ('1', '2 betaalde pilotovereenkomsten met onafhankelijke HE-instellingen in het VK via Jisc/CHEST, elk ≥ £4.000, met Critical Success Factors richting een volledige institutionele licentie.',
         'Bristol University, Goldsmiths — beide UK, in pipeline, nog geen formele Jisc/CHEST-pilot gestart.'),
        ('2', '1 institutionele licentie, jaarwaarde ≥ €40.000, looptijd ≥ 12 maanden.',
         'UTI — technische validatie rond, demo voor campus leadership 25 sep, business case in opbouw.'),
        ('3', '1 institutionele licentie, waarde ≥ €10.000, looptijd ≥ 12 maanden.',
         'Drie kandidaten tegelijk: Breederode (licentie in onderhandeling), Hogeschool Rotterdam (procurement gestart), Haagse Hogeschool (evaluatiemeeting 2 okt).'),
    ]
    y, row_h = 250, 170
    for num, cond, cand in rows:
        els += [rect(M, y, 50, 50, TINT_A, r=13)]
        els += [text(M, y + 4, 50, 42, num, font=HEAD, size=28, bold=True, color=AMBER, align='center')]
        els += [text(M + 74, y, 1600, 60, cond, font=BODY, size=25, color=NAVY, align='left', ls=1.3)]
        els += [text(M + 74, y + 76, 1600, 60, cand, font=BODY, size=23, bold=True, color=GREEN_DEEP, align='left', ls=1.25)]
        y += row_h
    els += board_foot(
        src='CLA-tranche milestones, Q3 board knowledge doc. Koppeling aan deals is een voorstel, nog te bevestigen.',
        page=12)
    return els


def slide_13_vragen():
    els = [rect(0, 0, 1920, 1080, NAVY)]
    els += [text(M, 460, 1920 - 2 * M, 160, 'Vragen',
                 font=HEAD, size=96, bold=True, color='FFFFFF', align='center')]
    els += [pic(LOGO_WIT, M, 928, 214, 58)]
    return els


SLIDES = [
    ('01-cover', slide_01_cover), ('02-agenda', slide_02_agenda), ('03-bathspa', slide_03_bathspa),
    ('04-financien', slide_04_financien), ('05-pipeline', slide_05_pipeline),
    ('06-keyaccounts1', slide_06_keyaccounts1), ('07-keyaccounts2', slide_07_keyaccounts2),
    ('08-patroon', slide_08_patroon), ('09-beslissing', slide_09_beslissing),
    ('10-product', slide_10_product), ('11-gtm', slide_11_gtm), ('12-milestones', slide_12_milestones),
    ('13-vragen', slide_13_vragen),
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
