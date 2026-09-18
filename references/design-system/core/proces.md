# Het designproces: drie poorten

Geldt voor alles wat er visueel uitziet: pagina, deck, tool, creative. Lees dit **voor** je begint te bouwen.

De regel: **nooit een volledig resultaat opleveren zonder tussenmomenten.** Dante stuurt bij op elk niveau, en hij doet dat voordat het dure werk gedaan is.

## Waarom dit zo werkt

Niet omdat later repareren aantoonbaar honderd keer duurder is. Die claim (de 1:10:100-vuistregel) blijkt niet uit Boehms eigen data te komen maar uit een niet-gepubliceerde IBM-trainingscursus, en een literatuuroverzicht vond vijf bevestigende en vijf niet-bevestigende studies. Boehm en Basili stelden de curve in 2001 zelf naar beneden bij. Gebruik dat argument dus niet.

De echte reden is dat de mate van afwerking bepaalt **waar het gesprek over gaat**. Bij een afgewerkt ontwerp praat je over kleur en detail, bij een ruwe opzet over volgorde en structuur. Dat is een cognitief effect (cognitive ease: over kleur praten is makkelijker dan over informatiestructuur), geen kwaliteitsverschil in wat je vindt. Onderzoek laat zien dat lo-fi en hi-fi ongeveer evenveel bruikbaarheidsproblemen blootleggen. Je wint dus geen betere fouten, je wint dat de structuur nog ter discussie staat.

En het best onderbouwde stuk van dit hele proces is niet de fasering maar **het tonen van meerdere richtingen**. NN/g vond dat parallel ontwerpen plus itereren betere bruikbaarheid oplevert dan itereren op één idee. Dat is de belangrijkste regel hieronder, niet een extraatje.

## Poort 1 — Opdracht en richting

**Eén bericht, waarin allebei zit.**

Wat ik lever:
- Maximaal 5 vragen, en alleen vragen waarbij een ander antwoord het werk echt verandert. **Bij elke vraag zet ik mijn eigen voorgestelde antwoord.** Dante kan dan reageren met "ja, ja, ja, nee bij 4 want X" in plaats van vijf keer zelf te moeten nadenken.
- **Twee wezenlijk verschillende richtingen**, in woorden, geen plaatjes. Verschil in volgorde, nadruk en waar het bewijs staat. Niet twee kleurvarianten van hetzelfde.
- Elke richting krijgt een label op de afweging, niet op de smaak: "A zet het cijfer voorop, B zet het verhaal voorop."
- Wat ik heb aangenomen, expliciet opgesomd.

Wat ik vraag: "Welke richting, en klopt de volgorde?"

Wat je hier **niet** hoeft te beoordelen: kleur, typografie, exacte formuleringen. Die bestaan nog niet.

Wat hierna vastligt: de opbouw en de volgorde.

## Poort 2 — Proef

**Eén onderdeel volledig af, op echte kwaliteit.** Niet een schets van alles, maar één ding goed: één sectie, één slide, één scherm.

Wat ik lever: dat ene onderdeel, en ik open het in de browser zodat je het echt ziet in plaats van beschreven krijgt.

Wat ik vraag: "Dit wordt het patroon voor de rest. Klopt de toon, de dichtheid en de typografie?"

Wat je hier **wel** beoordeelt: alles van craft. Dit is het moment.

Wat hierna vastligt: het visuele patroon. De rest wordt hierop gebouwd.

**Kies bij twijfel het spannendste dat nog binnen de opdracht past, niet het veiligste.** Een proef die er precies zo uitziet als wat er al stond, heeft de proef niet gebruikt. Dit gold nog niet expliciet toen de web-oppervlakte op 18-09-2026 als plat en saai werd afgekeurd — zie `web/regels.md` voor wat dat concreet betekent.

## Poort 3 — Uitrol en politoer

Ik bouw de rest op het goedgekeurde patroon en loop daarna zelf na:
- de reflexen-lijst uit `compositie.md` punt 12
- de squint-test en de tekstmasker-test uit `compositie.md` punt 6
- contrast, regellengte, uitlijning van tabelkoppen

Pas daarna lever ik op. Dante hoort geen dingen te hoeven melden die ik zelf had kunnen zien.

## De regels die dit laten werken

