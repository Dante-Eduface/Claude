# Person Research — Technical Reference

De diepte-technieken achter de skill. SKILL.md is de methode; dit zijn de details en het gereedschap.

## Bron-hiërarchie

Behandel bronnen naar betrouwbaarheid. Hoger = zwaarder, en bepaalt of iets "feit" of "aanname" is.

**Intern eerst (onze eigen bron, hoogste waarde voor interactiehistorie):**
- **Close CRM** — bestaat de persoon/instelling al als lead of contact? Is er een opportunity/deal en in welke stage? Lees notities, activiteit, eerdere mails/calls/meetings. Dit vertelt hoe we ze kennen en of ze al warm zijn. Nooit iemand koud benaderen die al in een deal zit.

**Primair (feit, direct citeerbaar):**
- Hun eigen publicaties, papers, lectorale redes, boeken.
- Officiële instituutpagina (functietitel, mandaat, portefeuille).
- Hun eigen posts / interviews / talks (let op: hier speelt WHY het sterkst, zie onder).
- Officiële benoemings- of persberichten van de organisatie.

**Secundair (feit mits geattribueerd, check dubbel):**
- Vakmedia, nieuwsartikelen, branche-publicaties.
- Deelnemerslijsten, programma's, sprekerbio's van events.

**Tertiair (alleen als hint, NOOIT als hard feit):**
- Aggregators zoals RocketReach, ContactOut, Crunchbase-scrapes.
- Gebruik puur voor een functietitel-hint of om verder te zoeken. Label altijd als onbevestigd tot een primaire bron het bevestigt.

## Waar je echt werk vindt

Iemand met onderzoek/publicaties? Ga verder dan Google:
- **Google Scholar** — profiel + citaties + co-auteurs.
- **HBO-kennisbank** (`hbokennisbank.nl`) — hbo-lectoren en toegepast onderzoek.
- **ResearchGate** — papers + soms full-text.
- **SURF / SURF Communities** — onderwijs-ICT, learning analytics, digitaal toetsen.
- **Instituut-repositories** en de onderzoek/lectoraat-pagina van de instelling.
- **Noordhoff / uitgevers** — voor methode-auteurs.
- **DOI / objectstores** (bv. SURF objectstore) — directe PDF's van redes en rapporten.

Vind de publicatielijst, kies de meest relevante 1-3 stukken, en lees die echt.

## PDF's uitlezen

WebFetch faalt vaak op PDF's (binaire FlateDecode). Werkwijze die werkt:
1. WebFetch slaat de PDF lokaal op en geeft het pad terug (`.../tool-results/webfetch-*.pdf`).
2. Trek de tekst eruit met Python:
   ```
   python3 -c "from pypdf import PdfReader; r=PdfReader('PAD'); print(len(r.pages));
   [print(f'=== PAGE {i+1} ===', (p.extract_text() or '')) for i,p in enumerate(r.pages)]"
   ```
3. Grote redes/rapporten: eerst inhoudsopgave + inleiding lezen, dan gericht naar de relevante hoofdstukken (bv. het hoofdstuk over toetsing/feedback/personalisatie/learning analytics). Grep op kernwoorden om snel de juiste passages te vinden.
4. Haal **echte citaten** eruit met paginanummer. Dat maakt een hook onweerlegbaar.

**Let op afgebroken woorden.** Rapporten in twee kolommen breken woorden af over regels: `for- matieve`, `examen- commissie`, `beoorde- ling`. Grepp je op `formatieve`, dan krijg je nul treffers terwijl het er twee keer staat. Zoek op het achterstuk (`matieve`), of strip eerst de afbreekstreepjes:
```python
t = re.sub(r'-\s*\n\s*', '', t)   # of: t.replace('- ', '') als de tekst al platgeslagen is
```
Een nul-treffer op een kernwoord is dus geen bewijs dat het er niet staat. Controleer het twee keer voor je concludeert dat een rapport ergens niets over zegt.

## De WHY-analyse

Voor elke publieke uitspraak of positie, reconstrueer:
- **Publiek:** tegen wie zei die dit? (collega's, bestuur, sector, studenten)
- **Aanleiding:** waarop reageerde die? Welk probleem speelde er?
- **Motief:** wat wil die bereiken of vermijden?
- **Reikwijdte:** gaat dit over hun huidige situatie, of algemeen? (Bv. een klacht over "leveranciers" gaat over hún leveranciers, niet over jou.)

Dit bepaalt of een citaat een goede hook is of juist een valkuil. Een uitspraak letterlijk teruggeven zonder de WHY leidt vaak tot een mail die precies de verkeerde snaar raakt. Sluit aan op `causal-research-not-footprint`: reconstrueer de redenering, inventariseer niet alleen het voetspoor.

Let ook op: iemands eigen woorden letterlijk terugpapegaaien in outreach voelt als scraping. Gebruik de WHY om het idee in je eigen woorden te raken, zodat het gevoel klopt (zie `new-feedback-overrides-old` en de communicatie-regels).

## Het onzekerheid-protocol

Standaard bij twijfel. Nooit dichtpoetsen. Formats:
- **Niet te verifiëren feit:** "Ik vond X op [tertiaire bron], maar geen primaire bevestiging. Behandel als aanname tot we het checken."
- **Interpretatie met meerdere kanten:** "Dante, lees dit: [citaat + bron]. Wat zie of versta jij hieruit?" Dante kent de context/persoon vaak beter dan het web.
- **Naamsverwarring:** "Er zijn twee [naam]'s; de aangeleverde link is waarschijnlijk de verkeerde. De juiste is vermoedelijk [link], maar verifieer voor je personaliseert."

## Efficiënt werken

- Fan-out mag parallel: meerdere web-searches en fetches tegelijk. Voor meerdere personen of accounts tegelijk kun je research-subagents parallel inzetten (zoals bij de Aeres/Avans-research), maar houd de eindconclusie en validatie bij jezelf.
- Begin breed (naam + instelling), verifieer identiteit, ga dan diep op de 1-2 sterkste bronnen. Niet elke bron hoeft; de beste primaire bron plus een echte publicatie is genoeg voor een sterke hook.

## Veelgemaakte fouten

- Een tertiaire aggregator als hard feit citeren.
- Een LinkedIn-profiel pakken zonder identiteit te checken (verkeerde naamgenoot).
- Een citaat als hook gebruiken zonder de WHY (raakt de verkeerde snaar).
- Alleen artikelen óver iemand lezen terwijl er echt werk ván die persoon te vinden is.
- Onzekerheid wegmoffelen met een zelfverzekerde formulering.
