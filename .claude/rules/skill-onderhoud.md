# Skills actueel houden

Vastgelegd 20-09-2026, op verzoek van Dante: een skill moet ervoor zorgen *"dat de skills altijd actueel en altijd actief zijn"*, en ik moet zelf nadenken *"op het moment dat ik ergens mee bezig ben met een bepaalde skill of ik praat over een bepaald onderwerp: moet ik misschien deze skill updaten?"*

Dit is de tweelingregel van `.claude/rules/context-onderhoud.md`. Die gaat over contextbestanden, deze over skills. Hetzelfde probleem: een skill die niet meer klopt is erger dan geen skill. Hij klinkt betrouwbaar, hij vuurt vanzelf, en niemand doet hem open.

Hoe je een skill bouwt staat in `.claude/skills/skill-builder/`. Deze regel gaat over wat er daarna gebeurt, en geldt in **elke sessie**, ook als skill-builder niet geladen is.

## 1. Twee manieren waarop een skill veroudert

**Een dode verwijzing.** De skill wijst naar een bestand, een skill, een sectie-ID of een campagne die niet meer bestaat. Vervelend, maar zichtbaar: de stap loopt vast en je merkt het.

Voorbeeld, 20-09-2026: `skill-builder/SKILL.md` wees naar `.claude/skills/hot-lead-outreach/` als voorbeeldskill. Die map bestaat niet meer.

**Een bevroren kopie.** De skill heeft een feit overgeschreven dat ergens anders is veranderd. Dit is de gevaarlijke. Er loopt niets vast, de skill doet gewoon overtuigend zijn werk op verouderde informatie.

Voorbeeld, 20-09-2026: `fitness-coach` stuurt op WHOOP-herstel, InBody-metingen en een gewichtdoel. Alle drie vervallen op 19 en 20-09. En `week-plannen` heeft de deep-work-tabel uit `Context/current-priorities.md` overgeschreven in plaats van ernaar te verwijzen: vandaag klopt hij, na de volgende wijziging zijn het twee waarheden.

De omvang is te meten: op 20-09-2026 verwezen **2 van de 29 skills** naar een bestand in `Context/`. De rest draait op wat er op de bouwdag in is gezet.

## 2. De reflex: moet deze skill bij?

**Draait een skill, of gaat het gesprek over het onderwerp van een skill, dan toets ik die skill tegen wat ik nu weet.** Niet als aparte klus, gewoon tijdens het werk.

Vier momenten waarop dat hoort te gebeuren:

1. **Ik gebruik een skill.** Iets in de body klopt niet met wat ik in de repo, de agenda of Close zie. Dat is een vondst, geen ruis.
2. **Dante corrigeert de uitkomst.** Gaat de correctie over dit ene resultaat, dan is het een correctie en blijft het bij het record (`.claude/rules/feedback.md`). Gaat hij over hoe de skill werkt, dan hoort hij in de skill zelf, en bij de SHIFT-agenten in hun `LEERPUNTEN.md`.
3. **Een contextbestand verandert.** Werk ik iets bij volgens `context-onderhoud.md`, dan vraag ik me af welke skill op dat feit leunt. `grep -rl "<het feit>" .claude/skills/` kost vrijwel niets en geeft direct antwoord.
4. **Het gesprek gaat over het onderwerp zonder dat de skill draait.** Praat Dante over zijn training, dan ligt `fitness-coach` op tafel, ook al heeft hij hem niet aangeroepen.

Wat ik hierbij **niet** doe: een ronde langs alle 29 skills omdat er ergens iets veranderd is. De toets gaat over de skill die op tafel ligt.

## 3. De grens: zelf doen of voorleggen

Dante, 20-09-2026: *"dan kan hij een vraag aan mij stellen ... of als het simpele dingen zijn, kan hij dat gewoon aanpassen."*

| Zelf aanpassen, melden in één regel | Eerst voorleggen |
|---|---|
| Een pad, bestandsnaam of ID dat verhuisd is | De procedure zelf, of de volgorde van de stappen |
| Een feit dat de skill tegenspreekt terwijl het in een contextbestand vastligt | Wat de skill oplevert, en aan wie |
| Een kopie vervangen door een verwijzing naar de bron | Een trigger toevoegen of weghalen |
| Een verwijzing naar een geschrapte of hernoemde skill | Een skill splitsen, samenvoegen of archiveren |
| Een datum, een tikfout, een dode link | Alles waarvan ik de bron niet zeker weet |

Twijfel ik aan welke kant iets valt, dan is het voorleggen.

Voorleggen gaat in **één of twee regels, met de tekst zoals die erin komt te staan**, zodat Dante ja of nee kan zeggen zonder de skill open te doen. Zelfde eis als in `feedback.md`: een regel die ik samenvat is bijna nooit wat hij bedoelde.

**Stil wijzigen mag nooit**, ook niet bij de linkerkolom. Elke wijziging in een skill wordt genoemd in mijn antwoord, met wat er verandert en waarom.

## 4. Als ik het niet zeker weet

Niet gokken, markeren.

- Een feit dat ik niet kan staven krijgt op de plek zelf de regel `> **Te toetsen (JJJJ-MM-DD):** ...`.
- Is het hele fundament onder een skill weg, dan krijgt hij een waarschuwingskop bovenaan: wat geldt er niet meer, en welk bestand wint. Zo is `fitness-coach` op 20-09-2026 afgehandeld, markeren in plaats van herschrijven, want herschrijven was een klus die Dante niet gevraagd had.
- Een vraag die alleen Dante kan beantwoorden gaat naar `Context/open-vragen.md`, niet als aanname de skill in.

## 5. Waar het landt

| Wat | Plek |
|---|---|
| De wijziging zelf | de `SKILL.md` of het referentiebestand ernaast |
| Feedback op wat een SHIFT-agent oplevert | het `LEERPUNTEN.md` van die agent |
| Een skill die vervalt of vervangen wordt | `Archive/`, met de vervanger bij naam genoemd |
| Een wijziging met gevolgen | `Decisions/log.md` |
| Een vraag die ik niet mag invullen | `Context/open-vragen.md` |

## 6. Wat ik nooit doe

- **Een feit in een skill zetten dat in een contextbestand hoort.** Verwijzen, niet overschrijven. De bronregel staat in `.claude/skills/skill-builder/SKILL.md`.
- **Een skill verwijderen.** Naar `Archive/`, met de vervanger erbij.
- **Een skill aanpassen zonder het te melden.**
- **De hele skillmap opschonen omdat er één ding veranderd is.**
- **Twee versies van hetzelfde feit laten staan.** Nieuw wint, oud gaat weg. Zelfde regel als bij context.
