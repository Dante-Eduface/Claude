# Kalibratie CAT POH-6

_Laatst bijgewerkt: 2026-09-23._ Werkbestand van de skill `grading-calibration`. Stand: het materiaal is binnen, de baseline in Eduface is nog niet gedraaid.

## Vak: OPEN

Dante noemde dit op 23-09-2026 "Master Kinderfysiotherapie". Al het materiaal is van **POH-6**: de bestandsnaam "POH NLQF niveau 6", groep "POH-6 24 Rotterdam", huisartsenzorg, NHG-standaarden en "het perspectief van de POH". Het MKF-materiaal kwam van Ivonne (08-09) en is iets anders. Zolang dit niet bevestigd is, gaat dit bestand uit van POH-6.

## Materiaal (checklist `reference.md` punt 2)

| # | Wat | Stand |
|---|---|---|
| 1 | Beoordelingsformulier | Ja, twee versies. **v3.0** (0/2/4 punten, met Onvoldoende-kolom): hiermee is gescoord. **v4.0** (juni 2026): alleen de Voldoende-tekst, verder niets |
| 2 | Opdrachtbeschrijving | Ja, Bijlage 1 versie 3. Verder Bijlage 2 (PICO), 5.1 (beoordelingsformulier artikel) en 7 (schema kwalitatief/kwantitatief) |
| 3 | 2 inzendingen | Ja. S1: kurkuma bij vrouwen met verhoogd cholesterol. S2: vitamine D en gewichtsverlies bij obesitas |
| 4 | Officiële beoordeling | Ja, per criterium punten plus feedback. Beoordelaar K.J. van Kruining, juni 2025 |
| 5 | Conceptcommentaar van de docent in de inzending | Nee, er zitten geen comments in de docx-bestanden |
| 6 | Live rubric + modelinstructies in Eduface | **Ontbreekt** |
| 7 | AI-uitkomst op S1 en S2 | **Ontbreekt** |
| extra | Voorbeeld 1 (inzending, resultaat onvoldoende) | Inzending wel, scores per criterium **niet**. Nodig als controle, zie hieronder |
| extra | Voorbeeld 2 (beoordeling goed, 30 punten) | Alleen het scoreformulier, de inzending zelf niet |

Let op: in de "anonieme" beoordelings-PDF van S1 staat de naam van de student nog in de tekstlaag onder de zwarte balk. Niet zo delen of uploaden.

## Ground truth

Formulier v3.0: 4 punten = Goed, 2 = Voldoende, 0 = Onvoldoende. Geslaagd = elk criterium minimaal 2 en in totaal minimaal 18.

| Criterium | S1 | S2 | Eduface-doel |
|---|---|---|---|
| 1 Aanleiding klinische vraag | 4 | 4 | Voldoende |
| 2 Onderzoeksvraag (PICO) | 4 | **2** | Voldoende |
| 3 Zoekstrategie | **2** | **2** | Voldoende |
| 4 Analyse artikelen | 4 | **2** | Voldoende |
| 5 Conclusie | **2** | **2** | Voldoende |
| 6 Discussie | 4 | 4 | Voldoende |
| 7 Klinische relevantie | **2** | 4 | Voldoende |
| 8 Reflectie | 4 | **3** | Voldoende |
| Totaal | 26 (8,1) | 23 (7,2) | 16x Voldoende |

## Wat anders is dan bij manuele therapie

- **Drie niveaus tegen twee.** Eduface kent per criterium Voldoende of Onvoldoende. De lat voor Voldoende is de 2-puntenkolom. De 4-puntenkolom is Goed en hoort niet in de Pass-tekst.
- **Het formulier zegt zelf waar het verschil zit.** Voor 2 punten moet iets **beschreven** zijn, voor 4 punten **onderbouwd**. Zo ook "reflecteert" tegenover "reflecteert kritisch", en "een antwoord" tegenover "een antwoord in stellende vorm".
- **De drempel staat letterlijk in v3.0.** Bij criterium 3, 6 en 7: "bij 2 of meer vastgestelde punten = onvoldoende". In v4.0 is die regel verdwenen, en dan leest de Voldoende-tekst als een lijst waarvan elk punt moet kloppen.
- **Alle 16 oordelen zijn Voldoende.** Een rubric die alles laat slagen scoort dan perfect. Daarom moet er een inzending mee die de docent op minstens één criterium Onvoldoende gaf, met die scores erbij (Voorbeeld 1).

