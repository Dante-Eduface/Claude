# Folder NL

Gevouwen A4-folder (liggend, dubbelgevouwen tot A5) voor Nederlandse instellingen.

- `folder-v1.pdf`: de oorspronkelijke versie.
- `folder-v2.html`: de bron van de nieuwe versie. Zelfde tekst als v1, nieuwe vormgeving in de beeldtaal van de whitepaper (kaarten, icoontegels, onder elkaar).
- `folder-v2.pdf`: de drukversie. Pagina 1 is de buitenkant (achterkant links, voorkant rechts), pagina 2 de binnenkant.
- `voor-na-*.png`: vergelijking v1 en v2.

- `folder-v3.html` / `folder-v3.pdf`: de huidige versie (30-10-2026). Kleurritme wit, navy, wit, navy in leesvolgorde: voorkant wit, binnen links navy (eigen model), binnen rechts wit, achterkant navy (cijferopbouw, logo's, contact).

- `folder-v4.html` / `folder-v4.pdf`: binnenkant herzien (30-10-2026). Links: geen ChatGPT/Gemini/Claude (logo's uit simple-icons, `logos-ai/`), waarop het model getraind is, 250.000. Rechts: Paper Grader en Exam Grader als hoofdzaak, dan explainability en auditability, vakgebieden als grijze voetregel.

- `folder-v5.html` / `folder-v5.pdf`: linkerbinnenpagina herzien (30-10-2026). Kop rustig "Eigen model", trainingsbronnen in volgorde van belang (docenten beoordelen > publicaties > feedbackvoorbeelden), het Eduface-model als witte kaart met netwerkicoon. Logo en Leiden/Radboud-regel eruit.
- `pptx/eigen-model-v4-bewerkbaar.pptx` en `pptx/eigen-model-v5-bewerkbaar.pptx`: de 'Eigen model'-pagina uit v4 en v5 als bewerkbare pptx (A5 staand). Opnieuw bouwen: `node pptx/extract.js folder-vX.html pptx/assets-vX` en `python3 pptx/build_pptx.py pptx/assets-vX pptx/<naam>.pptx`. De eerste losse versie staat in `Archive/folder-nl-pptx-2026-10/`.

Fase: v5 ter review bij Dante. Nog in te vullen: QR-link, en de echte logo's voor instellingen, LMS'en (ChatGPT/Gemini/Claude staan er sinds v4 echt in).
