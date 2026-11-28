# Eduface instrueren: hoe het werkt en wat we weten

_Laatst bijgewerkt: 2026-11-28._

Voor Dante, bij elke nieuwe opdracht die in Eduface komt. Gebaseerd op twee testrondes: Breederode (22 en 23 september 2026, twee vakken) en Academica (27 en 28 november 2026, één student, vijf runs). Dit document gaat over bedienen en instrueren. Voor wat we naar klanten mogen claimen blijft `Platform/product.md` de bron.

Elk punt heeft een bewijsniveau:

- **[Bevestigd]**: door Dante of in `product.md`.
- **[Waargenomen]**: in onze tests gezien, met erbij hoe vaak. Meestal één student, dus een aanwijzing en geen bewijs.
- **[Onbekend]**: niet getest. Niet aannemen.

## 1. De zeven regels

1. **Controleer eerst of het document bij de rubric hoort.** Past het niet, dan geeft Eduface toch vol vertrouwen een uitkomst.
2. **De rubric en het document bepalen het oordeel. De modelinstructies sturen vooral toon en lengte.** Wil je het oordeel verschuiven, ga dan niet bij de instructies zitten.
3. **Controleer de Context na elke generatie.** Eduface vult die zelf in en kan het verkeerde genre kiezen.
4. **Elke Regenerate is een nieuwe prompt.** Plak altijd de volledige tekst, nooit alleen een aanvulling.
5. **Harde regels werken, vage wensen niet.** "Nooit", "maximaal 50 woorden" en "elke opmerking bevat een verbeterpunt" hebben effect. "Wees kritisch" niet.
6. **De docent is de maatstaf.** Maak eerst je eigen beoordeling, blind, en leg die daarna naast Eduface en naast de scores van de docent.
7. **Verander één ding per run, en meet eerst de ruis.** Draai dezelfde instellingen twee keer voor je een verschil toeschrijft aan je wijziging.

## 2. Hoe een opdracht in elkaar zit

| Onderdeel | Wat het doet | Stuurt |
|---|---|---|
| Rubric (criteria, gewichten, niveauteksten) | Het oordeel per criterium | Oordeel |
| Beoordelingsstijl (Pass/Fail, Descriptive, Points 1-10) | Het aantal vaste niveaus | Oordeel |
| Beoordelingstype (Formative, Summative) | Wanneer de beoordeling gebruikt wordt | Oordeel en feedback |
| Wat er per inzending gegenereerd wordt | Algemene feedback per criterium (met maximaal aantal woorden), algemene feedback op de hele opdracht (aan of uit), specifieke opmerkingen per criterium | Vorm van de uitvoer |
| Modelinstructies: Context, Algemene feedback, Inline opmerkingen, Beoordelingsstrengheid | Hoe de feedback klinkt en wat Eduface denkt dat het leest | Toon, lengte, genre |
| Pillen (instructie per rubric-criterium, in het tekstveld) | Instructie voor één criterium | [Onbekend] |
| Export | `Feedback_Summary.pdf` en `Comments.pdf` met de inline opmerkingen als annotaties | Wat wij analyseren |

- **Modelinstructies zijn niet direct bewerkbaar [Bevestigd, Dante 22-09].** Je schrijft tekst in "Beschrijf je feedbackstijl", klikt op Regenerate en Eduface genereert er de vier onderdelen uit. "Bekijk modelinstructies" toont het resultaat.
- **Het eindoordeel is bij Breederode een handmatige keuze van de docent [Bevestigd, Dante 22-09].** Optimaliseer op de losse criteria, niet op de gewogen som.
- **Een drieniveau-rubric wordt vier niveaus [Waargenomen, Academica].** Laura's rubric had 0, 1 en 2 punten. Eduface maakte er vier niveaus van, en niet overal op dezelfde manier. Bij sommige criteria komt er een nieuw tussenniveau tussen Onvoldoende en Voldoende, bij andere een nieuw topniveau boven Goed. Reken de niveaus **per criterium** om voor je vergelijkt met de docent.
- **Een rubric als afbeelding-pdf is ingelezen [Waargenomen, Academica].** Twee rubrics zonder tekstlaag kwamen in Eduface als volledige criteria met niveauteksten terecht.
- **De bestandsnaam wordt de titel van de inzending in de export [Waargenomen].** Geef bestanden dus een naam met de opdracht erin.

