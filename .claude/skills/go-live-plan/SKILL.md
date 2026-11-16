---
name: go-live-plan
description: Maakt en onderhoudt het go-live plan voor een deal, het gedeelde document met de klant (Word en Google Doc) in de vaste Eduface-opmaak van het UTI-plan. Haalt de stand uit Close (mails, notes, taken en ALLE meeting-transcripten), zet die in een JSON per account en bouwt daaruit de .docx met een script, zodat de opmaak nooit afwijkt. Eerst PNG ter controle, dan de definitieve Word, daarna desgewenst de mail met de link. Trigger wanneer Dante zegt "maak een go live plan voor [account]", "update het go live plan", "verwerk dit gesprek in het go live doc", "zet de nieuwe stand in het go-live plan", "go-live document", of een transcript plakt met de vraag het plan bij te werken.
---

# Go-live plan

Het go-live plan is het gedeelde plan met de klant om samen live te gaan. Het gaat naar buiten, dus het is Engels, klopt tot op de datum, en staat er niets in dat intern is.

**Het voorbeeld is het UTI-plan:** `GTM/Accounts/uti/go-live-plan.json` (de bron) en `GTM/Accounts/uti/UTI_Go_Live_Plan.docx` (het resultaat). Twijfel je over vorm of toon, kijk daar.

## Bestanden

| Wat | Waar |
|---|---|
| Bouwscript | `scripts/build.py` |
| Sjabloon (opmaak, kleuren, tabellen) | `template/go-live-plan-template.docx` |
| JSON-schema, statussen, schrijfregels per sectie | `reference.md` |
| Per account: bron | `GTM/Accounts/<account>/go-live-plan.json` |
| Per account: resultaat en logo | `GTM/Accounts/<account>/<Klant>_Go_Live_Plan.docx`, logo als png in dezelfde map |
| Oud HTML-template (vervangen 16-11-2026) | `archief/template-html-2026-09/` |

## Werkwijze

1. **Haal de volledige stand uit Close.** Lead, opportunities, contacten, open taken, notes, alle mailthreads, en van **elke** meeting het transcript (`fetch_meeting_transcript`). Ook de oudere calls, niet alleen een samenvatting erover. Heeft een meeting geen transcript, zeg dat dan. Plakt Dante zelf een transcript, verwerk dat.
2. **Lees de vaste bronnen.** Prijs uit `GTM/Pricing/prijsmodel-psu-26-27.md`, elke productclaim uit `Platform/product.md`. Staat een claim daar niet, dan gaat hij het plan niet in.
3. **Schrijf of werk de JSON bij.** Bestaat er al een, pas dan alleen aan wat veranderd is en zet `last_updated` op vandaag. Volg de regels in `reference.md`.
4. **Bouw en lever eerst PNG's.**
   `python3 .claude/skills/go-live-plan/scripts/build.py GTM/Accounts/<account>/go-live-plan.json GTM/Accounts/<account>/<Klant>_Go_Live_Plan.docx --png <scratchpad>/<account>-png`
   Bekijk de PNG's zelf (geen gebroken rijen, geen verkeerde kleur) en stuur ze naar Dante. Zeg in één regel per punt wat je hebt aangenomen.
5. **Na akkoord: de Word.** Stuur de .docx, commit JSON plus .docx.
6. **Mail aan de klant, alleen als Dante erom vraagt.** Kort, Engels, met de link naar het Google Doc `<Klant> Go Live Plan` in de accountmap in Drive (zoek het op met de Drive-tool). De drie belangrijkste wijzigingen als bullets. Check of de nieuwste versie in dat Doc staat voordat de mail weggaat.

## Regels die vastliggen (uit Dante's feedback op het UTI-plan, nov 2026)

- **Owners voluit**, alle verantwoordelijken: "Jeroen van Gessel, Dante Torbed and Charlie Rosenbam". Geen initialen in de stappen.
- **Initialen alleen bij het Eduface-team** in "Who is involved". De klant krijgt geen initialen.
- **Alleen mensen van de klant zelf** in de klantlijst. Iemand van een zusterorganisatie of moederbedrijf hoort er niet in.
- **Stappen kort en zonder voorwaarden.** "Set up the LTI 1.3 connection in Blackboard Ultra", niet "..., after the Legal green light". Een afhankelijkheid zet je in de When-kolom ("To confirm"), niet in de actie.
- **Alleen echte stappen.** Geen stap die alleen een andere stap voorbereidt ("Planning for the days on campus") of die al door een andere stap gedekt is.
- **Geen vetgedrukte acties.**
- **"To confirm" is een prima When** als er nog geen datum is. Nooit een datum verzinnen.
- **Interne zaken blijven eruit:** verzekeringen, reiskosten, recht waaronder getekend wordt, dealwaarde, interne risico's, wie intern wat moet doen.
- **Q&A alleen met vragen die de klant echt stelde én een bevestigd antwoord.** Geen "To follow", geen vragen die je zelf bedenkt.
- **Implementatieplan:** komt net voor go-live. In "Where everything lives" blijft hij leeg tot hij er is.
- **Geen tegenstrijdige datums** tussen de stappen, de tabel met campusdagen en Information. Eén datumformaat: "6 Oct 2026".
- **Gebruik de term van de klant** voor de proefperiode (UTI zegt "pilot").

Komt er nieuwe feedback die een regel raakt: de trap uit `.claude/rules/feedback.md`, en de nieuwe regel komt hier, niet ernaast.

## Klaar als

- De PNG's zijn door Dante gezien en de .docx is gevalideerd (het script is zonder fouten gelopen).
- JSON en .docx staan gecommit in de accountmap.
- In je antwoord staat wat er veranderd is en wat je hebt aangenomen, elk in één regel.
