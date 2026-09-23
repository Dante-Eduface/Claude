# Leerpunten testdag-digitaal

Lees dit voordat je begint. Elk vak en elke testdag levert iets op dat de volgende scherper maakt.

Format per punt: datum, wat er gebeurde, wat er verandert. Feedback die een stap aanwijst is te
verwerken, feedback op het eindresultaat niet. Wijst Dante geen stap aan, vraag het dan in één regel.

| Stap | Waar het over gaat |
|---|---|
| 1 | materiaal uitlezen |
| 2 | criteria koppelen |
| 3 | het verschil vaststellen |
| 4 | de aanname zoeken |
| 5 | controleren |
| 6 | de vragen schrijven |
| 7 | het bestand bouwen |
| 7b | verspreiding |
| 7d | papier en de vangst |
| 8 | terug naar het model |

## 23-09-2026, bij het opzetten

**Stap 7, fonts.** Een bestand dat offline moet openen kan geen Google Fonts laden. De twee
merkfonts staan als woff2 in `sjabloon/fonts/` en gaan als base64 het bestand in. Samen 72 KB, het
hele dossier komt daarmee op ongeveer 130 KB. Haal die fonts er niet uit om het bestand kleiner te
maken: zonder fonts valt het terug op de systeemfont en ziet het er niet meer uit als Eduface.

**Stap 7b, mail werkt niet.** Een los `.html`-bestand als bijlage wordt door veel mailservers
geblokkeerd. USB-stick eerst, Drive-link als reserve.

**Stap 7d, één vangkanaal.** De verleiding is om ook invulvelden op het scherm te zetten. Niet doen.
Wie typt en wie schrijft levert twee halve oogsten op. Papier is de standaard, het scherm is om te
lezen.

**Stap 3, de tussenstand.** Een beoordelingsformulier met losse vinkjes binnen een criterium kent
een stand die het model niet heeft ("deels voldaan"). Die hoort in `rangorde` tussen de andere in,
en niet weggerond naar voldaan of niet voldaan. Bij CAT diagnostiek zat daar een van de twee
"model milder"-gevallen.

**Stap 5, ontbrekende output is een bevinding.** Bij CAT diagnostiek was er voor vier criteria van
student 2 geen uitkomst van het model. Die staan als `onbekend` in de tabel, tellen niet mee in de
kalibratiescore, en zijn een vraag geworden. Niet invullen, niet weglaten.
