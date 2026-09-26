# Close: Playbooks en Outcomes

_Aangelegd 2026-09-26. Bron: help.close.com (Playbooks, Outcomes, Note Templates and Summary Guidance, Using Playbooks on Calls, Notetaker, Call Assistant, AI Credits, Workflows), naast onze eigen Close-inrichting van dezelfde dag. Status: voorstel, nog niet ingericht._

## Hoe het werkt

**Playbook.** Een sjabloon per soort gesprek (call of meeting). Bundelt vier dingen:
- outcomes: de mogelijke uitkomsten van het gesprek
- custom fields: velden die je tijdens of na het gesprek invult
- note template: een vaste notitie-opbouw die na het gesprek op de lead verschijnt, template tags mogen erin
- summary guidance: een instructie voor de AI-samenvatting van dat soort gesprek

**Outcome.** De uitkomst van een verbonden call of een afgeronde meeting. Alleen te kiezen als er een playbook op het gesprek staat. Het playbook bepaalt welke outcomes er zijn.

Wat je moet weten:
- **Playbook kiezen** kan voor, tijdens of na het gesprek. Close AI vult hem zelf in als het zeker genoeg is, anders blijft hij leeg. Een vast playbook per dialer of leadtype kan niet.
- **De AI stelt de outcome voor** na afloop, op basis van het transcript en de beschrijving van elke outcome. Je kunt altijd overschrijven. Zit hij vaak mis, dan is de beschrijving het probleem.
- **Geen transcript, geen AI.** Zonder transcript geen voorgestelde outcome, geen samenvatting volgens de guidance, geen ingevulde velden. Handmatig kiezen werkt wel.
- **Custom fields** moeten eerst bestaan als Shared Field (Settings > Custom Fields). De waarde landt volgens de docs op de lead of het contact. Filterbaar in Smart Views en rapporten.
- **Playbook wisselen** wist een outcome die niet bij het nieuwe playbook hoort.
- **Outcomes zijn optioneel.** Na 24 uur klapt het veld in, via "More" kun je hem later nog zetten.
- **Beheer** in Settings > Playbooks and Outcomes, alleen met de permissie Manage Customizations. Naam wijzigen werkt overal door. Verwijderen raakt oude gesprekken niet. Archiveren bewaart de historie.
- **Rapportage.** Activity Overview en Activity Comparison tonen per outcome het aantal, de totale duur en de gemiddelde duur. Filters op leads en in Conversations: calls of meetings met outcome X, de laatste call met outcome X, de laatst afgeronde meeting met outcome X.
- **Workflows.** Een workflow kan starten op een Call event of Meeting Activity event en met Update Lead een status of veld zetten. De Workflow Goal "Outcome met" stopt een lopende run.
- **Voicemail drop** kan automatisch een outcome zetten. Eén outcome is aan te wijzen.
- **Plan:** Growth en Scale. Wij zitten op Growth.
- **Kosten.** De AI-invulling na het gesprek (outcome, samenvatting volgens guidance, velden) heet Auto Updates en kost AI-credits. Hoeveel per gesprek staat niet in de docs. Aan en uit via Settings > AI Credits. Notetaker zelf is gratis. Call Assistant (transcriptie van calls) kost 50 dollar per maand plus 2 cent per minuut, maar de AI-credits-pagina noemt call-transcripten ook onder de gratis Notetaker. Die twee pagina's spreken elkaar tegen, dus kijk in Settings > Notetaker en Settings > Plan wat er bij ons aan kan.

## Onze stand op 26-09-2026

- Growth, één gedeelde seat ("Eduface CRM"), 1.500 AI-credits per maand, waarvan 12 gebruikt (Enrichment).
- Vijf outcomes, Engels en generiek: Voice Mail, Requires Follow up, Referral, Demo Booked, Not Interested.
- 75 calls via Close tussen 26-06 en 26-09. De uitkomst staat als vrije tekst in de notitie ("VM", "VM ingesproken", "Ze heeft opgehangen"), het aantal lerenden ook ("Student aantallen zitten tussen de 48 - 96 deelnemers", "Tientallen").
- Calls worden opgenomen maar niet getranscribeerd. Voorbeeld: de call van 03-09 met Louis van Dam (Intop Zorgsector), 114 seconden, wel een opname, geen transcript, geen outcome.
- Meetings lopen via Notetaker, met transcript en samenvatting. Daar werkt de AI-kant wel.
- Vier custom fields, geen enkele shared. Er is dus nog niets om aan een playbook te koppelen.
- Vandaag ingericht: lead-statussen Contacted, Qualified en Disqualified, opportunity-status Qualified, en de workflow "Qualified" die een opportunity aanmaakt.

