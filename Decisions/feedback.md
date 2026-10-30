# Feedback

Losse opmerkingen van Dante, met datum en onderwerp. Hier houd ik bij wanneer iets
een patroon wordt.

**De regel** (`.claude/rules/feedback.md`): één opmerking is een correctie, twee keer
hetzelfde is een patroon, en pas na Dante's akkoord wordt het een regel — met de tekst
vooraf voorgelegd. Nooit een aanname invullen die je kunt navragen, nooit een regel
breder maken dan de feedback was, nooit stilletjes een skill wijzigen.

**Hoe te lezen:** status `correctie` is eenmalig, `patroon` is twee keer of vaker gezien
en wacht op akkoord, `regel` staat vastgelegd in `.claude/rules/` of in een skill.

Feedback op een tekst gaat niet hierheen maar naar `.claude/skills/schrijven/feedback-log.md`,
want die is gescheiden per content-type. Feedback op een SHIFT-agent gaat naar de
`LEERPUNTEN.md` van die agent.

---

## 2026

### 2026-09-19 · mappenstructuur · patroon
Bestandsnamen, opslagplek en duplicaten waren het grootste probleem: "ik weet niet wat waar
staat, wat waaruit leest, of welke skills ik heb." Geleid tot de herindeling van 19-09 en
tot `Context/kaart.md`. Volgende keer: een nieuwe map krijgt meteen een `README.md` en een
regel in de kaart, anders groeit dit terug.

### 2026-09-19 · naamgeving · regel
Spaties en hoofdletters mogen in mapnamen die een mens leest, mits kort en duidelijk.
Kleine letters met streepjes blijven verplicht onder `.claude/` en in `GTM/ICP/shift/master/`,
omdat commando's en scripts daarvan afhangen. Vastgelegd in `Context/kaart.md`.

### 2026-09-19 · skills · correctie
Overlappende skills samenvoegen in plaats van naast elkaar laten staan. `cro`, `schrijven`,
`outreach` en `meddpicc` slikten hun dubbelganger op. `sso-grid` bleef apart omdat de
scheiding met de scoringsskill met opzet is gebouwd.

### 2026-10-30 · folder SURF Onderwijsdagen · correctie
Bewijs moet de hook dekken: de 94% meet voorstel tegen docent, niet docent tegen docent, dus
consistentie onderbouwen met het mechanisme (zelfde rubric, cijferopbouw per criterium). Op
rustig gelezen materiaal het puntenverschil, niet de kale 94%. Geen "fractie van de tijd" zonder
nulmeting. Resultaten en klanten visueel gescheiden. Claims zonder bron eruit, niet "tot het
bevestigd is". Bath Spa noemen is een toestemmingsvraag voor Dante. Toegepast in
`GTM/Campaigns/folder-nl/inhoud.md`.
