# Vakdossier MSc Manuele Therapie, testdag Breederode 23-09-2026.
# Bron nakijker: .claude/skills/grading-calibration/examples/manuele-therapie-case-study.md
# Bron model: Eduface-export opdracht "CAT Model + Beoordelingsformulier", 22-09-2026 20:11.
# Geen namen van nakijker of studenten. Voornaam in een citaat is geredigeerd naar [...].

VAK = {
    "opleiding": "MSc Manuele Therapie",
    "vak": "CAT diagnostiek",
    "optie_gekozen": "voldaan of niet voldaan, per rubriekcriterium",
    "optie_doet": (
        "Het model spreekt per criterium alleen uit of eraan is voldaan. "
        "Het geeft geen kwaliteitsniveau en geen cijfer."
    ),
    "criteria": [
        ("Algemeen", "12%"),
        ("Klinisch scenario (stap 1)", "12%"),
        ("Klinische vraagstelling (stap 2)", "12%"),
        ("Zoekstrategie (stap 3)", "12%"),
        ("Kritische evaluatie van kwaliteit (stap 4)", "12%"),
        ("Evidentietabel (stap 5)", "12%"),
        ("Commentaar (stap 6)", "12%"),
        ("Conclusie (stap 7)", "16%"),
    ],
}

STUDENTEN = [
    {
        "label": "Student 1",
        "casus": "Labrumletsel van de heup, Arlington-test tegenover MRA",
        "datum_beoordeling": "9 december 2025",
        # voldaan / deels / niet-voldaan, per criterium, in de volgorde van VAK["criteria"]
        "nakijker": ["voldaan", "deels", "voldaan", "voldaan", "voldaan", "voldaan", "voldaan", "voldaan"],
        "model": ["voldaan"] * 8,
        "nakijker_eindoordeel": "voldaan",
        "model_eindoordeel": "voldaan",
        "nakijker_feedback": (
            "Hey [...], Deze opdracht heb je afgerond. Je hebt hier en daar wel wat kort door de bocht "
            "uitgevoerd. Maar dat is bij deze opdracht nog niet zo'n probleem."
        ),
        "nakijker_detail": (
            "Binnen Klinisch scenario is het onderdeel over de klinische relevantie en de motivatie voor "
            "de klinische vraag niet afgevinkt. De overige onderdelen wel."
        ),
        "model_feedback": [
            "Je hebt je CAT logisch opgebouwd, waardoor de redenering goed te volgen is. Maar de tekst is nog niet overal consistent en de overgang van resultaten naar conclusie kan duidelijker. Controleer vaste vaktermen en grammatica, zoals MRA/RMA en labrumletsel. Voeg verbindende zinnen toe die resultaten aan je conclusie koppelen. Ik vindt de feedback wel sterk alleen mist MRA nog een beetje.",
            "Je beschrijft de patiënt en haar klachten duidelijk en onderbouwt de hypothese van labrumletsel goed. Maar de presentatie kan nog vloeiender. Formuleer anamnese en onderzoek compacter en sluit af met één zin waarin je uitlegt dat de bevindingen samen de hypothese ondersteunen en de diagnostische vraag motiveren.",
            "Je hebt een heldere en goed meetbare klinische vraag opgesteld. Maar de onderbouwing van de lage voorkans blijft nog te algemeen. Licht kort toe waarom deze voorkans in de eerstelijn én bij deze patiënt aannemelijk is, en verbind dit niet alleen aan Simpto.nl.",
            "Je zoekstrategie is goed navolgbaar en je keuze voor het artikel is logisch gekoppeld aan je patiënt. Maar de toepasbaarheid kan duidelijker. Zet bij de artikelkeuze de publicatiedatum en taal en vergelijk de inclusie- en exclusiecriteria direct met de klachten en voorafkans van jouw patiënt.",
            "Je hebt de belangrijkste methodologische aandachtspunten helder benoemd en met goede voorbeelden aan de klinische praktijk gekoppeld. Maar het blijft onduidelijk wat het ontbrekende afkappunt betekent voor de betrouwbaarheid van sensitiviteit en specificiteit. Leg dit kort uit en verbind je conclusie daarna expliciet aan de beslissing voor jouw patiënt.",
            "Je hebt de kengetallen voor de artikelpopulatie en praktijksituatie correct en duidelijk weergegeven; zo wordt de invloed van een lage voorafkans zichtbaar. Maar de berekeningen zijn niet overal controleerbaar, omdat aantallen en percentages door elkaar lopen. Schrijf de tussenstappen consequent uit en vermeld eerst de aantallen, daarna het percentage.",
            "Je commentaar koppelt de beperkingen en testkenmerken goed aan deze patiënt. Maar de stap naar de eerstelijns manuele therapiepraktijk kan concreter. Beschrijf wanneer een negatieve test je vervolgbeleid beïnvloedt en formuleer dat de test labrumletsel minder waarschijnlijk maakt, maar niet zelfstandig uitsluit.",
            "Je Bottom Line beantwoordt de klinische vraag duidelijk en houdt terecht rekening met de beperkte generaliseerbaarheid. Maar de vervolgstap voor deze patiënt blijft nog te impliciet. Beschrijf concreet dat je geen directe MRA inzet, de patiënt klinisch vervolgt en bij aanhoudende of ernstige klachten herbeoordeelt of verwijst.",
        ],
        # blad 3: waar het uiteenloopt
        "divergenties": [
            {
                "criterium": "Klinisch scenario (stap 1)",
                "uitkomst": "model milder",
                "nakijker": "Het onderdeel over de klinische relevantie en de motivatie voor de klinische vraag is niet afgevinkt. De overige onderdelen van dit criterium wel.",
                "model": "“Je beschrijft de patiënt en haar klachten duidelijk en onderbouwt de hypothese van labrumletsel goed. Maar de presentatie kan nog vloeiender.” Het model vraagt om een compactere formulering en om één afsluitende zin.",
                "rubriek": None,
                "rubriek_reden": "De letterlijke rubriektekst van dit onderdeel is hier niet beschikbaar, dus deze regel blijft leeg.",
                "vraag": "Het model noemt de patiëntpresentatie en de hypothese voldoende en vraagt alleen om een vloeiendere formulering. Wanneer weegt de motivatie voor de klinische vraag bij jullie zwaar genoeg om dit onderdeel niet te laten voldoen?",
            },
        ],
        # blad 4: aannames en bevindingen
        "aannames": [
            {
                "kop": "Het model beoordeelt een criterium als één geheel",
                "model": "Op Klinisch scenario geeft het model één uitkomst voor het hele criterium.",
                "rubriek": "Het beoordelingsformulier splitst dit criterium in meerdere onderdelen, elk met een eigen vinkje.",
                "nakijker": "De nakijker vinkte één van die onderdelen niet af en de andere wel.",
                "vraag": "Het model geeft per criterium één uitkomst en kan een los onderdeel daarbinnen niet apart laten vervallen. Willen jullie de onderdelen apart beoordeeld zien, of is één uitkomst per criterium genoeg?",
            },
            {
                "kop": "Het model geeft de aangeleverde feedback terug",
                "model": "De feedback op Algemeen eindigt met: “Ik vindt de feedback wel sterk alleen mist MRA nog een beetje.” Dat is een zin in de eerste persoon over feedback, niet over het werk van de student.",
                "rubriek": "Het criterium Algemeen gaat over taalgebruik, samenhang en verwijzingen.",
                "nakijker": "Het bestand dat aan het model is aangeleverd bevatte het commentaar van de nakijker al.",
                "vraag": "Dit is een bevinding over het model: het neemt commentaar over dat al in het document staat. Wij leveren voor de testperiode de schone versie aan, en de vraag is of jullie willen dat het model bestaand commentaar juist wel meeneemt of juist negeert.",
            },
        ],
    },
    {
        "label": "Student 2",
        "casus": "Lumbale radiculopathie, Slump-test tegenover MRI",
        "datum_beoordeling": "10 december 2025",
        "nakijker": ["voldaan", "voldaan", "voldaan", "voldaan", "niet voldaan", "niet voldaan", "deels", "voldaan"],
        "model": ["voldaan"] * 8,
        "nakijker_eindoordeel": "voldaan",
        "model_eindoordeel": "voldaan",
        "nakijker_feedback": (
            "Hi [...], Je hebt een prima CAT geschreven met uitzondering op het methodologisch beoordelen "
            "van het hele artikel. Je had echt nog wat beter moeten omschrijven wat de goede en slechte "
            "kanten van het artikel waren en of je dus uberhaupt iets kon met de berekening/bevinding."
        ),
        "nakijker_detail": (
            "Kritische evaluatie van kwaliteit en Evidentietabel zijn op beide onderdelen niet afgevinkt. "
            "Bij Commentaar is de helft van de onderdelen afgevinkt. Het eindoordeel is voldaan."
        ),
        "model_feedback": [
            "Je deed goed werk met de duidelijke opbouw van patiëntsituatie naar klinische vraag, onderzoeksresultaten en conclusie. Maar taalfouten en een onrustige weergave van de zoekstrategie en tabellen maken het lastiger om je redenering te volgen. Corrigeer spelling en vaktermen, zoals ‘symptomen’ en ‘magnetic resonance imaging’, en maak de tabellen overzichtelijk en consistent.",
            "Je patiëntpresentatie is kort en duidelijk en leidt logisch naar de hypothese van lumbale radiculopathie. Maar de klinische redenering kan nog scherper. Koppel de belangrijkste bevindingen direct aan de hypothese en vervang ‘spraken’ door ‘sprake’ voor een professionelere formulering.",
            "Je hebt een duidelijke, meetbare klinische vraag opgesteld met alle belangrijke onderdelen en een onderbouwde prior-kans. Maar de afkorting voor de uitkomstmaat is niet overal hetzelfde. Gebruik consequent ‘PVW’ in de hele CAT, zodat je berekeningen en conclusies helder blijven.",
            "Je hebt de zoekstrategie en de koppeling tussen artikel, patiënt en inclusiecriteria duidelijk uitgewerkt. Maar de zoekactie is nog niet goed controleerbaar. Noteer de zoekdatum en database en controleer de zoekregistratie op vervormde termen, zodat iemand je aanpak kan herhalen.",
            "Je beoordeelt de methodologische kwaliteit zorgvuldig en benoemt zowel sterke punten als relevante beperkingen. Maar de gevolgen daarvan voor je conclusie blijven nog wat onduidelijk. Leg per belangrijkste beperking kort uit wat dit betekent voor de validiteit van het onderzoek en maak duidelijk onderscheid tussen een methodologisch probleem en beperkte toepasbaarheid in de eerstelijn.",
            "Je hebt de diagnostische uitkomsten helder uitgewerkt en de berekeningen goed navolgbaar gemaakt. Maar de notatie van formules en afrondingen is nog niet overal gelijk. Noteer de berekeningen op dezelfde manier en kies één vaste afronding, zodat de uitkomsten intern consistent en eenvoudig te controleren zijn.",
            "Je koppelt de onderzoekspopulatie goed aan de patiënt en gebruikt de PVW en NVW passend voor de klinische interpretatie. Maar de methodologische beperkingen mogen concreter. Licht toe hoe de onbekende testvolgorde en de twee niet-toegewezen deelnemers de betrouwbaarheid en toepasbaarheid voor deze patiënt beïnvloeden.",
            "Je Bottom line beantwoordt de klinische vraag helder en koppelt de testuitslag goed aan de praktijk. Maar de concrete vervolgstap ontbreekt nog. Voeg toe wanneer je de patiënt herbeoordeelt en wanneer verwijzing of MRI nodig is bij aanhoudende verdenking.",
        ],
        "divergenties": [
            {
                "criterium": "Kritische evaluatie van kwaliteit (stap 4)",
                "uitkomst": "model milder",
                "nakijker": "Beide onderdelen niet afgevinkt. Uit de eindfeedback: “Je had echt nog wat beter moeten omschrijven wat de goede en slechte kanten van het artikel waren en of je dus uberhaupt iets kon met de berekening/bevinding.”",
                "model": "“Je beoordeelt de methodologische kwaliteit zorgvuldig en benoemt zowel sterke punten als relevante beperkingen.” Het model vraagt daarna om de gevolgen voor de conclusie.",
                "rubriek": None,
                "rubriek_reden": "De letterlijke rubriektekst van dit criterium is hier niet beschikbaar, dus deze regel blijft leeg.",
                "vraag": "Het model noemt hier precies datgene voldoende wat in deze beoordeling niet is afgevinkt. Hier zag de nakijker iets dat het model niet noemt: wat was dat, zodat we het kunnen meenemen?",
            },
            {
                "criterium": "Evidentietabel (stap 5)",
                "uitkomst": "model milder",
                "nakijker": "Beide onderdelen niet afgevinkt.",
                "model": "“Je hebt de diagnostische uitkomsten helder uitgewerkt en de berekeningen goed navolgbaar gemaakt. Maar de notatie van formules en afrondingen is nog niet overal gelijk.” Het model behandelt de notatie als een verbeterpunt binnen een voldoende.",
                "rubriek": None,
                "rubriek_reden": "De letterlijke rubriektekst van dit criterium is hier niet beschikbaar, dus deze regel blijft leeg.",
                "vraag": "Het model ziet de notatie van formules en afrondingen als een verbeterpunt en komt op voldaan. Waar ligt voor jullie de grens waarop dit onderdeel niet meer voldoet?",
            },
            {
                "criterium": "Commentaar (stap 6)",
                "uitkomst": "model milder",
                "nakijker": "De helft van de onderdelen afgevinkt.",
                "model": "“Je koppelt de onderzoekspopulatie goed aan de patiënt en gebruikt de PVW en NVW passend voor de klinische interpretatie. Maar de methodologische beperkingen mogen concreter.” Het model geeft één uitkomst voor het hele criterium.",
                "rubriek": None,
                "rubriek_reden": "De letterlijke rubriektekst van dit criterium is hier niet beschikbaar, dus deze regel blijft leeg.",
                "vraag": "Het model geeft één uitkomst voor dit criterium en komt op voldaan. In deze beoordeling is de helft van de onderdelen afgevinkt: willen jullie die onderdelen apart beoordeeld zien?",
            },
        ],
        "aannames": [
            {
                "kop": "Het model streept een gevonden punt weg tegen de rest",
                "model": "Op drie criteria noemt het model een verbeterpunt en komt het toch op voldaan.",
                "rubriek": "Het formulier kent per onderdeel twee standen en geen tussenstand.",
                "nakijker": "Op diezelfde drie criteria is niet afgevinkt, terwijl het eindoordeel voldaan is.",
                "vraag": "Het model behandelt een gevonden verbeterpunt als groeifeedback binnen een voldoende. Willen jullie dat een gevonden punt op criteriumniveau zwaarder weegt, en zo ja op welke van de drie?",
            },
            {
                "kop": "Het model en het eindoordeel staan los van elkaar",
                "model": "Het model komt op alle acht criteria op voldaan en geeft als totaal voldaan.",
                "rubriek": "Het eindoordeel is een eigen keuze op het formulier en geen optelsom van de criteria.",
                "nakijker": "Drie criteria zijn niet of deels afgevinkt en het eindoordeel is voldaan.",
                "vraag": "In deze beoordeling leidt een niet afgevinkt criterium niet tot een onvoldoende eindoordeel. Willen jullie dat het model die twee lagen ook los houdt, of dat het bij het eindoordeel meeweegt?",
            },
        ],
    },
]

