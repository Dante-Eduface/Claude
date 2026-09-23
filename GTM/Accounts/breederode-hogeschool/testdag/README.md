# Testochtend 23-09-2026

Wat er geprint wordt voor de testochtend bij Breederode Hogeschool, Posthumalaan 120 Rotterdam, 09:00 tot 12:30.

## Wat hier staat

| Bestand | Wat het is |
|---|---|
| `mapje-manuele-therapie.pdf` | **Dit is wat er geprint wordt.** 7 doorlopend genummerde A4: voorblad, vier bladen dossier, twee beoordelingsformulieren. |
| `mapje-manuele-therapie-overzicht.png` | Alle zeven bladen naast elkaar, om te zien wat je in handen krijgt. |
| `beoordelingsformulier-testochtend.pdf` | Het losse standaardblad, voor wie geen mapje krijgt. 1 A4. |
| `vakdossier-manuele-therapie.pdf` | Alleen het dossier, 4 A4, zonder voorblad en formulieren. Zit ook in het mapje. |
| `bouw-map.py` | Zet een dossier plus het standaardblad om in een genummerd mapje. Regelt ook de beoordelingsoptie op het voorblad. |
| `*.html` en `*.css` | De bron. Renderen met headless Chromium, zie hieronder. |

## De beoordelingsoptie per vak

Staat op het voorblad van elk mapje, in het Nederlands.

| Vak | Optie | Waarom |
|---|---|---|
| MSc Manuele Therapie | voldaan of niet voldaan | de rubriek kent zelf ook twee standen, dus geen uitleg nodig |
| Master Kinderfysiotherapie | voldaan of niet voldaan | idem |
| POH-6 Huisartsenzorg | onvoldoende, voldoende, goed of uitstekend | de rubriek onderscheidt kwaliteitsniveaus, een vinkje zou dat weggooien. Let op: de tool kent vier niveaus, de rubriek stopt bij goed. |

## De oplage

Per vak, nooit als totaal. P is het aantal mensen bij dat vak, S het aantal studenten van wie werk beoordeeld is.

- mapjes: P, plus 1 reserve
- bladen per mapje: 1 + (S x 4) + aantal andere vakken
- studentenopdrachten los: P x S

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
