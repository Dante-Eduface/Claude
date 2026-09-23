# Grading calibration — technische referentie

Diepe uitleg achter de lus in `SKILL.md`. Lees dit voor je daadwerkelijk gaat schrijven of testen.

## 1. Hoe Eduface's beoordelingsconfiguratie werkt

Per vak ("opdracht" in Eduface) zit er een losse koppeling tussen een rubric en modelinstructies. Kopieer je een bronbestand naar een nieuwe opdracht, dan krijgt die zijn eigen (opnieuw gegenereerde) rubric en start met de default modelinstructies. Wil je varianten los van elkaar testen, moet je dus losse opdrachten aanmaken.

**Beoordeling-tab (rubric):** per criterium een gewicht (%, hoeft niet gelijk verdeeld, zwaardere criteria als de kernconclusie kunnen een hoger gewicht krijgen) plus een los te bewerken tekst per niveau. Klik op het vakje om te bewerken.

Er zijn **twee rubrictypes** (bevestigd 23-09-2026):

- **Binair**, twee vakjes: Fail-tekst + Pass-tekst. Gebruikt bij manuele therapie.
- **Descriptive**, vier vakjes: Unsatisfactory / Satisfactory / Good / Great. Gebruikt bij CAT EBP (POH).

Kies het type naar het bronformulier: heeft de bron meer dan twee niveaus (bijvoorbeeld puntenkolommen 4/2/0), neem dan Descriptive. Maar leg dan **eerst de zaklijn vast** uit de cesuur van de bron, want vier vakjes over drie bronniveaus verdelen is een keuze die niemand expliciet maakt en die stilzwijgend de hele schaal kan verschuiven. Zie de case study CAT EBP (POH), sectie 3 en 6.

**Feedback-tab (modelinstructies):** een vrij tekstveld "Beschrijf je feedbackstijl" ("Vertel Eduface hoe de AI-feedback moet klinken"), met een knop "Opnieuw genereren" die er de modelinstructies uit genereert. "Bekijk modelinstructies" toont het resultaat, altijd in dezelfde vaste structuur:

- **Context** — wat voor tekst wordt hier beoordeeld
- **Feedbackstijl en toon**
  - **Algemene feedback** — wat de feedback behandelt en hoe die geschreven wordt
  - **Inline opmerkingen** — wat opmerkingen bij passages behandelen en hoe
- **Beoordelingsstrengheid**
  - **Gegenereerde beoordelingsstrengheid** — lijkt structureel een kort label-veld ("normaal"), geen paragraafveld, zie punt 4 hieronder

**Modelinstructies zijn nooit rechtstreeks bewerkbaar** (bevestigd door Dante, 22-09-2026). De enige weg is de vrije tekst plus opnieuw genereren, en dat is een aparte AI-generatiestap die comprimeert, herformuleert en soms secties laat vallen. Zie punt 4.

**Output per inzending:** drie tabs. **Feedback** (algemene feedback per rubriekcriterium), **Opmerkingen** (inline comments op gemarkeerde tekst in het document), **Beoordeling** (per-criterium Voldoende/Onvoldoende plus een "Eindresultaat"-dropdown). Die dropdown moet de docent **handmatig** kiezen voor ze de inzending als voltooid kan markeren, dat is geen automatische optelsom van de gewogen criteria (bevestigd door Dante, 22-09-2026). Optimaliseer dus nooit op de gewogen som, alleen op de losse criteria.

**Export:** de knop "Inzendingen" op een opdracht levert een zip met per student een map met daarin een `..._Feedback_Summary.pdf` (bucket-verdicts + gewicht + algemene feedback tekst per criterium) en een `..._Comments.docx` of `.pdf` (het brondocument met alle inline comments erin, AI en eventueel al bestaande docent-comments samen).

## 2. Materiaal-checklist, met waarom

| # | Wat | Waarom |
|---|---|---|
| 1 | Origineel beoordelingsformulier (PDF/Word) | De bron-checklist waar de rubric ooit uit vertaald is. Zonder dit weet je niet of Eduface's rubric-tekst een trouwe of een afgezwakte/verscherpte vertaling is. |
| 2 | Schrijfformat/instructiedocument voor studenten, met uitgewerkt voorbeeld | Legt de WAAROM achter elke stap uit, vaak met nuance die het kale beoordelingsformulier niet geeft (bijv. het verschil tussen twee stappen die oppervlakkig op elkaar lijken). |
| 3 | Minstens 2 echte studenteninzendingen | Eén inzending is een casus, twee is het begin van een patroon. Kies bij voorkeur inzendingen die de docent uiteindelijk liet **slagen**, dat is het eerste dat moet kloppen. |
| 4 | De officiële beoordeling van de docent op diezelfde inzendingen (Voldaan/Niet voldaan per criterium + haar geschreven eindfeedback) | De ground truth waar je de AI tegen toetst. Zonder dit vergelijk je de AI met je eigen aanname, niet met de werkelijkheid. |
| 5 | De docent's eigen losse conceptcommentaar op de inzending (Word track-changes-achtige comments), als dat bestaat | Verreweg de rijkste bron. Laat zien of de docent hetzelfde ziet als de AI maar het anders weegt (drempel-probleem, zie punt 5) of iets heel anders ziet (inhoudelijk rubric-probleem). Vraag hier expliciet naar, Dante levert dit soms pas als je zelf niet doorvraagt. |
| 6 | De huidige, live rubric + modelinstructies in Eduface voor dat vak | Het startpunt. Kopieer de rubric-tekst letterlijk over naar je eigen bestand voor je iets aanpast, zie punt 6. |
| 7 | De huidige AI-uitkomst voor diezelfde inzendingen onder de huidige configuratie | De baseline waar je de mismatches uit haalt. |

