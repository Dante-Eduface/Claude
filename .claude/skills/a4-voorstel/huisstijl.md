# Huisstijl van het A4-voorstel

Vastgelegd 29-10-2026, uit Dantes feedback tijdens het Academica-voorstel. Alles hieronder is een keer gecorrigeerd. Niet terugdraaien zonder dat Dante het vraagt.

## Opbouw van een pagina
- Kop: klein nummer (01, 02, ...) boven een titel van **één woord over de inhoud**. Geen soortnaam als "Managementsamenvatting"; de opening heet "Voorstel".
- Daaronder kaarten **onder elkaar**, van belangrijk naar minder belangrijk. Naast elkaar alleen voor een echte vergelijking (Nu tegenover Met Eduface).
- Rangorde zit in de kaartsoort, nooit in nummers: `primary` (getinte kaart, icoon op donkere tegel), `secondary` (lichte tint), `tertiary` (wit met rand).
- Een toelichtende tekst onder de kaarten is ondergeschikt: kleine tekst, streepje links, geen vlak.
- Voetnoten met een sterretje, heel klein, onder de grafiek waar ze bij horen.
- Geef elke pagina één eigen blikvanger (groot getal, poppetjes, balken per docent). Zonder blikvanger lijken pagina's op elkaar.
- Laat ruimte: A4 staand, marge 20 mm, liever een halflege pagina dan een volle.

## Afwisseling door het document
- **Om en om wit en donker**: oneven pagina's wit, even pagina's in het donkerblauw. Geen kopbalk op witte pagina's.
- **Eigen tint per onderdeel** voor de primary en secondary kaarten, allemaal binnen de blauwfamilie (zie `TINT` in `motor/bouwstenen.py`).

## Kleur
- Donkerblauw `#000326` is **accent**: tekst, iconentegels, de balk waar het om gaat, en de achtergrond van donkere pagina's. Nooit als groot vlak op een witte pagina.
- Verder alleen lichtere varianten van dat blauw en wit.
- **Geen rood, groen of oranje.** Ook niet om een afwijking te markeren: gebruik donker tegenover licht, vet tegenover normaal.
- Logo's van instellingen houden hun eigen kleuren. Op een donkere pagina staat het logo op een wit vlak.

## Typografie (vast, staat in `motor/style.css`)
| Wat | Maat |
|---|---|
| Paginatitel | 30 pt League Spartan |
| Kaarttitel | 17 pt League Spartan |
| Groot getal | 36 pt League Spartan |
| Lopende tekst | 12 pt Inter |
| Uitleg in kaart | 11 pt Inter |
| Labels, voetnoten | 9 pt Inter |
Nergens een andere maat. Een titel is overal even groot, ook als de kaart minder belangrijk is.

## Tekst
- Minder tekst: kop plus hooguit één regel per kaart. Dante zegt het als er meer bij moet.
- Geen visualisatie bij een kaart die niet de belangrijkste is, tenzij gevraagd.
- Verzonnen voorbeeldcijfers krijgen het woord "Voorbeeld" erbij.
- Rekensommen zelf narekenen (bedragen, percentages, gemiddelden) en het melden als de getallen elkaar tegenspreken.

## Pptx
- Altijd bewerkbare tekstvakken, nooit platte plaatjes van de pagina. Iconen en poppetjes zijn plaatjes.
- Tekstvakken nooit laten krimpen en nooit voorbij de marge laten lopen; korte regels krijgen wat speling omdat fontbreedte per programma verschilt.
- Geen schaduwen (het standaardthema zet ze anders onder elk vlak).
- Paginanummer rechtsonder, logo instelling linksonder.
- Werkt het best in Canva; daar zitten League Spartan en Inter standaard in.