## Waar de AI waarschijnlijk afwijkt

Dit is een voorspelling, nog niet getoetst. De baseline moet het bevestigen voordat er iets aan de rubric verandert.

| Criterium | Student | Wat de docent zag en toch met 2 punten liet slagen | Zin in de rubric die een fail kan uitlokken |
|---|---|---|---|
| 5 Conclusie | **S1 en S2** | Niet in stellende vorm. S1 vat de studies opnieuw samen, S2 haalt al discussiepunten aan | Onvoldoende: "bevat informatie die nog niet eerder is benoemd", "omslachtig beschreven" |
| 3 Zoekstrategie | **S1 en S2** | S1: weinig synoniemen, de gedachtegang achter de zoekstrings niet uitgelegd. S2: de C zit in geen enkele zoekstring | Voldoende: "zorgvuldig een zoektabel", alle items als lijst |
| 2 Onderzoeksvraag | S2 | De vergelijking uit de PICO ontbreekt in de onderzoeksvraag | Voldoende: "alle elementen van de PICO zijn herkenbaar in de onderzoeksvraag" |
| 4 Analyse | S2 | "Had kritischer en vollediger gemogen", 'setting' verkeerd ingevuld, fouten met et al. | Onvoldoende: "beperkte of incomplete onderbouwing van zwakke of sterke punten" |
| 7 Klinische relevantie | S1 | Haalbaarheid benoemd maar niet onderbouwd, monitoring niet of te beperkt | Voldoende: vier onderdelen als lijst |
| 8 Reflectie | S2 | Blijft op hoofdlijnen, feedbackverwerking algemeen, toekomstige aanpak niet expliciet | Voldoende: vijf onderdelen als lijst |

Criterium 3 en 5 komen bij beide studenten terug. Die zijn het zekerst.

## Vaste rubricbasis (baseline)

Deze tekst komt in **elke** opdracht letterlijk hetzelfde: in de baseline en in elke variant. Laat Eduface de rubric nooit zelf uit de PDF halen, want die vertaling verschilt per keer.

Bron: de 2-puntenkolom (Voldoende) en de 0-puntenkolom (Onvoldoende) van v3.0. De Voldoende-tekst is gelijk aan die van v4.0. Spelfouten uit het origineel zijn verbeterd, de inhoud is niet veranderd. Het Goed-niveau staat er bewust niet in. Gewicht: 12,5% per criterium, want in het formulier tellen alle acht even zwaar. De randvoorwaarden (plagiaat, lettertype, woordenaantal, APA, Word-formaat) zijn geen criterium, want het zijn knock-outvoorwaarden die de docent zelf controleert.

**1. Aanleiding van de klinische vraag vanuit het EBP-principe**
- Voldoende: De aanleiding van de kritische beroepssituatie is beschreven met: (1) een volledige beschrijving van de casuïstiek uit de praktijk met onderscheid tussen hoofd- en bijzaken, waarin een concrete vraag, een aantal relevante kenmerken en de relevante NHG-standaarden beschreven zijn; (2) een eerste verkenning van de gevraagde interventie via relevante richtlijnen, standaarden en/of (wetenschappelijke) literatuur, waarin eventuele risico's, kanttekeningen en de noodzaak van verder onderzoek beschreven zijn vanuit de praktijk, de patiëntenpopulatie en het perspectief van de POH; (3) een beschrijving waarin de student vanuit de eigen expertise een aanvulling geeft met mogelijke implicaties, gevolgen en kansen.
- Onvoldoende: De aanleiding van de kritische beroepssituatie is onvoldoende beschreven, en/of de kenmerken of de concrete vraag zijn niet of niet concreet benoemd, en/of het is onvoldoende duidelijk wat de kanttekeningen of risico's van de gevraagde interventie zijn en er is geen duidelijke noodzaak voor verder onderzoek beschreven of onderbouwd, en/of de eigen expertise over implicaties, gevolgen en kansen voor de patiëntenpopulatie, de praktijk en de rol als POH is niet of zeer summier beschreven.

