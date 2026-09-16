# Vaste visuele regels

Geldt voor alle drie de oppervlakken. Kort, want dit is de laag die nooit verandert.

## Kleur

- Bijna alles is navy, wit en de navy-getinte neutralen. Groen is het enige accent.
- **Groen betekent: kijk hier, of dit is goed afgelopen. Groen betekent nooit "klik hier".**
  Mensen lezen fel groen als gelukt, klaar, veilig. Die reflex komt uit stoplichten en vinkjes en die win je niet met een designregel, dus sluit erop aan.
- **De primaire knop is navy. Altijd, op elk oppervlak.** Dat is `--color-primary`.
- Groen mag op precies twee plekken:
  1. De hero-CTA op een pagina. Dat is het enige punt waar "kijk hier" en "klik hier" samenvallen. Eén per pagina.
  2. Een bevestigde positieve status in een tool: klaar, goedgekeurd, loopt op schema.
- **Nooit groen op een getal of een staaf omdat de waarde gunstig is.** Een besparing wordt niet groen. Kleur codeert een toestand, geen mening over de uitkomst.
- Zet naast groen altijd een signaal dat geen kleur is (een vinkje, een label, een positie). Dan werkt het ook voor wie kleur slecht onderscheidt.
- Groen als tekst op wit: gebruik `green-deep` (#007b54), niet de felle `green`. De felle heeft te weinig contrast en werkt alleen als vlak met navy tekst erop.
- Nooit puur zwart of puur wit als tekstkleur op een gekleurd vlak. Navy is de zwart-vervanger.
- Verlaag contrast nooit om iets minder nadruk te geven. Gebruik grootte, gewicht of ruimte. Bron: [NN/g, Principles of Visual Design, 2020](https://www.nngroup.com/articles/principles-visual-design/).

## Donker: twee verschillende dingen

Niet door elkaar halen.

- **Inverse** is één donker blok op een verder lichte pagina: een navy sectie tussen witte secties, om een overgang of een uitspraak te markeren. Dit gebruik je actief. Tokens: `--color-background-inverse` en de bijbehorende `*-inverse` reeks in `core/tokens.css`.
- **Dark mode** is dat de hele interface donker wordt omdat de gebruiker dat in zijn systeem instelt. Dit gebruiken we alleen in `internal/`, omdat shadcn het gratis meelevert. We ontwerpen er niet actief voor, en op de site en in slides bestaat het niet.

## Contrast (harde ondergrens, geen smaak)
- Normale tekst minimaal **4.5:1**, grote tekst (vanaf 18pt regular of 14pt bold) minimaal **3:1**. Bron: [WCAG 2.2, W3C, 2023](https://www.w3.org/TR/WCAG22/).
- Dit is de enige regel in dit document met normatieve status. De rest is vakconventie.

## Typografie
- Twee fonts, niet meer. League Spartan voor koppen, Inter voor de rest.
- Hiërarchie met maximaal 2 tot 3 groottes of gewichten per scherm.
- Line-height en tracking zitten in de tokens. Niet handmatig bijstellen.
- Regellengte lopende tekst: 45 tot 90 tekens. Bron: [Butterick, Practical Typography](https://practicaltypography.com/line-length.html). Onze `--measure` staat op 68ch, midden in die band.

## Ruimte
- Alles op de 8pt-familie (8, 16, 24, 32, 48, 64, 96). Niet gokken tussen de trappen door.
- Dingen die bij elkaar horen staan dichter bij elkaar dan bij de rest. Groeperen doe je met ruimte, niet met lijnen.
- Veel witruimte, één duidelijke hiërarchie per scherm.

## Radius
- Vaste schaal: 6 / 8 / 10 / 12 / 20 / vol rond. Eén radius per componenttype.
- **Geneste hoeken:** binnenradius = buitenradius min de tussenruimte. Anders lopen de bogen niet parallel en ziet het er net verkeerd uit zonder dat je ziet waarom. In CSS: `border-radius: max(0px, calc(var(--radius) - var(--pad)))`.

## Schaduw
- Drie niveaus, subtiel, allemaal navy-getint. Niet stapelen, niet zwart.
- Diepte is een signaal (dit zweeft, dit is actief), geen versiering.

## Wat dit systeem niet oplost
Regels voorkomen dat iets er amateuristisch uitziet. Ze maken het niet onderscheidend. Onderzoek laat zien dat sites tussen 2010 en 2016 meetbaar meer op elkaar zijn gaan lijken door gedeelde libraries en defaults ([Goree e.a., CHI 2021](https://dl.acm.org/doi/10.1145/3411764.3445156)). Het onderscheid moet ergens anders vandaan komen: eigen beeldtaal, eigen woorden, het echte product laten zien. Zie `web/components.md` en de tegenspraak-sectie in `references/research/ux-ui-design-expertwerkwijze.md`.
