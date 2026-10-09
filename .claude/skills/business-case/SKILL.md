---
name: business-case
description: Bouwt samen met Dante een business case voor één klant, die de champion bij het eigen MT neerlegt om een go te krijgen. Vaste opbouw van 15 onderdelen, cijfer voorop, in de stem van de instelling zelf. Inhoud per onderdeel in de chat, managementsamenvatting als laatste, PDF in de huisstijl van de klant als allerlaatste stap. Trigger wanneer Dante zegt "business case", "maak de business case voor [klant]", "ga verder met de business case", "volgend onderdeel", "de champion moet het intern verkopen", of een onderdeel noemt (ROI, kosten-baten, pijn, koersplan) voor een business case.
---

# Business case

Een besluitstuk voor een MT-commissie, eerste doelgroep private instellingen. De champion legt het intern neer. Doel: een go voor alles, dus ook de uitrol.

## Eerst lezen, elke keer

- `GTM/Knowledge/business-case/structuur.md`: de 15 onderdelen, hun volgorde, de vorm per onderdeel en de toon. **Dat bestand is de regel, deze skill is het proces.** Wijk er niet van af zonder akkoord.
- Het werkbestand van de klant, als dat er al is (zie hieronder).

## Bronnen

- **Prijs en productclaims levert Dante aan.** Niet uit `GTM/Pricing/` of `Platform/product.md` halen, niet uit het hoofd. Ontbreekt iets, dan staat er `[aan te leveren: ...]`.
- Privacy (onderdeel 10): mag uit de skill `privacy-it`, maar alleen wat daar als bevestigd staat.
- Koersplan (onderdeel 3): uit het echte koersplan van de klant, letterlijk geciteerd. Vraag Dante om het document of de link.

## Proces

1. **Klant vaststellen.** Noemt Dante er geen, vraag het in één regel.
2. **Werkbestand.** `GTM/Accounts/<klant>/business-case.md`. Bestaat het niet, maak het aan met de 15 kopjes uit `structuur.md`, elk met `[nog te doen]`. Hier leeft de inhoud tussen sessies.
3. **Open punten uit `structuur.md`** (sectie Open) een keer voorleggen als ze nog open staan.
4. **Per onderdeel**, één tegelijk. Begin bij 2 (de pijn), want bijna alles bouwt daarop.
   - Vraag Dante wat hij heeft: max drie vragen, met je eigen voorstel erbij.
   - Schrijf een concept in de toon uit `structuur.md`, in de chat.
   - Na akkoord: wegschrijven in het werkbestand, kopje op `[akkoord]`.
5. **Managementsamenvatting (1) als laatste**, als 2 tot en met 15 akkoord zijn.
6. **PDF pas als Dante dat zegt.** Dan het design system: `Design/System/core/proces.md` plus `core/`, poort 2 met pagina 1 als proef, huisstijl van de klant als basis (kleur en logo aanvragen). Bouw HTML, render naar PDF, zelfde map als het werkbestand.

## Toetsen voor elk concept

- Staat er een getal waar een bijvoeglijk naamwoord stond?
- Spreekt de instelling ("wij"), en wordt niemand aangesproken?
- Geen productclaim of prijs die Dante niet heeft aangeleverd.
- Past het binnen de vorm uit `structuur.md` (tabel, drie getallen, checklist)? Geen lap tekst waar een tabel hoort.

## Done

Alle 15 kopjes op `[akkoord]` in het werkbestand, en een PDF in de huisstijl van de klant als Dante erom vraagt.