## 3. Annotaties/comments technisch uitlezen

De platte tekst-extractie (Read-tool op een PDF, of een docx converteren) laat inline comments/annotaties NIET zien, alleen een icoontje op de plek. Je moet ze apart uitlezen.

**PDF:** `pypdf` (Python). Zat in dit environment niet standaard geïnstalleerd:
```bash
pip3 install pypdf cffi
```
`cffi` is nodig, anders crasht de `cryptography`-import van pypdf met een Rust-panic. Comments zitten in `page["/Annots"]`, elk object heeft `/Subtype` (`/Text` = sticky note van een mens, `/Highlight` = gemarkeerde tekst met een comment erbij, vaak van AI), `/T` (auteur) en `/Contents` (de tekst). Let op: filter niet alleen op `/Text`, AI-comments zitten soms als `/Highlight`.

**DOCX:** pandoc en python-docx staan niet standaard geïnstalleerd, en pip-install van pandoc werkt niet (het is geen python-package). Fallback: unzip het bestand, lees `word/document.xml` (platte tekst en tabellen, via `xml.etree.ElementTree`) en `word/comments.xml` (de commentaartekst zelf, met auteur). Koppel een comment aan zijn plek in de tekst via `w:commentReference`/`w:id` in `document.xml`.

**Daal daarbij recursief af in `w:sdt`** (content controls). Een parser die alleen de directe kinderen van `w:body` langsloopt, slaat elk hoofdstuk over dat in een content control staat, en dat zijn er in studentverslagen met een automatische inhoudsopgave vaak meerdere. Bij CAT EBP (POH) scheelde dat 1.100 woorden en de complete Inleiding plus Aanleiding, waardoor het materiaal ten onrechte incompleet leek. Controleer altijd het woordenaantal tegen wat je op het oog van het document verwacht.

## 4. De twee-assen diagnose

Een AI-verdict dat niet matcht met de docent kan drie verschillende oorzaken hebben, en ze vragen andere fixes:

1. **De rubric-tekst vraagt letterlijk meer dan de docent in de praktijk eist.** Voorbeeld: een rubric die "hypotheses" in meervoud noemt, waardoor de AI een differentiaaldiagnose verwacht, terwijl één onderbouwde hypothese in de praktijk voldoende is. **Fix: rubric-tekst.**
2. **De AI ziet exact hetzelfde als de docent, maar zet het om in een fail waar de docent het als groeifeedback behandelt.** Dit bewijs je door de AI's eigen "Algemene feedback"-tekst naast de docent's eigen conceptcommentaar te leggen: vaak zijn het letterlijk dezelfde observaties. **Fix: instructies (Beoordelingsstrengheid/drempel).**
3. **De toon klopt niet** (te lang, te formeel, te prescriptief, herhaalt lof, geeft een grammaticales voor een typo), los van of het oordeel klopt. **Fix: instructies (Feedbackstijl en toon).**

Vraag altijd eerst de AI's eigen tekst op voor je een oorzaak claimt. Raden kost een testronde.

## 5. Rubric-tekst fixes schrijven

Patroon: voeg aan het **einde van de Voldoende-tekst** een zin toe die expliciet afbakent wat NIET vereist is, plus een generieke drempel-zin:

> "[Specifieke ontsnapping voor de gevonden overstrengheid]. Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."

Voorbeeld uit manuele therapie (Zoekstrategie): *"Dit hoeft niet uitputtend: een beknopte, beargumenteerde vergelijking op de belangrijkste kenmerken volstaat. Het is niet vereist om afgevallen artikelen apart te bespreken of te vermelden hoeveel artikelen er in totaal gevonden zijn."*

Raak de Onvoldoende-tekst meestal niet aan, tenzij die zelf een woord bevat dat een te strenge lezing uitlokt. Let op woorden als "navolgbaar" of "expliciet" die Eduface's eigen regeneratie er soms zelf insmokkelt, die zijn een signaal, geen neutraal woord.