## 3. Wat stuurt wat

| Je wilt veranderen | Gebruik | Bewijs |
|---|---|---|
| Het niveau klopt niet | De rubric-tekst, en dat het juiste document bij de rubric zit | Breederode: alleen instructies veranderde 0 verdicts. Alleen rubric kwam op 7 van 8 en 5 van 8 criteria overeen met de docent. Academica: verkeerde combinatie gaf een Uitstekend op een criterium dat niet in het document stond |
| Toon, lengte, lof, openingszinnen | Modelinstructies met harde regels | Academica: losse lof inline ging van 3 van 12 naar 2 van 12 naar 0 van 11. Breederode: 50 woorden haalde de sjabloonopener weg |
| Wat Eduface denkt te lezen | De Context | Academica: de automatische Context zei "academisch essay" voor een ontwerpsjabloon |
| Prioriteit in de feedback | De optie "General feedback on entire assignment" | [Onbekend], nog niet aangezet |

## 4. Bij elke nieuwe opdracht

1. **Verzamel:** de rubric(s), de documenten, en vooral de eigen beoordeling van de docent met scores. Zonder scores kalibreer je niet, je gokt. Zie de skill `grading-calibration` voor de volledige lijst.
2. **Koppel document en rubric.** Lees de criteria en kijk of die onderwerpen echt in het document staan, bijvoorbeeld met een zoekopdracht op termen als kerndoel, leerlijn en toetsing. Hoort een vak twee documenten en twee rubrics, bevestig dan bij de docent welke bij welke hoort. Aannames kosten een testronde.
3. **Geef bestanden een duidelijke naam** (zie punt 2).
4. **Kies de beoordelingsstijl** (zie punt 5).
5. **Stel de uitvoer in.** Beoordelingstype, maximaal aantal woorden per criterium en of de feedback op de hele opdracht aan staat.
6. **Schrijf de instructie** met het sjabloon in punt 6, regenereer, en lees "Bekijk modelinstructies". Controleer de Context.
7. **Eerste run, exporteer en vergelijk** (zie punt 7).

## 5. Beoordelingsstijl kiezen

Dit is de afspraak met Dante van 28-11-2026, geen productfeit.

| De rubric heeft | Kies |
|---|---|
| Alleen 0 of 1 (Onvoldoende, Voldoende) | **Pass/Fail** |
| Vier niveaus (Onvoldoende, Voldoende, Goed, Uitstekend) | **Descriptive** |
| Drie niveaus | **Descriptive** (Eduface maakt er vier van, zie punt 2) |
| Twee systemen onder elkaar: eerst 0/1-randvoorwaarden, daaronder de inhoud in vier niveaus | **Descriptive**, op basis van de inhoud |
| Punten van 1 tot 10 | **Points** (nog niet gebruikt) |

Open: bij Descriptive vallen de 0/1-randvoorwaarden weg. Tijd, omvang en plagiaatscan gaan over het inleveren. APA, structuur, taalgebruik en vormgeving kan Eduface wel beoordelen. Dante heeft nog niet beslist of die erbij komen.

## 6. Modelinstructies schrijven

### Hoe het werkt
- De vrije tekst is de **hele** prompt voor die generatie [Bevestigd, Dante 28-11]. Wat je niet opnieuw meegeeft, is niet gegarandeerd bewaard. Plak dus steeds de volledige tekst.
- Een nieuwe generatie vervangt de vorige: een eerdere versie van de gegenereerde instructies is niet terug te halen [Bevestigd, Dante 28-11]. Bewaar je eigen tekst dus buiten Eduface. Of er toch iets van de oude tekst doorwerkt, is **[Onbekend]**.
- Instructies horen bij één opdracht. Wil je een instructie testen zonder de huidige te verliezen, maak dan een tweede opdracht. Een nieuwe opdracht start met de standaardinstructies [Waargenomen, Breederode].
- De generatiestap comprimeert [Waargenomen, Breederode]. Voorbeeldzinnen overleven niet en bij twee voorbeelden blijft er één over. Geef er dus één.
- Breederode zei dat de sectie Inline opmerkingen niet doorkwam en dat Beoordelingsstrengheid een kort label blijft. Bij Academica veranderden de inline opmerkingen wel mee met de instructie (geen lof meer, maximaal twee korte zinnen). We hebben de gegenereerde tekst niet teruggelezen, dus waarom is **[Onbekend]**.

