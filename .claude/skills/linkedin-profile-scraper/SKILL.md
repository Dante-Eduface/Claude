---
name: linkedin-profile-scraper
description: Haalt via Apify een LinkedIn-profiel op (headline, about, functiebeschrijvingen, opleiding, publicaties) en desgewenst de eigen posts van die persoon. Bedoeld als laatste trap van de haakje-zoektocht voor outreach, wanneer gratis bronnen niets opleverden. Werkt zonder cookies. Trigger wanneer Dante zegt "scrape dit linkedin profiel", "haal de posts van [naam]", "gebruik apify", of wanneer een haakje-zoektocht op web en eigen site is vastgelopen.
disable-model-invocation: true
argument-hint: [linkedin-profile-url]
---

# LinkedIn-profiel en posts ophalen via Apify

Geverifieerd en gedraaid op 2026-07-22. Alles hieronder komt uit echte API-antwoorden, niet uit geheugen.

## Voor je begint

**De sleutel staat in `.env` als `APIFY_API_KEY`.** Niet `APIFY_API_TOKEN`. Laden met:

```bash
set -a && . ./.env && set +a
```

**LET OP, harde blokkade (ontdekt 2026-07-24): het gratis plan staat maar 20 runs toe, lifetime, niet per maand.** Bij de 21e run krijg je `Free users are limited to 20 runs. Please upgrade to a paid plan to run more.` Dat is een run-teller, geen geldlimiet: je kunt op $0,63 van $5 zitten en toch geblokkeerd zijn. De teller reset niet aan het begin van de maand. Om verder te kunnen moet het account naar een betaald plan. Controleer dit vóór je een batch belooft.

**Budget zodra het account betaald is:** ongeveer 5 dollar per maand aan platformgebruik. Gemeten kosten:

| Wat | Prijs | Bron |
|---|---|---|
| Profiel zonder e-mail | $0,004 per profiel ($4 per 1k) | staat in het enum van `profileScraperMode` |
| Profiel met e-mailzoektocht | $0,010 per profiel ($10 per 1k) | idem |
| Posts | circa $0,002 per post (gemeten: $0,0061 voor 3 posts) | verbruik voor en na de run |

Dat is dus ruwweg 1.250 profielen per maand. Ruim, maar check het verbruik als je een grote batch doet:

```bash
curl -s "https://api.apify.com/v2/users/me/limits?token=$APIFY_API_KEY" \
  | python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print(d['current']['monthlyUsageUsd'], 'van', d['limits']['maxMonthlyUsageUsd'])"
```

## Stap 1: controleer altijd eerst dat de actor bestaat

Nooit een slug uit je hoofd opschrijven. Actors verdwijnen. Controleer:

```bash
curl -s "https://api.apify.com/v2/acts/<slug>?token=$APIFY_API_KEY"
```

Krijg je `record-not-found`, dan **stop je en meld je dat**. Ga niet gokken naar een andere slug.

Geverifieerd bestaand op 2026-07-22:

| Slug | Actor-id | Titel |
|---|---|---|
| `harvestapi~linkedin-profile-posts` | `A3cAPGpwBEG8RJwse` | LinkedIn Profile Posts Scraper (No Cookies) |
| `harvestapi~linkedin-profile-scraper` | `LpVuK3Zozwuipa5bp` | LinkedIn Profile Scraper + Email ✅ No Cookies |
| `apimaestro~linkedin-profile-detail` | `VhxlqQXRwhW8H5hNV` | Profile Details Scraper for LinkedIn + EMAIL (No Cookies) |

De derde bestaat wel maar is **niet door mij gedraaid**, dus de outputvelden daarvan zijn onbekend. Gebruik hem alleen als terugval en inspecteer dan zelf de JSON.

**Bestaat niet meer:** `curious_coder~linkedin-profile-post-scraper`. Die stond in de vorige versie van deze skill en gaf `record-not-found`.

## Stap 2: profiel ophalen

Dit is wat je in bijna alle gevallen nodig hebt: headline, about en de beschrijvingen onder de functies.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/harvestapi~linkedin-profile-scraper/run-sync-get-dataset-items?token=$APIFY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "profileScraperMode": "Profile details no email ($4 per 1k)",
    "urls": ["https://www.linkedin.com/in/<publicIdentifier>/"]
  }'
