# Financiën, Dante

> **Wordt niet automatisch geladen**, net als `Context/personal.md`. Alleen openen als het gesprek over geld gaat.
>
> **Kijk vooruit, niet achteruit.** Dante op 19-09-2026: *"ik wil dat je niet zo bezig bent met het verleden, de situatie is heel anders."* De historische uitgavenanalyse uit de afschriften is daarom hier niet overgenomen. Gebruik dit bestand voor waar hij naartoe gaat, niet voor wat hij vorig jaar uitgaf.

_Laatst bijgewerkt: 20-09-2026. Bron: Dante zelf, plus zijn geldplan-app._

## Wat er binnenkomt

- **Ongeveer 2.000 euro netto per maand** van Blockbook B.V., de juridische naam van Eduface. Wat op de rekening staat is netto, daar hoeft niets van af.
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

**Actuele standen: nog niet bekend.** Dante vult de potjes opnieuw aan en levert een nieuw bestand met de standen. Tot dat er is, geen bedragen noemen. De cijfers in de geldplan-app zijn achterhaald.

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

**Het is een los HTML-bestand en dat blijft zo (20-09-2026).** Bewust geen gepubliceerd Artifact. Dante's vier redenen:

1. **De data bleef anders niet staan.** Een gepubliceerd Artifact krijgt eigen opslag. Elke aanpassing gaf een nieuwe kopie met een nieuwe link en een lege opslag, dus dagsaldi, vinkjes en instellingen waren weg.
2. **Startwaarden staan in de code.** Saldi, percentages, doelen en datums zijn hardcoded in het object `D`, met een `seed`-vlag die ze eenmalig forceert. Dat werkt alleen als het bestand zelf de bron is.
3. **Overdraagbaar.** Geen build, geen dependencies, geen framework. Openen in een browser en het werkt.
4. **Geen import van afschriften.** Categoriseren gebeurt buiten de app, de maandcijfers staan als `MAANDEN`-constante in de code. Dat houdt de app dom en voorspelbaar.

Het bestand hoort dus **in deze repo**, zodat het hier aangepast kan worden. Plek: `Personal/geldplan/geldplan.html`. Zolang het er niet staat, kan ik er niets aan veranderen.

**Eerste wijziging zodra het bestand er is:** `window.storage` vervangen door `localStorage` met JSON-serialisatie, in `load()` en `save()`. `window.storage` bestaat alleen binnen de Claude-artifactruntime. Twee dingen erbij:

- **Eén namespaced sleutel**, in de lijn van wat de andere apps hier gebruiken: `eduface.geldplan.v1`. Bij openen via `file://` behandelt Chrome alle lokale bestanden als dezelfde origin, dus een generieke sleutel als `state` botst met de andere HTML-apps in deze repo.
- **Houd `load()` en `save()` async.** `localStorage` is synchroon, `await` op een gewone waarde is onschuldig, en zo hoeven de aanroepen niet mee te veranderen.
