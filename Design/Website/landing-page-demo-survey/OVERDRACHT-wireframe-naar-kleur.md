# Overdracht: van wireframe naar een goede ingekleurde versie

Geschreven 15-09-2026 voor de sessie die de pijn-landingspagina bouwt. Alles wat in de wireframe-fase van de demopagina is geleerd, zodat je die ronde niet hoeft over te doen.

---

## 1. Waar het proces staat

De drie poorten uit `Design/System/core/proces.md` zijn leidend.

| Poort | Status |
|---|---|
| 1 · richting en volgorde | af, sectievolgorde ligt vast |
| 2 · proef, één onderdeel op echte kwaliteit | af voor hero (`proef-hero.html` v2) en bewijsblok (`proef-bewijsblok.html` v9) |
| 3 · uitrol | nog niet begonnen |

**Belangrijkste procesles:** de lo-fi wireframe is een wegwerpartefact. Zodra er twee ingekleurde proefs liggen is de wireframe achterhaald en moet je hem niet meer bijwerken. Wij verloren daar bijna een halve ronde aan.

---

## 2. Wireframe-lessen

**Geen placeholder-copy.** Nepzinnen in blokhaken leiden af. Vervang alle tekst door grijze balken (`height: 10px; border-radius: 5px; background: #d9d9d9`), met varianten voor h1/h2/h3/body. Alleen waar het getal of de naam zélf de beslissing is (percentage, klantnaam, citaat) zet je echte tekst.

**Elke sectie een eigen silhouet.** Achter elkaar dezelfde kaartenrij leest als sjabloonwerk. Wissel af: split, bento, tijdlijn met stippellijn, productrijen links/rechts, cijfers met balk, lijnen-FAQ, afgerond CTA-blok. Zie `core/compositie.md` punt 5.

**Ruimte is het halve werk.** 120px sectiepadding, wit en grijs afgewisseld als grond, één donkere band voor het zwaarste blok. Dante's eerste feedback was letterlijk "heel erg krap en alles op elkaar".

**Annotaties klein houden.** Begonnen met een rechterkolom vol uitleg per sectie, geëindigd met één klein nummerlabel. De uitlegkolom werd zelf ruis.

**Nav:** logo links, links gecentreerd, CTA rechts. `grid-template-columns: 1fr auto 1fr`.

**Hero:** gestapeld en gecentreerd. Kop, subkop, twee grote knoppen, dan ruimte, dan de eerste productbeelden die onder de vouw doorlopen. De tekst-links-beeld-rechts-split voelde krap.

---

## 3. Van wireframe naar kleur

**Laad alleen `core/` plus `web/`.** Nooit de hele design-system-map.

**Kleurregels die we het vaakst nodig hadden:**
- Primaire knop is navy. Altijd.
- Groen betekent "kijk hier" of "dit is goed afgelopen", nooit "klik hier". Eén groene hero-CTA per pagina is de enige uitzondering.
- Groen als tekst op wit: `green-deep` #007b54, niet de felle.
- Nooit groen op een getal omdat de uitkomst gunstig is.

**Wat in de proefs aantoonbaar werkt:**
- Kop in twee kleuren: eerste regel navy, tweede regel groen. Draagt de belofte zonder extra element.
- Eén echt productbeeld per sectie, nagebouwd als UI. Geen screenshot, geen stockbeeld.
- Donkere band (inverse) voor het bewijsblok. Het enige donkere blok tot de eind-CTA, dus het valt op zonder te schreeuwen.
- Een foto van de instelling naast de cijfers maakt een pilot concreet. Alleen als je de naam mag noemen.

**Voor oplevering:** reflexen-lijst uit `core/compositie.md` punt 12, plus squint-test en tekstmasker-test. Dante hoort niets te hoeven melden dat je zelf had kunnen zien.

---

## 4. Wat het bewijs-onderzoek opleverde

Volledig in `research/proof.md`. De kern:

- **Eén blok dat naam, cijfer en context combineert verslaat losse elementen.** Enige gecontroleerde experiment dat we vonden (comScore via Optimizely, n ≈ 2.500): testimonial mét klantlogo gaf 69% meer demo-aanvragen dan dezelfde zonder.
- **Voor onderwijsinkopers wegen pilots en demo's het zwaarst, testimonials het lichtst.** Onderzoek naar edtech-procurement noemt testimonials expliciet zwak onderbouwd.
- **Twee bronnen die hetzelfde mechanisme aanwijzen verslaan één groot getal.** Bij ons: 94 naar 98 na afstemmen (Bath Spa) naast ronde 1 naar ronde 2 na afstemmen (Rotterdam).
- **Generiek bewijs wordt genegeerd.** Logo-walls lijden aan banner blindness. Een veldexperiment uit 2026 vond geen enkel effect van zichtbare social proof op downloadgedrag. Specifiek en gekwantificeerd werkt wel.
- **Er bestaat geen gecontroleerde test over waar bewijs op een pagina hoort.** Alle percentages daarover komen uit blogs zonder methode, inclusief cijfers die ten onrechte aan Baymard worden toegeschreven. Niet citeren.

