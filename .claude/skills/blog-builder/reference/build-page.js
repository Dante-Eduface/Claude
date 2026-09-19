// Eduface blog compiler. Run via: npx @framer/agent@latest exec -s <id> -f build-page.js
// Before running: exec -s <id> -e "state.specFile='/abs/pageX.json'; state.idPrefix='q8a'"
// idPrefix MUST be unique per build (temp ids like k0,k1 collide with existing nodes otherwise).
// Requires a LinkStylePreset named "Body Link" for inline links (create once per project).
const fs = require("fs");
const spec = JSON.parse(fs.readFileSync(state.specFile, "utf8"));

let _n = 0;
const _P = state.idPrefix || "z";
const uid = () => _P + (_n++).toString(36);
const esc = (t) => String(t).replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\s*\n\s*/g, " ");

const NAVY = "rgb(0, 35, 51)", GREEN = "rgb(0, 224, 117)", PILLBG = "rgba(0, 224, 117, 0.15)",
      MINT = "rgb(240, 250, 247)", CARDBORDER = "1px solid rgb(214, 228, 235)",
      ZEBRA_A = "rgb(235, 242, 245)", ZEBRA_B = "rgb(242, 250, 247)";

function rich(parent, preset, tag, runs, width) {
  const r = uid(), tb = uid();
  const out = [
    `+RichTextNode ${r} parent="${parent}";`,
    `SET ${r} position="relative" width="${width || "100%"}" height="auto" textStylePreset="${preset}" textAlignment="start";`,
    `+TextBlock ${tb} parent="${r}" tag="${tag}";`
  ];
  for (const run of runs) {
    const tr = uid();
    out.push(`+TextRun ${tr} parent="${tb}";`);
    let s = `SET ${tr} text="${esc(run.text)}"`;
    if (run.bold) s += ' bold="true"';
    if (run.href) s += ` link.href="${run.href}" linkStylePreset="Body Link"`;
    out.push(s + ";");
  }
  return { id: r, dsl: out };
}
const runsFromBlock = (b) => b.runs ? b.runs.map(p => ({ text: p[0], bold: !!p[1], href: p[2] || null })) : [{ text: b.x }];

function renderBlock(content, b) {
  const out = [];
  if (b.t === "h2") return rich(content, "Blog H2", "h2", [{ text: b.x }]).dsl;
  if (b.t === "p") return rich(content, "Body 16", "p", runsFromBlock(b)).dsl;
  if (b.t === "pb") return rich(content, "Body 16 bold", "p", [{ text: b.x }]).dsl;
  if (b.t === "callout") {
    const f = uid();
    out.push(`+FrameNode ${f} parent="${content}"; SET ${f} fill="${MINT}" layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="start" gap="8px" padding="28px 26px 28px 26px" position="relative" radius="12px" width="100%" height="auto";`);
    out.push(...rich(f, "Body 16 bold", "p", [{ text: b.title }]).dsl);
    out.push(...rich(f, "Body 16", "p", runsFromBlock(b)).dsl);
    return out;
  }
  if (b.t === "cards") {
    const g = uid();
    out.push(`+FrameNode ${g} parent="${content}"; SET ${g} layout="grid" gridAlignment="center" gridColumnCount="${b.cols}" gridColumnMinWidth="240px" gridRowCount="1" gridRowHeightType="auto" gap="16px" position="relative" width="100%" height="auto";`);
    for (const it of b.items) {
      const c = uid();
      out.push(`+FrameNode ${c} parent="${g}"; SET ${c} border="${CARDBORDER}" fill="rgb(255, 255, 255)" layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="start" gap="8px" padding="26px 24px 26px 24px" position="relative" radius="12px" width="1fr" height="auto";`);
      out.push(...rich(c, "Body 16 bold", "p", [{ text: it.title }]).dsl);
      out.push(...rich(c, "Body 16", "p", [{ text: it.x }]).dsl);
    }
    return out;
  }
  if (b.t === "img") {
    const f = uid();
    out.push(`+FrameNode ${f} parent="${content}"; SET ${f} fill="${b.src}" border="${CARDBORDER}" overflow="clip" position="relative" radius="12px" width="100%" aspectRatio="${b.aspect}" altText="${esc(b.alt || "")}";`);
    return out;
  }
  if (b.t === "table") {
    const w = b.weights, tbl = uid();
    // Wide tables: keep fluid (width 100%). overflowX="auto" gets dropped by Framer on stacks.
    out.push(`+FrameNode ${tbl} parent="${content}"; SET ${tbl} border="${CARDBORDER}" fill="rgb(255, 255, 255)" layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="start" gap="0px" overflow="clip" position="relative" radius="12px" width="100%" height="auto";`);
    const hr = uid();
    out.push(`+FrameNode ${hr} parent="${tbl}"; SET ${hr} fill="${NAVY}" layout="stack" stackDirection="horizontal" stackDistribution="start" stackAlignment="start" gap="14px" padding="16px 18px 16px 18px" position="relative" width="100%" height="auto";`);
    b.head.forEach((h, j) => out.push(...rich(hr, "Cell Head", "p", [{ text: h }], `${w[j]}fr`).dsl));
    b.rows.forEach((row, i) => {
      const rr = uid();
      out.push(`+FrameNode ${rr} parent="${tbl}"; SET ${rr} fill="${i % 2 === 0 ? ZEBRA_A : ZEBRA_B}" layout="stack" stackDirection="horizontal" stackDistribution="start" stackAlignment="start" gap="14px" padding="15px 18px 15px 18px" position="relative" width="100%" height="auto";`);
      row.forEach((cell, j) => out.push(...rich(rr, j === 0 ? "Body 16 bold" : "Body 14", "p", [{ text: cell }], `${w[j]}fr`).dsl));
    });
    return out;
  }
  throw new Error("unknown block: " + b.t);
}

