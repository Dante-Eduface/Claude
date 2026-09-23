# Beoordelingsformulieren

Lege beoordelingsformulieren om het AI-nakijken mee te voeden of te demonstreren: de criteria staan erin, de oordelen niet.

**Fase:** twee formulieren, beide uit een aangeleverd ingevuld exemplaar (23-09-2026).
**Volgende stap:** afwachten welk formulier Dante hierna aanlevert. Elk formulier krijgt een eigen criteria-bestand plus een regel in `FORMULIEREN` in `build.py`.

| Formulier | Bron | Oordeelkolom |
|---|---|---|
| `beoordelingsformulier-cat-diagnostiek` | ingevuld exemplaar van 9-12-2025, manueeltherapie | Voldaan / Niet voldaan per criterium |
| `beoordelingsformulier-cat-mkf` | CAT MKF handleiding en feedbackformulier, Breederode Hogeschool, toetscode MKF26-WO1-CAT-1-5 | Feedback per criterium, eindoordeel onderaan |

Die twee verschillen niet omdat het mooier stond, maar omdat de bronnen verschillen: de eerste vinkt per criterium af, de tweede schrijft per criterium feedback en beoordeelt de CAT als geheel met voldaan of niet voldaan.

| Bestand | Wat het is |
|---|---|
| `criteria-*.md` | de bron per formulier: secties met daaronder de criteria, plus wat er met de brontekst is gedaan |
| `build.py` | maakt uit elk criteria-bestand de pdf en de docx |
| `beoordelingsformulier-*.pdf` | de oplevering |
| `beoordelingsformulier-*.docx` | dezelfde inhoud, bewerkbaar in Word |

Criterium aanpassen doe je in de `.md` en daarna `python3 build.py`. Niet in de pdf of de docx zelf, die worden overschreven.

De pdf komt uit headless Chromium, niet uit LibreOffice: deze omgeving heeft alleen libreoffice-core zonder Writer, dus docx naar pdf converteren gaat er niet.
