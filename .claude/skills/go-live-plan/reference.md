# Go-live plan: JSON-schema en schrijfregels

Het script `scripts/build.py` leest één JSON per account en bouwt daaruit de .docx op het sjabloon. Alle opmaak (kleuren, zebrastrepen, statuskleuren, kolombreedtes, rijen die niet over twee pagina's breken) doet het script. Jij levert alleen de inhoud.

## Schema

```json
{
  "client": "Universal Technical Institute",
  "last_updated": "12 November 2026",
  "author": "Dante Torbed",
  "client_logo": "uti-logo.png",
  "info": [["Company", "..."], ["Contracting party (Eduface)", "..."], ["Target contractual signing date", "..."], ["Target go-live date", "..."], ["Price per student per month", "..."]],
  "summary": ["alinea 1", "alinea 2", "alinea 3"],
  "eduface_team": [["Dante Torbed (DT)", "dante.torbed@eduface.me", "Customer Success Manager"]],
  "client_team": [["Robert Jordan", "rjordan@uti.edu", "Associate VP, Instructional Design"]],
  "steps": [["Action", "Owner(s) voluit", "When", "Status"]],
  "campus": {"title": "Three days on campus, Bloomfield NJ", "days": [["Day 1", "18 Jan 2027 (tentative)", "What happens", "To plan together"]]},
  "resources": [["Shared folder", "Shared", "Everything below sits in here.", "https://drive.google.com/..."], ["NDA", "Done", "Signed by both parties."]],
  "qa": [["Question", "Asked by", "Answer"]]
}
```

- `client_logo`: pad relatief aan de JSON. Schoollogo's staan in `Design/Merk/logo-van-scholen/`. Geen logo, dan staat er een grijze placeholder "Client logo".
- `campus`: `null` als er geen bezoek op locatie is; de hele tabel valt dan weg.
- `resources`: een vierde veld met een URL maakt de naam een link. Gebruik dat alleen voor de gedeelde map.
- Lege cel: `""`.

## Statussen en kleuren

| Status | Kleur | Wanneer |
|---|---|---|
| Done | groen | afgerond, met de datum waarop |
| In progress | oranje | loopt nu |
| Waiting on ... | oranje | geblokkeerd door een benoemde stap ("Waiting on NDA") |
| Proposed | geel | gepland, nog niet begonnen |
| To confirm | geel | gepland, datum of invulling nog niet bevestigd |
| Shared / To share | lichtgroen / geel | alleen bij "Where everything lives" |
| To plan together | donkergeel | alleen bij de campusdagen |

Een andere status kan, maar krijgt geen kleur. In "Where everything lives" mag de status leeg zijn.

## Per sectie

**Information.** Vaste vijf regels. De contractpartij is altijd "Blockbook B.V., doing business as Eduface, Utrecht, the Netherlands". De prijs komt uit `GTM/Pricing/`, in de valuta van de markt. Go-live: de datum plus scope (vak, aantal studenten, aantal docenten). Geen datum bekend: "January 2027, date to be set".

**Brief summary.** Drie alinea's. 1: het probleem van de klant in hun cijfers en woorden, uit de transcripten. 2: wat Eduface doet en het doel voor deze klant, alleen claims uit `Platform/product.md`. 3: het gezamenlijke doel met maand en jaar, en dat dit het gedeelde plan is dat beide teams bijhouden.

**Who is involved.** Eduface: Dante, Jeroen, Menno, Samuel met initialen, mail en rol. Klant: naam, mail, rol zoals ze die zelf voeren (uit de mailhandtekening of het transcript). Weet je de rol of mail niet, laat de cel leeg. Niet gokken.

**Planned steps.** Op volgorde van de tijd: afgeronde stappen bovenaan met hun echte datum, daarna wat loopt, daarna de planning tot en met go-live en onboarding. Typische blokken:
- kennismaking, materiaal van de klant, demo, prijs
- security en legal: VPAT, vragenlijst, NDA, review door de klant
- business case: cijfers van de klant, dan de case
- contract: concept licentieovereenkomst plus DPA, review, akkoord op hoofdlijnen, ondertekening
- techniek: testcursus, LTI-koppeling
- inrichting eerste cursus: setupcall, twee rondes fine-tuning, eindtest, cursus klaar
- training: dagen op locatie, super-instructor, opname
- implementatieplan net voor go-live, go-live, onboarding

**Days on campus.** Per dag één alinea wat er gebeurt. Datums "(tentative)" tot ze vastliggen.

**Where everything lives.** Gedeelde map met link bovenaan, daarna per document status en een detailzin. Wat er nog niet is: status leeg of "To share".

**Questions and answers.** Vraag zoals de klant hem stelde, wie hem stelde (voornaam of team), het antwoord in twee zinnen.

## Valkuilen die al eens misgingen

- Een datum in de stappen die botst met de tabel met campusdagen.
- Een stap op Done zonder datum, of met een vraagteken als datum.
- Een claim over het product die niet in `Platform/product.md` staat (bij UTI: "rubrics sync in from Blackboard").
- Een interne blokkade die in het klantdocument belandt (bij UTI: de cyberverzekering).
- Werken vanuit één samenvatting in plaats van de transcripten zelf.

## Het sjabloon aanpassen

Het sjabloon is het UTI-plan met een placeholder als klantlogo. Het script haalt zijn prototyperijen uit het sjabloon: de eerste stappenrij, de groepsrijen bij "Who is involved", en bij "Where everything lives" een rij met link, een met gekleurde status en een met lege status. Pas je het sjabloon aan, laat die rijen dan bestaan en bouw daarna het UTI-plan opnieuw als test: de tekst moet gelijk blijven.