# Blanco formulieren voor de andere opdrachten van die ochtend.
ANDERE_VAKKEN = [
    {
        "opleiding": "Master Kinderfysiotherapie",
        "vak": "CAT",
        "optie_gekozen": "voldaan of niet voldaan, per rubriekcriterium",
        "criteria": [
            "Algemeen",
            "Onzekerheid in de kinderfysiotherapeutische praktijk",
            "Onderzoeksvraagstelling en -doelstelling",
            "Zoekstrategie en scopesearch",
            "Beoordelen van de kwaliteit van artikelen",
            "Conclusies en aanbevelingen",
            "Implicaties voor de kinderfysiotherapiepraktijk",
        ],
        "standen": ["voldaan", "niet voldaan"],
    },
    {
        "opleiding": "Praktijkondersteuner Huisartsenzorg",
        "vak": "CAT",
        "optie_gekozen": "onvoldoende, voldoende, goed of uitstekend, per rubriekcriterium",
        "criteria": [
            "Beschrijving van de aanleiding van de klinische vraag vanuit het EBP-principe",
            "Beschrijving van een eenduidige en methodologische onderzoeksvraag op basis van het PICO-concept",
            "Gebruik van wetenschappelijke databanken en professionele weging van gevonden informatie",
            "Analyse van onderzoeksresultaten binnen de context van het praktijkprobleem",
            "Formulering van een conclusie vanuit de verkregen resultaten",
            "Kritische inhoudelijke discussie",
            "Klinische relevantie en toepasbaarheid van bevindingen en resultaten",
            "Reflectie op werkwijze, resultaten en eigen professionele rolontwikkeling",
        ],
        "standen": ["onvoldoende", "voldoende", "goed", "uitstekend"],
    },
]
