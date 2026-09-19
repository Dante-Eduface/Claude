# Voorstel Google Drive

Zelfde aanpak als bij de repo: lees het door, schrijf feedback achter **Feedback:**.
Ik voer niets uit tot je akkoord geeft.

---

## 0. Eerst dit: de repo hoort niet in Drive

`Eduface/Claud AE/` is je git-repo, inclusief de map `.git`. Google Drive synchroniseert die
map bestand voor bestand mee. Git en Drive schrijven allebei naar dezelfde bestanden, en
Drive maakt bij twijfel een kopie in plaats van te wachten.

Dat gebeurt al:

- `Eduface/Claude-AE/.claude 2` — een Drive-syncconflict, geen echte map
- In de zip die je uploadde zat `.git/index 2` — hetzelfde conflict, maar dan midden in de
  git-database. Dat bestand bepaalt welke versie van elk bestand git denkt te hebben.

Zolang dit zo staat kan de repo op een willekeurig moment stukgaan, en merk je dat pas als
je iets kwijt bent. **Advies: verplaats de repo op je Mac naar een map buiten Google Drive**,
bijvoorbeeld `~/Projecten/Claude`. Je werk zit veilig op GitHub, dus verplaatsen kost niets.

Dit is het enige punt waarvan ik zou zeggen: doe het los van de rest, en doe het eerst.

**Feedback:**
-

---

## 1. Wat er nu staat

### Mijn Drive
`Eduface` · `Persoonlijke` · `Archive` (leeg sinds april) · `Saved from Chrome`

### Eduface/
| Map | Wat |
|---|---|
| `Sales` | 2 submappen, 12 losse bestanden |
| `Marketing` | 13 submappen |
| `Branding` | 5 submappen, 1 losse PDF |
| `brand` | **leeg** |
| `Archive` | 11 submappen, ~25 losse bestanden vanaf 2024 |
| `archives` | een losse kopie van de `archives`-map uit de repo |
| `Claud AE` | **de repo** |
| `Claude-AE` | halve tweede kopie met een syncconflict erin |

---

## 2. De nieuwe indeling

Zelfde woorden als je repo en je Todoist.

```
Eduface/
  GTM/          nu Sales + Marketing
  Design/       nu Branding
  Platform/     nieuw
  Archive/      blijft
  Claud AE/     de repo, laat ik met rust
```

### GTM/

| Submap | Komt uit |
|---|---|
| `Accounts/` | `Sales/Samenwerking`, plus de losse accountdocumenten uit `Sales` (UTI Go Live Plan, DPA pilot NWU, Eduface x Nigel UON) |
| `Campaigns/` | `Marketing/Linkedin`, `Outreach`, `Lemlist`, `Facebook ads`, `Content`, `Momentum`, `SEO`, `PLG` |
| `Event manager/` | `Marketing/Events & Webinars` |
| `ICP/` | `Marketing/Lead lijsten`, `CRM data`, `User data`, `Shift`, plus `UK universiteiten score` en `eduface_lead_scores_ranked` uit Sales |
| `Knowledge/` | `TEMPLATE Go Live Plan`, `Sales conversation` |
| `Pricing/` | `Prijsmodel particuliere instellingen.pdf` |
| `Opnames/` | `Sales/Opnames` — gespreksopnames, hoort bij sales |

### Design/

| Submap | Komt uit |
|---|---|
| `Merk/` | `Branding/Merk`, `Brand guidlines.pdf`, `Branding/Photos`, `Branding/Product images`, `Branding/Logo van scholen` |
| `Website/` | `Branding/Framer` |

### Platform/

Nieuw en voorlopig leeg. Bedoeld voor productmateriaal (UI-beelden, testresultaten,
productclaims), zodat het niet meer bij Branding of Sales belandt.

**Feedback:**
-

---

## 3. Duplicaten die weg kunnen

| Wat | Waarom |
|---|---|
| `Eduface/brand` | Leeg. Bestaat sinds 8 juni, nooit iets in gezet. |
| `Eduface/archives` | Losse kopie van de `archives`-map die ook in de repo zit. |
| `Eduface/Claude-AE` | Halve tweede kopie van de repo, met een syncconflict erin. |
| `(Niet aangepast) UTI Go Live Plan` | Oudere versie naast `UTI Go Live Plan`. |
| `DPA pilot Eduface x NWU.docx` (2e) | Twee identieke bestanden van 238.045 bytes. |
| `eduface_lead_scores_ranked` (2 van de 3) | Bestaat als .md plus twee Google Docs-kopieën. |
| `Lijst van VK 44 - Linkedin campange` (3 varianten) | In `Archive`, uit juni 2025. |
| `Lijst van universiteiten van VK` + `2.0` | Idem. |

Alles gaat naar de **prullenbak**, niet definitief weg. Die bewaart 30 dagen.
De 7,3 GB aan oude zips en de Volda-opname blijven staan, zoals je zei.

**Feedback:**
-

---

## 4. Naamregels voor Drive

Anders dan in de repo, want hier zijn geen scripts of commando's die eraan hangen.
Spaties en hoofdletters mogen dus overal.

- **Geen spatie aan het eind.** Nu fout: `Linkedin `, `Shift `, `CRM data `, `Facebook ads `,
  `Merk `, `Product images `, `Logo van scholen `, `Foto's & video's `
- **Eén map per onderwerp.** Geen `Branding` naast `brand`, geen `Archive` naast `archives`.
- **Geen versienummers in namen.** Geen `2.0`, geen `(1)`, geen `(Niet aangepast)`.
  Google Docs houdt zelf versiegeschiedenis bij.
- **Typefouten corrigeren:** `Brand guidlines .pdf` wordt `Brand guidelines.pdf`,
  `Opnamens` wordt `Opnames`.

**Feedback:**
-

---

## 5. Wat ik niet aanraak

- **`Eduface/Claud AE/`** — dat is de repo. Die verandert vanzelf mee zodra je op je Mac
  `git pull` doet. Met de hand iets verplaatsen daarbinnen breekt git.
- **`Persoonlijke/`** — jouw privémappen. Zeg het als je die er ook bij wilt.
- **`Archive/`** — daar verandert alleen dat de drie dubbele CSV-lijsten eruit gaan.
  De rest blijft precies zoals het is.
- **Gedeelde bestanden blijven gedeeld.** Verplaatsen in Drive verandert het bestand-ID niet,
  dus elke link die je ooit hebt verstuurd blijft werken.

**Feedback:**
-

---

## 6. Volgorde

1. Prullenbak: de lege en dubbele mappen
2. `GTM/`, `Design/`, `Platform/` aanmaken
3. Verplaatsen, blok voor blok, met een meldregel per blok
4. Hernoemen: trailing spaces, typefouten, versienummers
5. `Sales`, `Marketing` en `Branding` opheffen als ze leeg zijn
6. Een `LEESMIJ` in `Eduface/` met dezelfde kaart als `Context/kaart.md` in de repo

**Feedback:**
-