```

**Inputvelden** (uit het schema van build `hUQaAf7ZuRs2RXMu7`): `profileScraperMode`, `urls`, `queries`, `publicIdentifiers`, `profileIds`. Geen daarvan is verplicht, maar zonder `urls` of `publicIdentifiers` krijg je niets.

`profileScraperMode` is een enum en de waarde moet **letterlijk** een van deze twee zijn, inclusief het prijsdeel:
- `Profile details no email ($4 per 1k)`
- `Profile details + email search ($10 per 1k)`

Gebruik de eerste. Wij zoeken geen e-mailadressen, dat scheelt ruim de helft.

**Echte outputvelden**, geverifieerd op een run:

```
id, publicIdentifier, linkedinUrl, firstName, lastName, emails, headline,
openToWork, hiring, premium, influencer, memorialized, creator, location,
objectUrn, registeredAt, topSkills, connectionsCount, followerCount, verified,
about, currentPosition, profileTopEducation, profileActions, profilePicture,
coverPicture, photo, profileLocales, primaryLocale, multiLocaleHeadline,
services, experience, education, certifications, projects, volunteering,
receivedRecommendations, skills, publications, courses, patents,
honorsAndAwards, languages, organizations, causes, featured,
composeOptionType, moreProfiles, interests, originalQuery
```

`experience` is een lijst met per item: `position, location, employmentType, workplaceType, companyName, companyLinkedinUrl, companyId, duration, description, skills, startDate, endDate, companyLogo, companyUniversalName`.

**Waar de haakjes zitten, op volgorde:**
1. `headline` — vaak een hele positionering in één regel
2. `about` — het rijkst, mensen schrijven daar hun visie
3. `experience[].description` — wat ze in die rol doen, in hun eigen woorden
4. `publications`, `education`, `honorsAndAwards`, `interests` — voor de langere zoektocht

## Stap 3: posts ophalen, alleen als stap 2 niets opleverde

```bash
curl -s -X POST "https://api.apify.com/v2/acts/harvestapi~linkedin-profile-posts/run-sync-get-dataset-items?token=$APIFY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "targetUrls": ["https://www.linkedin.com/in/<publicIdentifier>/"],
    "maxPosts": 5,
    "includeReposts": false,
    "includeQuotePosts": false
  }'
```

**Inputvelden** (schema van build `3LKhR2pMDYOrJY6LM`): `targetUrls`, `maxPosts`, `postedLimit`, `postedLimitDate`, `includeQuotePosts` (default true), `includeReposts` (default true), `scrapeReactions` (default false), `maxReactions`, `postNestedReactions`, `scrapeComments` (default false), `maxComments`, `commentsPostedLimit`, `postNestedComments`, `contextCountry`.

**Zet `includeReposts` en `includeQuotePosts` op false.** Standaard staan ze aan en dan krijg je gedeelde berichten van anderen terug. Wij willen alleen wat de persoon zelf schreef.

**Echte outputvelden**, geverifieerd op een run van 3 posts:

```
type, id, linkedinUrl, content, contentAttributes, author, postedAt,
postImages, postVideo, socialContent, comments, header, entityId, shareUrn,
shareLinkedinUrl, engagement, reactions, reactionIds, commentIds, query
```

- `engagement` bevat `id, likes, comments, shares, reactions`
- `postedAt` bevat `timestamp, date, postedAgoShort, postedAgoText`. `date` is ISO 8601, bijvoorbeeld `2026-07-21T09:09:34.551Z`
- `content` is de volledige posttekst
- `author` bevat `id, universalName, publicIdentifier, type, name, linkedinUrl, info, website, websiteLabel, avatar, urn`
- `header.text` was `null` bij eigen posts; bij reposts staat daar de deelcontext

**Negeer vacatureposts.** Herken ze aan woorden als "vacature", "we zoeken", "hiring", "join our team" in `content`. Die zeggen niets over wat de persoon zelf belangrijk vindt.

## Stap 4: wat je teruggeeft

Geen CSV nodig tenzij Dante erom vraagt. Lever per persoon:

- Het haakje: één concreet ding dat deze persoon zelf schreef, letterlijk geciteerd
- De bron: `linkedinUrl` van het profiel of van de post
- Uit welk veld het komt (headline, about, experience-beschrijving, of post van datum X)

Vraagt Dante wel om een CSV, bouw die dan op de velden hierboven en **inspecteer eerst de JSON die je terugkreeg**. Actors wijzigen hun schema. Print de keys voor je gaat mappen.

## Wanneer je deze skill NIET gebruikt

Dit is de laatste trap. Probeer eerst gratis:
1. Websearch op naam plus organisatie
2. De teampagina van hun eigen site, daar staat vaak een persoonlijk stukje
3. De organisatie zelf: AI-pagina, visiestuk, jaarverslag, NVAO-rapport
4. Vakbladen, congresprogramma's, podcasts

Stop zodra je iets hebt waar een bericht op kan staan. Ook als dat al bij trap 1 is.

## Foutafhandeling

- **`record-not-found`** op de actor: stoppen en melden. Niet naar een andere slug gokken.
- **401 of 403**: de sleutel is ongeldig. Controleer of `.env` geladen is en of het `APIFY_API_KEY` heet.
- **Lege dataset**: het profiel is privé of de URL klopt niet. Controleer de `publicIdentifier`.
- **Duurt lang**: `run-sync-get-dataset-items` wacht tot de run klaar is. Zet een timeout van 300 seconden. De testrun gaf HTTP 201 binnen die tijd.
