# Voice Samples - lever hier de echte posts aan

Deze map kalibreert de stemmen. LinkedIn is niet te scrapen vanuit de tools, dus de echte posts moeten hier handmatig in.

## Wat aanleveren
Per account 10-15 echte LinkedIn-posts (hoe meer hoe beter, ook oudere). Eén bestand per stem:
- `dante.md`
- `jeroen.md`
- `menno.md`
- `eduface.md`

## Hoe verzamelen
- **Snelst:** open je profiel -> Activity -> Posts, en copy-paste de tekst in het bestand. Eén post per blok, gescheiden door een lege regel of `---`.
- **Eigen posts compleet:** LinkedIn -> Settings & Privacy -> Data privacy -> Get a copy of your data -> "Posts" / `Shares.csv`. Plak de tekstkolom hier.
- **Via Buffer:** als posts via Buffer gingen, staat de historie daar. Exporteer/copy de teksten.

## Wat ik ermee doe
Zodra de bestanden er staan, analyseer ik per stem (zinslengte, openingen, jargon, emoji, formatting, NL/EN, hoe scherp) en vul de "Style markers (geijkt)" in `../voice-profiles.md`. Daarna schrijft de skill in de echte stem i.p.v. het provisionele profiel.

Geen gevoelige info nodig, alleen de publieke post-teksten.
