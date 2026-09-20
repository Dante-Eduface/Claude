# Website-analyse: default.com (juni 2026)

Onderzocht: homepage HTML + CSS + JS, sitemap, robots.txt, llms.txt, blogpost, product-SEO-pagina, blog-index, HTTP-headers, screenshot, plus de publieke design-procesbeschrijving van hun 2.0 redesign.

## Wat is Default
AI-infrastructuur voor revenue teams (lead routing, scheduling, workflows, enrichment). Series A, $20M totaal opgehaald. Site is hun belangrijkste inbound-kanaal en wordt geleid door Stan Rymkiewicz (Head of Growth, ex-Chili Piper).

## Tech-stack
- Next.js (App Router) + Sanity CMS, gehost op Vercel, styling met Tailwind
- 2 self-hosted fonts via next/font: Inter (body/UI) + een custom display-font
- Geen zware animatielibs (geen GSAP/Lottie/Three). Animaties zijn CSS/WAAPI + IntersectionObserver + spring-animaties in React. Product-illustraties zijn inline SVG-componenten
- Server-side prerendered, edge-cached (x-vercel-cache: HIT). HTML 968KB raw maar 112KB gzipped. JS-bundle ~1MB (niet licht, het frisse zit niet in lichtgewicht zijn)
- Historie: de 2.0-site was Webflow (agency-redesign in 8 weken, mini design system, "dots"-motief, Rive easter eggs). Voor de agent-launch in 2026 opnieuw gebouwd in Next.js. Ze behandelen de site als een product, niet als een brochure

## Waarom het zo fris voelt (design)
1. **Extreme beperking in het palet.** Vrijwel alles is near-black (#121315, #151618) met wit in opaciteiten (text-white/50). Accentkleuren (blauw #3b82f6, groen #4ade80) alleen in de product-UI-demo's. Kleur betekent dus iets
2. **Twee fonts, strakke typografie.** Display-font alleen voor koppen, Inter voor de rest. Negatieve letter-spacing (-0.32px op body, -1px op display), line-heights op de pixel gezet, `text-balance`/`text-pretty` tegen lelijke regelafbrekingen
3. **App-achtige precisie.** Spacing in kleine vaste stappen (8/10px paddings, 6px gaps), consistente radius-schaal (6/8/10/12/20px + pills). De marketingsite is gebouwd met dezelfde discipline als een app-UI
4. **Show, don't tell.** Het product wordt niet beschreven maar nagebouwd: versimpelde, geanimeerde UI-demo's (workflow-canvas, agent-chat, tabellen) als levende componenten in de pagina. 455 images waarvan het merendeel inline SVG-iconen voor die nep-UI
5. **Eén duidelijke hiërarchie per scherm.** Grote kop links, korte supporting copy, één primaire CTA (Request a Demo). Veel lucht eromheen

## Waarom alles duidelijk is (copy/structuur)
- Eén belofte in de H1: "Deploy agents that work across your go-to-market"
- Vaste opbouw: probleem ("Your revenue stack wasn't built for agents") → oplossing in 4 pijlers (elk een H3 + één zin) → capabilities → social proof van revenue leaders → CTA
- Elke zin is benefit + mechanisme: "Default unifies data from CRM, website, forms... into a single identity-resolved model in real time"
- Enterprise-vertrouwen expliciet: SOC 2 Type II, SSO/SAML, "every action is reviewed, logged, and reversible"
- Eén CTA door de hele site heen, geen keuzestress

## SEO: ja, ze doen het goed
**Strategie (185 van de 194 URL's zijn blogposts):**
- BOFU keyword-pagina's: /product/lead-enrichment-software, lead-routing-software, sales-scheduling-software, sales-workflow-software. Keyword in URL én H1
- Ecosysteem-keywords: ze liften mee op Salesforce/HubSpot-zoekvolume (salesforce lead routing, web-to-lead, territory planning, Marketo vs Salesforce)
- Comparison/alternatives-content: /comparison/revenuehero, "Chili Piper Alternatives" etc. Vangt kopers die al aan het vergelijken zijn
- Cadans: meerdere posts per week, jaartallen in titels ("...In 2025", "2026 Update"), 179 posts kregen in mei 2026 een lastmod-update (klassieke freshness-play)

**Blogpost-template (vrijwel perfect uitgevoerd):**
- Keyword-titel + jaartal, meta description met benefit
- "Key Takeaways"-blok bovenaan, vraaggedreven H2/H3-structuur, ~2.600 woorden
- 22 interne links per post + Related Articles
- BlogPosting + BreadcrumbList schema, auteur als Person met LinkedIn-URL (E-E-A-T)

**Technisch:**
- Schone robots.txt, sitemap met priorities/lastmod, canonicals, complete OG/Twitter-tags, RSS-feed
- **llms.txt aanwezig**: cureerde samenvatting van product + canonieke pagina's voor AI-zoekmachines (GEO)

**Zwakke plekken (eerlijk is eerlijk):**
- Homepage heeft geen Organization/ld+json schema
- Product-pagina's: twee H1's, dun (~380 woorden), generieke meta description
- Alt-teksten maar op ~19% van de images (veel is decoratief, maar toch)
- 1MB JS is fors

## Wat Eduface hiervan kan kopiëren (Framer)
1. **Eén H1 = één belofte**, dan probleem → product → bewijs → CTA. Eén primaire CTA per pagina
2. **Versimpelde product-UI tonen i.p.v. screenshots**: een gestileerde "feedback op een essay"-demo als levend component zegt meer dan tekst
3. **BOFU-pagina's per use case**: /product/ai-grading-software, ai-feedback-tool, assessment-platform etc. Keyword in URL + H1, en doe het beter dan Default (één H1, 800+ woorden, eigen meta description)
4. **Comparison-pagina's**: Eduface vs Turnitin/FeedbackFruits/handmatig nakijken
5. **Blogpost-template overnemen**: key takeaways, vraag-H2's, interne links, auteur-schema, jaartal in titel, vaste updateronde voor freshness
6. **llms.txt toevoegen aan eduface.me** (past direct bij de GEO-prioriteit)
7. **Design-discipline**: 2 fonts (display + Inter, hebben we al), vaste radius-schaal, near-monochroom palet met 1-2 accentkleuren, spacing-systeem strak aanhouden

## Bronnen
- [Process Breakdown: Default.com (designer, 2.0 redesign)](https://medium.com/@ayushsoni_io/process-breakdown-default-com-8ac73e6af0bf)
- [default.com](https://www.default.com) + sitemap/robots/llms.txt
- [Stan Rymkiewicz, Head of Growth](https://theorg.com/org/default/org-chart/stan-rymkiewicz)
