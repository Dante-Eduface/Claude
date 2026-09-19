---
name: kunnen-we-winnen
description: Bid/no-bid go-no-go check voor een nieuwe kans, uitvraag of tender, op basis van een 10-vragen scoringsraamwerk (elke vraag 0-2 punten x wegingsfactor, totaal boven 16 = GO, 12 tot 16 = OVERLEG, onder 12 = NO-GO). Gebruik deze skill ALLEEN wanneer Jeroen of Dante er expliciet om vraagt — bijvoorbeeld "moeten we hier tijd in steken", "kunnen we dit winnen", "doe een go/no-go op [kans]", "zullen we reageren op deze uitvraag", of een letterlijk verzoek om de 10 vragen / GO-NO-GO score. Trigger NIET automatisch bij elke deal die ter sprake komt (dat is het domein van meddpicc-qualifier, die de lopende deal daarna blijft volgen).
---

# Kunnen we winnen? — Bid/no-bid check

Voordat Eduface tijd, mensen en geloofwaardigheid in een nieuwe kans steekt, is er een simpeler vraag dan "hoe kwalificeren we deze deal": moeten we dit überhaupt oppakken? Dit is die vroege poortwachter. Waar `meddpicc-qualifier` een deal volgt die al in de pipeline zit, beantwoordt deze skill de vraag ervoor: is een nieuwe kans, uitvraag of tender het waard om op te reageren. Na een GO stroomt de kans gewoon door naar de normale pipeline, waar `meddpicc-qualifier` het overneemt.

## Wanneer dit toepassen

Alleen wanneer Jeroen of Dante er expliciet om vraagt. In tegenstelling tot `meddpicc-qualifier` (die ongevraagd meedenkt zodra een deal ter sprake komt) triggert deze skill niet vanzelf. Concrete aanleidingen: "moeten we hier tijd in steken", "kunnen we dit winnen", "doe een go/no-go op [kans]", "zullen we reageren op deze uitvraag", of een direct verzoek om de 10 vragen of een GO/NO-GO-score. Komt een kans terloops ter sprake zonder zo'n verzoek, ga er dan gewoon inhoudelijk op in zonder deze scoring erbij te halen.

## De 10 vragen

| # | Vraag | Weging |
|---|---|---|
| 1 | Willen we dit écht? Past het bij wie we zijn en wat we willen? | x2 |
| 2 | Kunnen we écht winnen? Hebben we een sterk winthema en onderscheidend aanbod? | x2 |
| 3 | Hebben we invloed gehad op de uitvraag? | x1,5 |
| 4 | Begrijpen we de achterliggende behoefte van de klant? | x1,5 |
| 5 | Hebben we de juiste mensen en middelen beschikbaar? | x1 |
| 6 | Hebben we voldoende tijd om kwaliteit te leveren? | x2 |
| 7 | Kunnen we dit strategisch gebruiken? Bijvoorbeeld voor zichtbaarheid, portfolio? | x2 |
| 8 | Is de uitvraag eerlijk en transparant? | x1 |
| 9 | Past het binnen onze commerciële doelstellingen? | x1 |
| 10 | Wat gebeurt er als we verliezen? Kunnen we dat hebben? | x0,5 |

Lees `references/framework.md` voor duiding per vraag in Eduface/hoger-onderwijs-context en `references/scoring-rubric.md` voor de exacte scoreformule en drempels, voordat je een analyse maakt.

## Bronnen: wat telt als bewijs

Dit raamwerk verschilt fundamenteel van MEDDPICC: de meeste van deze 10 vragen zijn strategische of subjectieve inschattingen ("Willen we dit écht?", "Kunnen we dit strategisch gebruiken?") die je niet uit CRM-notities kunt aflezen. Er bestaat geen "juiste" score die je autonoom kunt afleiden — het is een instrument om Jeroen en Dante scherper te laten nadenken, niet een rekensom die je voor ze maakt.

Doe dit dus interactief: leg de vragen één voor één (of gegroepeerd waar dat logisch is) voor, en vraag om een Ja/Twijfel/Nee-inschatting met een korte onderbouwing. Close CRM-context — eerdere contactmomenten, wat er al bekend is over de klant of de aanbesteding — mag je erbij halen om het gesprek scherper te maken of om iemand te herinneren aan relevante feiten, maar de score zelf komt altijd van het oordeel van de gebruiker, niet van een eigen inschatting op basis van CRM-data.

## Werkwijze

1. Bepaal om welke kans, uitvraag of tender het gaat.
2. Loop de 10 vragen interactief langs met de gebruiker. Vraag per vraag (of per klein groepje samenhangende vragen) om een Ja/Twijfel/Nee met een korte onderbouwing waarom.
3. Waar relevant, breng CRM-context of eerdere gesprekken in om de vraag scherper te maken — maar laat de gebruiker de score bepalen.
4. Reken per vraag de score (Ja=2, Twijfel=1, Nee=0) keer de wegingsfactor uit, en tel alle 10 subtotalen op tot een totaalscore.
5. Pas de drempel toe: >16 = GO, 12-16 = OVERLEG, <12 = NO-GO (zie `references/scoring-rubric.md`), en geef een onderbouwd advies dat teruggrijpt op de zwakste antwoorden.

## Output

Sluit af met:
- Een tabel per vraag: score, weging, subtotaal.
- Het eindtotaal en de GO/OVERLEG/NO-GO-duiding.
- Bij **OVERLEG**: benoem expliciet de belangrijkste risico's — meestal de vragen met de laagste score, vooral als die een hoge weging hadden.
- Bij **NO-GO**: benoem dat "nee" een geldig antwoord is; dit is geen falen maar een bewuste keuze om tijd en geloofwaardigheid elders in te zetten.
- Concreet vervolgadvies op maat van de uitkomst: bij GO wie dit oppakt en wat de eerste stap is, bij OVERLEG welk risico als eerste uitgezocht moet worden voordat er verder geïnvesteerd wordt, bij NO-GO hoe hier netjes van af te zien richting de klant.
