# Discovery-call landingspagina (institutionele buyers)

Gestart 18-09-2026. Losse pagina naast `projects/landing-page-demo-survey/` (die is voor docenten, self-serve demo-booking met survey). Deze pagina is voor **economic buyers**: COO / academic director bij UK/Ierland/NL/US-instellingen, gericht op institutionele deals van 50K-150K. Eén conversiepunt: **Book a Discovery Call** (nav-knop verkort: **Book a Call**).

Herkomst: structuur en copy-slots komen uit een Figma-wireframe ("ThrillX", een generiek copywriting-skelet met 13 secties). Dat bestand leverde **alleen** welke tekstvakken er staan en in welke volgorde — niet het uiterlijk. De vormgeving komt volledig uit `references/design-system/core/` + `web/`, dezelfde tokens als `landing-page-demo-survey`.

- `proef-hero.html`: sectie 1 (nav + hero), losstaand bestand, inline stijl + `.notes`-blok met de ontwerpbeslissingen. Lokaal bekijken: `node serve.mjs` → `http://localhost:3220`.
- Nog niet aangemaakt: `styles.css`, `pagina.html`, `build-pagina.mjs`, `brand_assets/` — die horen bij poort 3 (uitrol van de overige 12 secties), niet bij deze proef.

## Volledige copy (bron van waarheid, overdracht 18-09-2026)

CTA is overal dezelfde actie: **Book a Discovery Call**. Taal: uitsluitend Engels. Geen "pilot"-taal als marketingclaim, behalve de feitelijke attributie bij bewijs (bijv. "Piloted at Bath Spa University" — dat mag wel).

### 1. Nav + Hero — **status: proef gebouwd, wacht op akkoord**
- Nav: Platform · How It Works · Results · FAQ — CTA: Book a Call
- Eyebrow: Used by Hogeschool Rotterdam, De Haagse Hogeschool and Tilburg University
- H1: Become the Institution That Leads While Competitors Quietly Fall Behind
- Lead: Within your first week, every teacher sees a student's full feedback history and stops sending contradictory feedback to the students most likely to drop out, using Eduface's AI assessment platform.
- Value props: flags inconsistent grades before a complaint · works in existing LMS · 94% grading accuracy
- CTA: Book a Discovery Call — risk-reversal: No commitment. No credit card.
- Form: "Get in Touch" — Name, Work Email, Institution, Job Title, Message (optional) — knop: Book a Discovery Call

### 2. Trust-balk — nog te bouwen
Regel: "Built with UK and Dutch higher education institutions" (al goedgekeurd; alternatief overwogen: "Co-developed with Universiteit Leiden and Radboud Universiteit" — alleen wijzigen als dat bewust gebeurt). Logo-rij: placeholder.

### 3. Probleem/herkenning — nog te bouwen
Headline: Feeling like grading is bleeding your margin?
Body: Almost every institution wants consistent, high-quality feedback. Few can prove they deliver it. Under workload pressure, quality gets rushed, and markers grade the same work differently without anyone noticing until a student complains or an accreditor asks for evidence. Eduface gives every marker the same instructed standard, so consistency stops depending on who happens to be marking that week.

### 4. Social proof #1 — Bath Spa University — nog te bouwen
Headline: An AI Model That Marks Like Your Own Team
Subhead: Tested on real student work your markers had already graded. Not on a demo set.
Stats: 94% accurate before the lecturer instructs it → 98% accurate after, 4 points closer
Tag: Bath Spa University, Pilot, June 2026 — 435 assignments | 13 markers | 6 subjects
**Let op:** cijfers goedgekeurd, geen citaten van Bath Spa-medewerkers of -markers gebruiken (Helen King heeft expliciet gezegd Eduface niet aan te bevelen).

### 5. Value prop — Consistency — nog te bouwen
Eyebrow: Consistent grading, guaranteed
Subheadline: Every marker grades to the same standard, every time
Body: Eduface's Grader Comparison Dashboard shows the moment a marker's grade or feedback drifts from the instructed standard, before it reaches the student. You see the gap in one view instead of finding out from a complaint or an accreditation review.

