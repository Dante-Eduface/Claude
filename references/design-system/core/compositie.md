# Compositie en bewijsvoering

`regels.md` gaat over de kleine dingen (contrast, radius, spacing). Dit gaat over de grote: wat zet je waar, en waarom. Geldt voor alle drie de oppervlakken.

Grotendeels afgeleid van de Vercel brand guidelines (29-08-2026), vertaald naar Eduface. Let op: dat document is vakmanschap, geen bewijs. Het bevat geen enkel validatiecriterium. Gebruik het als oordeelskader, meet de uitkomst apart.

---

## 1. Begin bij de taak van de lezer, niet bij het soort document

Voor je iets ontwerpt, beantwoord privé:

- Wie opent dit, in welke situatie, om wat te beslissen of te begrijpen?
- Wat is het sterkste antwoord dat het materiaal ondersteunt?
- Welk bewijs maakt dat antwoord geloofwaardig?
- Welke afweging, onzekerheid of grens verandert de interpretatie ervan?
- Wat moet naslaanbaar blijven zonder de eerste lezing te domineren?

Kun je die vijf niet beantwoorden, dan ontwerp je nog niet. Dan verzamel je nog.

## 2. Twee leessnelheden

Dit is het meest bruikbare idee uit het hele document, en voor Eduface direct van toepassing: bij een hogeschool leest een directeur onderwijs iets anders dan de kwaliteitsmedewerker die het narekent.

- **Besluitpad:** titel, koppen, beslissende getallen, bijschriften en conclusie dragen het argument in één doorloop. Geschreven in gewone taal, die de minst gespecialiseerde genoemde lezer kan navertellen.
- **Naslagpad:** exacte tabellen, aannames, methode, voorbehouden en bronnen bewaren het bewijs. Hier staan de vaktermen en exacte metrieknamen.

Definieer een onbekende term één keer in gewone woorden, gebruik daarna consequent de exacte term.

**Vereenvoudig de taal, nooit de claim.** Elk voorbehoud, elke populatie, periode, eenheid en vergelijkingsbasis die de betekenis verandert blijft staan. "Binnen de meetruis" wordt geen "even snel". Voor Eduface concreet: "formatieve feedback op schrijfopdrachten" wordt geen "nakijken", en een pilotresultaat bij één opleiding wordt geen instellingsbrede uitspraak.

## 3. Kies eerst de geometrie, dan pas het component

Koppel het materiaal aan een visuele variabele voor je een component kiest:

| Wat je toont | Geometrie |
|---|---|
| Grootte of rangorde | positie of lengte op één schaal |
| Verandering over tijd | horizontale volgorde, uitgelijnde positie |
| Samenstelling | verhouding |
| Drempel of bandbreedte | afstand tot een grens |
| Proces of afhankelijkheid | verbinding en volgorde |
| Kwalitatieve alternatieven | uitgelijnde rijen of bewust contrasterende kolommen |

Tabellen voor exact opzoeken. Proza voor één conclusie. Grafieken alleen voor verbanden die visueel sneller te snappen zijn. Niet standaard staafjes omdat er getallen zijn.

## 4. Verwerp eerst de voor de hand liggende layout

Benoem privé welke opzet dit soort document normaal krijgt. Verwerp die, tenzij het materiaal hem verdient. Een webinar-uitnodiging hoeft niet op elke webinar-uitnodiging te lijken.

Zijn er meerdere structuren mogelijk, vergelijk dan twee wezenlijk verschillende opzetten voor je begint te bouwen. Verschil in topologie, dichtheid en plaatsing van het bewijs, niet in kleur of componentkeuze.

**Geef elk stuk één dragende ordeningszet die bij dít materiaal hoort** en die je niet ongewijzigd naar een ander onderwerp kunt kopiëren. Een vergelijkingsgeometrie, een drempel, een volgorde, een instellingsspecifiek schema. Het moet het onderwerp verduidelijken, niet versieren.

## 5. Eén dominant object per leesmoment

De eerste viewport is het argument, niet een titelbalk gevolgd door aanloop. Zag iemand alleen dat eerste scherm, dan moet hij het centrale verband onthouden, niet alleen de titel.

Bouw de pagina als een veld, niet als een stapel componenten. Eén doorlopende lijn over de pagina, één brandpunt per sectie, daaromheen weinig ondersteunende objecten en genoeg lucht om dat brandpunt te versterken.

Herhaling geeft ritme alleen als de herhaalde dingen echte gelijken zijn. Anders geeft het sjabloonruis. **Dwing ongelijke bevindingen niet in gelijke vakjes.** Rangschik ze, of geef de beslissende meer gewicht, zodat de vorm het argument volgt.

## 6. Twee gratis controles

- **Squint-test:** knijp je ogen samen. Is de dominante claim direct duidelijk en is het leespad stabiel?
- **Tekstmasker-test:** maak de woorden onleesbaar. Communiceert de hiërarchie dan nog steeds afzender, nadruk, groepering en voortgang?

Heeft elk blok even veel gewicht, dan herontwerp je voordat je verder bouwt.

## 7. Geef elke witruimte één eigenaar

Technische regel die veel scheelt. Een container (grid, stack, flow) zet de tussenruimte; zijn kinderen zetten geen eigen marges erbovenop. Reset de marges van gegroepeerde kinderen en gebruik de spacing-tokens.

Verticaal ritme volgt uit relaties, niet uit één universele stapelafstand:

- Kop naar eerste alinea: dicht
- Alinea naar alinea: één body-ritme
- Label, waarde, detail: identiek over alle gelijken heen
- Groep naar nieuwe sectie: duidelijk groter
- Bijschrift of bron naar het bewijs dat het toelicht: dicht genoeg om samen te lezen

