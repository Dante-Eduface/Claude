# SURF 2026 demo

_Aangemaakt 2026-11-10._ Opdrachten, beoordelingsformulieren en inzendingen voor de Eduface-demo op SURF 2026. Vier courses (MBO, HBO, WO, WO English), elk met dezelfde 7 opdrachten; alleen de moeilijkheid verschilt per niveau. Engels alleen op WO.

**Fase:** alle 28 opdrachten klaar en op 10-11-2026 in de Drive-map SURF 2026 gezet (per course een map, per opdracht een map met de Eduface-titel).
**Volgende stap:** Dante test in Eduface en geeft feedback per opdracht.

Per opdrachtnummer is de student op alle niveaus dezelfde (alleen een voornaam): 1 Lisa, 2 Daan, 3 Emma, 4 Sem, 5 Sophie, 6 Tim, 7 Noor. Eduface krijgt alleen de inzending en het beoordelingsformulier (of correctiemodel); formulieren hebben geen percentages en geen stijlregel. De bewuste fouten staan in `spiekbriefje.md`.

| Map | Wat |
|---|---|
| `opdrachten/` | bron per opdracht en niveau (`inzending.md`, `beoordelingsformulier.md`) plus `build.py` |
| `tentamens/` | bron per niveau (`mbo.py`, `hbo.py`, `wo.py`, `wo_en.py`) plus `build.py` |
| `uitvoer/<course>/<opdracht>/` | wat in Eduface gaat: tentamen, correctiemodel, inzending, als docx en pdf |

Aanpassen doe je in de bron, daarna `python3 tentamens/build.py`. Het script controleert dat de criteria per vraag optellen tot het aantal punten van de vraag.

Per bronbestand staan onder `fouten` de bewuste fouten in de inzending en onder `verwacht` de score die een goede beoordeling zou geven.
