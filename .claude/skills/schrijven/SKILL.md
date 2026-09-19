---
name: schrijven
description: Schrijft en reviseert alles wat naar buiten gaat — mails, offertes, website copy, presentaties, cold outreach, voorstellen — in de juiste stem per content-type, en reviewt bestaande tekst op overtuigingskracht. Kernregel, geen vage, overbodige of AI-klinkende taal. Verwerkt Dante's feedback SCOPED per type, zodat feedback op een mail nooit de marketingstem verandert. Trigger wanneer je klant-gerichte content schrijft of herschrijft, wanneer Dante feedback geeft op een tekst ("te vaag", "te lang", "klinkt als AI", "overbodig", "verwerk deze feedback"), en bij "kan dit korter", "is dit overtuigend genoeg", "check deze tekst", "maak dit sterker".
---

# Schrijven

De schrijfskill voor alles wat naar buiten gaat: stem-discipline plus overtuigingstechniek.
Opgenomen uit de vroegere skills `schrijven` en `schrijven`.

De stem-discipline. Bestaat omdat mijn content vaak te **vaag en overbodig** is en soms **als AI klinkt**. Deze skill traint dat eruit, en houdt de stem per content-type apart.

## Eerste stap, elke keer

1. **Bepaal het type** (dit bepaalt alles): formele mail · presentatie/slides · marketingtekst · cold outreach · opvolgmail · LinkedIn connectieverzoek. Twijfel je, vraag het in één zin.
2. **Lees de hele stem-sectie voor dat type** in `voice-by-type.md` + de recente feedback voor dat type in `feedback-log.md`. Niet alleen de nieuwste feedback uit het huidige gesprek: bestaande regels (bv. de social-proof-formulering) gaan net zo makkelijk mis als je ze niet herleest.
2b. **Check op een diep onderzoeksdossier voor deze persoon/organisatie** (`pipeline.py dossier <id>` voor de NL-pijplijn, `GTM/Campaigns/cold-calling/` voor de belllijn, of `person-research`-output) voor je een lichter CSV-veld (haakje, insteek) als beste bron aanneemt. Een snelle "insteek" uit een eerdere, snellere pass kan achterhaald of zwakker zijn dan een dieper dossier dat later is gemaakt.
3. Schrijf. Dan de anti-vaagheid-check hieronder langs voor je het oplevert.

## De kernregel: niet vaag, niet overbodig, niet AI

Voor je iets oplevert, schrap alles wat hieronder valt:
- **AI-tells** (dodelijk). Weg met: "wat me het meest bijbleef", "dat raakte me", "eerlijk gezegd", "het is belangrijk om te benadrukken", "in een wereld waar", "stel je voor", "niet alleen X, maar ook Y" als opvulsel. Dante herkent dit meteen en haakt af.
- **Vaag.** Zeg het concrete ding. Geen "diverse mogelijkheden", "een aantal zaken", "op verschillende vlakken". Noem wat je bedoelt.
- **Lege verbindingszinnen.** Weg met bruggen die niks zeggen: "dat sluit precies aan op waar wij mee bezig zijn", "dat is precies waar wij in geloven", "daar komen wij om de hoek kijken". Zeg meteen het concrete ding. Niet "dat sluit aan op ons werk", wel "wij bouwen X dat Y doet". Elke zin draagt een feit of een punt, geen opvulling.
- **Overbodig.** Elke zin moet iets toevoegen. Herhaalt een zin de vorige of de kop, schrap 'm.
- **De lezer-test (doe dit per zin).** Lees elke zin en vraag: wat denkt de lezer hierbij? Is het antwoord "duh, natuurlijk" of "waarom zegt die dit", dan eruit. Voorbeeld: "ik wilde je alvast even bereiken" -> de lezer denkt "je mailt me, tuurlijk wil je me bereiken". Schrappen. Zeg alleen wat de lezer nog niet dacht.
- **Leesbare zinnen, geen tel-tikkende opsomming.** Weinig dubbele punten, niet drie korte zinnen achter elkaar. Schrijf "ik zag dat je bij Aeres bezig was met X" in plaats van "ik zag wat je doet: X. En Y." Laat het lopen zoals je praat.
- **Opgeblazen woorden** (publieke content): gewone spreektaal. Zie `outreach-plain-language`. Geen "genuinely / slipping / chasing / faciliteren / caleidoscopisch".
- **Ritme.** Niet alles kort en hakkelig (staccato), niet alles lange bijzin-treinen. Normale, gevarieerde zinnen zoals een mens praat. Dit was een concrete Dante-correctie.
- **Geen em-dashes.** Komma, punt, of herstructureer (huisstijl-regel).
- **Beschrijf nooit dat je iemand hebt onderzocht of opgezocht.** "ik ben me even in je gaan verdiepen", "ik heb je opgezocht", "ik dook in je achtergrond" klinkt creepy. Zeg gewoon wat je zag of las: "ik las dat je scriptie ging over ...", "ik zag je rede over ...". (Je in de instélling verdiepen mag wel, "ik ben me in Avans gaan verdiepen"; in een persoon niet.)
- **Elke claim en elk verband moet bewijsbaar zijn.** Bij het opleveren van een gepersonaliseerde mail lever je niet alleen de tekst, maar ook waar elk feit vandaan komt en, als je zelf een verband legt tussen twee dingen (bv. "modulair werken dus meer beoordelingen"), waaróm je dat verband trekt. Dante moet elke claim kunnen verifiëren als hij ernaar vraagt. Geen bron of geen uitgelegde redenering = niet opleveren zonder dat expliciet te flaggen.
- **Altijd een korte redenering meeleveren bij elk stuk content, welk type dan ook.** Niet alleen bij mails: dit geldt voor LinkedIn, cold outreach, en ook toekomstige types die nog niet in deze skill staan (bv. offerte-copy). Bij elke oplevering: een korte toelichting waarom een zin/keuze/getal erin staat en waar het vandaan komt. Dit hoeft geen lange tabel te zijn zoals bij een grote batch, maar minimaal 1-2 zinnen per niet-vanzelfsprekende keuze. Geen aparte instructie nodig om dit te triggeren, dit is standaard bij opleveren.