1. **Nooit naar de volgende poort zonder akkoord.** Dat is het hele punt.
2. **Elke poort bevriest een laag.** Wat bij poort 1 is besloten, heropenen we bij poort 2 niet meer, tenzij Dante dat zelf wil. Zonder dat wordt het een oneindige lus.
3. **Eén beslisser: Dante.** Het bekende faalpatroon hier is design by committee, en de bronnen zijn het erover eens dat dat niet komt door het aantal rondes maar door onduidelijk eigenaarschap per ronde. Dus per poort één beslissing, één beslisser.
4. **Zeg per poort waar de feedback over moet gaan.** "Dit is de structuur, negeer kleur en formulering." Dat is precies wat Figma's critique-praktijk voorschrijft: de presentator zegt vooraf welke feedback hij wil.
5. **Stel een specifieke vraag, nooit "wat vind je ervan".**
6. **Noem je aannames.** Zodat Dante ze kan afschieten voordat ze in het eindresultaat zitten.

## Schaal

- **Klein** (één afbeelding, één slide, kleine aanpassing): poort 1 vervalt, ga direct naar de proef. Vraag hooguit één ding.
- **Normaal** (een pagina, een sectie, een set creatives): alle drie.
- **Groot** (heel deck, hele app, redesign): alle drie, en bij poort 2 lever je twee proeven in plaats van één, zodat de keuze ook op craft-niveau nog open is.

## Een bevroren poort heropenen

Regel 2 hierboven zegt: wat bij een poort is besloten, heropen je niet meer zonder akkoord. Dat gaat over **iteratie binnen dezelfde opdracht**. Het geldt niet meer zodra de opdracht zelf wezenlijk verandert — een andere koper, een andere boodschap, een ander register. Dan is een eerder "af" Poort-2-resultaat geen bevroren laag meer maar het antwoord op een vraag die niet meer gesteld wordt.

**Signaal dat dit aan de hand is:** je past alleen de tekst aan in een bestaand, goedgekeurd stuk, terwijl de reden dat de tekst verandert eigenlijk het hele beeld raakt. Dan patch je niet, je bouwt een nieuwe proef en legt uit waarom de oude niet meer volstaat. Gebeurd op 18-09-2026: een hero-kop wisselde van koud-advertentieverkeer-taal naar een institutionele koper, en alleen de kop werd vervangen terwijl de rest (beeld, toon) nog op de oude lezer was gebouwd.

## Ontsnappingsluiken

Dante mag altijd zeggen:
- "gewoon bouwen" → alle poorten overslaan
- "sla poort 1 over" → begin bij de proef
- "geen twee opties, kies zelf" → één richting, met de reden erbij

Het proces is er voor hem, niet andersom. Maar de standaard is: poorten aan.

## Bronnen

- [NN/g, Parallel and Iterative Design](https://www.nngroup.com/articles/parallel-and-iterative-design/) — parallel ontwerpen plus itereren verslaat itereren op één idee. Sterkste onderbouwing in dit document.
- [Figma, Design critiques at Figma](https://www.figma.com/blog/design-critiques-at-figma/) — zes critique-formats, presentator specificeert vooraf de gewenste feedback, geen "+1"-reacties.
- [Jakob Nielsen over design crits, 2024](https://jakobnielsenphd.substack.com/p/design-crit) — expliciet zeggen wat genegeerd moet worden stuurt de feedback.
- [Mountain Goat Software over de cost-of-change-curve](https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated) — waarom de 1:10:100-ratio niet houdbaar is; Boehm en Basili stelden hem in 2001 zelf bij.
- Connor & Irizarry, *Discussing Design* (2015) — kritiek koppelen aan het doel in plaats van aan smaak.
- Design by committee als risico: [Dovetail](https://dovetail.com/product-development/design-by-committee/) en [ProductPlan](https://www.productplan.com/learn/how-to-avoid-design-by-committee) — het probleem is ontbrekend eigenaarschap per ronde, niet het aantal rondes.

Let op het brontype: NN/g en Figma zijn de makers of onderzoekers zelf, de rest is vakblog zonder eigen meting. Er bestaat geen gecontroleerd experiment dat bewijst dat afgewerkte ontwerpen alleen detailfeedback uitlokken. Het is een goed onderbouwde vuistregel, geen wet.
