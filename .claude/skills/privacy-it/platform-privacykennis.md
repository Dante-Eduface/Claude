# Privacykennis over het Eduface-platform

_Laatst bijgewerkt: 2026-11-22. Beheerder: Jeroen van Gessel._

Opgebouwd uit de concept-verwerkersovereenkomst (SURF-model 4.0) en wat Jeroen daarover in de chat heeft bevestigd. De kennis staat per onderwerp, niet per artikel. Het origineel staat in `Archive/privacy-it-2026-10/dpa-surf-4-0-artikelsgewijs.md`, alleen openen als de letterlijke clausule ertoe doet.

Contractuele feiten (back-ups, beheer, termijnen) staan in de licentieovereenkomst. Bron in Drive: `Eduface_Licentieovereenkomst_Template - Tjarko .docx`, Bijlage 3 en 4. Waarden tussen vierkante haken in dat sjabloon zijn standaardwaarden, geen afspraken per klant.

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
| Microsoft Azure | Hosting van de AI-verwerking: compute, database, opslag. Documenten, rubrics, feedbacktekst, audit logs. | "Nederland + EU". BEVESTIGD 22-11-2026 (Dante). |
| Google Cloud | OCR van geüploade documenten en afbeeldingen. | europe-west4 (Eemshaven/Rotterdam). BEVESTIGD. |
| Railway | Databasehosting voor ondersteunende diensten. Interne metadata en tijdelijke verwerkingsgegevens. | Amsterdam. Wat er precies in staat is niet vastgelegd: Railway komt in geen enkele licentieovereenkomst in Drive voor (22-11-2026). Noem alleen de omschrijving hiernaast. |

- **Alle drie werken voor Eduface alleen met EU-infrastructuur.** BEVESTIGD 02-10-2026. Er gaat niets naar derde landen.
- De instelling geeft algemene toestemming voor deze verwerkers. Eduface blijft volledig aansprakelijk voor wat zij doen en legt hen dezelfde verplichtingen contractueel op.
- **Wijzigen van een verwerker of doorgifte buiten de EER:** Eduface meldt dat schriftelijk, de instelling heeft één maand voor gemotiveerd bezwaar, daarna volgt overleg. Komt er binnen twee maanden geen oplossing, dan kan de instelling opzeggen met één maand opzegtermijn en zonder schadevergoeding. Maakt de instelling geen bezwaar, dan geldt de wijziging als geaccepteerd.

## 5. Bewaren en verwijderen

- **Standaard 8 jaar**, om aan lokale regelgeving te voldoen. BEVESTIGD 02-10-2026.
- **Wordt een opdracht in het Eduface-systeem verwijderd, dan verwijdert Eduface hem ook.** BEVESTIGD 02-10-2026.
- Daarnaast wordt verwijderd op verzoek van de instelling en na afloop van de samenwerking.
- Na afloop van de overeenkomst vernietigt of retourneert Eduface binnen één maand alle persoonsgegevens, ook kopieën bij verwerkers. Kiest de instelling voor teruggave, dan in een gangbaar formaat aan haar of een aangewezen partij. Op verzoek bevestigt Eduface schriftelijk dat dat gedaan is.
- Back-ups: dagelijks, 30 dagen bewaard, doorlopend (licentie-sjabloon Bijlage 3 punt 8 en Bijlage 4A, 22-11-2026).
- **LET OP, botsing (22-11-2026).** Het licentie-sjabloon zegt: Klantdata blijft tot uiterlijk 60 dagen na het einde van de overeenkomst (art. 12.3, Bijlage 4A), logbestanden 12 maanden, en een datalek gaat binnen 36 uur naar de instelling (Bijlage 4 punt 9). Hierboven en in sectie 13 staan 8 jaar bewaren en 48 uur melden (Jeroen en de SURF-DPA, 02-10-2026). Noem naar een instelling geen bewaartermijn of meldtermijn tot Dante zegt welke geldt.

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

- Verwerking en opslag vinden plaats in Nederland en de EU (Azure: Nederland + EU), ook bij Google en Railway.
- Studentdata gaat nooit naar externe AI-aanbieders. Google Cloud OCR (europe-west4) leest alleen de tekst uit documenten en telt niet als AI-aanbieder (Dante, 22-11-2026), maar blijft wel een genoemde verwerker.
- Er wordt niet getraind op studentwerk of instellingsdata.
- De docent beslist, de AI assisteert. De instelling bepaalt of feedback eerst door de docent wordt goedgekeurd.
- Gegenereerde feedback bevat geen persoonsgegevens, tenzij een docent die er zelf in zet.
- Standaard 8 jaar bewaard, direct verwijderd als de opdracht uit het systeem gaat, en op verzoek en na afloop van de samenwerking. (Botst met het licentie-sjabloon, zie sectie 5.)
- Een datalek gaat binnen 48 uur naar de instelling. (Botst met het licentie-sjabloon, zie sectie 5.) Contactpersoon bij Eduface is Jeroen van Gessel, er is geen plaatsvervanger (Dante, 22-11-2026).

## 14. Wat je niet mag zeggen

- Een certificering of auditrapport, tot dat er is.
- "Alles staat in Nederland". Bevestigd is "Nederland + EU" (22-11-2026), dus niet alles in Nederland.
- Dat Amerikaans recht er niets mee te maken heeft. Er is bevestigd dat de infrastructuur EU-only is, niet wat dat betekent voor de Amerikaanse moederbedrijven.
- Iets over orale examens of Academic Integrity en gegevens.
- Een fallbackpositie. Die zijn er niet.

## 15. Open

Zie ook `Context/open-vragen.md`.

| # | Punt |
|---|---|
| V10 | Welk risicoprofiel hanteert Eduface zelf onder de AI Act (laag, midden, hoog)? De AI Act noemt AI die leerresultaten beoordeelt hoog risico (bijlage III). |
| V12 | Continuïteit van het bedrijf zelf (financiering, team, exit- of escrowregeling) en het aantal getekende verwerkersovereenkomsten met Nederlandse instellingen. |

## 16. Installatie en beheer

Uit het licentie-sjabloon (22-11-2026). Beantwoordt wat eerder V11 heette, voor zover het sjabloon het zegt.

- Het platform is een online webapplicatie (art. 1.13). Een lokale installatie wordt nergens genoemd.
- Standaardimplementatie: één LMS-koppeling en één online kick-off en training van maximaal twee uur (art. 8.2). Het sjabloon noemt Brightspace, Canvas, Moodle, Blackboard en ItsLearning.
- De instelling wijst één of twee Key users met beheerrol aan, beheert zelf de toegang van gebruikers en moet tijdig meewerken aan de LMS-koppeling met beheerrechten en een technisch contactpersoon (art. 9.1 en 9.2).
- Via het beheerdersdashboard of de LMS-koppeling kan de instelling cursisten deactiveren (art. 5.2).
- SSO staat als optie tussen haakjes in Bijlage 4B, niet als standaard vastgelegd.
- Functies per instelling aan en uit zetten staat niet in het sjabloon. Bèta-functies worden aangeboden zoals ze zijn (art. 3.5).
- Studenten verwijderen zichzelf niet. Verzoeken van betrokkenen lopen via de instelling (Bijlage 4 punt 7). De instelling kan Klantdata exporteren, en Eduface verwijdert uiterlijk 60 dagen na afloop (art. 12.3).