## Voorstel

Outcome-namen in het Engels, zoals de rest van onze Close-statussen. De beschrijvingen zijn waar de AI op stuurt, dus die zijn geschreven om te plakken.

### 1. Playbook "Discovery" (calls en meetings)

Waarom eerst: meetings hebben al een transcript, dus hier werkt alles meteen. De samenvatting volgt de Discovery-gate uit `meddpicc-states-and-gates.md`, zodat de recap-mail die de gate eist, de CRM-update en de prep voor het volgende gesprek uit één samenvatting komen. Playbooks gelden voor de hele organisatie, dus ook voor de gesprekken van Jeroen.

**Outcomes** (Rackham, dezelfde taal als `/sales-coach`):

| Outcome | Beschrijving |
|---|---|
| Advance | The prospect committed to a next step that requires action on their side, such as sharing data or documents, inviting a colleague or the budget holder, or planning a scoping session, with a date. |
| Continuation | The conversation ended positively but without a commitment from the prospect: "send me some information", "let's talk again later", or a new meeting without any action on their side. |
| Nurture | There is a fit, but no priority or timing now, for example because of a budget cycle, a reorganisation or other projects first. |
| No fit | The organisation is outside our target: fewer than 300 learners per year, no written work or exams to assess, or a need we do not serve. |

**Summary guidance:**

```
Summarise this discovery conversation about an AI platform for grading and feedback, sold to a university or training provider. Write in the language of the conversation. Use exactly these headings in this order, with short bullets under each. Leave out small talk and scheduling.

1. Pain: the problem in their own words, quoted where possible. Who suffers from it and what it costs them (hours, turnaround time of grades, feedback quality, complaints).
2. Players: every person mentioned, with role and what they care about. Mark who controls the budget and who wants this internally. Write "unknown" if not mentioned.
3. Why now: deadline, budget cycle, accreditation, policy or event that makes this urgent. Write "none mentioned" if absent.
4. Desired outcome: what success looks like for them, with numbers if they gave any.
5. Fit: number of learners per year, how they assess (written assignments, exams, oral), which LMS.
6. Next step: what was agreed, who does what, and the date. State explicitly whether the prospect committed to an action themselves.
7. Gaps: what under 1 to 6 is still unknown or vague, written as questions for the next conversation.

Never fill in anything that was not said. If something is unclear, say it is unclear.
```

**Note template** (voor wat de AI niet hoort):

```
Wat er volgens mij echt speelt:
Wie beslist volgens mij, en waarom:
Grootste risico:
```

### 2. Playbook "Cold call" (calls)

Waarom: de uitkomst staat nu in een notitie, en die kun je niet tellen. Met outcomes zie je per week hoeveel gesprekken je voerde en hoeveel een afspraak werden. Wordt A5 de leidende maat, dan telt Meeting booked het belkanaal vanzelf mee. Mail en LinkedIn niet, want outcomes bestaan alleen op calls en meetings.

Vijf van de zes bestaan al onder een andere naam. Hernoemen in plaats van nieuw maken: Demo Booked wordt Meeting booked, Requires Follow up wordt Callback, Referral wordt Referred, Voice Mail wordt Voicemail. Not Interested blijft. No fit is dezelfde als bij Discovery.

| Outcome | Beschrijving |
|---|---|
| Meeting booked | The prospect agreed to a follow-up meeting (video call or visit), with a date or a concrete agreement to schedule one. A callback without a meeting is not this outcome. |
| Callback | No meeting booked, but the prospect asked us to call back later or agreed a moment to talk again. |
| Referred | The prospect pointed us to someone else in the organisation who owns this topic, by name or role. |
| Not interested | The prospect declined: no need, no time or no interest. Also when they hung up after hearing why we called. |
| No fit | Zelfde outcome als bij Discovery. |
| Voicemail | We reached voicemail, whether or not a message was left. |

