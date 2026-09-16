---
name: haakje-research
description: VERVANGEN op 2026-07-22 door de subagent `shift-research`, die de skill `person-research` in batch-modus aanroept. Roep die aan in plaats van deze skill. Dit bestand blijft alleen staan zodat lopende chats niet breken.
---

> **Deze skill is vervangen.** Gebruik de subagent **`shift-research`** (`.claude/agents/shift-research.md`). Die roept `person-research` aan als methode en voegt de SHIFT-context toe. De inhoud hieronder is opgegaan in die twee bestanden.
>
> Reden: `person-research` had al een diepere methode (bron-hiërarchie, WHY-analyse, identiteitscheck, onzekerheid-protocol) en heeft de originaliteitsladder er inmiddels ook in. Twee skills met dezelfde ladder lopen na verloop van tijd uit elkaar.

# Agent 3: haakjes zoeken (oude versie)

Je zoekt per persoon **één concreet ding waar een bericht op kan staan**. Niet een profielschets, niet een dossier. Eén haakje met een bron.

**Jij bent eigenaar van `projects/targetlijst-nl/haakjes-nl.csv`.** Je schrijft niet in `contacten-linkedin-nl.csv` en niet in `targetlijst-nl.csv`, want daar zitten andere agents in.

## Begin altijd zo

1. Lees `projects/targetlijst-nl/contacten-linkedin-nl.csv`.
2. Lees `projects/targetlijst-nl/haakjes-nl.csv`. Wie daar al in staat met Gevonden = Ja sla je over.
3. Bepaal je werkvoorraad met de regel hieronder.
4. Pak een batch van 10 tot 15 personen en werk die af. Rapporteer pas aan het eind van de batch.

### Wie je onderzoekt, en wie niet

**Alleen de mensen die Agent 2 heeft aangewezen.** Dat zijn de rijen waar de kolom **`Waarom deze persoon` gevuld is**. Dat is het teken dat er bewust één contact per organisatie is gekozen.

De rest van het bestand is een oudere ronde: meerdere mensen per organisatie, in bulk uit Clay gehaald, zonder dat iemand heeft bepaald wie de juiste is. Bij Habeo+ staan bijvoorbeeld 18 opleidingsmanagers. Daar diep onderzoek op doen is weggegooid werk, want er gaat er straks maar één een bericht krijgen.

```python
import csv
rows = list(csv.DictReader(open("projects/targetlijst-nl/contacten-linkedin-nl.csv", encoding="utf-8")))
gedaan = {(r["Organisatie"], r["Naam"]) for r in
          csv.DictReader(open("projects/targetlijst-nl/haakjes-nl.csv", encoding="utf-8"))
          if r["Gevonden"] == "Ja"}
werkvoorraad = [r for r in rows
                if r.get("Waarom deze persoon", "").strip()
                and (r["Organisatie"], r["Naam"]) not in gedaan]
print(len(werkvoorraad), "personen te doen")
```

**Is die werkvoorraad leeg, dan stop je en zeg je dat tegen Dante.** Dat betekent dat Agent 2 nog niet gedraaid heeft. Ga dan niet zelf kandidaten uitkiezen uit de oude rijen, want dan doe je het werk van Agent 2 over en waarschijnlijk anders.

Vraagt Dante expliciet om toch door te gaan, werk dan alleen aan organisaties die **precies één** contact in het bestand hebben. Bij meer dan één moet Agent 2 eerst kiezen.

## Wat telt als haakje

Iets concreets waar je een bericht aan kunt ophangen. De lat is niet hoog en de eis is niet dat het over onderwijs gaat.

**Telt wel:**
- Een uitspraak van de persoon zelf, in een interview, post, profieltekst of vakblad
- Iets waar de persoon aantoonbaar aan werkt of voor staat
- Iets van de **organisatie** dat concreet genoeg is: een AI-pagina, een visiestuk, een accreditatietraject, een NVAO-oordeel, een net gestart programma
- Iets persoonlijks dat niets met onderwijs te maken heeft, zoals een nevenfunctie of een opleiding die ze deden. Dat mag (afgesproken 2026-07-22)

**Telt niet:**
- "Ze werken bij een opleider en die kijken werk na." Dat geldt voor iedereen op de lijst
- Iets wat je afleidt maar niet kunt aanwijzen. Geen bron is geen haakje

**Bij een organisatie-haakje is dat prima**, en soms het enige wat er is. Bij Salta bijvoorbeeld publiceren de mensen zelf vrijwel niets en worden er sinds circa 2022 geen namen meer opgenomen in NVAO-rapporten. Dan draagt de organisatie het bericht.

## De zoekladder

Goedkoop eerst. **Stop zodra je iets hebt waar een bericht op kan staan, ook als dat al bij trap 1 is.** Niet doorzoeken naar iets mooiers.

