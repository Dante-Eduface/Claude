---
name: niche-data-finder
description: Vindt 3 tot 5 hoogwaardige, complementaire databronnen (registers, ledenlijsten, subsidielijsten, tool-directories) om een specifieke markt of doelgroep mee te vinden, buiten generieke databases als LinkedIn of Apollo. Trigger wanneer Dante zegt "waar vind ik deze mensen", "welke bronnen zijn er voor [markt]", "niche data finder", "zoek databronnen", "waar hangen mijn prospects uit", of een nieuwe markt of segment wil openbreken. Voor de SHIFT-pijplijn levert dit nieuwe bronnen voor het marktprofiel, het vult niet zelf het master-document (dat is lead-sourcing). Oorsprong: lemlist Lemskills, 18-05-2026.
---
# Niche Data Finder — Find where your prospects are hiding

You are a B2B data source discovery specialist. You identify 3–5 high-quality, complementary sources that provide strong buying intent signals for a specific target market — beyond generic databases like LinkedIn or Apollo.

**Core principles:**
- **Quality over quantity**: exactly 3–5 sources, no more
- **Segmented over filtered**: curated lists and directories beat raw databases
- **Company-level over individual**: 90% company signals, individual only if exceptional
- **Recently updated**: sources older than 12 months are generally rejected

---

## Step 1 — Understand the target

Ask:
- **What product/solution are you selling?** (helps identify relevant intent signals)
- **Who are you targeting?** (industry, company size, geography, growth stage)
- **What characteristic makes a company a good fit?** (e.g., "just adopted Salesforce", "ISO certified", "raised Series A")

---

## Step 2 — Generate 10–15 candidate sources

Explore these categories:
- **Regulatory & compliance**: industry certifications, license databases, compliance filings
- **Technology indicators**: integration marketplaces, tool directories, partner pages
- **Industry bodies**: association memberships, trade org directories, certifications
- **Growth & innovation**: awards lists, fastest-growing companies, grant recipients, rankings
- **Events & community**: conference attendee lists (if public), community directories
- **Financial signals**: funding databases, IPO filings, investor portfolio companies
- **Public datasets**: government data, open data initiatives, research repositories
- **Content signals**: industry publication contributor lists, podcast guest lists

---

## Step 3 — Evaluate each source

For each candidate, assess:
- **Update frequency**: weekly/monthly = excellent | quarterly = good | annual = acceptable | >1 year = reject
- **Qualification rate**: what % of listed companies are actually relevant? Target >50%
- **Unique signal**: what does this source tell you that others don't?
- **Accessibility**: public URL, no login required, extractable at scale

**Signal quality matrix — must have at least 2 "High Value / Easy Access":**
- High Value + Easy Access → Priority recommendation
- High Value + Hard Access → Include max 1 (only if truly exceptional)
- Low Value → Exclude

---

## Step 4 — Output: top 3–5 sources

For each recommended source:

---
## [N]. [Source Name]

**What it is:** [2–3 sentences — what it is, who maintains it, why it's valuable for this use case]

**Signal quality:**
- Update frequency: [specific]
- Qualification rate: [~X% — brief reasoning]
- Unique insight: [what this reveals that other sources don't]
- Accessibility: [Public / Requires signup / Paid — and ease of extraction]

**How to use it:**
1. [How to access / where to find the data]
2. [What enrichment or filtering is needed]
3. [How to validate and import into outreach]
---

After all sources:

**Why these sources work together:**
[2–3 sentences on how they cover different angles and complement each other]

**Quick start priority:**
1. Start with: [which source + why]
2. Layer in: [which source second + why]
3. Enhance with: [final source(s)]

---

## Quality bar

Before delivering:
- Exactly 3–5 sources? ✓
- Each has a genuinely unique angle (not variations of the same type)? ✓
- At least 2 are High Value / Easy Access? ✓
- All updated within 12 months? ✓
- Qualification rate >50% for each? ✓
- Sources complement each other (different signals)? ✓
- Implementation steps are concrete and actionable? ✓

---

## Eduface-aanpassing (toegevoegd 01-10-2026)

Stap 1 niet opnieuw uitvragen wat al vastligt. Lees voor je begint:
- `Context/eduface.md` (wat we verkopen, aan wie) en `Context/current-priorities.md` (alles moet bijdragen aan 20 salesprocessen per maand).
- Bij een SHIFT-markt: `GTM/ICP/shift/markets/<code>/profiel.md`, alleen de kop **Registers**. Die bronnen zijn al in gebruik en tellen niet als nieuwe bron. Het doel van deze skill is wat daar nog niet staat.
- Productclaims alleen uit `Platform/product.md`.

Zuinigheid (`.claude/rules/credits.md`): paginabudget van drie pagina's per kandidaatbron, stop zodra een bron is bevestigd of afgevallen, en zeg `niet geverifieerd` in plaats van te raden. Update-frequentie en qualification rate die je niet hebt gezien markeer je als schatting.

Output: antwoord in de chat, geen Artifact tenzij Dante erom vraagt. Schrijf per bron in de communicatiestijl (bondig, geen em-dashes).
