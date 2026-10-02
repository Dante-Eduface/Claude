# Privacykennis over het Eduface-platform

_Laatst bijgewerkt: 2026-10-02. Beheerder: Jeroen van Gessel._

Opgebouwd uit de concept-verwerkersovereenkomst (SURF-model 4.0) en wat Jeroen daarover in de chat heeft bevestigd. De kennis staat per onderwerp, niet per artikel. Het origineel staat in `Archive/privacy-it-2026-10/dpa-surf-4-0-artikelsgewijs.md`, alleen openen als de letterlijke clausule ertoe doet.

Status per feit: **BEVESTIGD** = door Jeroen genoemd met datum. **TOEGEZEGD** = staat in de concept-DPA, niet apart bevestigd. **OPEN** = zie onderaan. Alles geldt voor de Enterprise-versie en voor Paper Grader en Exam Grader. Orale examens en Academic Integrity (beta) zijn niet vastgelegd.

## 1. Rollen

- De instelling is Verwerkingsverantwoordelijke, Eduface is Verwerker. Eduface is de handelsnaam van Blockbook B.V., Europalaan 93, Utrecht.
- Eduface verwerkt alleen in opdracht van de instelling, volgens haar schriftelijke instructies en alleen voor het afgesproken doel. Is een instructie in strijd met de wet, dan meldt Eduface dat meteen.
- Jeroen van Gessel is contactpersoon voor privacy en datalekken (jeroen.van.gessel@eduface.me).
- De PLG-versie (gratis accounts) is hier niet beschreven.

## 2. Welke gegevens

- **Studentopdrachten, rubrics, beoordelingsformulieren, lesmateriaal.** Tekst van opdrachten kan indirect persoonsgegevens bevatten, soms een naam in de documentkop of de metadata.
- **Betrokkenen:** studenten en docenten.
- **Gegenereerde feedback:** het model zet er zelf geen persoonsgegevens in. Voegt een docent er een naam of ander persoonsgegeven aan toe, dan staat dat er wel in. BEVESTIGD 02-10-2026.
- **Kwaliteitsfeedback** (duim omhoog of omlaag op AI-content, door docenten): anoniem en permanent geanonimiseerd, er is geen bewaartermijn voor persoonsgegevens nodig.
- **Audit logs** worden opgeslagen als onderdeel van de verwerking op Azure.

## 3. Hoe data door het platform beweegt

1. Upload van studentwerk, versleuteld tijdens transport.
2. Bij een gescande of afbeeldingsopdracht leest Google Cloud OCR de tekst uit. BEVESTIGD 02-10-2026: gebruikt, in de EU.
3. AI-verwerking op Azure: rubric analyseren, verrijken via RAG, gerichte feedback per criterium genereren, uitlegbare cijferopbouw.
4. De docent leest, past aan en geeft vrij, met rechten per rol. Pas daarna ziet de student iets.
5. Feedback gaat terug het leerproces in.

- Het model is een eigen model, geen API van een extern foundation model (`Platform/product.md`).
- Instellingen blijven van elkaar gescheiden, geen blootstelling tussen instellingen.

## 4. Hosting en verwerkers

| Verwerker | Wat | Waar |
|---|---|---|
| Microsoft Azure | Hosting van de AI-verwerking: compute, database, opslag. Documenten, rubrics, feedbacktekst, audit logs. | "Nederland + EU". Exacte regio OPEN (V1). |
| Google Cloud | OCR van geüploade documenten en afbeeldingen. | europe-west4 (Eemshaven/Rotterdam). BEVESTIGD. |
| Railway | Databasehosting voor ondersteunende diensten. Interne metadata en tijdelijke verwerkingsgegevens. | Amsterdam. Wat er precies in staat is OPEN (V8). |

- **Alle drie werken voor Eduface alleen met EU-infrastructuur.** BEVESTIGD 02-10-2026. Er gaat niets naar derde landen.
- De instelling geeft algemene toestemming voor deze verwerkers. Eduface blijft volledig aansprakelijk voor wat zij doen en legt hen dezelfde verplichtingen contractueel op.
- **Wijzigen van een verwerker of doorgifte buiten de EER:** Eduface meldt dat schriftelijk, de instelling heeft één maand voor gemotiveerd bezwaar, daarna volgt overleg. Komt er binnen twee maanden geen oplossing, dan kan de instelling opzeggen met één maand opzegtermijn en zonder schadevergoeding. Maakt de instelling geen bezwaar, dan geldt de wijziging als geaccepteerd.