**2. Eenduidige en methodologische onderzoeksvraag op basis van de PICO**
- Voldoende: De student beschrijft een beantwoordbare vraag die grotendeels samenhangt met de klinische vraag, waarin de (controle)interventie en de gewenste uitkomst geheel zijn meegenomen. De kenmerken zijn gedeeltelijk meegenomen om de vraagstelling en de PICO te formuleren. De onderzoeksvraag is geformuleerd met behulp van de PICO en alle elementen van de PICO zijn herkenbaar in de onderzoeksvraag opgenomen.
- Onvoldoende: De beantwoordbare vraag sluit niet in logische samenhang aan bij de aanleiding uit de beroepspraktijk: de onderzoeksvraag is onsamenhangend of niet onderzoekbaar, en/of de elementen van de PICO zijn niet gebruikt om de onderzoeksvraag te formuleren of zijn niet herkenbaar in de onderzoeksvraag opgenomen.

**3. Zoekstrategie in wetenschappelijke databanken**
- Voldoende: De student beschrijft een systematische zoekstrategie met: een zorgvuldig opgestelde zoektabel met vrije (Nederlandse en Engelse) zoektermen, MeSH-termen en synoniemen; combinaties van zoektermen met booleaanse operatoren (zoekstrings); methodologische in- en exclusiecriteria; gebruik van minimaal 1 wetenschappelijke database; een resultaat van minimaal 3 wetenschappelijke artikelen; een beschrijving van de keuze voor de geselecteerde artikelen; en, als de sneeuwbalmethode is gebruikt, een koppeling van het resultaat daarvan aan de oorspronkelijke zoekstrategie.
- Onvoldoende: De zoekstrategie is onvoldoende systematisch onderbouwd en sluit niet aan bij de beantwoordbare vraagstelling. Onvoldoende bij twee of meer van de volgende punten: een incomplete of niet eenduidige zoektabel; geen combinaties van zoektermen met booleaanse operatoren; geen of onduidelijke methodologische in- en exclusiecriteria; geen gebruik van minimaal 1 wetenschappelijke database; een incomplete of slordige presentatie; een resultaat van 1 of minder wetenschappelijke artikelen; de keuze voor de geselecteerde artikelen is niet of te beperkt beschreven of onderbouwd; een gebruikte sneeuwbalmethode is niet gekoppeld aan de oorspronkelijke zoekstrategie.

**4. Analyse van de onderzoeksresultaten binnen de context van het praktijkprobleem**
- Voldoende: De student analyseert de geselecteerde artikelen en onderbouwt die analyse met: de level of evidence-piramide; de methodologische kwaliteit met behulp van de beoordelingsformulieren (betrouwbaarheid, validiteit en generaliseerbaarheid); en per artikel welke onderdelen relevant zijn voor de CAT. De geanalyseerde data zijn verwerkt in een data-extractietabel.
- Onvoldoende: De analyse van de geselecteerde artikelen is onvoldoende: de analyse van de data in de data-extractietabel is beperkt of incompleet, en/of de onderbouwing van de relatief sterke en zwakke methodologische punten is beperkt of incompleet.

**5. Conclusie vanuit de verkregen resultaten**
- Voldoende: De student trekt de juiste conclusie op basis van de verkregen resultaten, met een kort en bondig antwoord op de klinische vraagstelling dat alleen eerder genoemde informatie bevat.
- Onvoldoende: De conclusie bevat informatie die nog niet eerder is benoemd en/of is omslachtig beschreven, en/of geeft onvoldoende antwoord om de volledige onderzoeksvraag te beantwoorden, en/of sluit onvoldoende aan bij de resultaten van de geselecteerde studies.

