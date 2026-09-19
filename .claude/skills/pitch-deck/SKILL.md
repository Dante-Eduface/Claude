---
name: pitch-deck
description: Bouwt Eduface-slides en decks die er af uitzien en die bewerkbaar zijn in Canva of PowerPoint. Eén bron levert zowel een PNG-preview als een pptx met echte tekstvakken, dus preview en oplevering lopen niet uit elkaar. Trigger wanneer Dante zegt "maak een slide", "bouw het deck", "maak er een pptx van", "maak een slide over X", "pas slide Y aan", of een schets of screenshot aanlevert die een slide moet worden. Ook voor losse slides, niet alleen hele decks.
---

# Pitch-deck

Slides voor een fysieke pitch of demo. Eén elementenlijst per slide is de bron; daaruit
komt zowel de HTML-preview (voor jezelf, om te controleren) als de bewerkbare pptx (voor
Dante, om in Canva te importeren).

## Voor je begint
1. `Design/System/slides/layouts.md` — de soorten slides.
2. `Design/System/slides/pitch-slides.md` — hoe een pitch-slide eruitziet. **Verplicht.**
3. `Platform/Product/product.md` — de enige bron voor productclaims. Staat het er niet, dan zet je het niet op een slide.
4. `reference.md` in deze map — de valkuilen. Scheelt drie rondes.

## De drie poorten
`Design/System/core/proces.md` geldt ook hier. Nooit in één klap een heel deck:
eerst één slide als PNG, akkoord, dan de rest. Dante slaat poorten over door "gewoon bouwen" te zeggen.

## De loop
```
1. RICHTING   wat is het ene idee van deze slide? Eén of twee woorden als titel.
2. BOUW       schrijf een slide-script: een lijst elementen (zie hieronder)
3. PREVIEW    render naar PNG, kijk er zelf naar
4. HERSTEL    overlap, ontbrekende iconen, tekst die uit zijn kader loopt
5. TOON       stuur de PNG naar Dante, vraag akkoord
6. PPTX       pas na akkoord render_pptx, controleer dat niets buiten het canvas valt
```

## Hoe een slide eruitziet in code
```python
from deckbuild import rect, oval, pic, text, title, tile, foot, cols, render_html, render_pptx, shoot

els  = title('Visitatie')
els += tile(960, 460, 'verschillen', 'amber')
els += [text(120, 630, 1680, 110, 'Toelichting leeg', font=HEAD, size=46, bold=True)]
els += foot(src='NQA, visitatie november 2024, p. 25.', page=4)

shoot(render_html(els, 'preview/visitatie.html'), 'preview/visitatie.png')
render_pptx([els], 'slide-visitatie-bewerkbaar.pptx')
```

Raster is 1920x1080 px, marge 120. `cols(n)` geeft de x-middens en de kolombreedte.
`foot()` zet de scheidingslijn, de bron, het logopaar en het paginanummer.
`tile()` zet een icoontegel; het icoon wordt zo nodig gerenderd met `icons.py`.

## Assets
Zet in de werkmap een `assets/` met:
- `logo_navy.png` en `logo_white.png` uit `Design/Merk/logos/`
- het klantlogo als `klant.png` (schoollogo's staan in `Design/System/Logo van scholen/`)
- SVG-logo's eerst naar transparante PNG renderen en de lege rand wegknippen, anders klopt de schaal niet

Iconen: `python3 icons.py verschillen variatie --tint amber`. Nieuw icoon nodig? Paadje toevoegen
aan `ICONS` in `icons.py`, dan staat het er voor elk volgend deck.

## Controle voor je oplevert
```python
from pptx import Presentation
p = Presentation('deck.pptx')
for i, sl in enumerate(p.slides, 1):
    buiten = [s.shape_id for s in sl.shapes
              if s.left < 0 or s.top < 0
              or s.left + s.width > p.slide_width or s.top + s.height > p.slide_height]
    print(i, 'buiten canvas:', buiten or 'geen')
```
Er is geen automatische layout. Tekst die te lang is, loopt over de volgende regel heen zonder
foutmelding. Altijd de PNG bekijken voordat je iets opstuurt.

## Waar het bestand heen gaat
`projects/<account>/deck/`. Bewerkbare pptx heet `...-bewerkbaar.pptx`. Previews in `preview/`.
