# SURF 2026 demo

_Aangemaakt 2026-11-10._ Opdrachten, beoordelingsformulieren en inzendingen voor de Eduface-demo op SURF 2026. Vier courses (MBO, HBO, WO, WO English), elk met dezelfde 7 opdrachten; alleen de moeilijkheid verschilt per niveau. Engels alleen op WO.

**Fase:** ronde 1 klaar, de tentamens (opdracht 7) op alle vier de niveaus.
**Volgende stap:** Dante test de tentamens in Eduface en geeft feedback; daarna opdrachten 1 tot en met 6. Pas aan het einde alles in de Drive-map SURF 2026 zetten.

| Map | Wat |
|---|---|
| `tentamens/` | bron per niveau (`mbo.py`, `hbo.py`, `wo.py`, `wo_en.py`) plus `build.py` |
| `uitvoer/<course>/<opdracht>/` | wat in Eduface gaat: tentamen, correctiemodel, inzending, als docx en pdf |

Aanpassen doe je in de bron, daarna `python3 tentamens/build.py`. Het script controleert dat de criteria per vraag optellen tot het aantal punten van de vraag.

Per bronbestand staan onder `fouten` de bewuste fouten in de inzending en onder `verwacht` de score die een goede beoordeling zou geven.
