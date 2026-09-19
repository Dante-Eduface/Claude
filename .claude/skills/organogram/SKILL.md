---
name: organogram
description: Build a clean, print-perfect organogram / org chart / stakeholder map as HTML then PDF, with real validated photos, role color-coding, and cards that never break across a page. Standalone and reusable — other skills (stakeholder-mapping, targeted-outreach) invoke this for their visual output. Trigger when Dante says "maak een organogram", "organigram", "org chart", "maak er een organogram van", or when another skill needs to render a people-map.
---

# Organogram

Turn a set of people (with roles, reporting lines, and deal-roles) into a **clean, one-look organogram** rendered HTML → PDF. This skill owns ONLY the visual. The research that produces the people lives in the calling skill (e.g. `stakeholder-mapping`).

Visual template to copy: `projects/rug-groningen/organogram.html`. Copy its tokens and structure, then apply the HARD RULES below (they fix mistakes made before).

## HARD RULES — non-negotiable, these are baked in because they were broken before

### 0. PDF only, portrait, print-safe
- **Deliver a PDF. Not an HTML file.** The HTML is only a build artifact — write it to the scratchpad dir, render the PDF into the project folder, and open ONLY the PDF. Dante does not want an HTML version.
- **Portrait A4 by default** (`@page { size: A4 portrait }`). Org charts go deep, so height is the scarce axis, not width.
- **Print-safe styling — this is why his printouts came out with grey blocks:**
  - NO `box-shadow` anywhere.
  - NO background gradients, dot/grid patterns, or tinted/semi-transparent container fills.
  - Page background is pure **white**. Structure comes from **thin solid borders and dividers only**.
  - Pills/labels: prefer outlined or plain colored text over filled backgrounds.
  - It must look on screen exactly like it will look printed.

### 1. Cards NEVER break across a page
This is the #1 past failure: a card got sliced in half by a page break, half its text on page 1, half on page 2, unreadable.
- Every card, row, tier, and block MUST have `break-inside: avoid; -webkit-column-break-inside: avoid; page-break-inside: avoid;`.
- Design to fit **one landscape A4 page** by default. Keep it dense. If it genuinely needs a second page, it must break cleanly **between tiers**, never inside a card.
- It is an organogram, **not a long white document**. If the rendered output is a tall sparse page with big gaps, tighten spacing and card sizes until it reads as one compact chart.

### 2. Members only — and NO legend, NO analysis box
The organogram contains ONLY the people and the lines between them.
- **NO legend.** If the chart needs a legend to be understood, it is too complex — fix the chart instead. Meaning must be carried by the label text on each card (write "Champion", "Beslist", "Ally" as words), with color only reinforcing it.
- **NO CRO/next-step/assessment box**, NO self-build/tool analysis, NO strategy essays, NO market context.
- **Title is plain**: `<Group> — <Institution>` (e.g. "Digital Oversight Group — Bath Spa University"). No logo, no accent rule/line, no subtitle or description paragraph.

### 2b. Simple, consistent color: Eduface palette only
Simple but good-looking. Use the **Eduface brand** (see [[brand-fonts]]), not arbitrary colors:
- Fonts: **League Spartan** (title, names, labels) + **Inter** (body). Never Roboto.
- Colors: navy `#002333`, green `#00E075`, deep green `#006754`, plus a soft grey for secondary text and a hairline `#e2e8ea`.
- Semantics, max 3: **navy** = decision power (chair, sponsor, signs the licence) · **green** = our people (champion, possible champion, ally to win) · **grey** = neutral/unknown.
- Confirmed vs inferred is NOT another color: **solid border = confirmed, dashed border = inferred**, plus a small check / question icon.
- Nice-but-print-safe touches that work: a solid navy tab label on the group block, colored photo rings, a small colored dot before the role label. No shadows, no tints.

### 2b-2. SVG icons, never emoji
Use **inline SVG icons** (stroke `currentColor`, ~11px). Emoji look cheap and inconsistent.
Standard set: target (what this person controls), key (the hook to win them), link (source), question-circle (inferred), check (confirmed).

### 2b-3. No dash as punctuation
Never use `—` or `-` as a separator or connector in titles or copy. It reads as AI-written. Title format: `<Group> van <Institution>`. In sentences use commas or periods. (Normal Dutch compound hyphens inside a word are fine, but avoid awkward hanging hyphens.)

### 2c. Visual over textual — group what was asked for
- If Dante asks to map a **specific group or department**, that group must be a **visually enclosed block**, not just a note in the text.
- If a person sits in two places (e.g. in the hierarchy AND in the group), **place them twice**. He wants to see it, not read it.
- Use **icons** (🎯 what they control, 🔑 the hook, 🔗 source) to make descriptions scannable. Keep each to one short line. Minimise reading.
- Put a **divider line** between the label/pill row and the description so they don't blur together.

### 2d. Card shape — wide and low, not narrow and tall
- High in the tree there are usually only 2–4 people, so make those cards **wide and short**. Width is cheap; height is not.
- Only switch to narrower/taller cards further down the tree when width genuinely runs out.

### 3. Every inferred placement needs a REASON + SOURCE
If a person's membership, role, or reporting line is **inferred** (not confirmed), the card MUST show:
- a short **why** ("ingeschat: DVC met digital-pedagogy portfolio"), and
- a **clickable source URL** so Dante can go verify and make the final call himself.
Confirmed nodes get a `geverifieerd` marker and their source too. Never present a guess as a fact. "Ingeschat" and "geverifieerd" must be visually distinct.

