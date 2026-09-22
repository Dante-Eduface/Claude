# Beoordelingsformulieren

Lege beoordelingsformulieren om het AI-nakijken mee te voeden of te demonstreren: de criteria staan erin, de oordelen niet.

**Fase:** eerste formulier staat er (CAT diagnostiek, 22-09-2026).
**Volgende stap:** afwachten of Dante er een prognostiek- of interventievariant bij wil. Die hebben andere criteria en dus een eigen bronbestand.

| Bestand | Wat het is |
|---|---|
| `criteria-cat-diagnostiek.md` | de bron: de 25 criteria in 8 secties, letterlijk uit het ingevulde formulier van 9-12-2025 |
| `build.py` | maakt uit die bron het lege formulier, pdf plus docx |
| `beoordelingsformulier-cat-diagnostiek.pdf` | de oplevering |
| `beoordelingsformulier-cat-diagnostiek.docx` | dezelfde inhoud, bewerkbaar in Word |

Criterium aanpassen doe je in de `.md` en daarna `python3 build.py`. Niet in de pdf of de docx zelf, die worden overschreven.

De pdf komt uit headless Chromium, niet uit LibreOffice: deze omgeving heeft alleen libreoffice-core zonder Writer, dus docx naar pdf converteren gaat er niet.
