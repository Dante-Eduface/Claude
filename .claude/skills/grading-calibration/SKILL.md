---
name: grading-calibration
description: Kalibreert Eduface's AI-beoordeling (beoordelingsformulier/rubric + modelinstructies) per vak zodat de AI-uitkomst het echte oordeel van de vakdocent benadert, zonder zelf feedback te schrijven. Trigger wanneer Dante zegt "fine-tune dit vak", "pas de rubric/het beoordelingsformulier aan voor [vak]", "de AI beoordeelt te streng/te soepel bij [vak]", "kalibreer de modelinstructies", "doe hetzelfde als bij manuele therapie voor [vak]", of een nieuw vak aanlevert met beoordelingsmateriaal plus een docent om tegen te toetsen.
---

# Grading calibration

Eduface's AI beoordeelt via twee losse instellingen per vak: het **beoordelingsformulier** (rubric, Voldoende/Onvoldoende-tekst per criterium) en de **modelinstructies** (context, toon, beoordelingsstrengheid). Deze skill kalibreert allebei tegen een echte, door de vakdocent beoordeelde inzending, zodat de AI-uitkomst haar oordeel benadert.

**Kernregel (Dante, 22-09-2026): we schrijven nooit zelf feedback. We schrijven instructies voor het model die zo goed mogelijk aansluiten bij de content van het vak.**

**Lees eerst `LEERPUNTEN.md` in deze map voordat je begint.** Elk vak levert inzicht op dat de methode scherper maakt, dat landt daar. Sla het niet over omdat het "vast wel hetzelfde is als vorige keer".

## Wanneer gebruiken

- Dante wil de AI-beoordeling van een vak scherper krijgen ("fine-tune dit vak", "de AI is te streng/soepel bij [vak]")
- Een nieuw vak start met dit traject: materiaal plus een docent om tegen te toetsen
- Eduface's huidige AI-uitkomst wijkt zichtbaar af van wat de docent zelf zou geven

## De lus

1. **Verzamel** het materiaal. Volledige checklist met uitleg in `reference.md`, kort: het originele beoordelingsformulier, een schrijfformat/instructiedocument met voorbeeld (als het bestaat), minstens 2 echte studenteninzendingen, de officiële beoordeling van de docent op diezelfde inzendingen, haar eventuele losse conceptcommentaar (bleek bij manuele therapie de goudmijn), de huidige live rubric + modelinstructies, en de huidige AI-uitkomst op diezelfde inzendingen. Zonder een **echt door de docent beoordeelde inzending** kun je niet kalibreren, alleen gokken.
2. **Vergelijk** de huidige AI-uitkomst criterium voor criterium tegen de docent, over minstens 2 studenten. Zoek mismatches die bij beide terugkomen: dat zijn de echte hotspots, geen toevalstreffer bij één student.
3. **Diagnosticeer** per mismatch met de AI's eigen "Algemene feedback"-tekst, nooit raden waarom hij afwijkt. Onderscheid drie soorten problemen, ze vragen andere fixes:
   - **WAT er gecheckt wordt** → rubric-tekst probleem
   - **OF een gevonden gaatje een fail wordt** → instructies/drempel-probleem
   - **HOE het geschreven is (toon)** → instructies/toon-probleem
4. **Schrijf** de fix. Rubric-tekst: voeg een expliciete cap toe aan de Voldoende-tekst ("X is niet vereist", "kleine onvolkomenheden die de kern niet ondermijnen staan een voldoende niet in de weg"). Modelinstructies: deze route is berucht lossy, zie de aanpak in `reference.md` voor je begint te schrijven.
5. **Test als varianten.** Minstens: alleen rubric, alleen instructies, allebei, elk in een eigen Eduface-opdracht naast de ongewijzigde baseline. Gebruik voor elke variant én de baseline dezelfde vaste, letterlijke brontekst voor de rubric (Eduface's eigen PDF-naar-rubric vertaling is niet deterministisch, dus nooit een vers gegenereerde versie als vergelijkingsbasis gebruiken).
6. **Vergelijk** elke variant tegen de docent, op twee assen apart: klopt het oordeel (Voldaan/Niet voldaan per criterium), en klopt de toon. Dat zijn meestal verschillende winnaars, zie punt 9 in `reference.md`.
7. **Concludeer en lever** de definitieve rubric-tekst en modelinstructies-tekst, klaar om te plakken, plus welke variant won en waarom.

## Kritieke valkuilen (kosten anders een testronde)

- **Eduface's eigen PDF-naar-rubric vertaling is niet deterministisch.** Hetzelfde bronbestand twee keer uploaden geeft andere bewoording, soms met een net strengere lezing erin (bijv. "navolgbaar" of "expliciet" die er zelf bij komen). Plak dus altijd een vaste, eigen tekst in elke opdracht, vertrouw nooit op een verse auto-generatie als controle-basis.
- **Modelinstructies zijn nooit direct bewerkbaar**, alleen via "Beschrijf je feedbackstijl" + "Opnieuw genereren", en die stap comprimeert. Concrete voorbeeldzinnen en de Inline-opmerkingen-sectie overleven dat zelden, ook niet met een expliciete "gebruik dit letterlijk"-instructie. Zie `reference.md` voor wat wel overleeft en hoe je daar het meeste uithaalt.
- **Het eindoordeel (Voldaan/Onvoldoende) is een handmatige keuze van de docent in Eduface**, geen automatische optelsom van de gewogen criteria. Optimaliseer dus op de losse criteria, niet op de weging.
- **Het echte gat is meestal geen kennisgat maar een drempelgat.** De AI ziet vaak precies wat de docent ook ziet, maar zet elk gevonden verbeterpunt om in een fail, waar de docent het als groeifeedback binnen een voldoende behandelt. Neem dit niet aan, check het via de docent's eigen conceptcommentaar op de inzending zelf, als dat bestaat (zie `reference.md`, sectie annotaties uitlezen).

## Waar het landt

- Rubric-tekst en modelinstructies: plakklaar in de chat, Dante zet ze zelf in Eduface (geen MCP-toegang tot Eduface, dus geen directe API-actie mogelijk).
- Bevindingen die de methode zelf verbeteren, ook uit een volgend vak: in `LEERPUNTEN.md`, met datum en vak.
- Een volledig uitgewerkt voorbeeld met echte teksten en vergelijkingstabellen: `examples/manuele-therapie-case-study.md`.

## Klaar is

Een variant waarvan de AI-uitkomst, zowel het oordeel als de toon, overeenkomt met wat de echte docent op minstens 2 studenten deed, met de exacte rubric- en modelinstructies-tekst gedocumenteerd en klaar om te plakken.
