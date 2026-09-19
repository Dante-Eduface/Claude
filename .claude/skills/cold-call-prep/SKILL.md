---
name: cold-call-prep
description: Zet het onderzoek naar een contact om in een uitgeschreven belscript in Dante's vaste template, met de bron onder elke regel waarin hij iets aanhaalt. Trigger wanneer Dante een naam plus organisatie aanlevert om te bellen, of zegt "bereid deze cold call voor", "maak een belscript", "ik ga [naam] bellen", of een lijst contacten plakt om te bellen. Ook de plek waar de roleplay-prompt staat.
---

# Cold Call Prep

**Lees `reference.md` in deze map voor je het script schrijft.** Daar staan de inhoudelijke regels: wat Eduface precies is en wat je dus mag claimen, welke klantnamen wel en niet, de pijn per trajectlengte, de vijf haakje-toetsen, de kwalificatieregels en de bijzondere situaties. Dit bestand is het proces, dat zijn de regels.

Eén contact aanleveren betekent altijd **twee** dingen opleveren: het onderzoek én het belscript (`cold-call-research-then-script`). Onderzoek zonder script is geen oplevering, want Dante belt met een script in beeld en niet met een dossier.

Doel van het telefoontje is een afspraak voor de Discovery-fase, niet meer. Dante's scope stopt bij de Discovery gate, daarna draagt hij over aan de founders (`scope-discovery-gate`). Sluit dus af op "een moment inplannen", niet op een toezegging verderop in de funnel.

Levert Dante meerdere namen tegelijk aan, werk ze dan één voor één af en lever per persoon compleet op. Niet eerst zes keer onderzoek en dan zes scripts.

## Stap 1: het onderzoek doet `person-research`

**Roep `person-research` aan in diepte-modus.** Die skill dekt de hele onderzoekskant: de CRM-check in Close en Gmail, de identiteitscheck en de functietitel uit twee bronnen, de zoekladder tot en met Apify, de visitatierapporten, het toetsprogramma, de AI-scan van de instelling inclusief LMS en beleid, de woordenlijst, de WHY-analyse, het onzekerheid-protocol en de bronnenlijst. Schrijf dat niet opnieuw op en doe het niet zelf.

Bij twee of meer personen tegelijk: `shift-research` (agent 3), zie `batch-research-not-per-person`. Sinds 17-09-2026 levert agent 3 dezelfde diepte als `person-research` (geen aparte ondiepe batch-modus meer) — het verschil is alleen dat hij de wachtrij als geheel afwerkt in plaats van dat jij `person-research` los per naam aanroept.

Jij begint waar person-research ophoudt.

## Stap 2: is dit een goed telefoontje?

Twee zinnen bovenaan het dossier: hoe sterk is deze prospect en waarom. Niet alles is een goede fit, en dat zeggen is nuttiger dan het verbergen. Dante moet weten of hij hiervoor gaat zitten.

Waar je op kijkt, met het toetsprogramma uit person-research in de hand:
- **Hoeveel geschreven werk** leveren lerenden in, en hoe vaak
- **Trajectlengte**: kort traject betekent werkdruk bij beoordelaars, lang traject betekent uitval (`eduface-werking-in-outreach`)
- **Taal**: internationale studenten die in een tweede taal schrijven zijn de sterkste use case
- **Aantal beoordelaars en locaties**: consistentie wordt een vraagstuk zodra het er meer dan een handvol zijn
- **Freelance of parttime docenten**: nakijken is dan bijwerk

Val nooit af op dealwaarde alleen (`small-deals-still-count`).

Zegt person-research dat er **geen laag onderwijs of kwaliteit** onder de directie zit, dan bel je de directeur toch, maar met een **aangepaste ask**: vraag om een introductie naar de persoon die over onderwijskundige kwaliteit gaat, niet om een demo.

