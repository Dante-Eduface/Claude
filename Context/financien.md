# Financiën, Dante

> **Wordt niet automatisch geladen**, net als `Context/personal.md`. Alleen openen als het gesprek over geld gaat.
>
> **Kijk vooruit, niet achteruit.** Dante op 19-09-2026: *"ik wil dat je niet zo bezig bent met het verleden, de situatie is heel anders."* De historische uitgavenanalyse uit de afschriften is daarom hier niet overgenomen. Gebruik dit bestand voor waar hij naartoe gaat, niet voor wat hij vorig jaar uitgaf.

_Laatst bijgewerkt: 20-09-2026. Bron: Dante zelf, plus zijn geldplan-app._

## Wat er binnenkomt

- **Ongeveer 2.130 euro netto per maand** van Blockbook B.V., de juridische naam van Eduface. Wat op de rekening staat is netto, daar hoeft niets van af. Uit de afschriften: 2.118,46 in juni en juli, 2.146,82 in augustus. Daarvoor, maart tot en met mei, was het 1.062,25. Het salaris is dus in juni ruim verdubbeld (afgelezen 20-09-2026).
- **129 euro zorgtoeslag per maand** van de Belastingdienst.

Reiskosten worden **niet** vergoed. Hij is er zelf mee bezig om die omlaag te krijgen, dus behandel het niet als een openstaand probleem.

## Wat ermee gebeurt

Op salarisdag zet hij **met de hand** geld apart volgens deze verdeling van het vrije geld:

| Deel | Aandeel | Waar naartoe |
|---|---|---|
| Sparen | 55% | Uit huis, Curaçao, zorgtoeslag |
| Leven | 35% | Betaalrekening |
| Aandelen | 10% | Trade Republic |

Die verdeling voert hij echt uit, het is geen voornemen.

## De rekeningen

| Pot | Waarvoor |
|---|---|
| Betaalrekening | Dagelijks |
| Uit huis | Verhuizen, doel 7.500 euro |
| Curaçao | De reis van 26-01-2027 |
| Zorgtoeslag | 129 per maand apart, voor de zorgpremie |
| Trade Republic | Aandelen. Rekening bestaat al. |
| Archiefrekening | Slaapt, geen bestemming |

### De stand per 18-09-2026

Uit de ABN-export van 20-09-2026, de laatste mutatie per rekening. Dit vervangt open vraag G15.

| Pot | Rekening | Stand |
|---|---|---|
| Betaalrekening | 882235753 | 31,53 |
| Uit huis fonds | 884479609 (Savings) | 0,11 |
| Curaçao | 118499882 | 122,10 |
| Zorgtoeslag | 142509299 (Zorgverzekering) | 53,00 |
| Trade Republic | los, handmatig | 0,00 |
| expired, doet niet mee | 147953219 | 0,00 |

Samen **206,74** op de rekeningen, min de 950 aan zijn vader is een vermogen van **min 743 euro**. Het doel is 10.000 binnen twaalf maanden.

**De potjes worden leeggehaald, dat is het echte patroon.** Op 8 augustus ging er 219 naar Savings en 529 naar Curaçao. Op 18 september staat Savings op 0,11 en Curaçao op 122,10. Het gaat in kleine bedragen terug naar de betaalrekening: 5, 14, 20, 40, 50 euro per keer. De verdeling van 55/35/10 wordt op salarisdag echt uitgevoerd, en daarna in de weken erna teruggedraaid. Zijn eigen rem, weinig op de rekening houden, werkt daardoor niet: het potje is één tik weg.

**September is een uitzonderingsmaand.** Op 18-09 was het salaris nog niet binnen en de zorgtoeslag ook niet. Wat er in september binnenkwam: 950 van zijn vader (de lening voor de vlucht, dezelfde dag doorbetaald aan KLM, 947,44), 159,26 uit Trade Republic, en 467 uit zijn eigen potjes. **Trade Republic is daarmee leeg.**

**Reizen is de grootste post en veel hoger dan gedacht.** Alleen NS: 139 in juni, 387 in juli, 414 in augustus, 247 in september tot de 18e. Inclusief overig vervoer kwam de categorie in juni tot en met augustus op 886, 898 en 665 per maand. In de app stond 140. Dat verschil alleen al verklaart waarom het plan niet uitkwam. Staat als G16 open.