## 5. Bewaren en verwijderen

- **Standaard 8 jaar**, om aan lokale regelgeving te voldoen. BEVESTIGD 02-10-2026.
- **Wordt een opdracht in het Eduface-systeem verwijderd, dan verwijdert Eduface hem ook.** BEVESTIGD 02-10-2026.
- Daarnaast wordt verwijderd op verzoek van de instelling en na afloop van de samenwerking.
- Na afloop van de overeenkomst vernietigt of retourneert Eduface binnen één maand alle persoonsgegevens, ook kopieën bij verwerkers. Kiest de instelling voor teruggave, dan in een gangbaar formaat aan haar of een aangewezen partij. Op verzoek bevestigt Eduface schriftelijk dat dat gedaan is.
- Back-ups zijn automatisch en hebben een beperkte bewaartermijn. Die termijn is niet vastgelegd (V9).

## 6. Training en hergebruik

- **Er wordt niet getraind op studentwerk of instellingsdata.** BEVESTIGD 02-10-2026: "training never happens".
- De instelling houdt eigendom van al het studentenwerk en alle instellingsdata (`Platform/product.md`).
- Let op: de concept-DPA zegt zachter "resultaten worden niet zonder toestemming hergebruikt voor training". Dat is minder sterk dan wat Jeroen zegt. In antwoorden aan een instelling geldt wat Jeroen zegt, in een DPA-tekst zou dit moeten worden aangescherpt. Dat is Jeroens beslissing.

## 7. Menselijke controle

- De docent houdt de regie, "The AI assists. The academic decides." De instelling kiest hoeveel menselijk toezicht ze wil: feedback direct naar de student, of pas nadat de docent hem heeft gelezen en goedgekeurd (`Platform/product.md`). In de interface staat het label "Lecturer + AI" als de docent het heeft bekeken. Let op: `Context/eduface.md` zegt dat de docent elke opmerking goedkeurt, dat is dus een instelling en geen vaste regel.
- Audit trail die voldoet aan de AI Act, voor alle summatieve beoordelingen (`Platform/product.md`).

## 8. Beveiliging

In de concept-DPA staan 14 maatregelen die Eduface toezegt. Per maatregel is niet apart bevestigd dat hij is ingevoerd. Status: TOEGEZEGD.

- Informatiebeveiligings- en privacybeleid dat aansluit op de AVG en op standaarden als ISO 27001/2/18, NOREA of CoBIT. Dat is *aansluiten*, geen certificering.
- Versleuteling in opslag en transport.
- Least privilege en need-to-know, toegang tijdig intrekken, versleuteling voor identificatie en authenticatie.
- Medewerkers geïnformeerd over hun verantwoordelijkheden, en gebonden aan geheimhouding.
- Schriftelijke afspraken met elke verwerker.
- Beleid om datalekken te detecteren, op te lossen en te melden.
- Doorlopend zoeken naar kwetsbaarheden en snel patchen.
- Bescherming van netwerk en systemen tegen misbruik en malware (firewalls, antivirus).
- Fysieke toegangsbeveiliging.
- Logging en monitoring, met passende actie bij niet-legitiem gebruik.
- Aantonen waar gegevens fysiek staan.
- Business continuity en disaster recovery.
- Veilige applicatie-ontwikkeling volgens industriestandaarden (OWASP, BSIMM, NIST).
- Een externe partij mag in overleg audits, kwetsbaarheidsscans en penetratietests uitvoeren. Een responsible disclosure policy of bug bounty is een pre.
- Eduface mag de maatregelen alleen aanpassen aan nieuwere standaarden en nooit onder het afgesproken niveau komen. Wijzigingen meldt zij schriftelijk.

## 9. Datalekken

- Eduface meldt een datalek of redelijk vermoeden daarvan **binnen 48 uur na ontdekking** aan de instelling. Stapsgewijs mag, als niet alles meteen bekend is.
- De melding bevat minimaal wat het Meldloket datalekken van de Autoriteit Persoonsgegevens vraagt.
- Eduface meldt **niet zelf** aan de Autoriteit Persoonsgegevens of aan betrokkenen, tenzij de instelling dat uitdrukkelijk schriftelijk vraagt.
- Eduface neemt zo snel mogelijk maatregelen om de oorzaak weg te nemen en de gevolgen te beperken.

## 10. Medewerking van Eduface

