# Correctiemodellen

Correctiemodellen (answer keys) als pdf die Eduface goed kan uitlezen: per vraag de letterlijke vraag aan de student plus het modelantwoord, verder niets.

**Fase:** drie modellen, ISU-19, RSC-7 en HCC-1, elk uit de Cengage answer guide plus het labblad (25-09-2026). De eerste versie met ISU-18 t/m 20 staat in `Archive/correctiemodellen-2026-09/`.
**Volgende stap:** afwachten welk model Dante hierna aanlevert.

| Bestand | Wat het is |
|---|---|
| `correctiemodel-*.md` | de bron: `## Exercise` per opgave, `## Context` met labels, per vraag een `Q (nr):`-, `A:`- en optioneel `O:`- (meerkeuze), `|`- (tabel) en `N:`-regel |
| `build.py` | maakt van elk `.md` de pdf (headless Chromium) |
| `correctiemodel-*.pdf` | de oplevering |

Vragen en antwoorden letterlijk overnemen uit de bron, niets aanvullen. Aanpassen in de `.md`, daarna `python3 build.py`.

Ook de vragen van het labblad zelf (summary statement, invulstappen) gaan erin, want die beantwoordt de student ook. Staat het antwoord niet in de officiële key, dan wordt het alleen uit de key en het labblad samengesteld, met een `N:`-regel die dat zegt.