**Belangrijk:** gebruik voor elke opdracht, baseline én elke variant, exact dezelfde vaste rubric-tekst als basis. Nooit een vers gegenereerde versie als "onveranderd"-controle gebruiken, want die is elke keer anders (zie punt 6).

## 6. Waarom je nooit op een verse auto-generatie mag vertrouwen

Bevestigd bij manuele therapie: hetzelfde bronbestand twee keer via Eduface's eigen PDF-naar-rubric conversie laten lopen gaf **elke keer andere bewoording**, ook al was de betekenis grotendeels hetzelfde. Concreet verschil: de tweede generatie introduceerde het woord "navolgbaar" bij Zoekstrategie, dat in de eerste versie nergens stond, en verving op meerdere plekken "duidelijk" door "expliciet" (een net strenger woord). Ook een kleine, feitelijke correctie kwam er de tweede keer beter uit (Kernconclusie: "wat volgens de beoordeling" werd "wat volgens de student", wat beter aansluit bij het origineel).

Consequentie: als je baseline en een testvariant allebei "vers gegenereerd" zijn, weet je nooit of een verschil in uitkomst van je eigen wijziging komt of van ruis in de generatiestap. Plak daarom bij elke opdracht dezelfde, letterlijke, door jou vastgestelde tekst.

## 7. Modelinstructies schrijven, gegeven de lossy pipeline

Vastgestelde patronen (twee testrondes bij manuele therapie, beide keren hetzelfde resultaat):

- **Concrete voorbeeldzinnen overleven nooit**, ook niet met een expliciete "gebruik deze zin letterlijk"-instructie ervoor.
- **Bij twee vergelijkbare elementen (zoals twee voorbeeldzinnen) lijkt de generator er één te kiezen en de rest te laten vallen.** Geef dus maar één voorbeeld, niet twee.
- **De "Inline opmerkingen"-sectie overleefde in onze tests nooit**, ook niet met een expliciete instructie. Reken erop dat dit stuk via deze route niet te sturen is.
- **"Beoordelingsstrengheid" als los blok overleeft slecht.** Inhoud die daar hoort (de drempel-regel) dook in onze tests verdund op onder "Algemene feedback" in plaats van in een eigen paragraaf, en het "Beoordelingsstrengheid"-veld zelf bleef een kort label ("normaal" of zelfs een contentloze bevestigingszin). Waarschijnlijk is dit structureel een kort label-veld, geen paragraafveld.
- **Wat wel opleverde:** een dichte, compacte tekst, met een "BELANGRIJK: vat niet samen, laat geen van de vier onderdelen weg"-instructie vooraan, en een harde woordlimiet voor Algemene feedback (50 woorden werkte: hield de verdicts intact bij een hertest én maakte de tekst merkbaar minder sjabloonmatig, zie de case study voor het bewijs).

Reken structureel op verlies. Zet je belangrijkste, minst compressiebestendige content niet in het deel dat waarschijnlijk sneuvelt (voorbeelden, Beoordelingsstrengheid-nuance). Context en Algemene feedback overleven het best, dus zet daar de kern.

## 8. Testopzet

Minstens vier opdrachten in Eduface, allemaal gestart vanuit dezelfde vaste rubric-basistekst (zie punt 6):

1. **Baseline** — ongewijzigd, gebruikt om de mismatches te vinden.
2. **Variant rubric** — alleen de rubric-tekst aangepast, modelinstructies ongewijzigd (default).
3. **Variant instructies** — alleen de modelinstructies aangepast via de vrije-tekst route, rubric-tekst = dezelfde vaste basistekst als de baseline.
4. **Variant beide** — de aangepaste rubric-tekst plus dezelfde aangepaste modelinstructies als variant 2.

Voor elke variant: dezelfde studenten opnieuw laten beoordelen (Dante doet dit handmatig in Eduface, geen MCP-toegang), exporteer, vergelijk.

## 9. Wat we bij manuele therapie vonden over welke variant wint

- **Rubric-tekst stuurt vooral OF het oordeel klopt.** De rubric-only variant loste de meeste, maar niet alle, verkeerde Onvoldoendes op.
- **Modelinstructies sturen vooral HOE het klinkt.** De instructies-only variant veranderde in onze test **geen enkel verdict** (0 flips op 2 studenten), precies omdat Beoordelingsstrengheid en Inline opmerkingen niet doorkwamen (punt 7), maar maakte de "Algemene feedback"-tekst wel meetbaar minder sjabloonmatig (het herhaalde "Je deed goed werk met..."-opener verdween volledig).
- **Alleen de combinatie won op beide assen tegelijk.** Verwacht dit patroon opnieuw bij een volgend vak, maar neem het niet zomaar aan, toets het net zo hard.
- Volledige tabellen, teksten en het exacte bewijs (de vergelijking van Marloes' eigen Word-comments naast de AI's comments op dezelfde zinnen) staan in `examples/manuele-therapie-case-study.md`.