Op verzoek helpt Eduface direct bij:

- verzoeken van betrokkenen (inzage, verwijdering en dergelijke);
- een DPIA en voorafgaande raadpleging van de toezichthouder;
- een DTIA (doorgifte-impactbeoordeling);
- verzoeken van (overheids)instanties.

Krijgt Eduface zelf een overheidsverzoek over de gegevens, dan neemt zij direct contact op met de instelling en volgt haar instructies. Geheimhouding wordt alleen doorbroken als dat nodig is voor de overeenkomst, door de wet, of door een uitspraak van een Nederlandse of andere EU-rechter. Bij een uitspraak van een rechter in een derde land overlegt Eduface eerst met de instelling.

## 11. Audit en aantonen

- **Er is nog geen onafhankelijke audit of certificering.** BEVESTIGD 02-10-2026.
- De concept-DPA belooft wel een jaarlijks auditrapport van een onafhankelijke deskundige, en laat de instelling zelf auditen bij concrete aanleiding (14 dagen vooraf, kosten voor de instelling tenzij Eduface tekortschiet). Wordt hiernaar gevraagd, dan is het eerlijke antwoord dat het er nog niet is. Dat gaat naar Jeroen.
- Eduface documenteert haar beveiligingsbeleid en toont op verzoek bewijs.

## 12. Aansprakelijkheid en recht

- Aansprakelijkheid, vrijwaring en schadevergoeding lopen via de commerciële overeenkomst. De DPA noemt zelf geen plafond.
- Bij tegenstrijdigheid over persoonsgegevens gaat de DPA voor.
- Dezelfde rechtskeuze als de overeenkomst.

## 13. Wat je wel mag zeggen

- Verwerking en opslag vinden plaats in de EU, ook bij Microsoft, Google en Railway.
- Er wordt niet getraind op studentwerk of instellingsdata.
- De docent beslist, de AI assisteert. De instelling bepaalt of feedback eerst door de docent wordt goedgekeurd.
- Gegenereerde feedback bevat geen persoonsgegevens, tenzij een docent die er zelf in zet.
- Standaard 8 jaar bewaard, direct verwijderd als de opdracht uit het systeem gaat, en op verzoek en na afloop van de samenwerking.
- Een datalek gaat binnen 48 uur naar de instelling.

## 14. Wat je niet mag zeggen

- Een certificering of auditrapport, tot dat er is.
- "Alles staat in Nederland". Alleen "EU" tot de Azure-regio bevestigd is (V1).
- Dat Amerikaans recht er niets mee te maken heeft. Er is bevestigd dat de infrastructuur EU-only is, niet wat dat betekent voor de Amerikaanse moederbedrijven.
- "Studentdata gaat nooit naar externe AI-aanbieders" (staat in `Platform/product.md`). Google OCR is een externe verwerker, of dat een "AI-aanbieder" is, is OPEN (V3).
- Iets over orale examens of Academic Integrity en gegevens.
- Een fallbackpositie. Die zijn er niet.

## 15. Open

Zie ook `Context/open-vragen.md`.

| # | Punt |
|---|---|
| V1 | Welke Azure-regio('s)? De DPA zegt zowel "Nederland + EU" als "gehost in Nederland". |
| V3 | `Platform/product.md` zegt "Studentdata gaat nooit naar externe AI-aanbieders". Google Cloud OCR verwerkt wel studentdocumenten. Blijft die zin staan, en telt OCR als "AI-aanbieder"? |
| V7 | Wie is plaatsvervanger voor Jeroen bij een datalek? |
| V8 | Wat staat er precies bij Railway? Zit er studentdata of een identificeerbare gebruiker in? |
| V9 | Hoe lang blijven back-ups bewaard na verwijdering van een opdracht? |
| V10 | Welk risicoprofiel hanteert Eduface zelf onder de AI Act (laag, midden, hoog)? De AI Act noemt AI die leerresultaten beoordeelt hoog risico (bijlage III). |
| V11 | Installatie en beheer: werkt alles in de browser zonder lokale installatie? Kunnen losse functies of modules per instelling aan en uit? Wat moet een instelling technisch inrichten (LMS-koppeling, SSO, accountbeheer)? Kunnen studenten zelf verwijderen? |
| V12 | Continuïteit van het bedrijf zelf (financiering, team, exit- of escrowregeling) en het aantal getekende verwerkersovereenkomsten met Nederlandse instellingen. |
