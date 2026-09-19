# Gaten: opleiders die hun contact kwijt zijn

Een **gat** is een gekwalificeerde organisatie waar geen bruikbaar contact meer aan hangt. Dat gebeurt als agent 3 tijdens het onderzoek ontdekt dat de aangewezen persoon toch niet klopt (vertrokken, verkeerde laag, geen mandaat) en agent 2 daarna geen vervanger vindt.

Zo'n gat mag niet stilletjes blijven staan: de organisatie is gekwalificeerd werk dat anders uit de pijplijn valt.

## De volgorde

1. **Agent 3** (`shift-research`) merkt het op, stopt het onderzoek, en roept **agent 2** aan voor die ene organisatie.
2. **Agent 2** (`contact-sourcing-nl`) zet de persoon op `rol=afgevallen` met reden en zoekt een vervanger via de ladder.
   - Gevonden → nieuwe `aangewezen`, klaar. Geen regel in dit bestand.
   - Niet gevonden → agent 2 zet één regel hieronder en zet `contact_zoekpoging` op de organisatie.
3. **Agent 1** (`lead-sourcing-nl`) leest dit bestand aan het begin van **zijn volgende batch** en zoekt per open regel één extra opleider erbij, zodat de pijplijn op peil blijft.

**Agent 1 start hier nooit een aparte ronde voor.** Gaten worden alleen meegenomen in een batch die toch al draait. Eén open gat is geen reden om agent 1 te laten lopen; dat kost onnodig credits.

## Openstaande gaten

| Datum | org_id | Organisatie | Categorie | Waarom het gat viel | Status |
|---|---|---|---|---|---|

Status is `open` of `gevuld <datum> door <naam nieuwe opleider>`. Regels blijven staan als ze gevuld zijn, ze verdwijnen niet.

_2026-08-18 (Agent 1): geen open gaten bij aanvang van de ronde van 18-08, dus niets extra opgevuld. De +30 uit die ronde zijn gewone aanvulling, geen gatvulling._

_2026-09-02 (Agent 1): geen open gaten bij aanvang van de groepen-ronde, dus niets extra opgevuld. De +31 rijen uit die ronde zijn merken onder uitgeklapte moeders, geen gatvulling._

_2026-09-02 (Agent 1): geen open gaten bij aanvang van de omvang-ronde HO/postacademisch, dus niets extra opgevuld. Hogeschool Tio is deze ronde toegevoegd maar staat op geblokkeerd (actieve Close-lead), dus die telt niet als gatvulling._

_2026-09-02 (Agent 1): geen open gaten bij aanvang van de omzet-/eigendomsronde, dus niets extra opgevuld. De +23 rijen uit die ronde zijn merken onder uitgeklapte investeerders en moeders, geen gatvulling._

_2026-09-02 (Agent 1, lane bedrijvenkant/SBI): geen open gaten bij aanvang, dus niets extra opgevuld. De 4 nieuwe rijen plus 2 upgrades uit die ronde zijn gewone aanvulling, geen gatvulling._
