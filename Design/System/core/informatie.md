# Informatie: wat een scherm zegt

`regels.md` en `compositie.md` gaan over hoe iets eruitziet. Dit document gaat over de laag daarboven: welke informatie er staat, en waarom die er staat. Dat is waar de meeste ontwerpfouten zitten, niet in de typografie.

Geldt overal: een landingspagina, een deck, een dashboard, een tool. Een statistiekenblok op een landingspagina maakt dezelfde fouten als een tabelrij.

---

## 1. Definieer je kernbegrip één keer

Zoek het begrip waar de rest uit volgt, schrijf het op, en leid alles daarvan af. Doe je dat niet, dan gaan losse elementen elkaar tegenspreken zonder dat iemand ziet waarom.

Voorbeeld uit het product: *een inzending wacht zolang de docent hem niet heeft goedgekeurd.* Daaruit volgt wat "te beoordelen" betekent, wat "langst wachtend" betekent, en wanneer een cursus afgerond is. Die drie kunnen elkaar daarna per definitie niet meer tegenspreken.

Het tegenvoorbeeld: een teller "2 van 4 open" naast een teller "20 te beoordelen". Het woord "open" was nooit gedefinieerd, en elke mogelijke definitie sprak de buurman tegen of herhaalde hem vager.

## 2. Eén feit, één weergave

Codeer hetzelfde niet twee of drie keer. Een ring, een breuk `12/32` en een getal `20 te beoordelen` zijn samen één feit in drie vormen. Kies degene waar iemand naar handelt en schrap de rest.

Zie ook de reflexen-lijst in `compositie.md`: herhaalde metric-boxjes waar één samengesteld verband duidelijker was.

## 3. Een label dat overal hetzelfde is, draagt geen informatie

Staat `Active` op zeven van de acht rijen, dan kost dat label aandacht en levert het niets. Laat de norm naamloos en toon alleen de afwijking.

Dit is dezelfde regel als in `compositie.md` over tabellen: verspil geen kolom aan dezelfde categorie voor een reeks rijen.

## 4. Toon een getal, of zeg waarom er geen is

Een lege cel, een streepje en een nul zijn drie verschillende dingen. Nul betekent "geteld, uitkomst nul". Een streepje betekent "niet van toepassing". Leeg betekent meestal "we weten het niet", en dat moet je zeggen in plaats van suggereren.

Teken ook geen voortgangsindicator voor iets dat geen voortgang heeft. Een lege ring bij "nog niets ingeleverd" leest als nul procent gedaan, dus als achterstand, terwijl er niets wordt verwacht.

## 5. Kleur codeert een toestand die iemand anders heeft gezet

De volledige kleurregel staat in `regels.md`. De informatiekant ervan: kleur mag een feit markeren, geen mening.

Een getal rood maken omdat wij twaalf dagen lang vinden, is onze mening verkleed als signaal. Een getal rood maken omdat het voorbij de deadline ligt die de instelling zelf heeft gezet, is een feit. Heb je geen extern vastgestelde grens, verzin er dan geen en presenteer hem al helemaal niet als norm.

## 6. Zonder kolomkop draagt elke waarde zijn eigen label

In een tabel doet de kop dat werk één keer voor de hele kolom. In een kaart, een tegel of een blok op een landingspagina betaal je het per stuk. Gevolg: minder waarden per blok, elk met een woord ernaast.

`1 day ago` zonder label kan van alles zijn. Praktisch: elk getal dat je op een kaart zet, kost je ook de ruimte voor zijn label. Kun je dat label niet kwijt, dan hoort het getal er niet.

## 7. Waar geen kop is om op te sorteren, ís de volgorde de rangschikking

Een tabel laat je op een kolom klikken. Een raster van kaarten niet. Dan moet de standaardvolgorde zelf het antwoord zijn op "waar moet ik nu heen", en moet je die volgorde op het scherm benoemen zodat hij niet als willekeur leest.