### 6. Value prop — Grading Accuracy — nog te bouwen
Eyebrow: Verified accuracy, not a claim
Subheadline: 94% accurate out of the box, 98% once it knows your standard
Body: Eduface isn't one generic model guessing at every subject. It runs six subject-trained models — Law, Economics, Social Sciences, STEM, Humanities and Health Sciences — each built on the reasoning and source conventions of its own field. Instructed on your rubric, accuracy climbed from 94% to 98% in Bath Spa University's pilot, tested against markers who had already graded the same work.
**Open punt:** 94% staat ook al in de hero als value prop — dubbel, één van de twee moet iets anders dragen.

### 7. Value prop — Retention & accreditation — nog te bouwen
Eyebrow: Protect what grading inconsistency puts at risk
Subheadline: Fewer students lost to feedback that let them down
Body: Inconsistent, late or generic feedback is one of the quiet reasons students disengage and drop out, and one of the reasons accreditors flag traceability gaps. Consistent, timely feedback closes both risks at once, without adding headcount.

### 8. Social proof #2 — Hogeschool Rotterdam (BDK) — nog te bouwen
Headline: The Second Round Is Where It Clicks
Content: pilot in Bedrijfskunde (BDK), Rotterdam Business School, groepsrapport 20+ pagina's; concept → rubric-feedback in de tekst → zichtbare vooruitgang in ronde 2; 79% van de studenten positief/neutraal zonder extra begeleiding; hoogst gewaardeerd: APA-controle, onderbouwing, samenhang, modelverbetering, denkimpuls, opmerkingen in de tekst; slotcitaat (niet toegeschreven): "We moeten als opleiding blijven werken met AI in ons onderwijs. Studenten verwachten het... Niets doen is geen optie."
**Let op:** alleen 79% gebruiken (niet de 57/22/21-verdeling), specifiek BDK, nooit koppelen aan de lerarenopleiding (aparte, betaalde klantrelatie bij Rotterdam).

### 9. Vergelijkingssectie — nog te bouwen
Headline: What Actually Makes Eduface Different — Eduface vs. generieke LLM, zelfgebouwd, LLM-wrapper.

| Criterium | Eduface | General LLM | Self-Built | LLM-Wrapper |
|---|---|---|---|---|
| Time to go live | Weeks | Instant | ~3 months | Weeks to months |
| Consistency & accuracy | ✓ | ✗ | ✗ | ✗ |
| AI Act / GDPR compliant | ✓ | ✗ | ✓ | ✗ |
| Works in your LMS | ✓ | ✗ | ✓ | ✓ |

**Open punt:** concurrentnamen niet bevestigd, geen namen zonder harde bron per naam.

### 10. How it works — nog te bouwen
Headline: From First Conversation to Consistent Grading
1. Discovery Call — We map where grading inconsistency and workload actually hurt your institution.
2. Instruct Eduface on Your Rubric — We configure Eduface on your exact criteria, so every grade matches your standard from day one.
3. Go Live in Your LMS — Eduface connects to your existing system and starts grading consistently from day one.

### 11. FAQ — nog te bouwen
1. **Does Eduface detect AI-generated student work?** Eduface doesn't claim hard AI-detection. Our Academic Integrity module (in beta) asks students to verbally defend their own paper, similar to a thesis defense, and flags inconsistencies for your markers to review. It never hands down an automatic verdict.
2. **Where is our data hosted, and does it meet GDPR requirements?** Eduface runs on infrastructure built for EU/UK data requirements. We'll walk your compliance team through it on the call.
3. **Does Eduface integrate with our existing LMS?** Yes. Eduface connects to Moodle, Brightspace and Itslearning through standard LTI integration.
4. **How accurate is the AI grading?** 94% out of the box, and up to 98% once it's instructed on your own rubric, tested against markers who had already graded the same work.
5. **Does a human still grade, or is it fully automated?** The AI assists. The academic decides. Institutions choose how much human oversight they want — feedback can go straight to students, or wait for your markers to review and approve it first.
6. **What does it cost?** Pricing scales with your institution's assessment volume. We'll walk through it on the call.