Mik op de onderwijslaag: directeur onderwijs/kwaliteit, niet de eigenaar die zelf lesgeeft (`route-to-onderwijslaag`). Examencommissie is een harde nee, die koopt niks; een opleidingsmanager alleen als er niks hogers is, met de directeur/hoofd onderwijs als tweede kandidaat ernaast (`never-examencommissie-opleidingsmanager-meh`).

**Vlak voor het bellen**: check of het nummer/de persoon nog klopt. Werkt hij/zij er nog en zit de functie nog in de ICP? Verifieer via LinkedIn, dat heeft als enige bron einddatums (`verify-contact-still-employed`, `linkedin-is-hoofdbron`). Klopt de functietitel niet met wat in het dossier staat, ga af op LinkedIn (`verify-title-on-org-source`).

## Stap 3: het belscript, Dante's vaste template

Herzien op 21-08-2026. De pitch staat nu **vóór** de unieke opening, niet erna. Reden: hij koopt in de eerste twintig seconden het recht om door te praten met wie hij is en wie er met hem werkt, en pas daarna gaat het over hen.

```
1. Opening        "Hi, met Dante van Eduface.
                   Spreek ik met [voornaam]? Fijn."

2. Toestemming    "Schikt het dat ik je kort even bel?"
                   Nee = vraag wanneer wel en bel dan echt terug. Niet doordrukken.

3. Pitch          "We hebben samen, met de hulp van de Universiteit Leiden en de
                   Radboud Universiteit, een AI-model gemaakt dat summatieve en
                   formatieve beoordeling kan doen. Dit model wordt momenteel ingezet
                   bij alle grote universiteiten in Nederland."

4. Sociale proof  "Onze tool wordt onder andere ingezet bij Hogeschool Rotterdam
                   en De Haagse Hogeschool."
                   Bij een academische of wo-prospect combineer je met Tilburg
                   University. TIO en ICM nooit noemen.

5. Unieke opening   observatie + open vraag die begint met een vraagwoord

6. LSD            luisteren, samenvatten, doorvragen, met bruggetjes terug naar het
                   script (`discovery-lds-methode`)

7. Persoonlijke vraag   standaard: "Zelf ben ik net terug van vakantie, weet niet
                        hoe dat bij jou zit?" Beter: iets uit hun eigen loopbaan

8. LSD

9. Afsluiten      voorstel om een moment in te plannen en samen te verkennen of
                   veilige en verantwoorde AI iets kan zijn voor [organisatie]
```

De productformulering blijft ongewijzigd: het gaat om **formatieve feedback op schrijfopdrachten**, en het model beslist niet, de examinator houdt het laatste woord. Zeg die grens zelf voordat de prospect hem noemt, zeker bij iemand met een toets- of examenachtergrond.

**Klantnamen, herzien 02-09-2026.** Er is één lijst voor alle segmenten: **Hogeschool Rotterdam, De Haagse Hogeschool, Tilburg University**. **TIO Business School en ICM Opleidingen nooit noemen**, dat draait de herziening van 21-08-2026 terug. Kies de naam die het type opleider spiegelt: bij een hbo of particuliere opleider twee hogescholen, bij een academische prospect Tilburg erbij. Welke naam je vooropzet is een personalisatie (heeft de prospect daar gestudeerd of gewerkt, noem dan díe).

Pas de pitch aan op de taal van de prospect. "Een Nederlands AI-model" klinkt bij een Engelstalige instelling als "werkt niet voor ons": zeg dan dat het mét Nederlandse universiteiten is gebouwd.

### De unieke opening: de belangrijkste regel van het script

De vorm van deze regel en van elke vervolgvraag in het script komt uit `question-builder`: ankeren op een bron, open vraag met een vraagwoord, en een kanteling klaar voor als het antwoord positief uitpakt.


**Één observatie die bewijst dat je je onderzoek hebt gedaan, met de vindplaats in de zin verwerkt, direct gevolgd door een open vraag die begint met een vraagwoord** (hoe, wat, wie, waar, wanneer, hoeveel) (`unieke-opening-observatie-plus-vraagwoord`).

