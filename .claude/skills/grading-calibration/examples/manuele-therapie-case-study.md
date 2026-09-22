# Case study: manuele therapie (CAT diagnostiek)

Het eerste vak waarop `grading-calibration` volledig is doorlopen. Volledig uitgewerkt zodat een volgend vak zich hieraan kan spiegelen, en zodat de exacte teksten niet verloren gaan.

- **Opleiding:** post-HBO vervolgopleiding manuele therapie (MSc Manuele Therapie), Breederode Hogeschool
- **Opdrachttype:** CAT diagnostiek (Critically Appraised Topic over een diagnostische test), 8 stappen: Algemeen, Klinisch scenario, Klinische vraagstelling, Zoekstrategie, Kritische evaluatie van de kwaliteit, Evidentietabel, Commentaar, Kernconclusie
- **Docent:** Marloes de Graaf
- **Studenten:** "Jurre" (Eduface-label "Student 1", casus: labrumletsel heup, Arlington-test vs MRA) en "Carlijn" (label "Student 2", casus: lumbale radiculopathie, Slump-test vs MRI)

## 1. Het originele beoordelingsformulier (bron)

8 secties, elk met meerdere Voldaan/Niet voldaan-items:
1. Algemeen (taalgebruik, max 1000 woorden, samenhang, titel)
2. Klinisch scenario (stap 1)
3. Klinische vraagstelling (stap 2)
4. Zoekstrategie (stap 3)
5. Kritische evaluatie kwaliteit (stap 4)
6. Evidentietabel (stap 5)
7. Commentaar (stap 6)
8. Bottom line (stap 7)

Plus vrije velden "Beoordeling:" en "Feedback:" die de docent met de hand invult. Eduface's rubric is een (niet-deterministische, zie `reference.md` punt 6) samenvatting hiervan tot 8 criteria met een gecombineerde Voldoende/Onvoldoende-tekst per criterium.

## 2. Marloes' officiële beoordeling (ground truth)

**Jurre**, 9-12-2025: alles Voldaan behalve Klinisch scenario-onderdeel "klinische relevantie/motivatie" (reden niet toegelicht). Eindoordeel: Voldaan. Feedback: *"Hey Jurre, Deze opdracht heb je afgerond. Je hebt hier en daar wel wat kort door de bocht uitgevoerd. Maar dat is bij deze opdracht nog niet zo'n probleem."*

**Carlijn**, 10-12-2025: Niet voldaan op Kritische evaluatie kwaliteit (beide items), Evidentietabel (beide items), en de helft van Commentaar. Alle overige criteria Voldaan. Eindoordeel: **Voldaan** (dus geen optelsom van de losse items, zie `reference.md` punt 1). Feedback: *"Hi Carlijn, Je hebt een prima CAT geschreven met uitzondering op het methodologisch beoordelen van het hele artikel. Je had echt nog wat beter moeten omschrijven wat de goede en slechte kanten van het artikel waren en of je dus uberhaupt iets kon met de berekening/bevinding."*

Beide eindfeedbacks: kort (2-3 zinnen), persoonlijk aangesproken bij naam, geen jargon, geen puntsgewijze opsomming.

## 3. De gouden vondst: Marloes' conceptcommentaar naast de AI

Eén geleverd bestand bleek Carlijns volledige inzending te bevatten met **Word-comments van zowel Marloes zelf (een eerder conceptcommentaar) als van de AI**, op dezelfde zinnen. Rechtstreeks vergelijkbaar:

| Passage | Marloes (kort, vaak een vraag) | AI (lang, dicterend) |
|---|---|---|
| Anamnese-opening | "is niet helemaal lekker verwoord ;)" (6 woorden) | Volledige uitlegzin waarom de alinea goed is |
| Klinisch dilemma | "En waarom wil je geen labrum laesie missen? Wat is er zo belangrijk aan dat de test niets mist?" | Twee lange, sturende zinnen die het argument bijna voorschrijven |
| Artikelkeuze | "En hoeveel papers heb je in totaal gevonden?" (8 woorden) | Vergelijkbare zorg, maar in een dicterende paragraaf |
| Bottom line | "Nog een beetje vaag geformuleerd, ga je hem nu wel of niet gebruiken en erop vertrouwen?" | Lange herschrijfinstructie |
| Bronvermelding-typo | (geen commentaar, te klein) | Volledige grammaticales over één woord ("is gebruikt gemaakt" → "is gebruikgemaakt") |

