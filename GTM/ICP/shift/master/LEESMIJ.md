# Het master-document

Alles van de SHIFT-opleiderspijplijn staat in deze map, voor alle markten tegelijk.

## De markt is een variabele (sinds 10-09-2026)

Eén master, één `pipeline.py`, en per markt een profiel in `GTM/ICP/shift/markets/<code>/`:

- `profiel.json`: de harde waarden waar het script mee rekent (valuta, staffel, drempel, titelrangorde, kanaal, taal, klantnamen, Lemlist-campagne). Valuta is alleen EUR, GBP of USD.
- `profiel.md`: veertien koppen met de kennis die de agents lezen (registers, toezicht, poort-0-afvallers, vocabulaire, student-signaal, doorlooptijdnorm, vaktermen, programmaduur, prijsmodel, titelrangorde, taal, klantnamen, kanaal, seizoen).
- `WERKVOORRAAD.md` en `GATEN.md`: de stand van agent 1 en de gaten, per markt.

Elke organisatie heeft een `markt`; personen erven die van hun organisatie. `queue`, `status`, `orgs`, `omvang`, `export` en `uitkomsten` kijken alleen naar de actieve markt. `exists`, `show`, `set`, `dossier` en `history` werken over markten heen, want een concern als Kaplan of Navitas zit in meer dan één markt en mag niet dubbel benaderd worden.

```
pipeline.py markt                       alle markten en of hun profiel compleet is
pipeline.py markt --nieuw us            lege markt met alle veertien slots leeg
pipeline.py --markt uk doctor           welke slots missen er nog
pipeline.py --markt uk queue --stage 2  wachtrij van die markt; weigert op een incompleet profiel
```

Zonder `--markt` (of `SHIFT_MARKT`) is de markt `nl`, dus alles gedraagt zich als voorheen.
 Niemand schrijft er met de hand in, alles loopt via `.claude/scripts/pipeline.py`.

- `orgs.csv` — een rij per organisatie
- `people.csv` — een rij per persoon
- `journal.csv` — wie wanneer welk veld veranderde, zodat niets ongemerkt verdwijnt
- `dossiers/` — het onderzoek zelf, één markdown-bestand per persoon en per organisatie

## Stand en inhoud zijn twee dingen

De CSV's bewaren de **stand**: wie is het, waar staat hij, wat is er verstuurd. Het **dossier** bewaart de inhoud: de citaten, de bronnen, de getallen, de twijfels.

Dat onderscheid is er sinds 14-08-2026 en het lost een echt probleem op. Het onderzoek van agent 3 moest passen in vier velden (`opvallend`, `haakje`, `toetsprogramma`, `schrijfwerk`), samen zo'n 1.050 tekens per persoon, terwijl een cold-call-dossier voor dezelfde soort prospect 11 tot 18 KB is. De rest verdween, en agent 4 moest de bron dan zelf opnieuw ophalen. Bovendien maakte één `opvallend` van 3.000 tekens `queue --table` onleesbaar.

Die vier velden bestaan nog, maar zijn nu een **samenvatting van hooguit 200 tekens** voor de wachtrij. Probeer je er meer in te zetten, dan weigert het script dat en verwijst het je naar het dossier.

```
pipeline.py dossier <id>                    het hele dossier
pipeline.py dossier <id> --sectie Citaten   alleen die kop, scheelt tokens
pipeline.py dossier <id> --sjabloon         lege kopstructuur om te vullen
pipeline.py dossier <id> --schrijf -        van stdin, gaat door het journaal
```

De regels en de koppen staan in `dossiers/SJABLOON.md`. De belangrijkste: **elk citaat draagt zijn drager** (student, beoordelaar, organisatie of panel), want daar ging het bij THIM mis. `doctor` valt op een citaat zonder drager.

Het oude `GTM/ICP/shift/master/dossiers/` blijft staan als rondelogboek. De organisatiedossiers die eruit te halen waren staan nu in `dossiers/orgs/`; wat erin achterbleef zijn procesnotities en afgevallen organisaties zonder record.

## Je hoeft geen veldnamen te onthouden

```
python3 .claude/scripts/pipeline.py uitleg              alle velden en waarden
python3 .claude/scripts/pipeline.py uitleg niveau       alleen wat op "niveau" lijkt
```

Vraag het gerust gewoon in de chat ("wat betekent haakje_trap ook alweer"), dan draai ik dat commando.

## De vijf stappen

Er is geen kolom die zegt in welke stap iemand zit. Dat wordt elke keer opnieuw uitgerekend uit de data, zodat het nooit uit de pas kan lopen.

