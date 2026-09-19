---
name: question-builder
description: Maakt vragen die een gesprek openen in plaats van een formulier invullen. Twee motoren, ankeren (van onderzoek naar een vraag met de bron erin) en kantelen (van het antwoord van de prospect naar de vervolgvraag die de rem blootlegt). Trigger wanneer Dante zegt "maak vragen voor dit gesprek", "welke vragen moet ik stellen", "verbeter deze vraag", "wat vraag ik hierop door", "hij zei X, wat nu", of research/een jaarverslag/een transcript aanlevert om vragen uit te halen. Voor een heel gesprek voorbereiden is dit de vraagmotor onder /sales-coach prep en /cold-call-prep, niet de vervanger daarvan.
---

# Question Builder

Doel: nooit meer "wat gaat er goed?". Elke vraag draagt bewijs dat Dante zijn huiswerk deed, of legt een last bloot die de prospect zelf nog niet hardop had gezegd.

Twee motoren. Motor 1 draait op onderzoek, motor 2 op wat de prospect net zei. Lees `reference.md` in deze map voor de kantelpatronen en de voorbeeldenbank.

## Motor 1: ankeren (onderzoek → vraag)

Vaste vorm, in deze volgorde:

```
[vindplaats + feit uit de bron]  →  [open vraag met vraagwoord over hun aanpak]
```

> "I read in your annual report that digital sales grew 40% this year. What do you put that down to?"

Regels:
- **Eén observatie, niet drie.** De vindplaats zit in de zin zelf (jaarverslag, visitatierapport, hun beleidsstuk, een post van hemzelf), niet als voetnoot.
- **Vraagwoord verplicht**: hoe, wat, wie, waar, wanneer, hoeveel, waarom. Nooit sluiten op "klopt dat?", "herkenbaar?" of "zou dat interessant zijn?".
- De vraag gaat over **hun huidige aanpak**, niet over Eduface en niet over interesse.
- Is het cijfer de basis voor de cost justification later, dan eerst toetsen en **daarna pas** de open vraag: "…around 35 lecturers. Is that still roughly where you are? … And how is the marking split across them?" De toets is nooit het slot van de beurt.
- Elke geankerde vraag krijgt de bron eronder (wat, wie, datum, link) zodat Dante "waar heb je dat gelezen?" direct kan beantwoorden.

## Motor 2: kantelen (antwoord → vervolgvraag)

Een antwoord is grondstof, geen eindpunt. Erken kort, kantel dan.

**Positief antwoord → zoek de rem.** Dit is de belangrijkste beweging.
> "40% is impressive. Is there anything you feel held you back from growing even more?"

Waarom dit werkt: mensen verdedigen hun succes niet, ze willen graag vertellen wat er ondanks dat succes niet lukte. Daar zit de pijn, en die hebben ze zelf benoemd in plaats van jij.

**Negatief antwoord → zoek de poging en de prijs**, niet nog een klacht.
> "What have you already tried, and where did it break down?"

De volledige lijst kantelingen (rem, prijs, houdbaarheid, uitzondering, incident, spreiding, tegenspraak) staat in `reference.md`. Kies er één per beurt, nooit twee.

## LDS eromheen

Nooit een kale lijst opleveren, dan gaat Dante als een robot van vraag naar vraag. Elke vraag komt met:
- **twee doorvraaglagen** ("what do you mean exactly", "can you give me an example of the last time that happened")
- **één samenvatzin** die terugspeelt in hun woorden ("so if I've got this right… is that fair?")
- **een bruggetje** naar het volgende blok

Reken met 6 tot 8 vragen per half uur inclusief LDS. Label per vraag **must** of **als er ruimte is**. Check de agenda voor de echte duur en reken terug. Past het niet, dan gaat de rest naar een sectie "gesprek 2", alleen als thema's, niet uitgeschreven.

## De vijf toetsen (elke vraag doorloopt ze voor je hem oplevert)

1. **Google-toets** Kon ik dit zelf opzoeken? Dan schrappen, dat kost punten in het gesprek.
2. **Vraagwoord-toets** Begint hij niet met een vraagwoord, dan levert hij ja of nee op en is het stil. Herschrijven.
3. **Spiegel-toets** Zit ons antwoord al in de vraag ("hoeveel tijd kost nakijken jullie?"), dan is het een pitch vermomd als vraag. Haal de oplossing eruit.
4. **Complimenttoets** Vleit de vraag alleen? Dan mist de kanteling. Voeg de rem toe.
5. **Eén-vraag-toets** Twee vragen in één beurt betekent dat ze de makkelijkste beantwoorden. Splitsen.

## Gevoelige vragen

Besluitvorming, budget en tegenstanders altijd indirect. Nederlandse directheid landt niet bij een Britse of Ierse prospect. Vraag naar gewoontes in plaats van bevoegdheden, gebruik "if" bij budget, en vraag om hulp bij een bezwaar in plaats van naar een tegenstander. Formuleringen staan in `reference.md`.

## Taal

Uitleg en toelichting in het Nederlands. **Elke zin die Dante letterlijk tegen een Engelstalige prospect uitspreekt schrijf je in het Engels**, apart gezet zodat hij hem hardop kan oefenen.

## Output

Per blok een kop met het doel, daaronder per vraag:

```
[must] Vraag in de spreektaal van het gesprek
  bron: waar het feit vandaan komt (met link)
  door: laag 1 / laag 2
  kantel: welke kanteling je klaar hebt liggen als het antwoord positief is
  beweegt: welk element in de kwalificatie dit verplaatst
```

Daarna de bruggetjes tussen de blokken, en tot slot "voor gesprek 2" met de thema's die niet passen.

## Wat deze skill niet doet

- Geen onderzoek. Dat is `person-research` (één persoon) of `shift-research` (meerdere).
- Geen volledig belscript. Dat is `cold-call-prep`.
- Geen dealdiagnose of debrief. Dat is `sales-coach`.
Deze skill levert alleen de vragen, en wordt door die drie aangeroepen.
