---
name: meeting-prep-tasks
description: Zet de voorbereidingstaken voor een aankomende meeting automatisch in Todoist. Maakt een parent-taak "[Account] kwalificeren" in Eduface > Sales met de vaste set discovery-voorbereidingssubtaken, gevuld met wat al bekend is uit Close en de agenda. Trigger wanneer Dante zegt "zet de voorbereiding voor [account] in Todoist", "maak prep-taken voor de meeting met X", "ik heb dinsdag een gesprek met Y, zet het klaar", "meeting prep", of wanneer er een nieuwe discovery/kennismaking in de agenda staat zonder voorbereidingstaken.
---

# Meeting Prep Tasks

Van "ik heb een gesprek met X" naar een complete voorbereidingschecklist in Todoist. Gemodelleerd op de CMI-kwalificatietaak (2026-07-21).

Dante's scope loopt tot de Discovery gate. Deze skill dient dus één doel: zorgen dat hij het gesprek in gaat met de juiste vragen, de juiste kennis, en een beeld van de organisatie.

## Input die je nodig hebt

- **Account** (verplicht). De rest zoek je zelf op, vraag niet door.
- **Datum van de meeting**. Staat die niet in de vraag, zoek dan in Google Calendar (`search_events` op de accountnaam, komende 30 dagen). Niet te vinden en niet genoemd: zet de deadline op vandaag + 3 dagen en meld dat in je antwoord.
- **Type gesprek**. Default = discovery/kwalificatie. Bij een tweede gesprek, demo of scoping: zie "Varianten".

## De loop

```
1. ZOEK      meeting-datum in Google Calendar, account in Close (lead + opportunity + notes)
2. CHECK     bestaat er al een "[Account] kwalificeren" parent in Todoist? Zo ja: vul aan, maak geen tweede
3. MAAK      parent-taak + de vaste subtaken (zie hieronder)
4. VUL       zet per subtaak in de description wat al bekend is uit Close, en wat nog open staat
5. MELD      korte bevestiging aan Dante: link naar de parent, datum, wat er al ingevuld staat
```

## Waar het heen gaat

- Project **Eduface** `6g45VgPCC6MHp22p`, sectie **Sales** `6g45W5JMF3H83JPG`.
- Parent-taak: `[Account] kwalificeren`, priority **p1** als de meeting binnen 7 dagen is, anders **p2**.
- Alle subtaken hangen onder de parent via `parentId`, zelfde project + sectie.
- **Deadline** (`deadlineDate`) op alle taken = de dag vóór de meeting. De meeting zelf is een harde constraint, de voorbereiding moet daarvoor af.
- `dueString` op de subtaken: verdeel over de werkdagen tussen nu en de meeting. Alles op één dag proppen werkt niet.

## De vaste set subtaken

Dit is de kern. Deze zes komen altijd terug:

1. **Discovery vragen voorbereiden** — de vragenlijst voor dit specifieke gesprek. Gebruik `/discovery` of de LDS-methode: geen kale vragenlijst, luisteren + doorvragen + samenvatten, must vs optioneel, gesplitst over meerdere meetings. Besluitvorming en budget subtiel formuleren.
2. **Discovery kennis strak hebben** — wat moet Dante uit z'n hoofd weten: het product (alleen wat echt bestaat, zie `references/eduface-product.md`), de referentieklanten, de prijsstructuur, de antwoorden op de standaard bezwaren.
3. **Weten wat hij/zij belangrijk vindt** — persoonlijk onderzoek naar de contactpersoon. Roep hiervoor `/person-research` aan. Publicaties, LinkedIn-posts, onderwijsvisie, wat drijft die persoon.
4. **Huidige situatie bij hen in kaart brengen** — toetsprogramma eerst: wat leveren lerenden in, hoeveel, wie kijkt na. Plus LMS, onderwijsvisie, lopende AI-initiatieven.
5. **Financieel plaatje** — dealwaarde-inschatting op basis van `references/pricing/`. Wie heeft budget, welk budget is dit (opleidingsbudget, innovatie, IT), en wat kost hun huidige situatie.
6. **Hoe groot is [Account]** — aantal lerenden, aantal opleidingen, aantal beoordelaars, omzet. Bepaalt de staffel en of dit een pilot of meteen een licentie is.

Pas de titels aan op het account (subtaak 3 en 6 krijgen de echte naam). Voeg extra subtaken toe als de situatie erom vraagt, maar laat er nooit één van deze zes weg.

## Vullen met wat al bekend is

Een lege checklist is half werk. Voordat je de taken aanmaakt:

- Zoek de lead in Close (`lead_search` op accountnaam), lees de opportunity, de notes en de mail-historie.
- Zet per subtaak in de `description` wat je al gevonden hebt, met bron, plus expliciet **wat nog open staat**. Dat is het werk dat Dante moet doen.
- Weet je iets niet, schrijf dan "nog uitzoeken" in plaats van een gok. Nooit iets invullen dat niet uit een bron komt.
- Staat er al een Artifact of onderzoeksdocument over dit account, link die in de description van de parent (zoals de CMI-taak doet).

## Varianten

- **Tweede gesprek / verdieping** — parent heet `[Account] tweede gesprek voorbereiden`. Subtaken: openstaande discovery-vragen uit gesprek 1, LMS/integratie uitzoeken (techniek hoort in gesprek 2), stakeholders in kaart, cost justification met hun eigen cijfers laten bevestigen.
- **Demo** — parent `[Account] demo voorbereiden`. Subtaken: demo-scenario op hun eigen opdrachttype, wie zit erbij, wat is de gewenste next step, wie doet welk deel.
- **Scoping / hand-off naar Jeroen** — Dante's scope stopt bij de Discovery gate. Maak dan geen executietaken, maar één taak: overdracht voorbereiden voor Jeroen (samenvatting pijn, spelers, why now, BANT, afgesproken next step).

## Applying

Todoist-wijzigingen zijn intern en omkeerbaar. Gewoon aanmaken, niet eerst vragen. Gebruik `add-tasks` (max 25 per call): eerst de parent in één call, dan de subtaken met de teruggegeven `parentId`.

Bestaat de parent al: voeg alleen de ontbrekende subtaken toe en werk de descriptions bij. Nooit dubbele taken, nooit iets afvinken of verwijderen.

## Output

Kort in de chat, geen Artifact:
- Link naar de parent-taak
- Meeting-datum + deadline die je hebt gezet
- Per subtaak één regel: wat er al ingevuld staat, wat open staat
- Wat je niet kon vinden

## Done

- Parent + zes subtaken staan in Eduface > Sales, onder elkaar, met deadline vóór de meeting.
- Elke subtaak heeft een description met wat bekend is en wat open staat.
- Dante weet in één blik wat hij nog moet doen voor het gesprek.
