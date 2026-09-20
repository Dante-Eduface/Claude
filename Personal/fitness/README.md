# fitness

Prive. Krachttraining en voeding, hoort bij de skill `/fitness-coach`.

**Status:** lopend. Staat op 2.800 kcal sinds 19-09-2026. Geen WHOOP, geen InBody, geen gewichtdoel: een weging per week op zaterdagochtend is het enige signaal.

**Volgende stap:** K1, K2 en K3 in `Context/open-vragen.md` beantwoord krijgen, dan het weekmenu naar zaterdagochtend verplaatsen als K1 ja is.

## Bestanden

- `weekmenu.html` - het weekmenu van de lopende week, de enige pagina die je opent
- `menu/` - een JSON per week, dat is de bron
- `build.py` - rendert de nieuwste JSON naar `weekmenu.html`. `python3 build.py` of `python3 build.py 2026-W39`
- `calorieen.md` - waar de 2.800 vandaan komt en hoe je hem bijstelt
- `schema/` - de trainingsschema's
- `data/` - ruwe exports. `whoop/` is bevroren, hij draagt hem niet meer

Het receptenboek, de rotatieregels en de prepvolgorde staan in `.claude/skills/fitness-coach/recepten.md`.
