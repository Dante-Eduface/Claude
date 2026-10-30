// Haalt het linker binnenpaneel (.panel.model) uit een folder-HTML: vormen, tekst met runs, en iconen als transparante PNG.
// Gebruik: node extract.js <folder.html> <uitmap>
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [file, out] = [path.resolve(process.argv[2]), path.resolve(process.argv[3])];
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 4 });
  await p.goto('file://' + file, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const data = await p.evaluate(() => {
    const panel = document.querySelectorAll('.sheet')[1].querySelector('.panel.model');
    const P = panel.getBoundingClientRect();
    const box = e => { const r = e.getBoundingClientRect(); return { x: r.left - P.left, y: r.top - P.top, w: r.width, h: r.height }; };
    const font = e => { const c = getComputedStyle(e); return { color: c.color, size: parseFloat(c.fontSize), weight: c.fontWeight, family: c.fontFamily, lh: c.lineHeight, align: c.textAlign }; };
    const out = { panel: { w: P.width, h: P.height, bg: getComputedStyle(panel).backgroundColor }, shapes: [], texts: [], icons: [] };
    const consumed = new Set(); let n = 0;
    for (const e of panel.querySelectorAll('*')) {
      if (e.closest('svg') && e.tagName !== 'svg') continue;
      const c = getComputedStyle(e);
      if (e.tagName === 'svg' || e.tagName === 'IMG') { e.setAttribute('data-ic', 'i' + n); out.icons.push({ id: 'i' + n, ...box(e) }); n++; continue; }
      const bg = c.backgroundColor, bw = parseFloat(c.borderTopWidth);
      if (bg !== 'rgba(0, 0, 0, 0)' || (bw > 0 && c.borderTopStyle !== 'none'))
        out.shapes.push({ ...box(e), bg, bc: c.borderTopColor, bw, bs: c.borderTopStyle, r: parseFloat(c.borderTopLeftRadius) });
      if (consumed.has(e)) continue;
      const direct = [...e.childNodes].some(k => k.nodeType === 3 && k.textContent.trim());
      if (!direct) continue;
      const runs = [];
      for (const k of e.childNodes) {
        if (k.nodeType === 3) { if (k.textContent.trim() || runs.length) runs.push({ t: k.textContent.replace(/\s+/g, ' '), ...font(e) }); }
        else if (k.tagName === 'BR') runs.push({ br: true });
        else if (k.nodeType === 1 && !['svg', 'IMG'].includes(k.tagName) && getComputedStyle(k).display.startsWith('inline') && !k.classList.contains('ic')) {
          consumed.add(k); k.querySelectorAll('*').forEach(x => consumed.add(x));
          runs.push({ t: k.innerText, ...font(k) });
        }
      }
      if (runs.length) out.texts.push({ ...box(e), ...font(e), runs });
    }
    // het rode kruisje zit in ::after, dus apart
    panel.querySelectorAll('.notthis > div').forEach(e => { const r = e.getBoundingClientRect(); out.shapes.push({ x: r.right - P.left - 13, y: r.top - P.top - 9, w: 22, h: 22, bg: 'rgb(179, 38, 30)', bc: 'rgb(0, 35, 51)', bw: 2, bs: 'solid', r: 11, cross: true }); });
    return out;
  });
  for (const ic of data.icons) await (await p.$(`[data-ic="${ic.id}"]`)).screenshot({ path: `${out}/${ic.id}.png`, omitBackground: true });
  fs.writeFileSync(`${out}/layout.json`, JSON.stringify(data, null, 1));
  await b.close();
})();
