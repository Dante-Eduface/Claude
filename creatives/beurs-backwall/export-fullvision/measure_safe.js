// Meet alle tekst, logo's en iconen in een drukvariant en toetst ze aan de veiligheidszone.
// Gebruik: node measure_safe.js <html> <breedte> <hoogte> [--edge 210] [--corner 260] [--skip-vertical]
const { chromium } = require('playwright'); const path = require('path');
const [,, file, W, H, ...rest] = process.argv; const W_ = +W, H_ = +H;
const opt = (k, d) => { const i = rest.indexOf(k); return i >= 0 ? +rest[i + 1] : d; };
const EDGE = opt('--edge', 210), CORNER = opt('--corner', 260);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W_, height: H_ } });
  await p.goto('file://' + path.resolve(file)); await p.evaluate(() => document.fonts.ready);
  const items = await p.evaluate(() => {
    const out = []; const wall = document.querySelector('body');
    // tekst: elke tekstnode
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) { const n = walker.currentNode; if (!n.textContent.trim()) continue;
      const r = document.createRange(); r.selectNodeContents(n);
      for (const q of r.getClientRects()) if (q.width > 1 && q.height > 1) out.push({ k: 'tekst', t: n.textContent.trim().slice(0, 40), x0: q.left, y0: q.top, x1: q.right, y1: q.bottom }); }
    // logo's en iconen met inhoud: img en svg (niet de decoratieve achtergrondlagen)
    for (const e of document.querySelectorAll('img,svg')) { const q = e.getBoundingClientRect(); if (q.width < 4) continue;
      if (e.closest('#d')) continue;   // gevel: halftone-stippen zijn beeld, geen inhoud
      out.push({ k: e.tagName.toLowerCase(), t: (e.getAttribute('src') || 'svg').split('/').pop(), x0: q.left, y0: q.top, x1: q.right, y1: q.bottom }); }
    return out; });
  const bad = []; let minL = 1e9, minR = 1e9, minT = 1e9, minB = 1e9;
  for (const i of items) {
    minL = Math.min(minL, i.x0); minR = Math.min(minR, W_ - i.x1); minT = Math.min(minT, i.y0); minB = Math.min(minB, H_ - i.y1);
    const why = [];
    if (i.x0 < EDGE) why.push(`links ${i.x0.toFixed(0)}`); if (W_ - i.x1 < EDGE) why.push(`rechts ${(W_ - i.x1).toFixed(0)}`);
    if (i.y0 < EDGE) why.push(`boven ${i.y0.toFixed(0)}`); if (H_ - i.y1 < EDGE) why.push(`onder ${(H_ - i.y1).toFixed(0)}`);
    const inC = (x0, x1, y0, y1) => i.x0 < x1 && i.x1 > x0 && i.y0 < y1 && i.y1 > y0;
    if (inC(0, CORNER, 0, CORNER) || inC(W_ - CORNER, W_, 0, CORNER) || inC(0, CORNER, H_ - CORNER, H_) || inC(W_ - CORNER, W_, H_ - CORNER, H_)) why.push('hoekzone');
    if (why.length) bad.push({ ...i, why: why.join(', ') });
  }
  console.log(`${items.length} elementen gemeten. Kleinste afstand tot rand (mm op ware grootte): links ${minL.toFixed(0)}, rechts ${minR.toFixed(0)}, boven ${minT.toFixed(0)}, onder ${minB.toFixed(0)}`);
  console.log(`Eisen: >= ${EDGE} van elke rand (200 vanaf snijrand + 10 bleed), hoeken ${CORNER}.`);
  if (!bad.length) console.log('Geen enkel element in de verboden zone.');
  else { console.log(`${bad.length} elementen in de verboden zone:`); for (const x of bad.slice(0, 30)) console.log(`  ${x.k} "${x.t}" (${x.why})`); }
  require('fs').writeFileSync(path.join(path.dirname(path.resolve(file)), 'measure_' + path.basename(file, '.html') + '.json'), JSON.stringify({ items, bad }, null, 1));
  await b.close();
})();
