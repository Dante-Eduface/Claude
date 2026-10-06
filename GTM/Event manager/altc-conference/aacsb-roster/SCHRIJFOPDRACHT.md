# Schrijfopdracht agent 4: AACSB-roster (UK en NL)

_2026-10-06. Voor de agent die per batch de Lemlist-velden schrijft. Alles hieronder is door Dante in de proef goedgekeurd of gecorrigeerd._

## Lees eerst
1. `.claude/skills/outreach/SKILL.md`: de campagnekop (Lemlist-flow, velden), de brontoets en de dragertoets.
2. `.claude/skills/outreach/LEERPUNTEN.md`.
3. **De lat:** `GTM/Event manager/altc-conference/aacsb-proef/lemlist-velden.md`. Dit zijn tien goedgekeurde voorbeelden in exact het format dat je oplevert. O'Mahony, Finn, Mercado en Barac hebben een sterk haakje. Daly is het voorbeeld zonder haakje. Bolat is het voorbeeld van een criticus.

## Het event
- Titel: **The Business Outcomes of AI Marking and Feedback**. Donderdag 15 oktober 2026, 11:00 tot 12:00 UK-tijd, op Teams (12:00 NL).
- Link: `[link]` als placeholder. Die vul ik zelf in bij de export.
- **Noem Jisc en ALT nooit.** Dat ze meedoen is niet zeker. Sociaal bewijs mag alleen zijn "with several universities joining".

## De flow in Lemlist, en wat dat betekent
Eerst het verzoek. Na 4 dagen splitst de flow:
- **Geaccepteerd:** `linkedInMessage`, daarna een belttaak.
- **Niet geaccepteerd:** `firstEmail`, daarna een belttaak.

Niemand krijgt dus zowel het LinkedIn-bericht als de mail. De mail staat op zichzelf en opent met "I sent you a LinkedIn request a few days ago, so here it is by email as well." Er is één `Call_script` voor beide takken, dus neutraal openen: "I reached out earlier about...".

## Per persoon lever je
`linkedInConnectionRequest` (max 300 tekens, tel ze), `linkedInMessage`, `firstEmailSubject`, `firstEmail`, `Call_script` (opening met een echte vraag, dan uitnodiging, bij ja, voicemail) en **2a** (antwoord op een ja, dat Dante zelf stuurt).

**2a heeft altijd vorm B:**
> Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
> [link]
> I'd genuinely love to hear your take on [hun eigen onderwerp] afterwards.

## Regels die Dante in de proef heeft gezet
- **Elke stap draagt een ander feit uit het dossier.** Verzoek: het sterkste haakje plus jouw reactie. LinkedIn-bericht: een tweede, andere observatie. Mail: een derde. Belscript: een echte vraag over hun werk. Dezelfde reden in andere woorden telt niet ("which is why you came to mind" na een verzoek dat al zei waarom: afgekeurd).
- **Origineel en authentiek.** Reageer op het feit (wat is er verrassend aan?) in plaats van het op te sommen.
- **Is iemand kritisch op AI, gebruik dat juist.** Zeg dat je hun sceptische blik waardevol vindt (Bolat).
- **Zonder haakje (ROL-ALLEEN): draai de volgorde om.** Eerst de sessie, dan de rol, zacht ("I thought it might be up your street"). Daarna komt in elke stap toch een ander element: wat de sessie behandelt, de ruimte om een collega aan te dragen, een vraag over hun rol.
- Geen dubbele punten en geen em-dashes in de berichttekst. Britse spelling. Sign-off: "Best,\nDante Torbed\nEduface". Geen functietitel.
- Brontoets en dragertoets zoals in de skill. Claim nooit meer lezing dan het dossier toont: alleen een titel gezien betekent "came across", niet "read". Geen "recent" of "just" zonder datum binnen 6 maanden.
- **Nederlandstalig** (zie het dossier): alles in het Nederlands, "je", en vermeld dat de sessie in het Engels is (zie Kleijnen).
- **Close-contact of een lopende deal in het dossier:** schrijf het wel, maar zet bovenaan **LET OP** met de reden. Bij VU Amsterdam altijd LET OP (lopend spoor).
- **Vertrokken naar een niet-onderwijsorganisatie, of de persoon is niet te vinden:** niets schrijven, één regel "AFGEVALLEN: reden".

## Oplevering
Schrijf naar `GTM/Event manager/altc-conference/aacsb-roster/berichten/batch-XX.md`, met per persoon exact de opbouw uit de proef:

```
## <id> <naam>, <functie>, <organisatie>
LinkedIn: ... · e-mail: ... · telefoon: ...
Haakje per stap: verzoek = ...; bericht = ...; mail = ...; bellen = ... (elk met bron)

**linkedInConnectionRequest** (<tekens>)
...
**linkedInMessage**
...
**firstEmailSubject**
...
**firstEmail**
...
**Call_script**
Opening: "..."
Uitnodiging: "..."
Bij ja: "..."
Voicemail: "..."
**2a. Bij ja (zelf sturen)**
...
**Twijfels:** ...
```

Geen mailadres: `firstEmailSubject / firstEmail: geen adres.` Geen nummer: schrijf het belscript wel, met "(via de centrale)".

Eindrapport aan de hoofdagent: max ~150 woorden. Aantal geschreven, aantal afgevallen met reden, en de echte twijfels.
