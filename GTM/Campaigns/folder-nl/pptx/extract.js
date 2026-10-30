// Haal posities, tekst en stijl uit het linker binnenpaneel van folder v5, en knip de iconen los als transparante PNG.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [dir, out] = [process.argv[2], process.argv[3]];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 4 });
  await p.goto('file://' + dir + '/folder-v5.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const data = await p.evaluate(() => {
    const panel = document.querySelectorAll('.sheet')[1].querySelector('.panel.model');
    const P = panel.getBoundingClientRect();
    const box = e => { const r = e.getBoundingClientRect(); return { x: r.left - P.left, y: r.top - P.top, w: r.width, h: r.height }; };
    const st = e => { const c = getComputedStyle(e); return { bg: c.backgroundColor, bc: c.borderTopColor, bw: parseFloat(c.borderTopWidth), bs: c.borderTopStyle, r: parseFloat(c.borderTopLeftRadius), color: c.color, size: parseFloat(c.fontSize), weight: c.fontWeight, family: c.fontFamily, lh: c.lineHeight }; };
    const out = { panel: { w: P.width, h: P.height, bg: getComputedStyle(panel).backgroundColor }, shapes: [], texts: [], icons: [] };
    panel.querySelectorAll('.notthis > div, .src2 > div, .model-card, .mc-ic, .ic').forEach(e => out.shapes.push({ ...box(e), ...st(e) }));
    panel.querySelectorAll('h2, .m-lbl, .notthis span, .src2 b, .src2 em, .mc-k, .model-card b, .model-card em').forEach(e => out.texts.push({ t: e.innerText, ...box(e), ...st(e) }));
    let i = 0;
    panel.querySelectorAll('svg').forEach(e => { e.setAttribute('data-ic', 'i' + i); out.icons.push({ id: 'i' + i, ...box(e) }); i++; });
    // het rode kruisje van ::after
    panel.querySelectorAll('.notthis > div').forEach(e => { const r = e.getBoundingClientRect(); out.shapes.push({ x: r.right - P.left - 13, y: r.top - P.top - 9, w: 22, h: 22, bg: 'rgb(179, 38, 30)', bc: 'rgb(0, 35, 51)', bw: 2, bs: 'solid', r: 11, cross: true }); });
    return out;
  });
  for (const ic of data.icons) {
    const el = await p.$(`[data-ic="${ic.id}"]`);
    await el.screenshot({ path: `${out}/${ic.id}.png`, omitBackground: true });
  }
  fs.writeFileSync(`${out}/layout.json`, JSON.stringify(data, null, 1));
  await b.close();
})();