Bijkomend: kaarten maken vergelijken moeilijker dan rijen, want je oog kan geen kolom aflopen. Compenseer dat met de volgorde, niet met meer vulling per kaart. ([NN/g, Data Tables](https://www.nngroup.com/articles/data-tables/): mensen zoeken iets specifieks, vergelijken records, of handelen op een record. Kaarten zijn goed in de eerste en de derde.)

## 8. Wrijving schaalt mee met wat er verloren gaat

Een omkeerbare actie krijgt geen bevestigingsdialoog, maar wel een ongedaan-maken achteraf. Een onomkeerbare actie krijgt wrijving vooraf, en die wrijving groeit met de schade: een lege map weggooien is één klik, een map met andermans werk weggooien benoemt in aantallen wat er verdwijnt en laat je de naam overtypen.

Zet een omkeerbare en een onomkeerbare actie nooit naast elkaar in hetzelfde menu, gelijk van grootte. Haal de onomkeerbare weg uit de plek waar mensen snel werken.

## 9. Een control die verschijnt en verdwijnt breekt het model

Toon geen filterbalk vanaf 25 items die bij 24 weer weg is. De gebruiker deed niets aan die balk, en toch is hij er niet meer. Dat is precies het patroon dat in de literatuur over automation surprise fout gaat: het systeem doet iets dat het mentale model van de gebruiker niet dekt (Sarter, Woods & Billings, 1997).

Dezelfde fout op kleinere schaal: een keuze uit een menu verbergen of uitzetten omdat hij nul oplevert. Die nul is informatie.

Een drempel op aantallen is bovendien zelden eenduidig: telt hij het totaal of de gefilterde stand? Bij de gefilterde stand verdwijnt de balk terwijl je hem gebruikt.

## 10. Verzin geen structuur die er niet is

Geen filter op een programma-niveau dat niet bestaat. Geen tags als het datamodel geen tags kent. Geen periode als we die data niet uithalen. Een control die op lucht staat, is erger dan een ontbrekende control, want hij belooft iets.

Zelfde regel als bij productclaims: staat het niet in de bron, dan bestaat het niet. Zie `Platform/Product/product.md`.

---

## De toets

Voor elk element op een scherm, in deze volgorde:

1. **Verandert dit wat iemand nu gaat doen?** Zo niet, dan is het context en geen signaal, en dan hoort het niet op de plek met het meeste gewicht.
2. **Is het waar op dit niveau, of alleen afgeleid?** Afgeleid mag, maar dan moet het label dat zeggen. Een cursus heeft geen deadline, een opdracht wel. Zet je hem toch op de cursus, noem hem dan `eerstvolgende deadline` en niet `deadline`.
3. **Heeft het een fatsoenlijke lege staat?**
4. **Bestaat de data echt?**
5. **Doet het hetzelfde werk als zijn buurman?**

Zakt een element op vraag 1 of 5, dan gaat het eruit. Zakt het op 2, 3 of 4, dan moet het label of de definitie eerst kloppen.

---

## Herkomst

De regels hierboven komen uit het ontwerpwerk aan de docentomgeving, september 2026, en uit drie onderzoeksdocumenten:

- `Platform/Onderzoek/notities/ux-ui-design-expertwerkwijze.md` — wat een ontwerp goed maakt, en waar de vakliteratuur elkaar tegenspreekt.
- `Platform/Onderzoek/notities/designkeuzes-bij-spanning.md` — hoe je kiest als twee opties allebei verdedigbaar zijn, wat gewoontes doorbreken kost, en welke toets welke vraag beantwoordt.
- `Platform/Onderzoek/notities/onboarding-naar-eerste-waarde.md` — hoe je iemand naar zijn eerste waardemoment brengt, wachttijd ontwerpen, en wat er bekend is over docentadoptie en vertrouwen in AI-feedback.