Toon met Dante intern: casual, recht voor z'n raap. Publiek: nog casualer en menselijker. Zie `.claude/rules/communication-style.md`.

## Voor mails: insteek eerst

Schrijf een mail nooit meteen uit. Dat kost de meeste tijd als de hoek daarna nog schuift.
1. Na de research kom je terug met **2-4 mogelijke insteken**, kort omschreven, niet uitgeschreven.
2. **Dante kiest** de insteek (en lengte/toon).
3. Pas dan schrijf je 'm, één keer, met de structuur al vast. Max 1-2 tweaks.

Verplaats de iteratie van "hele mails herschrijven" naar "een hoek aanvinken".

## Elke interactie is anders

De stem verschilt per type. Verwar ze niet. Details staan in `voice-by-type.md`, kort:
- **Formele mail** (prospect, academicus, beslisser): menselijk maar professioneel, eerlijk, kort, één duidelijke CTA. Hou het beknopt, een drukke lezer haakt af bij een lap tekst.
- **Presentatie/slides**: punchy, één idee per slide, weinig woorden. Bouw via `marketing-creatives`.
- **Marketingtekst**: casual, menselijk, plain, een hook. Verkoopt een gevoel, geen feature-dump.
- **Cold outreach**: verankerd aan het `cro`-handboek (Discovery-logica, pijn + proof + why-now).

Voor LinkedIn-posts bestaat een aparte skill (`linkedin-content`) met stem-profielen per persoon. Gebruik die daar; deze skill is voor de rest.

## Feedback verwerken (SCOPED, dit is de crux)

**Eerst: pak het principe, niet de zin.** Dante's grootste frustratie is dat ik de exacte zin die hij aanwijst fix en de rest laat staan. Als hij één zin afkeurt, is dat een voorbeeld van een regel. Haal die regel eruit en pas 'm toe op de **hele tekst** en op alles wat er in de toekomst op lijkt. Voorbeeld: hij keurt "dat sluit precies aan" af -> het principe is "geen lege verbindingszinnen", dus ook "precies de kant die jij onderzocht" moet weg. Na het verwerken: lees de hele tekst opnieuw langs het nieuwe principe, niet alleen de gemarkeerde plek.

Als Dante feedback geeft op een tekst:
1. Bepaal op welk **type** de feedback slaat.
2. **Formuleer het onderliggende principe** (niet de instantie), en pas het toe op de hele tekst.
3. Log 'm in `feedback-log.md` onder dat type (datum + de regel + waarom).
4. Werk de stem voor **dat type** bij in `voice-by-type.md`.
5. **Raak de andere types niet aan.** Feedback op een formele mail mag de marketingstem niet veranderen. Een correctie op één plek is geen universele wet (maar binnen dat type wél overal toepassen).

Uitzondering: alleen als Dante expliciet zegt dat iets voor álle content geldt, zet je het in de kernregel hierboven in plaats van onder één type.

## Overtuigingstechniek: de vier pijlers

Uit een Nederlands boek over overtuigend schrijven bij aanbestedingen. Generiek genoeg voor
offertes, outreach, website copy, LinkedIn en voorstellen. Lees
`references/schrijfprincipes.md` voor de volledige uitwerking per pijler voordat je
een langere tekst schrijft of reviewt.

1. **Structuur** — kernboodschap eerst, niet pas in de conclusie. Tussenkopjes als reddingsboei. Korte alinea's, max 5-6 regels, met witregels ertussen.
2. **Schrijfstijl** — MANDI: kan het korter? Korte zinnen, gemiddeld 10-15 woorden, gemengd met een enkele lange. Actief, nooit lijdend.
3. **Neuro-woorden** — gedoseerd woorden rond vertrouwen, resultaat, gemak, autoriteit. Eén tot drie per sectie, niet meer, anders klinkt het als een reclamefolder.
4. **Vormgeving** — overzicht, positieve emotie, herkenbare huisstijl.

Deze pijlers zijn **aanvullend** op de kernregel hierboven en op
`.claude/rules/communication-style.md`. Bij conflict wint de communicatiestijl-regel.

### Een bestaande tekst reviewen

1. Loop de vier pijlers langs als checklist.
2. Geef per pijler concrete feedback, en schrijf de betere versie er meteen bij. Niet "dit kan beter".
3. Wijs wollige woorden en passieve zinnen specifiek aan.
4. Sluit af met een verdict: klaar, of de 2-3 dingen die het meeste verschil maken.

## Done

- Type bepaald, juiste stem + feedback-log gelezen.
- Anti-vaagheid-check gedaan: geen AI-tells, niks vaags of overbodigs, gevarieerd ritme, geen em-dashes.
- Bij een langere tekst: de vier pijlers langsgelopen.
- Nieuwe feedback correct gelogd onder het juiste type, zonder de andere types te vervuilen.
