# LinkedIn Content

Organische LinkedIn-content in 4 stemmen (Dante, Jeroen, Menno, Eduface-pagina). De agent schrijft, Dante/de persoon keurt, posten gaat via Buffer. Aangedreven door de skill `/linkedin-content`.

## De werkbestanden (intake)
In `werkbestanden/` staan 4 self-contained HTML-bestanden, 1 per stem. Ze openen op de laptop (geen installatie), zijn voor-ingevuld uit de echte posts, en hebben een Download-knop.

Doel: Jeroen en Menno (kritisch, willen controle) zien precies op basis van welke info de agent schrijft, en kunnen alles aanpassen. Vertrouwen via transparantie + controle.

- `eduface-stem-jeroen.html`
- `eduface-stem-menno.html` (extra blok: technische feiten vergrendelen)
- `eduface-stem-dante.html`
- `eduface-stem-eduface.html` = **master**, definieert de gedeelde CTA (geldt voor alle 4)

## De flow
1. Elke persoon opent zijn bestand, leest, corrigeert (~10 min), klikt **Download ingevuld bestand** (`.md`), mailt het naar Dante.
2. Dante geeft de ingevulde `.md`'s aan de agent.
3. De agent verwerkt ze in `.claude/skills/linkedin-content/voice-profiles.md` (stem-markers bijwerken) en schrijft posts.
4. Concept naar de persoon, die keurt goed (of past aan), daarna inplannen in Buffer. Niets wordt automatisch geplaatst.

## Kernregels
- CTA is uniform over alle 4 de stemmen (master = het Eduface-bestand).
- Geen AI-tells (bold-unicode, emoji per regel, "Excited to announce", feature-dumps). Zie `voice-profiles.md`.
- Verdeling 10/10/10 over Dante/Jeroen/Menno voor de eerste 30.

## Output
Afgeschreven batches komen in deze map (bijv. `batch-01.md`), plak-klaar voor Buffer.