| stap | wat er moet gebeuren | wanneer val je erin |
|---|---|---|
| 2 | contact zoeken | organisatie gekwalificeerd, nog geen aangewezen persoon |
| 3 | haakje zoeken | aangewezen persoon, onderzoek nog niet gedaan |
| 3r | alleen een niveau toekennen | haakje gevonden maar nooit beoordeeld, reparatiewachtrij |
| 4 | bericht schrijven | haakje op niveau 2, 2b of 3, nog geen bericht |
| 5 | naar Lemlist | bericht goedgekeurd |

## De belangrijkste woordenlijsten

**rol** — wat iemand voor ons is binnen zijn organisatie
`aangewezen` (de een die we benaderen) · `tweede_kandidaat` (reserve als de eerste niet reageert) · `doorverwijzing` · `al_in_close` · `afgevallen` · `achtergrond`

**haakje_niveau** — hoe sterk het haakje is
`1` te zwak · `2` bruikbaar · `2b` bruikbaar met kanttekening · `3` sterk, hij zegt het zelf · `onbeoordeeld` nooit beoordeeld

**icp_status** — waar een organisatie in de kwalificatie staat
`kandidaat` · `gekwalificeerd` · `afgevallen` · `geblokkeerd` (loopt al via Close) · `te_klein` (past qua fit, maar er komt geen 10k uit; blijft staan, buiten de outreach)

**omvang_niveau** — hoe hard het omvangsgetal is
`hard` citaat van de opleider zelf · `afgeleid` zelf geteld of gerekend · `geschat` proxy zoals een medewerkersband · `onbekend` gezocht en niets gevonden

**bericht_status** — waar het bericht staat
`concept` wacht op jou · `goedgekeurd` · `afgekeurd` · `verstuurd` · `vervallen` · `gepauzeerd`

**uitkomst** — hoe het afliep
`geen_interesse` · `interesse` · `gesprek_gepland` · `doorverwezen` · `later_terugkomen` · `geen_reactie`

## Vertel me hoe een gesprek afliep

Zeg het gewoon in de chat: "Thim van der Laan zei nee, hij vond dat het over de student ging en niet over de organisatie." Dan leg ik het vast met:

```
pipeline.py uitkomst p_thim-van-der-laan-364701b --status geen_interesse \
  --reden "..." --kanaal email --datum 2026-08-13
```

Dat zet meteen `bericht_status` op vervallen, zodat die persoon niet opnieuw in een wachtrij belandt. Later terugvragen kan altijd:

```
pipeline.py uitkomsten                          alles wat er is vastgelegd
pipeline.py uitkomsten --status geen_interesse  alleen de nee's, met reden
pipeline.py history p_thim-van-der-laan-364701b elke wijziging op dat record
```

## De commando's die je zelf kunt vragen

```
pipeline.py status --doel 50     wat heb ik nodig om vandaag 50 outreach te doen
pipeline.py exists --naam "X"    zit deze persoon al ergens in de keten
pipeline.py show <id>            alles van een persoon of organisatie
pipeline.py promote <id>         tweede kandidaat wordt de aangewezen persoon
pipeline.py doctor               klopt alles nog
```

## Hoe groot is een opleider, en is dat groot genoeg

Sinds 19-08-2026 toetst agent 1 per opleider of er een deal van minstens 10.000 euro in zit (poort 0d in `icp.md`). Vier velden dragen dat: `lerenden_per_jaar`, `aantal_opleidingen`, `cursusprijs` en `omvang_medewerkers`, met `omvang_citaat` plus `omvang_url` als bewijs. `omzet_indicatie` en `geschatte_jaarwaarde` rekent het script zelf uit, die vul je nooit met de hand.

```
pipeline.py omvang --toets org_x          groot genoeg, te klein of onbekend, met de reden
pipeline.py omvang                        wie staat er op te_klein en waarom
pipeline.py omvang --aandeel 20           wie komt er terug als de prijs 20% van de omzet mag zijn
pipeline.py omvang --aandeel 20 --herzien en zet die groep terug op gekwalificeerd
```

De drempel is 10.000 euro jaarwaarde plus de eis dat onze prijs hoogstens 10% van de programma-omzet is. Dat tweede getal doet het werk: de prijsstaffel begint op 10.000 euro, dus iedereen met een echte opleiding haalt de eerste eis. Wat een opleider afvoert is dat 10.000 euro te veel is van wat zo'n programma omzet.

## Handmatige beslissingen

Keuzes die jij maakt en die een herhaalde migratie moeten overleven, staan bovenin `.claude/scripts/migrate-master.py` in `DANTE_KIEST`, `DANTE_DUBBEL` en `DANTE_UITKOMSTEN`. Verander je van gedachten, dan pas ik die aan en draai de migratie opnieuw.
