# Framer CMS build prompt — Eduface blog

Paste this into Framer's AI / hand to a builder. Brand tokens are baked in so it lands on-brand.

---

Build a **CMS-driven blog** for Eduface (eduface.me) to replace the current static blog pages at `/resources/blog`. It must keep everything the current blog has and add cover images + category tags, in a proper responsive card grid.

## Brand (use these exact values, never invent others)
- Colours: navy `#002333` (primary text + dark surfaces), green `#00E075` (accent/highlight), readable green `#007B54` (green text on white), light surface `#F3F7F8`, border `#E7EEF0`, muted text `#5B7480`.
- Fonts: **League Spartan** for headings/display, **Inter** for body/UI. Not Roboto.
- Radius: cards `20px`, pills/tags `9999px`. Card shadow: soft, `0 12px 40px rgba(0,35,51,.10)`.
- Tone: clean, lots of whitespace, navy + white + grey, green used sparingly so it means something.

## 1. CMS Collection — "Blog Posts"
Create a collection with these fields:
- `title` — text (article headline)
- `slug` — slug
- `cover` — image (the article cover illustration; aspect ratio 4:3, 1200×900)
- `category` — option/text (e.g. Thought Leadership, Compliance, Research, Product, Integrations)
- `readTime` — text (e.g. "7 min read")
- `excerpt` — text (1–2 sentence summary; also reused as meta description)
- `author` — text (default "Eduface Team")
- `authorAvatar` — image (default: Eduface green mark)
- `publishedDate` — date
- `body` — rich text (the full article)
- `seoTitle` — text
- `seoDescription` — text
- `featured` — boolean (optional, to pin a hero post)

Migrate the existing 24 posts from `/resources/blog` into this collection (title, excerpt, read time, body, slug all already exist on the live pages).

## 2. Blog index page (collection list)
- Keep the existing hero: heading "Insights for higher education" + the tagline.
- Below it, a **responsive card grid**: 1 column on mobile, 2 on tablet, 3 on desktop. Generous gaps, plenty of whitespace.
- Optional: category filter pills row under the hero (filters the grid by `category`).

**Card anatomy (top → bottom):**
1. `cover` image — full card width, rounded `20px`, 4:3 ratio, object-fit cover.
2. `category` tag — small pill, uppercase, green-deep text `#007B54` on light green tint, just under the image.
3. `title` — League Spartan, navy `#002333`, ~22–24px, 2 lines max.
4. `excerpt` — Inter, muted `#5B7480`, ~15px, 3 lines max.
5. Footer row (space-between): left = small `authorAvatar` (Eduface mark) + `author` name; right = `readTime` in muted text, or a "Read article →" link.
- White card, soft shadow, hover: slight lift + shadow increase. Whole card links to the post.

## 3. Article detail page (CMS template)
- **Cover hero:** `cover` image at the top, full content-width, rounded.
- **Meta row:** `category` tag + `readTime` + `publishedDate`.
- **Title:** League Spartan, large (display scale, ~44–56px), navy.
- **Author row:** `authorAvatar` + `author`.
- **Body:** render `body` rich text. Style headings in League Spartan navy, body in Inter at 18px with 1.6 line-height and comfortable max-width (~720px), green-deep for links, styled lists/quotes.
- **Bottom CTA block:** navy section, white text, one green button "Book a demo" (single primary CTA).
- Optional: "Related articles" — 3 cards from the same `category`.

## 4. SEO
- Page title from `seoTitle` (fallback `title`), meta description from `seoDescription` (fallback `excerpt`).
- Open Graph image = `cover`. Set OG title/description per post.
- Clean slug URLs under `/resources/blog/<slug>` (keep existing slugs so links don't break).

## Done = looks like a premium, on-brand blog: navy/green, League Spartan/Inter, cover image per card, category tags, responsive 3-column grid, working detail template, existing 24 posts migrated, existing URLs preserved.
