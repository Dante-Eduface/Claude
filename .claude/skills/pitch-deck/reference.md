# Valkuilen

Opgedaan bij het Windesheim-deck, september 2026. Dit zijn de dingen die tijd kostten.

## Er is geen auto-layout
De renderer zet elementen op vaste coördinaten. Wordt een tekst twee regels in plaats van
één, dan loopt hij over het volgende element heen en krijg je geen foutmelding. Twee gevolgen:

- **Kijk altijd naar de PNG** voordat je iets opstuurt. Niet naar de code.
- Reken de verticale opbouw uit voordat je bouwt. Titel 88 tot 208, inhoud tot ongeveer 820,
  scheidingslijn van de voet op 868, logo's op 900.

Overloop kwam telkens terug bij: een citaat van drie regels, een bronregel van twee regels,
en een label dat in een smalle kolom afbrak.

## Iconen bestaan pas als je ze rendert
`tile()` verwijst naar `assets/icon-<naam>-<tint>.png`. Bestaat dat bestand niet, dan rendert
de HTML een leeg kadertje en de pptx een grijs vlak. Geen crash. Render eerst, bouw dan.
Elke tint is een apart bestand, dus een icoon in groen betekent niet dat navy er ook is.

## SVG-logo's hebben een lege rand
Render je een SVG naar PNG, dan staat het logo links met transparante ruimte ernaast. Knip
die weg op het alfakanaal, anders schaal je lucht in plaats van logo:

```python
from PIL import Image
im = Image.open(f).convert('RGBA')
bbox = im.split()[3].getbbox()
if bbox: im.crop(bbox).save(f)
```

## Donkere logo's verdwijnen op navy
Het klantlogo heeft meestal donkere letters. Op een navy slide zet `foot(dark=True)` het
logopaar daarom op een wit afgerond vlak. Gebruik nooit een op navy ingebakken PNG-variant,
die valt alsnog weg.

## Titels op een donkere slide
`title()` gebruikt navy. Op een navy achtergrond moet `title('Demo', dark=True)`, anders staat
er navy op navy en lijkt de slide leeg. Dit is twee keer misgegaan.

## De previewmap heeft eigen paden
De preview-HTML staat in `preview/`, dus relatieve paden naar `assets/` kloppen daar niet.
`render_html` zet er standaard `../` voor. Zet je previews ergens anders neer, geef dan
`prefix` mee.

## PowerPoint-maten
1 ontwerp-pixel is 6350 EMU en een pixel is een halve punt (1920 px over 13,333 inch).
Dus een tekst van 46px wordt 23pt. Dat zit in `render_pptx`, maar je hebt het nodig zodra je
zelf iets uitrekent.

## Canva
Canva importeert pptx en houdt tekstvakken bewerkbaar, mits het echte tekstvakken zijn en geen
platte afbeelding. League Spartan en Inter staan allebei in Canva, dus de typografie blijft
kloppen. Iconen blijven afbeeldingen: verplaatsen en schalen kan, hun kleur veranderen niet.

## Bestanden kunnen terugvallen
Twee keer bleek een buildscript teruggezet naar de laatste commit, waardoor eerdere wijzigingen
weg waren. Controleer bij hervatten of het script nog is wat je denkt, en commit tussendoor.
Werk in de hoofdmap, niet in een worktree, zie de memory `worktree-vinkje-uit`.

## Fictieve data
Zet je verzonnen cijfers in een dashboard-achtige slide, dan hoort er letterlijk bij dat het
een voorbeeld is. Bij een publiek met een IT-architect of compliance officer is dat geen
formaliteit maar zelfbescherming.