### Wat werkte
1. **Zeg wat voor tekst het is en wat het niet is** (bijvoorbeeld "geen academisch essay, dus geen betoog en geen bronnen"). In de run met de automatische Context vroeg een opmerking om een betrouwbare bron, in de vier runs erna niet. Die eerste run had ook de verkeerde rubric, dus het is niet zuiver [Waargenomen].
2. **"Beoordeel alleen wat de student zelf heeft opgeschreven. Leg geen verbanden die de student niet zelf heeft gelegd."** Kerndoelen ging van Goed naar Voldoende [Waargenomen, 1 run].
3. **"Zorg dat het niveau past bij je eigen feedback."** Leerdoelen methode ging van Uitstekend naar Goed. Eduface schreef er zelf bij dat de opbouw nog niet zichtbaar was en gaf toch het hoogste niveau [Waargenomen, 1 run].
4. **"Kies het hoogste niveau alleen als de tekst de omschrijving aantoonbaar haalt."**
5. **Harde woordlimiet bij de algemene feedback** (50 woorden) [Waargenomen, Breederode: de sjabloonopener verdween. Bij Academica staat het als instelling en bleef de feedback daaronder].
6. **Voor inline opmerkingen: "elke opmerking bevat een verbeterpunt, nooit alleen iets positiefs"** [Waargenomen, 0 van 11 losse lofopmerkingen].
7. **"Maximaal twee korte zinnen, één punt per opmerking, hetzelfde punt één keer."**

### Wat niet werkte
- Instructies die het **oordeel** moeten verschuiven. Het niveau werd vooral bepaald door rubric en document.
- Voorbeeldzinnen en vage wensen ("wees kritisch").
- Een eigen paragraaf voor Beoordelingsstrengheid.
- "Maximaal twee korte zinnen" hielp niet bij de verkeerde rubric: opmerkingen werden gemiddeld 47 woorden, tot 79. Bij de goede rubric bleven ze onder de 48. De lengte hangt dus ook aan wat de rubric vraagt.

### Sjabloon (invullen en plakken)

```
De opdracht is [soort tekst] van [wie, welk niveau]: [onderwerp in één zin]. Het is geen [wat het niet is]. Er is dus geen [wat niet nodig is]. Beoordeel of [waar het om gaat].

Beoordeel alleen wat de student zelf heeft opgeschreven. Controleer eerst of een onderdeel echt in het ingeleverde document staat voordat je een niveau kiest. Neem niet aan dat het elders staat, vul niets zelf in en leg geen verbanden die de student niet zelf heeft gelegd. Geef daar ook geen lof voor. [Alleen voor ontwerp- of planningsdocumenten: Controleer of de onderdelen onderling overeenkomen en benoem verschillen concreet.] Gebruik de niveaus van de rubric letterlijk en kies Uitstekend alleen als de tekst de omschrijving aantoonbaar haalt. Zorg dat het niveau past bij je eigen feedback: als je schrijft dat iets nog niet duidelijk, onvolledig of niet zichtbaar is, geef dan niet het hoogste niveau.

Algemene feedback per criterium: maximaal 50 woorden. Begin met wat bij dit specifieke criterium goed is en verwijs naar een concreet onderdeel uit de tekst. Geef daarna het ene belangrijkste verbeterpunt. Geen lof over andere criteria en geen standaardzinnen. Noem het cijfer of het niveau niet in de feedbacktekst. Toon: [toon en doelgroep].

Inline commentaar: elke opmerking bevat een verbeterpunt. Schrijf nooit een opmerking die alleen iets positiefs zegt. Maximaal twee korte zinnen, over één punt per opmerking. Zeg wat er beter kan en waarom. Benoem hetzelfde punt maar één keer. Vraag niet om onderdelen die de opdracht niet vraagt. Dezelfde toon als hierboven.
```

Bewaar de uiteindelijke tekst per opdracht in de map van het account, zodat je hem de volgende keer niet opnieuw hoeft te bedenken.

## 7. Testen en vergelijken

