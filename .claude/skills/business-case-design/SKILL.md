---
name: business-case-design
description: Business Case Design Skill. Maakt een business case of voorsteldocument voor een instelling als bewerkbare A4-pptx (Canva-proof), in de vaste Eduface-documentstijl - één pagina per onderdeel, om en om wit en donker, eigen tint per onderdeel, rangorde van belang per kaart. Dante levert per onderdeel ruwe tekst of een schets, ik kort in, ontwerp, bouw en controleer. Trigger bij "business case", "maak een business case voor [instelling]", "maak een voorstel(document)", "maak hier een A4 van", "zet dit in het document", "maak een pagina voor [onderdeel]", "maak er een pptx van" voor een document (geen presentatie), of als Dante een screenshot of tekst aanlevert voor een pagina in een voorstel aan een instelling. Voor 16:9-slides en decks is het pitch-deck.
---

# Business Case Design Skill

Een document van een paar A4-pagina's voor het MT van een instelling. Elke pagina is één onderdeel (Voorstel, Kosten, Opbrengst, Accreditatie, Koersplan, Privacy, ...). Gebouwd als HTML op één stylesheet, daarna omgezet naar een pptx met echte tekstvakken.

## Voor je begint
1. `huisstijl.md` in deze map: de vaste regels, allemaal uit Dantes feedback. **Verplicht.**
2. `Platform/product.md` voor elke productclaim. Privacyclaims via de skill `privacy-it` (`platform-privacykennis.md`). Prijzen naast `GTM/Pricing/` leggen en afwijkingen melden.
3. `voorbeeld/academica.py`: het complete Academica-voorstel (okt 2026). Dit is het referentieniveau.

## Werkwijze
1. **Per pagina** levert Dante tekst of een screenshot. Kort in tot een kop plus hooguit één regel per kaart. Vraag naar de rangorde als die niet blijkt.
2. **Schrijf een paginascript**: kopieer `voorbeeld/academica.py` naar de werkmap van de klant en vervang de inhoud. Bouwstenen staan in `motor/bouwstenen.py`:
   - `page(map, 'N-naam', body)`: maakt pagina N; de eerste `<h1>` wordt de kop met nummer, even nummers worden donker.
   - `ttl(icoon, titel)`, `icon()`, `hbar()`, `dots(k)` (poppetjes), `lens()`, `item()`, `lst()`.
   - Kaarten: `card primary` (belangrijkst), `card secondary`, `card tertiary`.
   - Risico-rijen (`.risk` met `.meter`): zie `Design/Concepts/risicoanalyse/risicoanalyse.py`.
3. **Bouw**: `bash .claude/skills/business-case-design/motor/bouw.sh <werkmap> <uit.pptx> <logo-instelling.png>`
4. **Kijk naar de controleplaat** (`<werkmap>/build/controle.png`) en de margecheck in de uitvoer. Nooit opleveren zonder de plaat bekeken te hebben.
5. **Lever de pptx** met `SendUserFile`. Geen Artifact, geen PDF tenzij gevraagd.

## Waar het landt
- Werkmap: `Design/Concepts/<klant>-voorstel/` (pagina's plus paginascript), pptx heet `<klant>-voorstel-bewerkbaar.pptx`.
- Logo van de instelling: `Design/Merk/logo-van-scholen/Logo's/`. Niet aanwezig? Vraag Dante om een link of bestand, gebruik nooit een logo van een naamgenoot.

## Poorten
Nieuwe klant of nieuw soort pagina: eerst één pagina als proef laten zien, dan de rest. Een pagina toevoegen aan een bestaand document mag direct.

## Altijd melden
- Claims die je hebt afgezwakt of weggelaten, met de reden.
- Getallen die tussen pagina's verschillen.
- Wat nog open staat voor het document de deur uit kan.
