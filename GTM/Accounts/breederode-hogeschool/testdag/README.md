# Testochtend 23-09-2026

Wat er geprint wordt voor de testochtend bij Breederode Hogeschool, Posthumalaan 120 Rotterdam, 09:00 tot 12:30.

## Wat hier staat

| Bestand | Wat het is |
|---|---|
| `beoordelingsformulier-testochtend.pdf` | Het standaardblad. 1 A4, identiek voor iedereen, met bovenaan een vinkje voor welke opdracht het blad gaat. |
| `vakdossier-manuele-therapie.pdf` | 3 A4. Het oordeel van Marloes de Graaf naast dat van Eduface, met de verschillen eruit gelicht. |
| `*.html` en `*.css` | De bron. Renderen met headless Chromium, zie hieronder. |

## De drie groepen

Iedereen hoort bij precies een vak en krijgt het dossier van zijn eigen vak, plus het standaardblad voor de twee andere opdrachten.

| Vak | Wie | Wiens beoordeling ligt naast Eduface |
|---|---|---|
| MSc Manuele Therapie | Marloes de Graaf, Jochem van Schalkwijk | Marloes, twee ingevulde formulieren |
| Master Kinderfysiotherapie | Ivonne Duiser, Sanne Toonen-Zwinkels, Carina Wind | Ivonne, twee ingevulde feedbackformulieren |
| POH-6 Huisartsenzorg | Marina Vinken-Hol, Selma de Nijs, Kas van Kruining | Kas, twee ingevulde beoordelingen met cijfer |

Irma van der Velden hoort bij geen vak. Marlies van Hell (hbo-v) doet deze ronde niet mee.

## Wat er nog niet is

- **Vakdossier Kinderfysiotherapie en POH-6.** Daarvoor is de Eduface-output nodig, die er op 23-09 nog niet was. Die twee vakken gaan met het standaardblad.
- **Het echte Breederode-logo.** Wat er nu staat is een benadering in hun kleur, geen origineel bestand.

## Opnieuw renderen

```
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
$CH --headless --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=blad.pdf blad.html
```

Fonts zijn lokaal ingesloten (Inter als TTF), want Google Fonts is vanuit de renderomgeving niet bereikbaar.
