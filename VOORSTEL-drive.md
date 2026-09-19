# Voorstel Google Drive — versie 2

Jouw feedback verwerkt. Schrijf nieuwe opmerkingen achter **Feedback:**.

**Uitgangspunt dat je gaf:** dit wordt een map waar jij handmatig in verder werkt.
Geen agent die hem onderhoudt. Dus geen indexbestanden, geen kaart, geen LEESMIJ —
de structuur moet gewoon kloppen als je erdoorheen klikt.

---

## Wat er veranderd is t.o.v. versie 1

| Jouw feedback | Verwerkt |
|---|---|
| Repo moet in Drive blijven | ✓ blijft staan, zie risico hieronder |
| `Claude-AE` niet aanpakken | ✓ blijft precies zoals hij is |
| Opnames hoeven niet in GTM, mogen weg | ✓ naar prullenbak |
| `(Niet aangepast) UTI Go Live Plan` toch bewaren | ✓ blijft |
| Versienummers in namen mogen | ✓ die regel is eruit |
| `Persoonlijke/` mag ook opgeruimd | ✓ toegevoegd als blok 5 |
| Geen LEESMIJ in Eduface | ✓ eruit |

---

## 0. De repo in Drive: het echte risico

Je houdt hem in Drive. Prima, maar dit is wat er kan gebeuren, van klein naar groot:

| Wat | Hoe vaak | Wat je kwijtraakt |
|---|---|---|
| `* 2`-conflictbestanden in `.git` | Regelmatig, gebeurt al | Niets, alleen rommel |
| `fatal: index file corrupt` | Af en toe | Niets. `rm .git/index && git reset` en klaar |
| Packfile half geüpload tijdens `git gc` | Zelden | Niets als je gepusht hebt. Opnieuw clonen |
| **Niet-gecommit werk** | Als het misgaat | Dit is het enige dat echt weg kan |

Commits liggen in `.git/objects/` en worden na het schrijven nooit meer aangeraakt.
Die zijn dus vrij veilig. De index wordt bij elke `git add` en `git status` volledig
herschreven, en dat is het bestand waar Drive overheen gaat.

**De hele mitigatie is: vaker committen en pushen.** GitHub is je backup, Drive niet.
Zolang je pusht is de schade altijd terug te draaien.

Ruim wel de `* 2`-bestanden op als je ze ziet. Nu staat er bijvoorbeeld
`Eduface/Claude-AE/.claude 2`. Die raak ik niet aan, dat zei je, maar hij is er wel.

**Feedback:**
-

---

## 1. De nieuwe indeling

```
Eduface/
  GTM/          nu Sales + Marketing
  Design/       nu Branding
  Platform/     nieuw
  Archive/      blijft
  Claud AE/     de repo, blijft, raak ik niet aan
  Claude-AE/    blijft, raak ik niet aan
```

### GTM/

| Submap | Komt uit |
|---|---|
| `Accounts/` | `Sales/Samenwerking` + de losse accountdocumenten uit `Sales`: UTI Go Live Plan, `(Niet aangepast) UTI Go Live Plan`, DPA pilot NWU, Eduface x Nigel UON, Pre-pilot survey |
| `Campaigns/` | `Marketing/`: Linkedin, Outreach, Lemlist, Facebook ads, Content, Momentum, SEO, PLG |
| `Event manager/` | `Marketing/Events & Webinars` |
| `ICP/` | `Marketing/`: Lead lijsten, CRM data, User data, Shift + uit `Sales`: UK universiteiten score, eduface_lead_scores_ranked |
| `Knowledge/` | `TEMPLATE Go Live Plan`, `Sales conversation` |
| `Pricing/` | `Prijsmodel particuliere instellingen.pdf` |

### Design/

| Submap | Komt uit |
|---|---|
| `Merk/` | `Branding/Merk`, `Brand guidlines.pdf`, `Photos`, `Product images`, `Logo van scholen` |
| `Website/` | `Branding/Framer` |

### Platform/

Nieuw en voorlopig leeg, voor productmateriaal: UI-beelden, testresultaten, productclaims.
Zodat dat niet meer bij Branding of Sales belandt.

**Feedback:**
-

---

## 2. Naar de prullenbak

Blijft 30 dagen terug te halen.

| Wat | Waarom |
|---|---|
| `Sales/Opnames` | Jouw besluit: mogen weg |
| `Eduface/brand` | Leeg sinds 8 juni |
| `Eduface/archives` | Exacte kopie van `Claud AE/archives`: zelfde mappen, zelfde bestandsgroottes, alleen andere ID's. De echte staat in de repo |
| `DPA pilot Eduface x NWU.docx` (tweede) | Twee bestanden van exact 238.045 bytes |
| `eduface_lead_scores_ranked` (2 van de 3) | Bestaat als .md plus twee Google Docs-kopieën. De .md blijft |
| `Lijst van VK 44 - Linkedin campange` (2 van de 3) | In `Archive`, juni 2025, drie bijna-identieke CSV's |
| `Lijst van universiteiten van VK` + `2.0` | Idem, 2.206 bytes allebei |

**Blijft staan:** `(Niet aangepast) UTI Go Live Plan` (jouw correctie), `Claude-AE`,
`Bewaren.zip` (3,5 GB), de Volda-opname (3,8 GB), en de rest van `Archive`.

**Feedback:**
-

---

## 3. Hernoemen

Alleen dit, want versienummers mogen blijven:

| Nu | Wordt | Waarom |
|---|---|---|
| `Linkedin ` | `LinkedIn` | spatie aan het eind |
| `Shift ` | `Shift` | idem |
| `CRM data ` | `CRM data` | idem |
| `Facebook ads ` | `Facebook ads` | idem |
| `Merk ` | `Merk` | idem |
| `Product images ` | `Product images` | idem |
| `Logo van scholen ` | `Logo van scholen` | idem |
| `Foto's & video's ` | `Foto's & video's` | idem |
| `Brand guidlines .pdf` | `Brand guidelines.pdf` | typefout + spatie |
| `Opnamens` | `Opnames` | typefout |

Een spatie aan het eind is onzichtbaar in Drive maar breekt wel zoekopdrachten en
links naar die map.

**Feedback:**
-

---

## 4. Persoonlijke/

| Nu | Voorstel |
|---|---|
| `Foto's & video's ` | spatie eraf |
| `Persoonlijke document` | → `Documenten` |
| `Oude Persoonlijk` | → `Archief` |
| `Persoonlijke ontwikkeling` | blijft, matcht je Todoist-sectie |
| `Sporten` | blijft |
| `Hemhofen` | blijft |
| `selectie eduface` | **vraag:** dit is werk, in je privémap. Naar `Eduface/` of hier laten? |

**Feedback:**
-

---

## 5. Volgorde

1. Prullenbak: `Opnames`, `brand`, `archives`, de dubbele bestanden
2. `GTM/`, `Design/`, `Platform/` aanmaken
3. Verplaatsen per blok, met een meldregel per blok
4. Hernoemen: trailing spaces en de twee typefouten
5. `Sales`, `Marketing` en `Branding` opheffen zodra ze leeg zijn
6. `Persoonlijke/` als laatste

Deellinks blijven werken: verplaatsen verandert het bestand-ID niet.

**Feedback:**
-