**6. Kritische inhoudelijke discussie**
- Voldoende: De student bediscussieert het eigen onderzoek en de resultaten uit de gebruikte artikelen met: een beschrijving van het aantonen van de validiteit van het eigen onderzoek; een beschrijving van nieuwe inzichten uit de studies; een verheldering en verkenning van conflicterende perspectieven; het benoemen van de belangrijkste sterke en minder sterke methodologische punten van de studies; een beschrijving van de beperkingen van het eigen onderzoek; en een beschrijving van oorzaken en gevolgen voor het resultaat.
- Onvoldoende: De resultaten zijn onvoldoende bediscussieerd. Onvoldoende bij twee of meer van de volgende punten: bij het aantonen van de validiteit van het eigen onderzoek staat de eigen mening centraal; geen of een beperkte beschrijving van nieuwe inzichten uit de studies; geen of een beperkte verheldering en verkenning van conflicterende perspectieven; alleen de minder relevante sterke en minder sterke methodologische punten zijn benoemd of onderbouwd; geen of een beperkte beschrijving of onderbouwing van de beperkingen van het eigen onderzoek.

**7. Klinische relevantie en toepasbaarheid in concrete handelingsalternatieven**
- Voldoende: De klinische relevantie en toepasbaarheid van de bevindingen zijn uitgewerkt met: concrete, actiegerichte aanbevelingen voor handelingsalternatieven die logisch voortvloeien uit het verkregen bewijs; een beschrijving van de implicaties van het invoeren van de aanbevelingen voor patiënt en praktijk; een beschrijving van de haalbaarheid van de aanbeveling; en een beschrijving van hoe de aanbeveling in de praktijk gemonitord kan worden.
- Onvoldoende: Handelingsalternatieven zijn niet of onvoldoende beschreven of onderbouwd. Onvoldoende bij twee of meer van de volgende punten: incomplete of ondoordachte aanbevelingen die niet of niet eenduidig voortvloeien uit het verkregen bewijs; er zijn geen implicaties benoemd voor patiënt en praktijk; er is geen of een ondoordachte beschrijving van de haalbaarheid; er is geen of een ondoordachte beschrijving van hoe de aanbeveling in de praktijk gemonitord kan worden.

**8. Reflectie op werkwijze, resultaten en eigen professionele rolontwikkeling**
- Voldoende: De student reflecteert op het eigen onderzoeks- en leerproces: de aanpak bij het maken van de CAT; de tevredenheid over het eindresultaat; de ontvangen feedback van medestudenten, docent en praktijk en hoe die is of wordt verwerkt; de essentie van wat hij of zij geleerd heeft; en hoe hij of zij een dergelijk onderzoek in de toekomst zou aanpakken.
- Onvoldoende: De student reflecteert niet kritisch op het eigen leerproces op deze onderdelen: de aanpak bij het maken van de CAT, de tevredenheid over het eindresultaat, de ontvangen feedback en hoe die is verwerkt, de essentie van wat geleerd is, en de aanpak in de toekomst.

## Testopzet

- Onderwijsniveau in Eduface: HBO Bachelor (NLQF 6). Bij manuele therapie maakte deze instelling niets uit, maar zet hem wel goed.
- **Ronde 1:** alleen de baseline (vaste rubricbasis hierboven, standaard modelinstructies) op S1, S2 en Voorbeeld 1. Exporteer via "Inzendingen" (zip). Daaruit komen de echte afwijkingen, met de eigen tekst van de AI erbij.
- **Ronde 2:** drie varianten (alleen rubric, alleen instructies, allebei), elk in een eigen opdracht, op dezelfde drie inzendingen. De rubric-fixes komen alleen op criteria die in ronde 1 echt afwijken.

## Klaar voor ronde 2, nog niet plakken

### Rubric-toevoegingen (aan het eind van de Voldoende-tekst, alleen waar de baseline afwijkt)

