---
name: task-planning
description: Dagelijkse, wekelijkse en maandelijkse taakplanning en prioritering voor Dante in Todoist. Haalt zijn open en verlopen taken op, rangschikt ze tegen context/current-priorities.md, beschermt zijn deep-work-blokken, levert een plan op en past de wijzigingen toe in Todoist. Trigger als Dante zegt "plan mijn dag", "wat moet ik vandaag doen", "wat staat er vandaag", "weekplanning", "plan mijn week", "maandoverzicht", "prioriteer mijn taken", of op een ochtendcron.
---

# Task Planning

Dante's planningsmotor. Maakt van een stapel Todoist-taken een geordend plan en ruimt de lijst meteen op.

> **Status op 19-09-2026: werkt, maar is niet af.** De ladder hieronder is bijgewerkt op de nieuwe prioriteiten, de kapotte verwijzingen zijn eruit, en de deep-work-blokken zijn toegevoegd. Wat nog mist staat onderaan bij **Wat hier nog moet gebeuren**. Gebruik hem, maar behandel de uitkomst als een voorstel, niet als een oordeel.

## De ankers

Twee bestanden, elke run opnieuw lezen:

- `context/current-priorities.md`: de twee doelen en de leidende maat.
- `references/deep-work.md`: waarom de ochtendblokken heilig zijn.

De twee doelen zijn:

1. **Elke maand 20 salesprocessen starten**, gemiddeld 50.000 euro.
2. **NPS boven de 50 op de Enterprise-versie.**

De leidende maat is **uren deep work**. Een plan dat de doelen dient maar de ochtendblokken opeet, is een slecht plan.

## Modes (uit het verzoek afleiden)

- **daily** (standaard): vandaag plus verlopen. "plan mijn dag", "wat moet ik vandaag doen".
- **weekly**: deze week plus een korte terugblik. "weekplanning", "plan mijn week".
- **monthly**: de maand tegen de doelen. "maandoverzicht", "wat moet er deze maand af".

Twijfel je, neem **daily**. Niet vragen.

## De loop

```
1. LOAD     lees context/current-priorities.md (het anker)
2. PULL     haal taken uit Todoist voor het venster van de mode
3. BLOK     zet de deep-work-blokken eerst vast, plan de rest eromheen
4. SCORE    rangschik elke taak op de ladder hieronder
5. PLAN     schrijf het plan in Dante's stem (sjabloon in reference.md)
6. APPLY    herprioriteren, verlopen taken verzetten, ontbrekende taken toevoegen
7. GAPS     meld doelen zonder taak erachter, en wat er veranderd is
```

## De prioriteitsladder

- **P1, nu doen.** Start of beweegt een salesproces (outreach die vandaag de deur uit moet, een discovery, een voorstel dat ligt te wachten), of raakt direct de Enterprise-NPS (een klant die vastloopt, een openstaande klacht, een onboarding die stilstaat). Ook: een harde externe deadline binnen het venster.
- **P2, belangrijk.** Vult de bak voor volgende maand: prospectonderzoek, lijsten, sequences klaarzetten, opvolging op warme leads. Draagt bij aan de 20 per maand, maar niet vandaag.
- **P3, ondersteunend.** Verbeteringen aan hoe het werk loopt: skills, documentatie, rapportage, interne tooling.
- **P4, administratie.** Bundelen of schrappen.

Tiebreakers op volgorde: deadline, dan fase van de deal (een late deal wint van een koude), dan impact per uur.

**Niet opblazen.** Vijf keer P1 is geen prioritering. Er is altijd één bovenste taak.

## Deep work gaat eerst

Voor je taken over de dag verdeelt:

- **Ma t/m do 07:40 tot 09:10 en 09:20 tot 10:30** zijn geblokkeerd. **Vrijdag thuis 08:00 tot 09:30 en 10:00 tot 11:30.**
- In die blokken komt **één** taak, en dat is de bovenste P1 die echt denkwerk vraagt. Geen mail, geen Close bijwerken, geen belrondje.
- Shallow werk (CRM, mail, opvolging, inplannen) gaat naar de middag.
- De ochtendtrein van 06:23 tot 07:23 is de plek voor afgebakende klussen van hooguit een uur. Zet daar bewust iets neer, anders lekt het naar het ochtendblok.
- Zie je een afspraak vóór 10:30 staan, meld dat. Dat is de enige regel die de hele opzet draagt.

