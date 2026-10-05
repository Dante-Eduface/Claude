# Leerpunten blog-writer

Append-only. Elke opmerking van Dante op een blog komt hier, ook als er nog geen regel uit volgt. De skill leest dit bestand voordat hij schrijft.

Format: `[JJJJ-MM-DD] blog (slug): wat er mis was | welke stap | wat ermee gedaan is`

## Feedback die werkt

"Deze blog is niet goed" kan de skill niets mee. Wijs de stap aan:

| Stap | Wat er dan mis is | Voorbeeld |
|---|---|---|
| **Hoek** | verkeerde vraag of verkeerde lezer | "dit is voor docenten, het moet voor de learning technologist" |
| **Opbouw** | koppen, volgorde, wat ontbreekt | "de setup hoort vóór de compliance" |
| **Claim** | iets over Eduface of een bron klopt niet | "dat doen we niet zo, de docent kiest dat zelf" |
| **Stem** | klinkt verkeerd | "te stijf", "klinkt als AI", "te verkoperig" |
| **Zin** | één specifieke formulering | "deze zin mag weg" |

Een losse zin-correctie blijft hier staan. Twee keer dezelfde soort opmerking wordt een voorstel voor `stijl.md`, met de tekst erbij.

## Punten

[2026-09-25] algemeen: Dante vindt dat vooral de langere blogs goed werken, "vaak ook met een aantal afbeeldingen en visuele elementen" | lengte en opbouw | toegepast op de batch van 8 (law, health, business): lang, met figuren, flowdiagrammen, tabellen en callouts. Nog geen regel; bij een tweede keer voorstellen om de lengterichting in `artikeltypes.md` op te hogen.

[2026-09-25] algemeen: Dante: "neem het op in de skill" | lengte en opbouw | **regel geworden.** Lengterichting opgehoogd en minimum aan visuele elementen vastgelegd in `artikeltypes.md` ("Lengte en visuele elementen"), plus een regel in `SKILL.md` stap 5 en zelfcheck C.

[2026-09-28] Graide/KEATH-vergelijking: Dante: "do not backlink to Graide or keath" | claim/bronnen | geen links naar graide.co.uk of keath.ai in de tekst of de References; bron wel bij naam en datum noemen. Geldt voor deze twee concurrenten; bij een volgende concurrent navragen of het breder geldt.

[2026-10-05] onderwerpkeuze (10 voorstellen voor for-profit HE): Dante: "make sure that the terms that come out are actually being searched for, this seems to be too random or specific [...] focus on keywords, grading hours and instructor retention is never something someone is going to search for." | brief (zoekvraag) | onderwerpen opnieuw gekozen op Google-autocomplete (wat mensen echt typen) plus Google Trends (relatief volume, US). Pijn uit Close is een hoek binnen een blog, geen zoekterm. Resultaat in `GTM/Campaigns/blog-launch/zoekwoorden-2026-10-05.md`. Nog geen regel; bij een tweede keer voorstellen om in stap 1 een verplichte zoekvraag-check (autocomplete + Trends) op te nemen.
