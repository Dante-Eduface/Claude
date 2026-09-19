# Usability test Eduface

Feedbacklog op het platform. Bron: `data.json`, render: `build.py` → `artifact.html` → gepubliceerd als Artifact.

## Kleurcodes (onderdeel waar de bevinding speelt)
- Grading tab, blauw
- Feedback tab, paars
- Signup flow, amber
- Manage rubric, teal
- Algemeen, grijs
- Bugs, rood, eigen sectie zonder scores

## Feedback toevoegen
In `data.json`, onder het criterium waar het bij hoort:

```json
{ "tab": "grading",
  "tekst": "...",
  "bron": "Todoist: ...",
  "afbeeldingen": [{ "pad": "afbeeldingen/naam.png", "bijschrift": "..." }] }
```

Bugs staan in de losse `"bugs"` lijst onderaan `data.json`.
Daarna `python3 build.py` en de Artifact opnieuw publiceren op hetzelfde bestandspad.

## Afbeeldingen
Staan in `afbeeldingen/`, verkleind naar max 1400px breed. Klik in de Artifact op een screenshot
om hem over de volle breedte te bekijken. Nieuwe beelden: zet ze in die map en verwijs ernaar in `data.json`.

| bestandsnaam | wat erop staat |
|---|---|
| signin-onverwachte-fout.png | inlogscherm met toast Onverwachte fout |
| processing-submissions-paneel.png | Processing submissions paneel over assessment setup |
| taal-dropdown-over-tabs.png | taalmenu over de Grading/Feedback tabs |
| feedbacktab-regenerate.png | Feedback tab, Regenerate in Describe your feedback style |
| criterion-vakje-open.png | rubric criterium klapt over volle breedte open |
| extra-criterium-0-procent.png | toegevoegd criterium op 0 procent |
| lemlist-stap-1-sequence.png | Lemlist, sequence bouwen met stappenbalk bovenin |
| lemlist-stap-2-leads.png | Lemlist, leads importeren, lege staat met een duidelijke volgende stap |

## Weggelaten
Uit het originele formulier: E (vergelijking met LMS) en F (boomer test als losse categorie).
De boomer-observatie over horizontaal scrollen zit nu onder C2.