### 12. Laatste CTA — nog te bouwen
Headline: Every Term You Wait Is Another Cohort Graded the Old Way
Body: Grading inconsistency and rushed feedback don't fix themselves between terms. The institutions ahead of this are already instructing their rubric into Eduface before the next intake starts.

### 13. Footer — nog te bouwen
Logo (placeholder) · Nav herhaald: Platform · How It Works · Results · FAQ · Legal: Privacy Policy · Terms of Service · Contact: Get in Touch · © 2026 Eduface. All rights reserved.

## Nooit noemen / harde regels
- **TIO Business School en ICM Opleidingen**: nergens, in geen enkel kanaal.
- **Bath Spa**: cijfers mogen, citaten van medewerkers nooit (Helen King heeft Eduface expliciet niet aanbevolen).
- **Hogeschool Rotterdam**: de betaalde klantrelatie zit bij de lerarenopleiding; de BDK-case (sectie 8) is een apart goedgekeurd case study — nooit suggereren dat de klantrelatie bij BDK zit.
- Woordkeuze: overal "accurate", nooit "correct".

## Poort 2, proef: nav + hero (18-09-2026)

Bestand: `proef-hero.html`. Eén sectie volledig af, als patroon voor de rest — conform `core/proces.md`.

**Wat vastligt als dit akkoord is:**
- Kleur: navy (`#002333`) als grond/primary, groen (`#00e075`) als de ene toegestane accentkleur per pagina — hier op de hero-CTA. Formulierpaneel wit, submit-knop navy (bewust anders dan de hero-CTA, zie hieronder).
- Type: League Spartan voor de kop (display-lg, 56px, niet de grootste display-xl van 72px — de kop is elf woorden lang in een kolom die de helft van de breedte deelt met het formulier), Inter voor de rest.
- Ruimte: 8pt-familie, gap op de parent, geen margins op children (Framer-proof), grid met `minmax()` i.p.v. een vaste kolomverdeling.
- Radius 10px op knoppen, 20px op het formulierpaneel. Schaduw navy-getint.

**Bewuste keuzes, expliciet toegepast:**
1. **Eyebrow als gewone regel, geen hoofdletter-pill/badge.** Staat op de reflexen-lijst (`compositie.md` §12) als af te raden, ook al kent het design system zelf een eyebrow-badge-patroon elders (`eyebrow-preview.html`). Hier bewust een gewone zin.
2. **Achtergrond is een placeholder**, geen namaak-stockfoto: effen `ink-900`-vlak met een klein, onopvallend devlabel. De donkere overlay-gradient blijft staan zodra er een echte foto in komt — dan wel opnieuw op contrast checken, deze verhouding is afgestemd op het huidige vlakke fond.
3. **"Book a Discovery Call" staat twee keer op het scherm** (hero-CTA en form-submit). De hero-knop is groen (de ene toegestane accentkleur), de submit-knop is navy: zelfde tekst, andere rol — uitnodiging versus transactionele actie — niet dubbel groen.
4. **Formulier is puur markup**, geen backend-koppeling. Native HTML5-validatie (`required`, `type=email`) is genoeg voor deze proef.
5. **Mobiel:** de twee kolommen stapelen (copy eerst, dan formulier), nav-links klappen in — zelfde patroon als `landing-page-demo-survey`.

**Nog open na dit akkoord:** trust-balk logo's zijn placeholder (sectie 2), en de dubbele 94% (hero vs. sectie 6) moet nog worden opgelost — geen van beide hoort bij deze proef.

Lokaal bekijken: `cd projects/landing-page-discovery-call && node serve.mjs` → `http://localhost:3220`.