**Kernvondst:** Marloes ziet vaak exact hetzelfde als de AI (het "hoeveel papers"-voorbeeld is bijna letterlijk wat de AI later ook opmerkte), maar haar officiële eindoordeel op diezelfde criteria is gewoon Voldaan. Het verschil zit niet in WAT er gezien wordt, maar in de **conversie** van een gevonden gaatje naar een verdict: bij Marloes blijft het groeifeedback binnen een voldoende, bij de AI wordt het een fail. Dit is het drempel-mechanisme uit `reference.md` punt 4.

Gemiddelde lengte: Marloes ~8-10 woorden per opmerking, AI ~40 woorden. Nooit veranderd, ook niet na de modelinstructies-fix (zie sectie 7).

## 4. Baseline AI-uitkomst en de mismatches

| Criterium | Jurre: AI | Jurre: Marloes | Carlijn: AI | Carlijn: Marloes |
|---|---|---|---|---|
| Algemeen | PASS | Voldaan | PASS | Voldaan |
| Klinisch scenario | PASS | 2/3 (borderline) | **FAIL** | Voldaan |
| Klinische vraagstelling | **FAIL** | Voldaan | PASS | Voldaan |
| Zoekstrategie | **FAIL** | Voldaan | **FAIL** | Voldaan |
| Kritische evaluatie kwaliteit | PASS | Voldaan | onbekend | Niet voldaan |
| Evidentietabel | PASS | Voldaan | onbekend | Niet voldaan |
| Commentaar | PASS | Voldaan | onbekend | gemengd |
| Kernconclusie | **FAIL** (16% gewicht) | Voldaan | onbekend | Voldaan |

Zoekstrategie is de enige mismatch die bij **beide** studenten terugkomt, dus de meest zekere hotspot. De overige mismatches verschillen per student (elk hun eigen zwakke plek), wat past bij het drempel-mechanisme: niet één specifiek criterium is fout geformuleerd, het patroon (elk gevonden gaatje wordt een fail) kan overal opduiken.