**Note template** (werkt ook zonder transcriptie):

```
Wat ze letterlijk zei:
Volgende stap en datum:
Wat ik de volgende keer anders doe:
```

De laatste regel is wat Dante nu al uit zichzelf opschrijft ("het probleem met dit beldje was dat ik hem niet liet praten").

**Summary guidance** (werkt pas als calls getranscribeerd worden, zie W6):

```
Summarise this cold call in at most five bullets, in the language of the call: 1) who we spoke with and their role, 2) how they assess learners now (written assignments, exams, oral) and how many learners, if mentioned, 3) their reaction or objection, quoted literally, 4) the agreed next step with date, 5) other people they mentioned, with role. Leave out small talk. Never fill in anything that was not said; write "not mentioned" instead.
```

### 3. Twee shared fields, gekoppeld aan beide playbooks

| Veld | Type | Beschrijving |
|---|---|---|
| Lerenden per jaar | Getal | Totaal aantal lerenden per jaar over de hele organisatie. Alleen invullen als er een getal genoemd is. Bij een bandbreedte de ondergrens. |
| Toetsvorm | Keuze, meerdere | Schriftelijke opdrachten, Tentamens, Mondeling. Alleen wat genoemd is. |

Waarom Lerenden per jaar: volgens `GTM/Pricing/prijsmodel-psu-26-27.md` is dat het belangrijkste veld van de pijplijn (prijs, drempel en segment in één), en het was op 16-09-2026 gevuld bij 84 van de 776 organisaties. Dante vraagt het al in zijn calls, nu landt het in een veld in plaats van in een notitie.

Waarom Toetsvorm: dat is de fitvraag die Dante na de call met Louis van Dam zelf noemde ("had ik moeten vragen: bestaat het uit schriftelijke opdrachten"). De drie keuzes volgen de modules: Paper Grader, Exam Grader, Oral Examination.

De ondergrens bij een bandbreedte is een keuze van mij, naar "default to the lower state" uit de MEDDPICC-referentie. Nog niet door Dante bevestigd.

### 4. Smart Views, na twee weken data

- Terugbellen: laatste call met outcome Callback.
- Voicemail: laatste call met outcome Voicemail.
- Continuation: laatst afgeronde meeting met outcome Continuation. Deals die een echte vervolgstap nodig hebben.
- Onder de drempel: Lerenden per jaar kleiner dan 300.

### 5. Later: workflows op outcomes

Pas als de outcomes twee weken goed gezet worden. Elke koppeling eerst op één lead testen.
- No fit zet de lead op Disqualified.
- Nurture zet de lead op Nurturing.
- Outcome X zet de lead op Qualified, waarna de bestaande workflow "Qualified" de opportunity aanmaakt. Welke outcome X is, is open (W7).

Twee dingen die de docs niet zeggen en die de test moet uitwijzen: of een Call-trigger op outcome kan filteren, en of een statuswijziging door de ene workflow de workflow "Qualified" start.

## Wat we bewust niet doen

- Chloe voice agents: AI die zelf belt past niet bij persoonlijke outreach, en kost credits plus beltarief.
- Voicemail drop: onze voicemails zijn persoonlijk, een standaardbericht past daar niet bij.
- Playbooks voor Scoping, EB meeting en POV: weinig volume. Eerst bewijzen op Discovery en Cold call.
- Workflow Goals: onze sequenties draaien in Lemlist, niet in Close.

## Open

In `Context/open-vragen.md`:
- **W6** Call-transcriptie aanzetten?
- **W7** Welke outcome zet een lead op Qualified?

## Inrichten, in deze volgorde

1. Settings > Custom Fields: de twee shared fields aanmaken.
2. Settings > Playbooks and Outcomes: de vier bestaande outcomes hernoemen, No fit, Advance, Continuation en Nurture toevoegen, met de beschrijvingen hierboven.
3. De twee playbooks aanmaken en outcomes, velden, note template en summary guidance koppelen.
4. Settings > AI Credits: Auto Updates aan. Na een week het verbruik bekijken.
5. Na twee weken: de Smart Views, en daarna pas de workflows.

Via de Close-koppeling van Claude kunnen playbooks, outcomes en velden niet aangemaakt worden. Dit gaat met de hand.