---

## 5. Claim-regels (hard)

`Platform/product.md` is de enige bron voor productclaims. Staat het er niet, dan beweer je het niet.

**Mag wel:**
- 94% accuraatheid met de dragers erbij: 435 opdrachten, 13 markers, 6 vakken, Bath Spa University, juni 2026. 98% bij markers die het model hadden afgestemd.
- Rotterdam BDK: 79% van de studenten positief of neutraal. Ronde 2 beter beoordeeld dan ronde 1.
- Klantnamen: Hogeschool Rotterdam, De Haagse Hogeschool, Tilburg University, Radboud Universiteit. Bath Spa mag sinds 11-09-2026 ook.
- Citaat Els Stapersma, met naam en instelling, bevestigd door Dante: "It never gets tired, and in some ways it gives better feedback than I do." Origineel: "Bovendien wordt die tool nooit moe en geeft hij in sommige opzichten betere feedback dan ik."

**Mag niet:**
- "95% accuraat", "#1", "30.000 studenten". Geen bron.
- TIO en ICM, nooit, nergens.
- Citaten van Bath Spa-medewerkers of markers. Helen King heeft expliciet gezegd Eduface niet te zullen aanbevelen.
- Uitval, NSS-effecten of implementatietijd beloven.
- Een cijfer zonder zijn dragers.

**Besluit 11-09-2026:** de methode van het cijfer hoeft niet op de pagina. De dragers blijven wel, want dat is de identiteit van het getal, niet de methode.

---

## 6. De pijn

Bron: `GTM/ICP/pijn-oplossing/HANDOFF-landingspagina.md`, 50 goedgekeurde uitspraken uit Close.

Eén pijn met drie gezichten:
1. **De docent voelt tijd.** Maar zegt nooit "minder werk". Zegt: "ik kom niet toe aan de feedback die ik wil geven."
2. **De student ziet willekeur.** Hetzelfde werk, een 7 bij de een en een 6 bij de ander.
3. **De beslisser betaalt voor risico.** Als het zichtbaar wordt voor een derde: een klacht, een NVAO-rapport, of staff die al AI gebruikt zonder goedgekeurde route.

**Dragend woord: consistentie** (besluit Dante, 11-09-2026). Niet navolgbaarheid, niet tijd.

Why-now per segment: accreditatie bij particulier, krimp bij NL hoger onderwijs, governance in het VK.

---

## 7. Valkuilen die tijd kostten

- **`python3 -m http.server` faalt op de Drive-map** met PermissionError. Gebruik node: kopie van `Design/Website/website-building/serve.mjs`, root via `fileURLToPath(new URL(".", import.meta.url))`. Met `.pathname` worden spaties `%20` en krijg je overal 404.
- **Het in-app browserpaneel geeft lege screenshots zodra het verborgen is.** Gebruik puppeteer uit `Design/Website/website-building/node_modules`, script tijdelijk in die map zetten zodat de bare import resolvet.
- **Scroll de pagina helemaal door voor je screenshot maakt**, anders staan alle in-view reveals leeg.
- **Let op CSS-klassebotsingen.** Wij hadden `.cta` voor zowel de nav-knop als het eind-CTA-blok; de nav-knop werd een enorm donker vlak. Geef nav-elementen een eigen naam.
- **Open HTML altijd zelf in Chrome** met `open -a "Google Chrome" <pad>`. Dubbelklikken opent bij Dante een code-editor.
- **Worktrees lopen uiteen.** Meerdere sessies werkten aan dezelfde bestanden in verschillende worktrees. Check de wijzigingsdatum voor je iets overschrijft.

---

## 8. Bestanden

| Bestand | Wat |
|---|---|
| `proef-hero.html` | ingekleurde hero, v2, poort 2 af |
| `proef-bewijsblok.html` | ingekleurd bewijsblok, v9, poort 2 af |
| `wireframe.html` | lo-fi, acht secties, achterhaald |
| `research/proof.md` | bewijs-onderzoek plus alle besluiten |
| `onderzoek.md` | eerder landingspagina- en survey-onderzoek |
| `README.md` | projectbesluiten en design-inspiratie |

Referentie die Dante mooi vindt: https://habitline-wbs.framer.website/

---

## 9. Open punten

- 94% staat nu zowel als kaart in de hero als hoofdgetal in het bewijsblok. Eén van de twee moet iets anders dragen.
- Hero en bewijsblok formuleren hetzelfde verschillend: "our proposed grade against the marker's" tegenover "before/after the lecturer instructs it". Kies één.
- De kwalificatievragen vóór de agenda zijn geparkeerd, niet geschrapt.
- Alles gaat uiteindelijk naar Framer. Bouw binnen dat model: stacks en gap, nooit margins op children, geen vaste hoogtes, minmax-grids, framer-motion als enige animatielib. Zie `Design/System/web/framer.md`.
