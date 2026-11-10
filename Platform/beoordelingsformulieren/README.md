# Beoordelingsformulieren

Lege beoordelingsformulieren om het AI-nakijken mee te voeden of te demonstreren: de criteria staan erin, de oordelen niet.

**Fase:** zes formulieren (bijgewerkt 10-11-2026). Twee uit een aangeleverd ingevuld exemplaar (23-09-2026), twee zelf opgesteld als oefenformulier uit één bron (05-11-2026), om in Eduface te vergelijken of uitgeschreven Voldoende/Onvoldoende-teksten beter werken dan alleen criteria.
**Volgende stap:** afwachten welk formulier Dante hierna aanlevert. Elk formulier krijgt een eigen criteria-bestand plus een regel in `FORMULIEREN` in `build.py`.

| Formulier | Bron | Oordeelkolom |
|---|---|---|
| `beoordelingsformulier-cat-diagnostiek` | ingevuld exemplaar van 9-12-2025, manueeltherapie | Voldaan / Niet voldaan per criterium |
| `beoordelingsformulier-cat-mkf` | CAT MKF handleiding en feedbackformulier, Breederode Hogeschool, toetscode MKF26-WO1-CAT-1-5 | Feedback per criterium, eindoordeel onderaan |
| `beoordelingsformulier-ma-earn-out` | zelf opgesteld oefenformulier (05-11-2026): economie-essay over een overname door KPN met earn-out, grafiek en MEDDPICC, gewicht per sectie | Lege kolom Voldoende / Onvoldoende per criterium |
| `beoordelingsformulier-ma-earn-out-beschreven` | zelfde bron (`criteria-ma-earn-out.md`), liggend | Per criterium uitgeschreven wanneer het Voldoende en wanneer het Onvoldoende is |
| `beoordelingsformulier-ma-earn-out-simpel` (+ `-beschreven`) | simpele versie (10-11-2026): opdracht van 3 kantjes, zelfde casus zonder waarderingsmethodes en disconteringsvoet, bron `criteria-ma-earn-out-simpel.md` | Lege kolom, of per criterium uitgeschreven Voldoende/Onvoldoende |

Die twee verschillen niet omdat het mooier stond, maar omdat de bronnen verschillen: de eerste vinkt per criterium af, de tweede schrijft per criterium feedback en beoordeelt de CAT als geheel met voldaan of niet voldaan.

| Bestand | Wat het is |
|---|---|
| `criteria-*.md` | de bron per formulier: secties met daaronder de criteria, plus wat er met de brontekst is gedaan |
| `build.py` | maakt uit elk criteria-bestand de pdf en de docx |
| `beoordelingsformulier-*.pdf` | de oplevering |
| `beoordelingsformulier-*.docx` | dezelfde inhoud, bewerkbaar in Word |
| `voorbeeld-inzendingen/` | fictieve studentenpapers om een formulier mee te testen in Eduface. De `.docx` is uploadklaar, de `.md` is de bron met bovenaan de fictief-melding en de bewuste fouten. `maak_figuur.py` maakt de grafiek, inclusief de bewuste fout (doel 2027 op 24,0 in plaats van 22,0) |

Criterium aanpassen doe je in de `.md` en daarna `python3 build.py`. Niet in de pdf of de docx zelf, die worden overschreven.

De pdf komt uit headless Chromium, niet uit LibreOffice: deze omgeving heeft alleen libreoffice-core zonder Writer, dus docx naar pdf converteren gaat er niet.