| Trap | Wat | Kosten |
|---|---|---|
| 1 | Websearch op `"naam" + organisatie`, en op `"naam" interview` | gratis |
| 2 | Het LinkedIn-profiel: headline, about, en de beschrijvingen onder de functies | gratis als het laadt, anders trap 6 |
| 3 | Teampagina of "over ons" van de eigen site. Bij opleiders staat daar vaak een persoonlijk stukje | gratis |
| 4 | De organisatie zelf: AI-pagina, visiestuk, handboek, jaarverslag, NVAO-rapport, nieuwsberichten | gratis |
| 5 | Opleidingsachtergrond: waar gestudeerd, scriptie, publicatie, lidmaatschappen | gratis |
| 6 | Vakbladen, congresprogramma's, podcasts, nieuws van hun brancheorganisatie | gratis |
| 7 | **Apify**, via de `linkedin-profile-scraper` skill. Alleen als 1 tot 6 niets opleverden | circa 0,4 cent per profiel |

### Over trap 2 en 7
LinkedIn blokkeert automatisch ophalen vaak. Lukt het via zoekresultaten of cache, prima. Lukt het niet, ga dan door naar trap 3 tot 6 en gebruik Apify pas als die ook leeg blijven.

Bij Apify: **eerst het profiel** (headline, dan about, dan de functiebeschrijvingen). Levert dat niets op, dan pas de eigen posts, met `includeReposts` en `includeQuotePosts` op false. **Vacatureposts negeer je meteen**, die zeggen niets over wat iemand belangrijk vindt.

Het gratis Apify-plan is 5 dollar per maand, ongeveer 1.250 profielen. Ruim genoeg, maar controleer het verbruik bij een grote batch. Hoe, staat in de `linkedin-profile-scraper` skill.

## Geef elk haakje een niveau

**Dit is het belangrijkste veld dat je oplevert**, want het is de poort van Agent 4. Onder niveau 2 wordt er geen bericht geschreven.

De ladder staat volledig uitgewerkt in `.claude/skills/linkedin-outreach/haakje-zoeken.md`. **Lees dat bestand voor je begint.** Kort:

- **Niveau 3** — je maakt iets op basis van hun eigen idee en geeft het weg, krediet volledig naar hen
- **Niveau 2** — je ziet iets in hun situatie dat zij zelf niet hebben gezegd, en trekt daar een consequentie uit
- **Niveau 2b** — de eerlijke non-sequitur: iets menselijks en zichtbaars van hun profiel, waarbij je meteen zelf toegeeft dat het niks met je reden te maken heeft
- **Niveau 1** — citeren en dan pitchen. Niet goed genoeg. Iedereen doet dit

Twee tests voor je een niveau toekent:
1. **Had dit ook naar honderd anderen gekund?** Ja, dan is het geen niveau 2.
2. **Waarom stuurt uitgerekend Dante dit, en waarom nu?** Kun je dat niet in één zin, dan ontbreekt de why-now.

Lever een niveau 1 gewoon aan met `Niveau = 1`. Niet weggooien, want Dante haalt er soms nuance uit die jij mist. Maar schrijf het niet mooier op dan het is.

## Wat je oplevert

Eén rij per persoon in `haakjes-nl.csv`.

**Lees eerst de kopregel van het bestand en volg die volgorde.** De kolommen zijn in de loop van het project uitgebreid, dus ga niet uit van een vast aantal. Op 2026-07-22 waren het er elf:

`Organisatie, Naam, Functie, LinkedIn, Haakje, Bron-URL, Bron-type, Niveau, Trap, Gevonden, Alternatief`

- **Haakje**: is het een citaat, neem het dan letterlijk over tussen aanhalingstekens. Anders in één zin wat het is.
- **Bron-type**: headline, about, experience, teampagina, organisatie, publicatie, post, vakblad, interview
- **Niveau**: 1, 2, 2b of 3. Zie hierboven
- **Trap**: bij welke trap van de zoekladder je het vond. Zo meten we of de ladder klopt
- **Gevonden**: Ja of Nee. Nee mag, en is beter dan iets verzinnen

**Altijd aanvullen met een script, nooit het bestand herschrijven.** Bouw de rij op de kopregel, dan blijft het goed gaan als er later een kolom bijkomt:

```python
import csv
pad = "projects/targetlijst-nl/haakjes-nl.csv"
hdr = next(csv.reader(open(pad, encoding="utf-8")))
waarden = {"Organisatie": org, "Naam": naam, "Haakje": haakje,
           "Bron-URL": url, "Bron-type": brontype, "Niveau": "2",
           "Trap": "2", "Gevonden": "Ja"}
with open(pad, "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow([waarden.get(k, "") for k in hdr])
```

## Regels

- **Nooit een citaat of bron verzinnen.** Niets gevonden is Gevonden = Nee. Dat is een geldige uitkomst.
- **Naamgenoten uitsluiten.** De persoon moet aantoonbaar aan déze organisatie hangen. Bij kleine ondernemers is dit een reëel risico.
- **Schrijf het bericht niet.** Dat is stap 4 en dat doet Dante mee. Jij levert de grondstof.
- **Meld het als iemand vertrokken lijkt.** Dat is waardevoller dan een haakje.
- **Laadt een bron niet, sla hem over en ga door.**

## Afsluiten

Meld per batch: hoeveel personen gedaan, hoeveel haakjes gevonden, bij welke trap ze gevonden werden, en bij wie het niet lukte. Die verdeling over trappen is belangrijk: als bijna alles uit trap 4 komt, moeten we de ladder aanpassen.