**Reden per mismatch** (uit de AI's eigen "Algemene feedback"-tekst, nooit geraden):
- Klinisch scenario (Carlijn): wilde een expliciete differentiaaldiagnose ("vergelijk met perifere zenuwproblematiek en andere oorzaken"), terwijl de rubric-tekst "hypotheses" in meervoud gebruikt en één onderbouwde hypothese in de praktijk voldoende is.
- Zoekstrategie (Carlijn): wilde de 5 afgevallen artikelen apart benoemd, niet alleen de gekozen.
- Zoekstrategie (Jurre): wilde een systematische vergelijking patiënt-vs-populatiecriteria, ook al was de zoekstrategie zelf "goed controleerbaar".
- Kernconclusie (Jurre): vond de conclusie "te voorwaardelijk", wilde een decisievere, minder gehedgede aanbeveling.

**Doodlopende hypothese: onderwijsniveau.** Eduface had een instelling "Selecteer onderwijsniveau" (Universiteit Master/Bachelor, HBO, MBO 1-4) die op "Universiteit Master" stond, terwijl Breederode een Hogeschool is (geen Universiteit). Getest door dit naar HBO te zetten en Carlijn opnieuw te laten beoordelen: **geen enkel verschil in verdict**. Verklaring achteraf: het programma heet zelf "MSc Manuele Therapie" (bevestigd via een ChatGPT-zelfcheck van Jurre, bijgevoegd als bijlage in zijn inzending), dus geen van de 7 opties in de dropdown dekt "post-HBO professionele MSc" goed, en de echte oorzaak lag toch al in de rubric-tekst, niet in dit soort instellingen.

## 5. De rubric-tekst fix (variant "rubric")

Alle 8 criteria zijn hieronder ongewijzigd tenzij anders vermeld; alleen de 4 met bewijs voor een mismatch zijn aangepast (surgisch, niet de hele rubric preventief herschreven).

**Klinisch scenario** — toegevoegd aan het eind van de Voldoende-tekst:
> "Eén onderbouwde hypothese is voldoende; een expliciete vergelijking met alternatieve diagnoses of andere mogelijke oorzaken wordt niet vereist. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."

**Klinische vraagstelling** — toegevoegd:
> "De onderbouwing van de prior kans hoeft niet uitputtend te zijn of elke tegenstrijdige bevinding te bespreken; een plausibele, beargumenteerde schatting op basis van een redelijke bron is voldoende. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."

**Zoekstrategie** — toegevoegd:
> "Dit hoeft niet uitputtend: een beknopte, beargumenteerde vergelijking op de belangrijkste kenmerken volstaat. Het is niet vereist om afgevallen artikelen apart te bespreken of te vermelden hoeveel artikelen er in totaal gevonden zijn; een gemotiveerde keuze voor het gekozen artikel is voldoende. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."

**Kernconclusie** — toegevoegd, plus een correctie ("volgens de beoordeling" → "volgens de student", een vertaalfout in de auto-gegenereerde tekst die niet aansloot bij het origineel):
> "...wat volgens **de student** de beste volgende stap in het diagnostische traject is. Een conclusie mag genuanceerd zijn of onder voorbehoud wanneer de evidentie daar aanleiding toe geeft, zolang er wel een concrete volgende stap genoemd wordt. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."

Algemeen, Kritische evaluatie kwaliteit, Evidentietabel en Commentaar: bewust **niet** aangepast, geen bewijs voor een probleem op het moment van schrijven (Kritische evaluatie kwaliteit had bij Carlijn wel een mismatch, maar in de andere richting: AI te soepel waar Marloes streng was, en zonder AI-tekst om te diagnosticeren is dat bewust open gelaten in plaats van gegokt).

## 6. De modelinstructies-tekst (variant "instructies")

Geschreven als lopende tekst (geen kopjes, zie `reference.md` punt 7), met een woordlimiet-instructie voor Algemene feedback:

> "Feedback wordt gegeven op een CAT (Critically Appraised Topic) diagnostiek, onderdeel van de post-HBO vervolgopleiding manuele therapie. De student is een werkend fysiotherapeut die een diagnostische vraag uit de eigen praktijk uitwerkt: klinisch scenario, klinische vraag, literatuuronderzoek, kritische beoordeling van één artikel, en een praktijkvertaling naar de eigen patiënt. Dit is professioneel toegepast werk voor ervaren clinici, geen wetenschappelijk onderzoeksartikel, dus verwacht geen academische uitputtendheid maar vakbekwame, praktijkgerichte redenering.
>
> Schrijf de algemene feedback per criterium kort, in maximaal 50 woorden, zoals een ervaren, drukke docent die net het werk gelezen heeft. Begin met wat goed ging, benoem daarna alleen het belangrijkste verbeterpunt. Cijfers komen niet voor.
>
> Schrijf inline opmerkingen in 1 tot 2 zinnen, vaak als vraag in plaats van als kant-en-klare instructie. Laat de lengte van de opmerking passen bij het gewicht van het punt.
>
> Houd de beoordelingsstrengheid normaal, met deze toelichting: een criterium is Voldoende zodra de kern overtuigend is uitgevoerd, ook met kleine gaten. Een gevonden verbeterpunt is groeifeedback, geen automatische reden voor Onvoldoende. Alleen Onvoldoende bij een onbeantwoorde kernvraag, een ontbrekend verplicht onderdeel, of een feitelijk foute redenering."

**Wat hiervan overleefde na "Opnieuw genereren"** (twee testrondes, zelfde resultaat beide keren): Context bleef grotendeels intact. Algemene feedback behield structuur/lengte/toon-beschrijving. **Inline opmerkingen verdween volledig**, geen spoor in de gegenereerde modelinstructies. **Beoordelingsstrengheid werd leeg** ("De gevraagde beoordelingsstrengheid is al toegepast", zonder inhoud), met een verdunde versie van de drempel-regel die in plaats daarvan onder Algemene feedback opdook. De 50-woorden-limiet werkte wel (gemeten: 41 woorden op een steekproefcriterium).

## 7. Resultaten van alle 4 varianten

| Criterium | Marloes: Jurre | Baseline: Jurre | Rubric: Jurre | Instructies: Jurre | Beide: Jurre | Marloes: Carlijn | Baseline: Carlijn | Rubric: Carlijn | Instructies: Carlijn | Beide: Carlijn |
|---|---|---|---|---|---|---|---|---|---|---|
| Algemeen | Voldaan | PASS | PASS | PASS | PASS | Voldaan | PASS | PASS | PASS | PASS |
| Klinisch scenario | 2/3 | PASS | PASS | PASS | PASS | Voldaan | FAIL | PASS | FAIL | PASS |
| Klinische vraagstelling | Voldaan | FAIL | PASS | FAIL | PASS | Voldaan | PASS | PASS | PASS | PASS |
| Zoekstrategie | Voldaan | FAIL | PASS | FAIL | PASS | Voldaan | FAIL | FAIL | FAIL | **PASS** |
| Kritische evaluatie kwaliteit | Voldaan | PASS | PASS | PASS | PASS | Niet voldaan | ? | PASS | PASS | PASS |
| Evidentietabel | Voldaan | PASS | PASS | PASS | PASS | Niet voldaan | ? | PASS | PASS | PASS |
| Commentaar | Voldaan | PASS | PASS | PASS | PASS | gemengd | ? | FAIL | PASS | **PASS** |
| Kernconclusie | Voldaan | FAIL | FAIL | FAIL | **PASS** | Voldaan | ? | FAIL | FAIL | **PASS** |

**Uitkomst: variant "beide" scoort 8/8 op allebei de studenten, exact gelijk aan Marloes' eindoordeel. Variant "rubric" alleen komt op 7/8 (Jurre) en 5/8 (Carlijn). Variant "instructies" alleen verandert geen enkel verdict ten opzichte van de baseline (0 flips), op geen van beide studenten.**

Mooiste losse bewijs: Kernconclusie/Jurre. Rubric-variant en beide-variant geven bijna identieke kritiek ("een concrete vervolgstap ontbreekt nog"), maar rubric-variant = FAIL, beide-variant = PASS. Zelfde waarneming, ander oordeel: de instructies-toevoeging kantelt hier de conversie, ook al is de tekst verdund.

## 8. De toon-as (los van het oordeel)

Opener van criterium "Algemeen" bij Jurre, alle 4 condities:
- Baseline: "Je deed goed werk met de logische opbouw en heldere uitleg van vaktermen."
- Rubric: "Je deed goed werk met de logische opbouw en de koppeling tussen sensitiviteit, voorafkans en conclusie."
- Instructies: "Je CAT is logisch opgebouwd en de stap van casus naar conclusie is goed te volgen."
- Beide: "Je hebt een duidelijke en logisch opgebouwde CAT geschreven, met helder en professioneel taalgebruik."

Over alle 8 criteria bij Jurre geteld: de opener "Je deed goed werk met/door..." komt voor in baseline 3x, rubric-variant 6x, **instructies-variant 0x, beide-variant 0x**. De modelinstructies zijn dus wat het sjabloonmatige eruit haalt, ongeacht of de rubric is aangepast, exact het spiegelbeeld van de oordeel-as.

Geen van de vier varianten kwam in de buurt van Marloes' eigen korte, vraag-vormige, bij-naam-aansprekende stijl in de Algemene feedback of Opmerkingen-tab, dat bleek via deze route (sectie 6) niet stuurbaar.

## 9. Eindconclusie

Rubric-tekst is de hefboom voor **of het oordeel klopt**. Modelinstructies zijn de hefboom voor **hoe het klinkt**, voor zover die het via de lossy generatiestap redt. Beide los zijn onvoldoende, alleen de combinatie haalde een perfecte match met de echte docent op twee onafhankelijk geteste studenten.
