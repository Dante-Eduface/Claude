# Folder SURF Onderwijsdagen, inhoud per paneel

_Laatst bijgewerkt: 2026-10-30. Opgesteld uit het gesprek Dante en Jeroen van 30-10-2026, herzien na Dante's feedback dezelfde dag. Alles in het Nederlands._

Elke claim komt uit `Platform/product.md` of `.claude/skills/privacy-it/platform-privacykennis.md`. Wat daar niet staat, staat niet op de folder. Geen "tot het bevestigd is": een folder ligt gedrukt voordat iemand iets bevestigt.

| Paneel | Rol | Inhoud |
|---|---|---|
| 1 Voorkant | Hook + belofte + visual | Probleem, headline, productbeeld, LMS-logo's |
| 2-3 Binnenkant | Details | Hoe Eduface werkt, resultaten, klanten (los van elkaar) |
| 4 Achterkant | CTA | Concreet aanbod, QR, contact, vertrouwensregel |

---

## Blokkerend voor de drukker

1. **94%: gaf de docent zijn cijfer vóór of ná het zien van het AI-voorstel?** Nog niet uitgezocht (`product.md`). Bepaalt of de meting onafhankelijk is. Menno of Samuel checken. Geen antwoord, dan gaat het cijfer eraf.
2. **Wat staat er in het impactrapport, en wie maakt het?** Zonder dat is de achterkant niet te schrijven.
3. **Bath Spa: hebben we toestemming om de naam te noemen?** Jouw beslissing. Hoe het ook uitvalt, het blijft één pilot bij één instelling.

---

## Paneel 1, voorkant

**Hook.** Eén probleem: consistentie tussen beoordelaars.

> Twee beoordelaars. Eén paper. Twee verschillende cijfers.

Drie korte zinnen achter elkaar is hier een bewuste keuze. Dat ritme komt verder nergens op de folder terug.

**Headline:**
> Dezelfde maatstaf voor elke inzending.

**Subline:**
> Eduface stelt feedback en een cijfervoorstel op volgens jullie rubric, met een eigen onderwijskundig AI-model. De docent bekijkt elk punt, past het aan waar nodig en keurt het goed.

**Visual:** productbeeld van de reader, met opmerkingen die eruitzien alsof ze nog geschreven worden. Bestaande beelden: `Design/Merk/product/`.

**LMS-strook:** *Geïntegreerd in jullie LMS* + logo's Moodle, Blackboard, Brightspace, Canvas.
- OPEN: LMS-logo's staan nog niet in `Design/Merk/`.

---

## Paneel 2-3, binnenkant: zo werkt Eduface

### 1. Dezelfde rubric, elke inzending
Dit blok draagt de hook. Het bewijs voor consistentie is het mechanisme, geen percentage.
> Elke inzending wordt langs dezelfde rubric gescoord, met een uitlegbare cijferopbouw per criterium. Zo zie je bij elk cijfer waar het vandaan komt, en waar twee beoordelaars uit elkaar lopen. Het dashboard dat beoordelaars vergelijkt laat in één oogopslag zien wie afwijkt van het team of van het AI-voorstel.

### 2. Een eigen model
> Eduface draait niet op OpenAI, Anthropic of een ander algemeen model. Het is getraind op 250.000 onderwijsspecifieke feedbackvoorbeelden en op peer-reviewed onderzoek naar hoe docenten beoordelen.

### 3. Een model per vakgebied
> Zes vakmodellen, elk getraind op de conventies van het eigen vakgebied: Recht, Economie, Sociale Wetenschappen, STEM, Geesteswetenschappen en Gezondheidswetenschappen.

- Niet beweren wat elk submodel per vak precies kent, dat is nog niet bevestigd.
- OPEN: Dante levert de vakgebieden nog aan. In `product.md` staan deze zes. Zelfde lijst?

### 4. Paper Grader en Exam Grader
- **AI Paper Grader:** feedback per concept tijdens het schrijven, plus volledige beoordeling op de rubric met annotaties in de tekst.
- **AI Exam Grader:** open en gesloten vragen nakijken op schaal. Hij markeert waar hij twijfelt, en het cijfer gaat na goedkeuring terug naar het LMS.

### 5. De docent beslist
> De AI assisteert, de docent beslist. De docent ziet en keurt elk punt voordat de student het leest. De instelling kiest zelf hoeveel toezicht ze wil. Voor summatieve beoordelingen houdt Eduface een audit trail bij volgens de AI Act.

### Resultaten (eigen blok, visueel los van de klanten)
Label: *pilot bij één instelling, juni 2026*. Instellingsnaam afhankelijk van blokkerend punt 3.

- **Hoe dicht het voorstel bij de docent zit:** over 435 opdrachten en 13 docenten lag het cijfervoorstel gemiddeld ongeveer 6 punten van het cijfer van de docent. Bij docenten die het model hadden afgestemd was dat ongeveer 2 punten.
  - De 2 punten zijn het sterkste stuk: het model wordt beter zodra de docent stuurt.
  - Alleen als percentage als het moet, en dan met dragers: *94% accuraatheid, 98% bij afgestemde modellen, over 435 opdrachten en 13 docenten.* Nooit kaal.
  - Afhankelijk van blokkerend punt 1.
- **Reviewtijd per inzending in de pilot:** 2 tot 3 minuten. Als los feit, geen vergelijking met "zonder Eduface", want die nulmeting is er niet.

### Klanten (eigen blok)
> Gebruikt door Hogeschool Rotterdam, De Haagse Hogeschool, Tilburg University en Radboud Universiteit.

Nooit TIO of ICM.

---

## Paneel 4, achterkant: call to action

**CTA.** Moet zeggen wat je krijgt. Richting, pas definitief als blokkerend punt 2 is opgelost:
> Wij rekenen uit wat nakijken jullie opleiding nu kost.

Gevolgd door één zin over wat er in het rapport staat en hoe je het aanvraagt.

**QR-code + contact.**
- OPEN: waar leidt de QR heen?
- OPEN: wiens naam, mail en telefoonnummer?

**Vertrouwensregel:**
> Jullie data blijft in de EU. Er wordt nooit getraind op jullie data.

- Beide bevestigd in `platform-privacykennis.md` (02-10-2026).
- "Nederland" niet, alleen "EU" tot de Azure-regio vaststaat (V1).
- Eventueel erbij: *beleid sluit aan op de AVG*. Nooit "voldoet aan de AVG", dat is geen certificering.

---

## Productie

- SURF Onderwijsdagen. Spoed, levering dinsdag 03-11-2026.
- OPEN: formaat (A4 naar A5 gevouwen?) en drukker.

## Eruit gehaald

- 48,5% tijdsbesparing en "20+": geen bron in `product.md`.
- "In een fractie van de tijd": geen nulmeting.
- Het label "Lecturer + AI": productkeuze voor Menno of Samuel, niet voor de copy. Beschreven in plaats van geciteerd.
- "Voldoet aan de AI Act": breder dan wat er staat. Nu "audit trail volgens de AI Act", en het risicoprofiel staat nog open (V10).
- UK GDPR.

## Bewust niet erin

- Academic Integrity en Oral Examination (beta).
- Prijs.
- Operationele efficiëntie als probleem.