Dante's eigen maatstaf:
> "Ik zag in het NVAO-visitatierapport, hoofdstuk toetsing, dat de intercodeurbetrouwbaarheid bij het nakijken van schrijfopdrachten een aandachtspunt was voor jullie sectie. Hoe pakken jullie dat momenteel zelf aan?"

- Eén observatie, niet drie. Een opsomming is huiswerk laten zien, geen gesprek openen
- De vraag gaat over **hun huidige aanpak**, niet over Eduface en niet over interesse
- Nooit afsluiten met "klopt dat?", "herkenbaar?" of "zou dat interessant zijn?"
- Geef altijd één zachter alternatief mee

### Elke aangehaalde regel draagt zijn bron

Onder elke scriptregel waarin Dante iets aanhaalt komt direct de bron, niet alleen in een lijst onderaan (`script-lines-carry-their-source`). Aan de telefoon moet hij "waar heb je dat precies gelezen?" in één seconde kunnen beantwoorden, zonder te scrollen.

> **Bron, als hij ernaar vraagt:** [wat voor document], [organisatie/auteur], [datum en kenmerk], [hoofdstuk of standaard]. Letterlijk: *"..."*. [link]

Zet erbij wat hij wel en niet gelezen heeft. Nooit "ik las jullie handreiking" als je alleen de beschrijving ervan in een rapport hebt gezien.

### Verder verplicht in het script

- **Waar hij op moet letten tijdens de LSD**: vier tot zes signalen die deze prospect waarschijnlijk noemt, met per signaal de doorvraag. Neem het **LMS** altijd mee als vraag, integratie bepaalt adoptie en de beheerder is een aparte stakeholder; techniek hoort pas in gesprek twee (`lms-integratie-altijd-meenemen`)
- Budget en besluitvorming **indirect** bevragen, niet recht-toe-recht-aan ("wie beslist hierover meestal?" in plaats van "wie heeft het budget?"). NL-directheid landt niet altijd, zeker niet bij buitenlandse of internationale instellingen (`discovery-subtiel-vragen`)
- **Verwachte bezwaren** met antwoorden, minimaal vier, waaronder het bezwaar dat bij hun specifieke situatie hoort, plus prijs (zie reference.md) en een eventuele concurrent (bv. Onderwijs Orakel in de NL-markt, `competitor-onderwijs-orakel`)
- **Wat je NIET moet noemen**: een oude onvoldoende die inmiddels hersteld is, een gevoelig persoonlijk detail, of iets wat op naam van "de opleiding" staat en niet van deze persoon
- De **woordenlijst** uit person-research, overgenomen in het dossier zodat Dante hem tijdens het bellen voor zich heeft
- **Onzekerheden**, apart en expliciet
- Noemt de prospect een cijfer of claim die Dante zelf onderzocht heeft, laat hem dat aan de prospect laten bevestigen in plaats van het als feit te brengen (`discovery-verify-sources-with-prospect`)

## Oplevering

- Bestand: `GTM/Campaigns/cold-calling/<voornaam-achternaam-organisatie>.md`
- In de chat: de kern in bullets, plus het script als hij erom vraagt. Geen Artifact tenzij hij erom vraagt (`deliver-as-artifact`)
- Bronnenlijst onderaan, gesplitst primair / secundair / niet gelezen

## Roleplay

Wil Dante oefenen, dan staat de prompt klaar in `GTM/Knowledge/cold-call-roleplay-prompt.md`. Plakken in een nieuwe chat met het dossier eronder. Claude speelt de prospect, mag hem laten falen, en geeft daarna feedback per scriptstap plus praatverhouding en taalgebruik.

## Done

- `person-research` gedraaid, niet zelf overgedaan
- Fit-oordeel in twee zinnen bovenaan
- Script compleet in de zeven stappen, met bron onder elke aangehaalde regel
- LSD-signalen, bezwaren, woordenlijst en onzekerheden erbij
- Bestand staat in `GTM/Campaigns/cold-calling/`
