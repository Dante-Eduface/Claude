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

### 2026-09-25 · demoscript · correctie
Voorleesscript voor de UTI-demovideo: "het enige wat erin hoeft te staan is de tekst die ik
daadwerkelijk zeg." Kliks mogen blijven, bronnen en uitleg eruit. Toegepast op
`GTM/Accounts/uti/uti-demo-video-script.md`.
Tweede ronde, zelfde dag: de toon paste niet (kort en hakkelig, veel pijn), geen uitleg over
het lab, Roberts team niet noemen, niet op de pijn ingaan. Herschreven in zijn eigen woorden,
getoetst aan `.claude/skills/linkedin-content/voice-profiles.md`. De regel tegen hakkelige
zinnen stond al in de schrijfskill; die was niet gevolgd.

### 2026-09-25 · voorleesscript · patroon
Tweede keer dat Dante niet-gesproken tekst uit het demoscript haalt: eerst de bronnen, daarna
de klikstappen. In zijn woorden: "het enige wat erin hoeft te staan is de tekst die ik
daadwerkelijk zeg." Regel voorgesteld voor `.claude/skills/schrijven/voice-by-type.md`,
wacht op akkoord.
