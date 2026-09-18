# Eduface Design System

Eén merk, drie oppervlakken. Ze delen de kern en verschillen in alles daarboven.

## Laad alleen wat je nodig hebt

**Dit is de belangrijkste regel van dit systeem.** Lees nooit de hele map. Kies je oppervlak en lees alleen die map plus `core/`. Bouw je een interne tool, dan hoort de marketingsite niet in je context.

| Wat bouw je | Lees | Lees NIET |
|---|---|---|
| Marketingsite, landingspagina, blog | `core/` + `web/` | slides, internal |
| Deck, pitch, webinar-slides | `core/` + `slides/` | web, internal |
| Eigen app, tool, agent-UI, dashboard | `core/` + `internal/` | web, slides |
| Iets anders: document, rapport, offerte, one-pager, mailtemplate, formulier | `core/` + afleiden, zie hieronder | het dichtstbijzijnde oppervlak klakkeloos overnemen |

Begin je aan een eigen app of tool, start dan bij **`internal/starten.md`**. Daar staat de hele opzet: project, fonts, tokens, shadcn, en de controle achteraf.

Gaat iets naar **Framer**, en alleen dan, lees `web/framer.md` erbij. React met Tailwind is de standaard manier van bouwen, Framer is de uitzondering.

`core/` is klein en verandert bijna nooit: kleuren, fonts, radius, schaduw. Dat is het merk.
De rest is per oppervlak: type-schaal, dichtheid, componenten.

## Staat jouw geval niet in de tabel

Dan pak je **niet** het oppervlak dat er het meest op lijkt. Dat is precies het faalpad waarvoor dit systeem gesplitst is: een verkoopdocument dat `web/` leent wordt een landingspagina met een hero en een CTA, terwijl het een stuk is dat een klant opslaat en later terugleest.

Leid de regels af uit wat het ding is. Vijf vragen, in deze volgorde.

**1. Op welke afstand wordt het gelezen?** Dit bepaalt alleen de type-schaal, verder niets. Geprojecteerd op vijf meter is `slides/`. Op een scherm of op papier op armlengte is de bodyschaal van `web/`, dus niet de heroschaal die daarbij hoort.

**2. Wordt het gescand, gelezen of bediend?** Gescand betekent scherpe hiërarchie en weinig woorden. Gelezen betekent regellengte 45 tot 90 tekens, ruime regelafstand, echte alinea's. Bediend betekent dichtheid, toestanden, hover en lege staten. Alleen bij dat laatste heb je iets uit `internal/` nodig.

**3. Scherm of papier?** Papier kent geen dark mode, geen hover en geen scroll, paginaovergangen zijn een ontwerpelement, en kleur mag nooit de enige drager zijn want het wordt zwart-wit uitgeprint.

**4. Binnen of buiten, en moet het overtuigen?** Intern is beschrijvend, geen overtuigingswerk. Een extern document mag overtuigen maar niet schreeuwen: geen marketing-CTA's, geen logobalken, geen hero. Het bewijs doet het overtuigen.

**5. Hoe lang leeft het?** Wordt het één keer in een overleg doorgenomen, of belandt het in een map en leest iemand het over een half jaar terug die er niet bij was? Bij het tweede moet het zelfdragend zijn: bronnen op de pagina zelf, geen "zoals besproken", data voluit.

**Daarna geldt:** `core/` is altijd volledig van toepassing, dus kleur, fonts, radius, schaduw, contrast, ruimte, compositie en `informatie.md`. Uit het dichtstbijzijnde oppervlak leen je alleen de type-schaal, en je schrijft erbij welke je geleend hebt. Verder neem je daar niets uit over zonder reden.

En de gouden regel blijft: verzin nooit een losse waarde.

**Voorbeeld van de afleiding.** Een go-live-document voor een klant: gelezen op armlengte, gelezen en niet gescand, extern maar geen marketing, en het wordt opgeborgen en later teruggelezen. Uitkomst: bodyschaal van `web/` zonder de heroformaten, `core/` volledig, geen CTA-taal en geen hero, bronnen op de pagina, en het moet zwart-wit uitgeprint overeind blijven. Niets uit `internal/`, want niemand bedient het.

**Komt hetzelfde soort ding een tweede keer terug, dan wordt het een eigen oppervlak.** Organisch bouwen, niet vooruit verzinnen. Eén keer is afleiden, twee keer is een map.

## Hoe je werkt, ongeacht het oppervlak

**`core/proces.md` lees je altijd eerst.** Daarin staan de drie poorten: nooit in één klap een af resultaat opleveren, maar eerst de richting met twee opties, dan één onderdeel als proef, dan pas de uitrol.

Daarnaast:
- `core/regels.md` — de vaste visuele regels (contrast, type, ruimte, kleur, radius).
- `core/compositie.md` — wat zet je waar en waarom, plus de reflexen-lijst die sjabloonwerk afvangt.
- `core/informatie.md` — welke informatie er op het scherm hoort en waarom. De laag boven de vormgeving: kernbegrip één keer definiëren, één feit één weergave, labels alleen bij afwijking, wrijving die meeschaalt met de schade. Hier zitten de meeste ontwerpfouten, niet in de typografie.
- `core/voorbeelden.html` — dezelfde regels als zichtbaar voorbeeld, fout naast goed. Openen in de browser.

## Waarom gesplitst

Dezelfde kop van 72px die op een homepage goed werkt, is onleesbaar dicht op een slide en absurd in een tabelweergave. Een type-schaal is een keuze over kijkafstand, niet over merk. Merk = kleur en font, en dat is gedeeld.

Tweede reden: context. Alles in één bestand betekent dat elke designtaak de hele website meesleept.

## De gouden regel (geldt overal)

Verzin nooit een losse waarde. Geen `#1f9d57`, geen `padding: 47px`, geen willekeurige radius. Pak een token. Heb je een waarde nodig die er niet is, voeg eerst het token toe en gebruik het daarna. Een afwijking is een bug, geen uitzondering.

## Structuur

```
core/       proces.md      de drie poorten (lees dit eerst)
            tokens.css     kleur, font, radius, schaduw, status   <- gedeeld
            regels.md      de vaste visuele regels (microcraft)
            compositie.md  wat zet je waar, en waarom (bewijsvoering)
            voorbeelden.html   fout naast goed, in de browser
web/        tokens.css     display-schaal + sectieritme
            components.md  knoppen, cards, secties, nav (spec, geen Framer-code)
            regels.md      creatieve ruimte voor hero's en productbeelden (lees dit ook)
            framer.md      bouwbeperkingen van Framer
slides/     tokens.css   1920x1080 canvas + projectie-schaal
            layouts.md   de vaste slidesoorten
internal/   tokens.css     dichte schaal + shadcn-mapping + dark
            starten.md     van niks naar een draaiende app
            components.md  shadcn-workflow en patronen
```

Naast dit systeem: `brand-guidelines.md` (merk breed), `roadmap-naar-topniveau.md` (waarom deze opzet), `framer-audit-en-migratie.md` (Framer-specifiek).

`tokens.css` in deze hoofdmap is de oude gecombineerde versie. Blijft staan zodat oude verwijzingen niet breken, maar gebruik `core/` + je oppervlak.