1. **Maak eerst je eigen beoordeling, blind.** Zodat de uitkomst van Eduface je niet beïnvloedt. Reken die om naar Eduface's niveaus.
2. **De docent is de maatstaf.** Mijn eigen beoordeling is een schatting. Bij Academica ontbreken Laura's scores nog.
3. **Gebruik voor elke variant dezelfde vaste rubric-tekst.** Eduface's eigen pdf-naar-rubric vertaling is elke keer anders [Bevestigd, Breederode].
4. **Verander één ding per run.** Meet ruis met een herhaalrun op dezelfde instellingen. Dat is bij Academica nog niet gedaan.
5. **Minstens twee studenten.** Bij Academica is er maar één, dus alles hieronder is voorlopig.
6. **Beoordeel twee dingen apart:** klopt het oordeel, en klopt de toon. Dat hebben vaak verschillende winnaars.
7. **Lees ook wat Eduface mist.** Controleer of het niveau past bij zijn eigen feedback.
8. **Annotaties uitlezen:** gewone tekstextractie laat inline opmerkingen niet zien. Gebruik `pypdf` op `/Annots`, zie `.claude/skills/grading-calibration/reference.md`, punt 3. De AI-opmerkingen zitten als `/Highlight` met auteur `AI_INSTRUCTOR`.

## 8. Wat Eduface goed en minder goed doet

Waargenomen bij Academica, op één student en vijf runs.

**Goed:**
- Hij vindt tegenstrijdigheden tussen onderdelen, bijvoorbeeld leerdoelen die niet overeenkomen met de toetsing.
- Hij vindt wat niet gedekt wordt, zoals meten en route in de lessen en de toetsing maar niet in de overkoepelende doelen.
- Hij vindt koppelfouten (een lesdoel tot en met 10 gekoppeld aan een leerlijndoel tot 20).
- Hij vond schatten dat niet getoetst werd, wat ik zelf miste.

**Minder goed:**
- **Dezelfde oorzaak bij meerdere criteria.** In de laatste run noemde hij meten en route bij vier criteria apart, zonder te zeggen dat het één probleem is. Elf opmerkingen voelen als elf problemen.
- **Detailtegenstrijdigheden mist hij vaak:** een doelcriterium dat "binnen 3 seconden" zegt terwijl de toets 2 minuten voor 20 sommen geeft, "begrijpen en gebruiken" in één leerdoel, en doelen die in geen enkele les voorkomen.
- **Hij vult gaten zelf in,** en geeft dan een te hoog niveau (Kerndoelen op Goed).
- **Pagina-einde als ontbrekend:** een kerndoel dat over twee pagina's liep werd waarschijnlijk als "niet volledig" gemeld [Waargenomen, 1 keer].
- **Hoge niveaus bij ontbrekende informatie** als het verkeerde document bij de rubric zit.
- **Stijl:** alleen opdrachten ("Voeg toe", "Neem op", "Koppel"), geen vragen, en rubric-taal als "traceerbaar" en "controleerbaar".
- **Stabiliteit:** vier van de zeven niveaus bleven in drie runs gelijk. Een vijfde wiebelde. Ruis is niet apart gemeten.

## 9. Nog te testen

1. Werkt er na een Regenerate nog iets door van de eerdere instructies? (Dat een oude versie niet terug te halen is, is bevestigd.)
2. Blijven pillen bestaan na een Regenerate, en hebben ze effect op het oordeel?
3. Hoeveel ruis zit er in dezelfde instellingen (herhaalrun)?
4. Helpt "General feedback on entire assignment" tegen de herhaling bij meerdere criteria?
5. Zit Eduface op vijf van de zeven criteria echt een niveau te streng, of ligt het aan mijn lezing? Antwoord: Laura's scores.
6. Gelden deze uitkomsten ook voor een tweede student en een ander vak?
7. Is het pagina-einde-probleem reproduceerbaar, en lost een regel erover het op?
8. Waarom werkte de Inline-sectie bij Academica wel en bij Breederode niet?

## 10. Bronnen

- Skill `grading-calibration`: `.claude/skills/grading-calibration/reference.md` en de case study Manuele therapie (Breederode).
- Academica-test: Drive, Accounts, Academica, Test dag. Opdracht: Lessenserie ontwerpen, Laura Wildemann.
- `Platform/product.md` voor productclaims.