## Wat je ophaalt

- **Include:** project **Eduface** `6g45VgPCC6MHp22p` (alle secties) plus de **Inbox** `6M5QRjwfxMV42g4Q`.
- **Exclude:** project **Personal** `6R32RmpH44VRMGJv`. Alleen meenemen als Dante om een persoonlijk of gecombineerd plan vraagt, en dan geldt `.claude/rules/context-loading.md`.
- Daily: `find-tasks-by-date` met `startDate: today` en `overdueOption: include-overdue`. Weekly: `daysCount: 7`. Monthly: `daysCount: 30` plus `find-completed-tasks` voor de terugblik.

**Vervallen op 19-09-2026:** de subprojecten Hot Lead Outreach, Webinar HHS aanmeldingen en Webinar HHS replies bestonden niet meer. Er zijn nog maar drie projecten: Inbox, Eduface, Personal. Kom je die ID's ergens tegen, dan zijn ze dood.

## Secties in Eduface (voor nieuwe taken)

Gecontroleerd op 19-09-2026:

| Sectie | ID |
|---|---|
| GTM | `6g45W5JMF3H83JPG` |
| Design | `6g45W5QRj6vVpCMG` |
| Eduface platform | `6g45WXVxh35HMW8j` |
| Event manager | `6g45W5PgFV3fcWVp` |

De secties Marketing, Lemlist, PLG en GEO/SEO bestaan niet meer. GTM heette eerder Sales, Design heette Framer.

## Wijzigingen toepassen (standaard doen)

Todoist-wijzigingen zijn intern en terug te draaien, dus voer ze uit in plaats van elke keer te vragen:

- **Herprioriteren** waar de Todoist-prioriteit niet met de ladder klopt (`update-tasks`, `p1` tot `p4`).
- **Verlopen taken verzetten** met `reschedule-tasks`, nooit met `update-tasks`, anders sneuvelt de herhaling en de tijd.
- **Toevoegen** als een doel uit `current-priorities.md` niets achter zich heeft staan. In de juiste sectie.
- **Melden** wat je veranderd hebt. Nooit stil iets verwijderen of afvinken. Afvinken alleen als Dante zegt dat het af is.

## Oplevering

Plan in Dante's stem: bondig, bullets, Nederlands, geen em-dashes, geen opsmuk. Begin met het ene dat vandaag het belangrijkst is. Sjablonen per mode staan in `reference.md`.

## Klaar als

- Er ligt een geordend plan, bovenste taak eerst, met de deep-work-blokken erin.
- Todoist klopt met het plan.
- Gaten zijn gemeld: een doel zonder taak, of iets dat achterloopt.

## Wat hier nog moet gebeuren

Bewust niet gedaan op 19-09-2026, omdat het echte data en keuzes van Dante vraagt:

1. **De 20 per maand telbaar maken.** De skill weet nu niet hoeveel salesprocessen er deze maand gestart zijn. Dat moet uit Close komen, niet uit Todoist, en dan kan het plan zeggen "nog 7 te gaan met 9 dagen".
2. **De NPS aan een bron hangen.** Zolang niet vastligt hoe en wanneer die gemeten wordt (vraag W4), kan de skill er niet op sturen.
3. **Deep-work-uren terugkoppelen.** Het scorebord staat in de agenda. De weekplanning zou de gehaalde uren van vorige week moeten noemen, maar leest de agenda nu niet.
4. **De cron.** Kan op een ochtendjob, is niet aangesloten. Alleen bouwen als Dante erom vraagt.
5. **Prioriteit per uur van de dag.** Nu gaat alles op één hoop. Zijn agenda zegt dat na 11:00 de meetings beginnen, dus taken die overleg vragen horen daar, niet om 08:00.

Pak je hier iets van op, werk dan deze lijst bij en log het in `decisions/log.md`.