- **2:** Ontbreekt één PICO-element in de uitgeschreven onderzoeksvraag terwijl het wel in de PICO staat, bijvoorbeeld de vergelijking, dan is dat een verbeterpunt en geen reden voor Onvoldoende. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.
- **3:** Onvoldoende pas bij twee of meer tekortkomingen uit de lijst. Een zoektabel met weinig synoniemen, een PICO-element dat niet in de zoekstrings terugkomt, of een gedachtegang achter de zoekstappen die niet is uitgelegd, zijn verbeterpunten zolang de zoekstrategie navolgbaar en herhaalbaar is en er minimaal 3 artikelen met een beschreven keuze zijn. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.
- **4:** Een analyse die op punten kritischer of vollediger kan, bijvoorbeeld een zwak punt dat benoemd is zonder uit te werken wat het betekent voor betrouwbaarheid of validiteit, of een kleine fout in een onderdeel van het beoordelingsformulier of in de bronvermelding, is Voldoende zolang elk artikel op level of evidence en methodologische kwaliteit is beoordeeld en de data in een extractietabel staan. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.
- **5:** Een stellende formulering is niet vereist, die hoort bij het niveau Goed. Een conclusie die de studies nog eens samenvat of al discussiepunten zoals beperkingen of generaliseerbaarheid aanhaalt, is Voldoende zolang ze een duidelijk antwoord op de onderzoeksvraag geeft dat aansluit bij de resultaten. Discussiepunten tellen niet als nieuwe informatie. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.
- **7:** Onvoldoende pas bij twee of meer tekortkomingen uit de lijst. Een haalbaarheid die benoemd is maar niet onderbouwd telt als beschreven. Een monitoring die ontbreekt of summier is, is een verbeterpunt zolang er concrete aanbevelingen met implicaties voor patiënt en praktijk staan. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.
- **8:** Niet elk onderdeel hoeft diepgaand of expliciet. Een reflectie die op hoofdlijnen blijft, de verwerking van feedback algemeen beschrijft of de toekomstige aanpak niet expliciet noemt, is Voldoende zolang de student zichtbaar reflecteert op aanpak, resultaat en eigen leren. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg.

### Modelinstructies (vrije tekst bij "Beschrijf je feedbackstijl")

> BELANGRIJK: vat deze tekst niet samen en laat geen van de vier onderdelen weg: context, algemene feedback, inline opmerkingen en beoordelingsstrengheid.
>
> Feedback op een CAT (Critically Appraised Topic) over een interventievraag, de eindopdracht van de POH-opleiding op NLQF-niveau 6 van Breederode Hogeschool. De student is een werkende praktijkondersteuner huisartsenzorg die een vraag uit de eigen huisartsenpraktijk uitwerkt: aanleiding met NHG-standaarden, PICO en onderzoeksvraag, zoekstrategie, kritische beoordeling van minimaal drie artikelen, conclusie, discussie, vertaling naar de praktijk van de POH en reflectie. Het beoordelingsformulier van de school kent drie niveaus: Onvoldoende, Voldoende en Goed. Beoordeel alleen of Voldoende gehaald is. Voor Voldoende moet een onderdeel beschreven zijn. Onderbouwen, kritisch analyseren en een stellende conclusie horen bij Goed en zijn geen voorwaarde voor Voldoende. Ontbreekt één onderdeel of is het summier, dan is dat groeifeedback binnen een Voldoende.
>
> Schrijf de algemene feedback per criterium in maximaal 80 woorden, in de jij-vorm, zoals een betrokken docent die het werk net gelezen heeft. Gebruik korte regels die beginnen met + voor wat sterk is en +/- voor wat deels goed is. Noem bij een verbeterpunt één concreet voorbeeld uit de tekst, of stel het als vraag. Zeg bij een Voldoende wat het werk naar Goed zou tillen. Geen cijfers.
>
> Schrijf inline opmerkingen in één of twee zinnen, vaak als vraag, met een lengte die past bij het gewicht van het punt.
>
> Houd de beoordelingsstrengheid normaal. Waar het formulier zegt dat een criterium pas bij twee of meer tekortkomingen Onvoldoende is, geldt dat letterlijk.

Keuzes daarin: 80 woorden in plaats van 50, want deze docent schrijft per criterium ruim 35 tot 160 woorden, meestal rond de 90. De +/- regels omdat hij zelf zo schrijft. De drempelregel staat in de context, omdat de Beoordelingsstrengheid-sectie bij manuele therapie de generatiestap niet overleefde.

## Open voor Dante

1. POH-6 of Master Kinderfysiotherapie?
2. De scores per criterium van Voorbeeld 1, de inzending met resultaat onvoldoende.
3. Staat deze CAT al in Eduface? Dan de huidige rubric plus de export van de AI-uitkomst op S1 en S2.
4. Later: wil Breederode het onderscheid tussen Voldoende en Goed in Eduface terugzien? Eduface kent per criterium maar twee niveaus, dus het cijfer (26 punten = 8,1) valt er niet direct uit te halen.
