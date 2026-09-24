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

## Een Linux/remote-sessie is geen Mac

Opgedaan bij het board-deck van 24-09-2026, in een sandboxed Claude Code on the web-sessie
(niet Dante's Mac). `deckbuild.py` corrigeert dit nu zelf, maar goed om te weten waarom.

- **Chrome bestaat hier niet.** Het gekopieerde Mac-pad in `CHROME` klopt niet meer. Er
  draait wel een Chromium op `/opt/pw-browsers/chromium`. `_find_chrome()` probeert nu
  beide plus een paar `which`-namen.
- **Root heeft `--no-sandbox` nodig**, anders weigert Chrome meteen te starten
  ("Running as root without --no-sandbox is not supported").
- **De onderste ~90px van elke slide bleef wit**, ook met een navy achtergrond die de hele
  1920x1080 zou moeten vullen. Headless Chrome reserveert binnen `--window-size` ruimte
  voor een onzichtbare vensterbalk, dus de echte viewport is korter dan gevraagd. Fix:
  vraag `--window-size=1920,1200` en snijd terug naar 1920x1080.
- **Google Fonts laadt hier niet.** Niet een certificaatprobleem (de CA klopt en staat al
  in de systeemstore), maar een bewuste policy-block op Google-domeinen. Chrome valt dan
  stil terug op een systeemfont, zonder foutmelding, en de preview lijkt precies goed totdat
  je goed naar de letters kijkt. Fix: `render_html` bakt `LeagueSpartan-Bold.ttf` en
  `Inter-Regular.ttf` zelf in als base64 i.p.v. de CDN-link, dus zet die twee bestanden in
  `assets/` (bron: `Design/Merk/fonts/`). Nooit `--ignore-certificate-errors` gebruiken om
  hier omheen te werken, dat is geen certificaatfout.
