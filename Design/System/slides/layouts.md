# Slide-layouts

Canvas is vast **1920x1080**. Veilige marge 120px, daarbuiten komt niks. Ontwerp in px, niet in rem.

## De regel die alles bepaalt
**Eén idee per slide.** Heb je twee ideeën, dan heb je twee slides. Een slide is geen document: wat je zegt staat niet op het scherm, alleen waar de kijker naar moet kijken.

Tweede regel: **32px is de ondergrens** voor tekst die iemand moet kunnen lezen. Kan het niet op 32px, dan staat er te veel op.

## De vaste soorten

**1. Opening**
Navy vlak, witte tekst. Titel op `slide-hero`, daaronder één regel context op `slide-sub` in `foreground-inverse-soft`. Logo linksonder. Verder niks.

**2. Statement**
Eén zin op `slide-hero`, verticaal gecentreerd, veel lucht. Voor het moment waarop je wilt dat mensen stoppen met meelezen en luisteren. Wit of navy, wissel af met de slides eromheen.

**3. Kop + inhoud**
Kop op `slide-title` bovenaan, inhoud eronder. De standaardslide. Kop is een bewering, geen label: "Nakijken kost 40% van de contacturen", niet "Nakijken".

**4. Drie kolommen**
Max 3 naast elkaar, gat 48px. Per kolom: kopje op `slide-sub`, twee regels op `slide-body`. Meer dan drie kolommen wordt onleesbaar op afstand.

**5. Eén groot cijfer**
Cijfer op `slide-stat` (180px) in navy of groen, eronder één regel uitleg op `slide-sub` en de bron op `slide-caption` in `muted`. Dit is de slide waar mensen een foto van maken.

**6. Grafiek**
Grafiek links of vol, kop erboven op `slide-title`, aslabels op `slide-caption`. Maximaal 2 kleuren: navy voor de hoofdreeks, groen voor waar het over gaat. De rest grijs.

**7. Quote**
Citaat op `slide-sub`, naam plus functie op `slide-caption`. Geen aanhalingstekens-illustraties, geen ronde fotolijstjes.

**8. Afsluiting**
Navy, één vraag of één actie, contactgegevens op `slide-caption`. Nooit "Bedankt voor uw aandacht".

## Kleurritme
Wissel af: wit, wit, navy, wit. Een navy slide markeert een overgang of een statement. Zet er nooit twee achter elkaar tenzij je een blok wilt afbakenen.

## Bronnen
Elke claim en elk cijfer krijgt zijn bron op de slide zelf, op `slide-caption` in `muted`, niet in een bronnenlijst aan het eind. Je moet "waar komt dat vandaan?" kunnen beantwoorden zonder door te klikken.