Grote lege rechthoeken door een half gevulde split of een derde item dat alleen staat zijn geen lucht maar een fout. Herverdeel of stapel.

## 8. Diagnose: druk of luid

Twee verschillende problemen die je anders oplost.

- Voelt het **druk**, dan is er te veel. Weghalen, samenvoegen, herordenen.
- Voelt het **luid**, dan is er te veel intensiteit. Minder concurrerende kleur, schaal, gewicht, randen, vlakken.

Houd altijd één bewust anker overeind. Ingetogenheid mag niet doorslaan in vlakke eenvormigheid.

## 9. Tabellen zijn bewijs

- Semantische `<table>` met caption, thead, tbody.
- Volle breedte van de sectie. Zet de inleiding erboven, niet ernaast.
- **Kolomkop krijgt dezelfde uitlijning als zijn cellen.** Getalkolommen rechts, ook de kop. Dit gaat bijna altijd mis.
- Cellen lijnen uit op de eerste tekstregel, niet gecentreerd of onderaan.
- Geef de labelkolom genoeg breedte zodat korte labels niet afbreken terwijl er ruimte over is.
- Verspil geen kolom aan dezelfde categorie voor een reeks rijen. Groepeer die rijen.
- Consistente eenheden en precisie. Geen nepprecisie.

## 10. Staafgrafieken delen één raster

Ontwerp de set als één layout, niet rij voor rij. Eén labelbaan, één plotbaan, één waardebaan. Elke staaf begint en eindigt op dezelfde rasterlijn, alleen de vulling verschilt. Verandert een lang label de plotbreedte van die rij, dan is de layout fout.

Nulpunt als basis, tenzij je expliciet een bandbreedte of verschil toont. Kleine verschillen niet uitvergroten door de as af te snijden.

**Let op de noemer.** Vergelijk geen ruwe aantallen alsof de bases gelijk zijn. Kies bewust tussen aantal en percentage op basis van de vraag van de lezer, en toon de andere erbij.

Directe labels boven een legenda.

## 11. Kleur draagt betekenis of hoort er niet

Ontwerp in principe monochroom: navy, wit, de neutralen. De volledige kleurregel staat in `regels.md`; de kern: **groen betekent kijk hier of dit is goed afgelopen, nooit klik hier.** De primaire knop is navy. Maak een besparing of aanbeveling niet groen omdat hij gunstig is, en zet naast kleur altijd een signaal dat geen kleur is.

Verdien een vlak of een rand pas als hij selectie, interactie, waarschuwing of een echte groepering uitdrukt die ruimte niet kan uitdrukken. Niet elke sectie in een kaartje. Geen kaartjes in kaartjes.

## 12. De reflexen-lijst

Dit is in de praktijk het bruikbaarste stuk van het hele Vercel-document: een lijst waaraan je AI-gegenereerd en sjabloonwerk herkent. Loop hem langs voor je iets oplevert.

- Kapitalen-labeltjes boven koppen, decoratieve sectienummers
- Em-dashes
- Decoratieve gradiënts, gloed, blobs, strepen, textuur, glas, sierschaduwen
- Gecentreerde hero-tekst gevolgd door een kaartjesraster
- Herhaalde metric-boxjes waar één samengesteld verband duidelijker was
- Een badge of pill om gewone metadata
- Kaartjes in kaartjes, of randen die zwakke hiërarchie moeten repareren
- Een donker afgerond blok om elke grafiek
- Willekeurige icoontegels, te grote iconen, gemengde icoonstijlen
- Kleine grijze tekst om dichtheid passend te maken
- Een smalle tabel in een brede sectie, of een brede tabel platgedrukt tot afgebroken woorden
- Decoratieve grafieken, legenda's die directe labels vervangen, kleur zonder betekenis
- Identieke sectiesilhouetten voor onderling verschillende vragen
- Herhaalde aanbeveling-, samenvatting- en conclusieblokken die hetzelfde zeggen
- Procesverslag in de tekst ("hoe deze pagina is opgebouwd")
- Stockbeeld, nepscreenshots, decoratieve merktekens

En het tegengif erbij: los dit niet op door een steriel anti-design op te leveren. Ingetogenheid is scherpe hiërarchie, goede typografie, duidelijk bewijs en bewuste spanning. Niet zwart-wit met dunne lijntjes en veel marge.

**Deze lijst is een verdediging tegen sjabloonwerk, geen plafond op ambitie.** Dante, 18-09-2026: de web-oppervlakte voelde hierdoor te voorzichtig, te plat. Voor hero's en productbeelden op de marketingsite geldt daarom een expliciete, bewuste uitzondering op "decoratieve gradiënts, gloed" — zie `web/regels.md`. De rest van deze lijst (stockbeeld, nepscreenshots, kaartjes-in-kaartjes, herhaalde metric-boxjes) blijft overal onverkort gelden, ook op web.

## 13. Beweging

Standaard stil. Geen scroll-onthullingen per sectie, geen parallax, geen typemachine-cursors, geen pulserende bolletjes. Beweging alleen als die een toestandsverandering uitlegt of een actie bevestigt. De pagina moet compleet zijn zonder beweging.

## 14. Governance: wat Vercel structureel goed doet

Los van de smaak, dit is het overneembare systeemidee:

- Er is één gepubliceerde token- en class-API. Die is de publieke kant.
- Pagina-eigen CSS mag alleen uit die tokens lezen en mag nooit een foundation-class aanspreken.
- Eigen dingen krijgen een eigen namespace (bij hen `vbg-custom-*`).
- Een eigen class die op een foundation-primitive lijkt mag diens layout, typografie, vlak, rand of controlstijl niet wijzigen.

Dat is precies de discipline die `core/` hier moet krijgen: core is de publieke API, oppervlakken bouwen erop, niemand hackt in core.