### 4. Real, validated photos — not initials-by-default
You CAN find a person online and put their real face on the card. Do it.
- Source order: the institution's own staff profile page (best) → LinkedIn / Google image where the name+institution clearly match.
- **Validate**: the image must come from a page that is unambiguously about THAT named person at THAT institution. If you're not confident it's the right person, validate against a second source (e.g. LinkedIn) before using it.
- **Download** it to a local faces folder next to the output (e.g. `projects/<deal>/<inst>-faces/lastname.jpg`) with `curl -sL -A "Mozilla/5.0" "<IMG_URL>" -o <path>`, then verify it's a real image (`file` + `ls -la`, > ~3KB, actually JPEG/PNG).
- Embed via **local relative path** with an initials fallback: `<img src="faces/king.jpg" onerror="this.style.display='none'"><span>HK</span>`.
- A **wrong face is worse than initials** — if you truly can't validate, fall back to initials and say so. Never use a random or guessed image.

### 5. Card layout — photo top, name beside, text below (readable)
The cramped narrow text column next to the photo is a past failure. Use this structure so the description has full width:
- **Top row**: photo (left) + name + role (right, beside the photo).
- **Below, full width**: the description / why / source + role tags.

```html
<div class="card hl-champ">            <!-- hl-* sets the role border color -->
  <div class="top">
    <div class="av ph"><img src="faces/king.jpg" onerror="this.style.display='none'"><span>HK</span></div>
    <div class="head">
      <div class="nm">Prof. Helen King</div>
      <div class="rl">Director of Learning, Innovation, Development &amp; Skills</div>
    </div>
  </div>
  <div class="body">
    <div class="tags"><span class="pill p-champ">Champion</span><span class="pill p-conf">geverifieerd</span></div>
    <div class="hot">Trekt de pilot intern. <a href="SOURCE_URL">bron</a></div>
  </div>
</div>
```
```css
.card{display:flex;flex-direction:column;break-inside:avoid;page-break-inside:avoid;
      background:#fff;border:1px solid #eceff1;border-radius:16px;padding:12px 14px;
      box-shadow:0 4px 16px rgba(16,40,60,.07);min-width:210px;max-width:250px;}
.card .top{display:flex;gap:11px;align-items:center;}
.av{width:46px;height:46px;border-radius:50%;overflow:hidden;flex:none;position:relative;
    background:#eef2f4;display:inline-flex;align-items:center;justify-content:center;}
.av img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.av span{color:#5a6b73;font-weight:700;font-size:14px;} .av.ph{background:#002333;} .av.ph span{color:#fff;}
.head .nm{font-weight:700;font-size:13.5px;color:#0e1c24;line-height:1.15;}
.head .rl{font-size:11px;color:#7a8a91;margin-top:2px;line-height:1.2;}
.body{margin-top:9px;}
.tags{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:6px;}
.hot{font-size:9.5px;color:#7a8a91;line-height:1.4;}
.hot a{color:#067a43;}
```

## Process

1. **Take the people list** from the caller (or gather it): name, verified title, reporting line, deal-role, confirmed-vs-inferred + source per fact.
2. **Get photos** per Rule 4 — this can run as a parallel sub-agent (find + validate + download to the faces folder). A wrong face is worse than initials.
3. **Build the HTML** from the RUG template + the card structure above. Tiers top-to-bottom follow the reporting line. Role color-coding via `hl-*` borders + `p-*` pills. Legend + a short CRO/next-step box (about these people only).
4. **Render** portrait A4. Build the HTML in the scratchpad, output the PDF into the project folder:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="<project>/name.pdf" "<scratchpad>/name.html"`
   (Photos must be referenced with paths that resolve from the HTML's location — use absolute `file://` paths or copy the faces folder next to it.)
5. **MANDATORY visual QA** — rasterise the PDF and LOOK at it (`sips -s format png x.pdf --out x.png`, then Read the PNG). Confirm: (a) no card cut across a page boundary, (b) compact, not a sparse long document, (c) photos load and are the right people, (d) no grey blocks / shadows / background fills that would print badly. Page count: `python3` count of `/Type /Page` (mdls is unreliable/stale). If any check fails, fix and re-render before showing Dante.
6. **Open ONLY the PDF** (`open name.pdf`). Do not ship or open an HTML version.

## Role vocabulary + colors (from cro-of-eduface handbook)
- Economic Buyer — navy `#002333` (`hl-eb` / `p-eb`)
- Beslisser / swing — purple `#5b3ea8` (`hl-swing` / `p-swing`)
- Champion — amber `#b8860b` (`hl-champ` / `p-champ`)
- Coach / ally — green `#067a43` (`hl-coach`/`hl-ally` / `p-coach`/`p-ally`)
- Enemy — red `#b3261e` (`hl-enemy` / `p-enemy`)
- Neutraal / ingeschat — grey `#9aa7ad` (`p-inf`)
- Confirmed marker — green pill `p-conf` ("geverifieerd")

## Done checklist
- [ ] **PDF only**, portrait A4. No HTML shipped or opened.
- [ ] **Print-safe**: white background, no shadows, no gradients/pattern fills, no tinted containers. Looks on screen exactly as it prints.
- [ ] **No legend, no analysis box.** Plain title `<Group> — <Institution>`, no logo/rule/subtitle.
- [ ] Max ~3 colors, meaning carried by the label words. Confirmed vs inferred = solid vs dashed + ✓/?.
- [ ] The requested group is a **visually enclosed block**; people in two places appear **twice**.
- [ ] Icons + a divider between labels and description; descriptions are one short scannable line.
- [ ] Cards wide-and-low at the top of the tree.
- [ ] Every card fits on its page, none sliced by a page break (verified by looking at the rasterised PDF).
- [ ] Every inferred node shows a why + a source link; every confirmed node shows a source.
- [ ] Real validated photos where findable; honest initials fallback where not.
