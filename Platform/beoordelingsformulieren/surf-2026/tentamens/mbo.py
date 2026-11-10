"""Tentamen micro-economie, MBO niveau 4. Bron voor build.py in deze map.

Elke vraag: nr, punten, onderwerp, vraag (markdown), context (voor de AI-beoordelaar),
antwoord (antwoordmodel), criteria [(naam, punten, alle punten als, deel van de punten als)],
student (de fictieve inzending).
"""

TENTAMEN = {
    "code": "mbo",
    "taal": "nl",
    "titel": "Tentamen micro-economie",
    "niveau": "MBO niveau 4, vak Economie",
    "tijd": "60 minuten",
    "student": "Daan Jansen",
    "studentnummer": "MBO-238471",
    "vragen": [
        {
            "nr": 1, "punten": 2, "onderwerp": "Opofferingskosten",
            "vraag": "Jesse werkt in het weekend bij een supermarkt en verdient €12 per uur. Zaterdag kan hij 6 uur werken, maar hij wil ook naar een festival. Het kaartje van €45 heeft hij al gekocht.\n\na. Leg uit wat opofferingskosten zijn.\n\nb. Bereken de opofferingskosten als Jesse naar het festival gaat.",
            "context": "Deze vraag toetst of de student begrijpt dat opofferingskosten gaan over wat je opgeeft: de opbrengst van het beste alternatief. Het kaartje is al betaald en hoort niet in de berekening. Dat is een bewuste afleider.",
            "antwoord": "a. Opofferingskosten zijn de opbrengst van het beste alternatief dat je laat schieten als je een keuze maakt.\n\nb. Jesse laat 6 × €12 = **€72** loon schieten. Het kaartje van €45 is al betaald en telt niet mee.",
            "criteria": [
                ("Uitleg van het begrip", 1, "De student legt uit dat het gaat om wat je opgeeft, de opbrengst van het beste alternatief.", "0,5 punt: de student noemt alleen 'kosten' of 'geld dat je uitgeeft', zonder dat het om een gemist alternatief gaat."),
                ("Berekening", 1, "€72, zonder het kaartje.", "0,5 punt: juiste methode met een rekenfout, of het kaartje is erbij opgeteld."),
            ],
            "student": "a. Opofferingskosten zijn de kosten die je maakt als je iets gaat doen.\n\nb. 6 x 12 = 72 euro. Plus het kaartje van 45 euro is het 117 euro.",
        },
        {
            "nr": 2, "punten": 2, "onderwerp": "Vraag",
            "vraag": "De benzineprijs stijgt flink. Wat gebeurt er met de vraag naar e-bikes? Leg je antwoord uit.",
            "context": "Deze vraag toetst de invloed van de prijs van een vervangend product op de vraag. Autorijden wordt duurder, dus de e-bike wordt als vervanging aantrekkelijker.",
            "antwoord": "De vraag naar e-bikes **stijgt**. Autorijden wordt duurder door de hogere benzineprijs, dus meer mensen kiezen voor korte ritten de e-bike als vervanging van de auto.",
            "criteria": [
                ("Richting", 1, "De student zegt dat de vraag naar e-bikes stijgt.", "0,5 punt: de student zegt dat er meer e-bikes verkocht worden, maar verwart dat met een hogere prijs van e-bikes."),
                ("Uitleg", 1, "De student koppelt het aan de auto: autorijden wordt duurder, de e-bike is een vervanging.", "0,5 punt: er is een uitleg, maar zonder verband met de auto of benzine."),
            ],
            "student": "De vraag naar e-bikes stijgt, omdat mensen dan liever gaan fietsen dan met de auto rijden want tanken is duurder.",
        },
        {
            "nr": 3, "punten": 3, "onderwerp": "Marktevenwicht",
            "vraag": "In de tabel zie je de vraag en het aanbod van fietslampjes.\n\n| Prijs | Gevraagd (× 1.000 stuks) | Aangeboden (× 1.000 stuks) |\n|---|---|---|\n| €30 | 80 | 20 |\n| €35 | 60 | 30 |\n| €40 | 40 | 40 |\n| €45 | 20 | 50 |\n| €50 | 0 | 60 |\n\na. Wat is de evenwichtsprijs en wat is de evenwichtshoeveelheid?\n\nb. De prijs is €45. Is er dan een overschot of een tekort? Hoe groot is het?",
            "context": "Deze vraag toetst of de student het evenwicht uit een tabel kan aflezen en het verschil kent tussen een overschot en een tekort. Let op de eenheid: de hoeveelheden staan in duizenden.",
            "antwoord": "a. Evenwicht waar gevraagd gelijk is aan aangeboden: prijs **€40**, hoeveelheid **40.000 stuks**.\n\nb. Bij €45 is er een **overschot**: aangeboden 50.000 min gevraagd 20.000 = **30.000 stuks**.",
            "criteria": [
                ("Evenwichtsprijs", 1, "€40.", "0,5 punt: niet van toepassing, het is goed of fout."),
                ("Evenwichtshoeveelheid", 1, "40.000 stuks.", "0,5 punt: de student noemt 40 maar vergeet dat het om duizenden gaat."),
                ("Overschot of tekort", 1, "Een overschot van 30.000 stuks.", "0,5 punt: de juiste grootte maar de student noemt het een tekort, of het woord overschot met een verkeerde grootte."),
            ],
            "student": "a. De evenwichtsprijs is €40 en de hoeveelheid is 40.000 stuks.\n\nb. Bij €45 is er een tekort van 30.000, want mensen willen er dan maar 20.000.",
        },
        {
            "nr": 4, "punten": 2, "onderwerp": "Accijns",
            "vraag": "De overheid verhoogt de accijns op frisdrank met suiker. Wat gebeurt er met de prijs en met de verkochte hoeveelheid frisdrank? Leg uit.",
            "context": "Deze vraag toetst het effect van een belasting op prijs en hoeveelheid. Producenten rekenen de accijns door, de hogere prijs remt de vraag.",
            "antwoord": "De **prijs stijgt**, omdat producenten de accijns doorberekenen aan de klant. Door de hogere prijs kopen mensen minder: de **verkochte hoeveelheid daalt**.",
            "criteria": [
                ("Prijs", 1, "De prijs stijgt, met als reden dat de accijns wordt doorberekend.", "0,5 punt: alleen 'de prijs stijgt', zonder reden."),
                ("Hoeveelheid", 1, "De hoeveelheid daalt, omdat mensen bij een hogere prijs minder kopen.", "0,5 punt: alleen 'er wordt minder verkocht', zonder reden."),
            ],
            "student": "De prijs gaat omhoog want de fabrikant rekent de accijns door aan de klant. Mensen kopen dan minder frisdrank omdat het duurder is.",
        },
        {
            "nr": 5, "punten": 2, "onderwerp": "Prijsgevoeligheid",
            "vraag": "Als brood 10% goedkoper wordt, kopen mensen bijna niet meer brood. Als vliegvakanties 10% goedkoper worden, boeken mensen veel meer vakanties. Leg uit waar dit verschil door komt.",
            "context": "Deze vraag toetst prijsgevoeligheid zonder formule. Een eerste levensbehoefte koop je toch, bij een luxe product reageer je sterk op de prijs.",
            "antwoord": "Brood is een **eerste levensbehoefte**: je koopt het toch en je eet niet meer brood omdat het goedkoper is. De vraag is niet prijsgevoelig.\n\nEen vliegvakantie is een **luxe**: je kunt hem uitstellen of iets anders doen. Een lagere prijs maakt hem voor veel meer mensen aantrekkelijk. De vraag is prijsgevoelig.",
            "criteria": [
                ("Brood", 1, "Eerste levensbehoefte, dus niet prijsgevoelig, met een reden.", "0,5 punt: de juiste conclusie zonder reden."),
                ("Vliegvakanties", 1, "Luxe product, dus prijsgevoelig, met een reden.", "0,5 punt: de juiste conclusie zonder reden."),
            ],
            "student": "Brood heb je elke dag nodig, dus dat koop je toch wel, ook als het niet goedkoper is. Vakanties zijn gewoon leuk.",
        },
        {
            "nr": 6, "punten": 4, "onderwerp": "Kosten en break-even",
            "vraag": "Bakkerij De Korenaar heeft per maand €12.000 vaste kosten (huur, ovens, personeel). De variabele kosten zijn €1,50 per brood. Een brood kost in de winkel €3,50.\n\na. Bereken de dekkingsbijdrage per brood.\n\nb. Hoeveel broden moet de bakkerij per maand verkopen om quitte te spelen (break-even)?\n\nc. Bereken de winst als de bakkerij 8.000 broden per maand verkoopt.",
            "context": "Deze vraag toetst kostenberekening op MBO-niveau. De student moet vaste en variabele kosten uit elkaar houden. Een fout die doorwerkt in een volgende deelvraag wordt één keer bestraft.",
            "antwoord": "a. €3,50 − €1,50 = **€2,00** per brood.\n\nb. €12.000 / €2,00 = **6.000 broden**.\n\nc. Omzet 8.000 × €3,50 = €28.000. Variabele kosten 8.000 × €1,50 = €12.000. Vaste kosten €12.000. Winst = €28.000 − €12.000 − €12.000 = **€4.000**.",
            "criteria": [
                ("Dekkingsbijdrage", 1, "€2,00.", "0,5 punt: juiste methode met een rekenfout."),
                ("Break-even", 1.5, "6.000 broden, vaste kosten gedeeld door de dekkingsbijdrage. Rekent de student goed door met een foute dekkingsbijdrage uit a, dan alle punten.", "0,5 punt: vaste kosten gedeeld door de prijs (12.000 / 3,50) of een andere verkeerde methode met een poging."),
                ("Winst", 1.5, "€4.000, met zowel de variabele als de vaste kosten eraf.", "1 punt: één rekenfout bij de juiste methode. 0,5 punt: een van de twee kostensoorten vergeten."),
            ],
            "student": "a. 3,50 − 1,50 = €2,00 per brood.\n\nb. 12.000 / 2 = 6.000 broden.\n\nc. 8.000 × 3,50 = 28.000 omzet. 28.000 − 12.000 = €16.000 winst.",
        },
        {
            "nr": 7, "punten": 3, "onderwerp": "Omzet en winst",
            "vraag": "Een koffiekraam op de markt verkoopt op een zaterdag 200 bekers koffie voor €2,50 per beker. De inkoop (koffie, beker, melk) kost €0,80 per beker. De standplaats kost €150 per dag.\n\na. Bereken de omzet.\n\nb. Bereken de totale kosten.\n\nc. Bereken de winst.",
            "context": "Deze vraag toetst het verschil tussen omzet, kosten en winst. Een fout die doorwerkt in c wordt niet nog een keer bestraft.",
            "antwoord": "a. 200 × €2,50 = **€500**.\n\nb. Inkoop 200 × €0,80 = €160, plus standplaats €150 = **€310**.\n\nc. €500 − €310 = **€190**.",
            "criteria": [
                ("Omzet", 1, "€500.", "0,5 punt: juiste methode met een rekenfout."),
                ("Totale kosten", 1, "€310, inkoop en standplaats samen.", "0,5 punt: alleen de inkoop of alleen de standplaats."),
                ("Winst", 1, "€190, of goed doorgerekend met eigen uitkomsten uit a en b.", "0,5 punt: juiste methode met een rekenfout."),
            ],
            "student": "a. 200 × 2,50 = €500\n\nb. 200 × 0,80 = 160 + 150 = €310\n\nc. 500 − 310 = €190 winst",
        },
        {
            "nr": 8, "punten": 2, "onderwerp": "Externe effecten",
            "vraag": "Een fabriek in een woonwijk maakt 's nachts veel lawaai.\n\na. Wie betaalt hier de kosten van: de fabriek of iemand anders? Leg uit.\n\nb. Noem één maatregel die de gemeente kan nemen en leg uit hoe die helpt.",
            "context": "Deze vraag toetst het begrip negatief extern effect op MBO-niveau: de kosten komen terecht bij mensen die niet bij de productie betrokken zijn.",
            "antwoord": "a. De **omwonenden** betalen de kosten: zij slapen slecht. De fabriek merkt daar zelf niets van in haar kosten. Dit heet een negatief extern effect.\n\nb. Bijvoorbeeld een **geluidsnorm met een boete** of een **heffing**. Dan wordt lawaai duur voor de fabriek, waardoor ze gaat isoleren of 's nachts minder produceert.",
            "criteria": [
                ("Wie betaalt", 1, "De omwonenden, met de uitleg dat de fabriek de kosten zelf niet draagt.", "0,5 punt: omwonenden genoemd zonder die uitleg."),
                ("Maatregel", 1, "Een maatregel én hoe die het lawaai vermindert.", "0,5 punt: alleen een maatregel, zonder uitleg hoe die helpt."),
            ],
            "student": "a. De mensen die er wonen, want zij slapen slecht en de fabriek merkt daar niks van.\n\nb. De gemeente kan een boete geven.",
        },
        {
            "nr": 9, "punten": 2, "onderwerp": "Concurrentie",
            "vraag": "Twee grote supermarkten spreken af dat ze allebei de prijs van melk verhogen. Waarom is dit verboden in Nederland? Noem ook wie hierop let.",
            "context": "Deze vraag toetst waarom prijsafspraken verboden zijn en wie toezicht houdt. Het verwachte antwoord noemt de Autoriteit Consument & Markt (ACM).",
            "antwoord": "Door de afspraak verdwijnt de **concurrentie** en betaalt de **consument meer** dan nodig. De **Autoriteit Consument & Markt (ACM)** let hierop, op basis van de Mededingingswet.",
            "criteria": [
                ("Waarom verboden", 1, "Hogere prijzen voor de consument en/of minder concurrentie.", "0,5 punt: alleen 'dat mag niet', zonder reden."),
                ("Toezicht", 1, "De ACM.", "0,5 punt: 'de overheid' in het algemeen."),
            ],
            "student": "Omdat de klanten dan meer moeten betalen en de supermarkten niet meer met elkaar concurreren. De overheid let hierop.",
        },
        {
            "nr": 10, "punten": 3, "onderwerp": "Marktvormen (invultabel)",
            "vraag": "Vul de tabel in. De tabel heeft **3 kolommen**: aantal aanbieders, soort product (hetzelfde of verschillend) en een voorbeeld uit Nederland. De **4 rijen** zijn de vier marktvormen. Zet in elke cel je antwoord.\n\n| Marktvorm | Aantal aanbieders | Soort product (hetzelfde of verschillend) | Voorbeeld uit Nederland |\n|---|---|---|---|\n| Volkomen concurrentie | | | |\n| Monopolistische concurrentie | | | |\n| Oligopolie | | | |\n| Monopolie | | | |",
            "context": "Dit is een invultabel. Beoordeel per kolom: elke kolom is één criterium. Een kolom met alle 4 cellen juist levert 1 punt op, met 3 juiste cellen 0,5 punt, met 2 of minder 0 punten. Andere voorbeelden zijn goed als ze echt bij de marktvorm passen.",
            "antwoord": "| Marktvorm | Aantal aanbieders | Soort product | Voorbeeld uit Nederland |\n|---|---|---|---|\n| Volkomen concurrentie | Heel veel | Hetzelfde | Aardappeltelers, de bloemenveiling |\n| Monopolistische concurrentie | Veel | Verschillend | Kappers, restaurants, kledingwinkels |\n| Oligopolie | Weinig | Hetzelfde of verschillend | Supermarkten, telecom (KPN, VodafoneZiggo, Odido) |\n| Monopolie | Eén | Uniek, geen alternatief | ProRail, het waterbedrijf in je regio |",
            "criteria": [
                ("Kolom aantal aanbieders", 1, "Alle 4 cellen juist.", "0,5 punt: 3 van de 4 cellen juist."),
                ("Kolom soort product", 1, "Alle 4 cellen juist. Bij oligopolie zijn hetzelfde en verschillend allebei goed.", "0,5 punt: 3 van de 4 cellen juist."),
                ("Kolom voorbeeld", 1, "Alle 4 voorbeelden passen bij de marktvorm.", "0,5 punt: 3 van de 4 voorbeelden passen."),
            ],
            "student": "| Marktvorm | Aantal aanbieders | Soort product (hetzelfde of verschillend) | Voorbeeld uit Nederland |\n|---|---|---|---|\n| Volkomen concurrentie | Heel veel | Hetzelfde | Boeren op de markt |\n| Monopolistische concurrentie | Veel | Verschillend | Kappers |\n| Oligopolie | Weinig | Verschillend | Albert Heijn en Jumbo |\n| Monopolie | Eén | Uniek | Bol.com |",
        },
    ],
    # Voor het spiekbriefje: wat een goede beoordeling zou geven.
    "verwacht": {1: 1, 2: 2, 3: 2.5, 4: 2, 5: 1.5, 6: 3, 7: 3, 8: 1.5, 9: 1.5, 10: 2.5},
    "fouten": [
        "V1: begrip te vaag en het al betaalde kaartje opgeteld (117 in plaats van 72).",
        "V3b: noemt het een tekort, het is een overschot.",
        "V5: geen reden bij vakanties.",
        "V6c: vaste kosten vergeten, winst 16.000 in plaats van 4.000.",
        "V8b en V9: maatregel zonder uitleg, 'de overheid' in plaats van de ACM.",
        "V10: Bol.com is geen monopolie.",
    ],
}