**De zorgpremie loopt niet via het zorgpotje.** De incasso van 129,45 gaat rechtstreeks van de betaalrekening af, en rekening 142509299 krijgt alleen losse stortingen van de zorgtoeslag. Het geld draait dus rond in plaats van op te bouwen. Het doel van 1.548 in de app (twaalf maal 129) hoort daar niet bij. Staat als G17 open.

## Wat vaststaat

| Wat | Bedrag | Wanneer |
|---|---|---|
| Curaçao | 2.030 | Reis staat geboekt, 26-01-2027 |
| Schuld aan zijn vader | 950 | Terugbetalen zodra het salaris binnen is. Was voor het boeken van Curaçao. |
| Uit huis | 7.500 | Streefdatum 01-08-2027, naar Utrecht of Rotterdam |
| Vermogen | 10.000 | Binnen 12 maanden. Nog steeds het doel. |

## Het ritme

Elke **zaterdag** staat "Financieel controle" in zijn agenda, wekelijks. Dat is het moment om dit bestand tegen de werkelijkheid te leggen.

**Hoort op 11:00 tot 12:00**, niet om 09:00. Zoals hij nu staat valt hij in deep-work-blok 2, en een financiële controle is shallow werk. Het pauze-uur is geen alternatief, want dat blijft leeg. Na blok 2 en voor de lunch is de plek. Zie `Context/deep-work.md`.

## De geldplan-app

Dante heeft een eigen HTML-app met potjes, een dagelijkse saldo-check en een projectie naar 10.000 euro. Die blijft de plek waar hij zijn standen bijhoudt. De doelen en de verdeling hierboven komen daaruit.

**Niet gebruiken als cijferbron.** De maandtabel erin is met de hand ingevuld en klopte op 19-09-2026 niet met zijn afschriften.

**Staat sinds 20-09-2026 in de repo: `Personal/geldplan/geldplan.html`.** Draait op `localStorage` onder de sleutel `eduface.geldplan.v1`, met de standen hierboven als startwaarden en de maandcijfers herberekend uit de afschriften. De ruwe afschriften staan bewust **niet** in de repo.

**Het is een los HTML-bestand en dat blijft zo (20-09-2026).** Bewust geen gepubliceerd Artifact. Dante's vier redenen:

1. **De data bleef anders niet staan.** Een gepubliceerd Artifact krijgt eigen opslag. Elke aanpassing gaf een nieuwe kopie met een nieuwe link en een lege opslag, dus dagsaldi, vinkjes en instellingen waren weg.
2. **Startwaarden staan in de code.** Saldi, percentages, doelen en datums zijn hardcoded in het object `D`, met een `seed`-vlag die ze eenmalig forceert. Dat werkt alleen als het bestand zelf de bron is.
3. **Overdraagbaar.** Geen build, geen dependencies, geen framework. Openen in een browser en het werkt.
4. **Geen import van afschriften.** Categoriseren gebeurt buiten de app, de maandcijfers staan als `MAANDEN`-constante in de code. Dat houdt de app dom en voorspelbaar.

**Wat er op 20-09-2026 aan veranderd is:**

- `window.storage` vervangen door `localStorage` met JSON-serialisatie in `load()` en `save()`. Sleutel `eduface.geldplan.v1`, namespaced omdat Chrome bij `file://` alle lokale bestanden als dezelfde origin ziet en er hier meer HTML-apps draaien. `load()` en `save()` blijven async, zodat de aanroepen niet hoefden te veranderen. Safari blokkeert `localStorage` op `file://`: werkt het daar niet, serveer het bestand dan via een lokale server.
- Startwaarden op de echte stand van 18-09-2026, onder een nieuwe `seed7`-vlag.
- `MAANDEN` herberekend uit de afschriften van maart tot en met augustus. September staat er niet in, die maand is niet af. De kolom heet nu Binnen in plaats van Salaris, want er zit meer in dan salaris.
- De regel die alles van en naar Lindeborg als vaste last boekte is eruit. Geld naar zijn moeder is huur, geld van haar is inkomen; de richting bepaalt dat, niet de naam.
- Rekening 147953219 staat op expired en doet niet mee.
