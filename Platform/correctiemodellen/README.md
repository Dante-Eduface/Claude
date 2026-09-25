# Correctiemodellen

Correctiemodellen (answer keys) als pdf die Eduface goed kan uitlezen: per vraag de letterlijke vraag aan de student plus het modelantwoord, verder niets.

**Fase:** eerste model, ISU-18 t/m ISU-20 uit een aangeleverde Cengage answer guide (25-09-2026).
**Volgende stap:** afwachten welk model Dante hierna aanlevert.

| Bestand | Wat het is |
|---|---|
| `correctiemodel-*.md` | de bron: `## Exercise` per opgave, per vraag een `Q:`- en `A:`-regel |
| `build.py` | maakt van elk `.md` de pdf (headless Chromium) |
| `correctiemodel-*.pdf` | de oplevering |

Vragen en antwoorden letterlijk overnemen uit de bron, niets aanvullen. Aanpassen in de `.md`, daarna `python3 build.py`.