async function apply(dsl, opts) {
  const res = await framer.agent.applyChanges(dsl, opts);
  if (res.errors && res.errors.length) console.log("ERRORS:", JSON.stringify(res.errors).slice(0, 1000));
  return res;
}

const page = uid(), bp = uid(), hero = uid(), heroInner = uid(), pill = uid(),
      content = uid(), cta = uid(), ctaInner = uid(), btns = uid(), b1 = uid(), b2 = uid();

const shell = [];
shell.push(`+WebPageNode ${page} name="${esc(spec.cardTitle)}" path="${spec.path}";`);
shell.push(`SET ${page} layoutTemplate="default" metadata.title="${esc(spec.seoTitle)}" metadata.description="${esc(spec.seoDesc)}";`);
shell.push(`+FrameNode ${bp} parent="${page}"; SET ${bp} width="1200px" height="auto";`);
shell.push(`+FrameNode ${hero} parent="${bp}"; SET ${hero} fill="${NAVY}" layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="center" gap="18px" overflow="clip" padding="80px 24px 48px 24px" position="relative" width="100%" height="auto";`);
shell.push(`+FrameNode ${heroInner} parent="${hero}"; SET ${heroInner} layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="center" gap="18px" position="relative" width="100%" height="auto" maxWidth="760px";`);
shell.push(`+FrameNode ${pill} parent="${heroInner}"; SET ${pill} fill="${PILLBG}" layout="stack" stackDirection="horizontal" stackDistribution="center" stackAlignment="center" gap="0px" padding="7px 14px 7px 14px" position="relative" radius="100px" width="auto" height="auto";`);
shell.push(...rich(pill, "Box Title", "p", [{ text: spec.hero.eyebrow }], "auto").dsl);
shell.push(...rich(heroInner, "Hero H1 White", "h1", [{ text: spec.hero.h1 }]).dsl);
shell.push(...rich(heroInner, "Description Wit", "p", [{ text: spec.hero.subtitle }]).dsl);
shell.push(...rich(heroInner, "Description Wit", "p", [{ text: spec.hero.meta }]).dsl);
shell.push(`+FrameNode ${content} parent="${bp}"; SET ${content} layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="start" gap="22px" padding="56px 24px 72px 24px" position="relative" width="100%" height="auto" maxWidth="720px";`);
shell.push(`+FrameNode ${cta} parent="${bp}"; SET ${cta} fill="${NAVY}" layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="center" gap="22px" overflow="clip" padding="64px 24px 64px 24px" position="relative" width="100%" height="auto";`);
shell.push(`+FrameNode ${ctaInner} parent="${cta}"; SET ${ctaInner} layout="stack" stackDirection="vertical" stackDistribution="start" stackAlignment="center" gap="22px" position="relative" width="100%" height="auto" maxWidth="600px";`);
shell.push(...rich(ctaInner, "CTA Title", "h2", [{ text: spec.cta.title }]).dsl);
shell.push(...rich(ctaInner, "Description Wit", "p", [{ text: spec.cta.desc }]).dsl);
shell.push(`+FrameNode ${btns} parent="${ctaInner}"; SET ${btns} layout="stack" stackDirection="horizontal" stackDistribution="center" stackAlignment="center" gap="12px" position="relative" width="auto" height="auto";`);
shell.push(`+FrameNode ${b1} parent="${btns}"; SET ${b1} fill="${GREEN}" layout="stack" stackDirection="horizontal" stackDistribution="center" stackAlignment="center" gap="0px" link.href="https://calendly.com/eduface/30min?back=1" link.openInNewTab="true" padding="13px 24px 13px 24px" position="relative" radius="10px" width="auto" height="auto" minHeight="46px";`);
shell.push(...rich(b1, "Body 16 bold", "p", [{ text: "Book a demo" }], "auto").dsl);
shell.push(`+FrameNode ${b2} parent="${btns}"; SET ${b2} border="1px solid rgb(255, 255, 255)" layout="stack" stackDirection="horizontal" stackDistribution="center" stackAlignment="center" gap="0px" link.href="https://app.eduface.me/signup" link.openInNewTab="true" padding="13px 24px 13px 24px" position="relative" radius="10px" width="auto" height="auto" minHeight="46px";`);
shell.push(...rich(b2, "Description Wit", "p", [{ text: "Create free account" }], "auto").dsl);

const res0 = await apply(shell.join("\n"), {});
const map = res0.renamedIds || {};
const contentId = map[content] || content;
console.log("CHUNK0:", res0.status, "content:", contentId);

const blocks = spec.blocks, BATCH = 4;
for (let i = 0; i < blocks.length; i += BATCH) {
  const dsl = [];
  for (const b of blocks.slice(i, i + BATCH)) dsl.push(...renderBlock(contentId, b));
  await apply(dsl.join("\n"), { pagePath: spec.path });
}
console.log("DONE", spec.slug, "blocks:", blocks.length, "pageId:", map[page] || page);
