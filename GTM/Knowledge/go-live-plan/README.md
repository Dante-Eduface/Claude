# Go-Live Plan

Klantgericht, levend document voor de closing-fase. Vervangt het interne close plan.
Terminologie: geen "pilot", wel **proof of value** (4 weken standaard).

## Bestanden

- `go-live-plan-template.html` — bron van het template. Aanpassen doe je hier, daarna opnieuw
  uploaden naar Drive als Google Doc (conversie vanuit HTML behoudt tabellen en celkleuren).
- `proef.html` — de losse proef uit poort 2, het patroon dat de rest volgt.

## Google Doc

`Go Live Plan — TEMPLATE (EN)` in Drive:
https://docs.google.com/document/d/1oWPEqZcd1hIqkM64w1cE1ouu5tw0KnEfT7OPq-bu_1A/edit

Per deal: maak een kopie, hernoem naar `[Klant] Go Live Plan`, zet hun logo erbij.

## Design

Volgt `Design/Design system/core/` plus de bodyschaal van `web/`, de afleiding die de
README van het design system zelf als voorbeeld geeft voor een go-live-document.

- Opbouw: het waarom eerst, dan pas het plan.
- Alle kleuren komen uit `core/tokens.css`. Voeg geen losse waarden toe.
- Statuskolom toont alleen afwijking: afgerond krijgt een vinkje, de lopende stap krijgt
  nadruk, toekomstige stappen blijven leeg. Rood alleen als een datum echt verstreken is.
- Groeperen met ruimte en haarlijnen, geen gevulde balken of zebrastrepen.
- Zwart-wit printbaar: elke status heeft een woord naast de kleur.
