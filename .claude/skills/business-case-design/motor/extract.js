// Leest de opmaak van elke HTML-pagina uit (vlakken, tekst, iconen) als bron voor de pptx.
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');
const pages = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const out = [];
  for (const [i, file] of pages.entries()) {
    const p = await b.newPage({viewport: {width: 794, height: 1123}, deviceScaleFactor: 4});
    await p.goto('file://' + path.resolve(file));
    await p.waitForTimeout(1500);
    const data = await p.evaluate(() => {
      const items = [], svgs = [];
      const col = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
        const [r,g,b_,a='1'] = m[1].split(',').map(s=>s.trim()); if (+a === 0) return null;
        return {hex: [r,g,b_].map(v=>(+v).toString(16).padStart(2,'0')).join(''), a: +a}; };
      const box = el => { const r = el.getBoundingClientRect(); return {x:r.left,y:r.top,w:r.width,h:r.height}; };
      const consumed = new Set();
      // Paginakleur als eerste vlak, zodat donkere pagina's ook in de pptx donker zijn
      const bodyBg = col(getComputedStyle(document.body).backgroundColor);
      if (bodyBg && bodyBg.hex !== 'ffffff') items.push({k:'rect', x:0, y:0, w:794, h:1123, fill: bodyBg, line:null, lw:0, r:0});
      const all = [...document.body.querySelectorAll('*')];
      for (const el of all) {
        if (el.closest('svg') && el.tagName !== 'svg') continue;
        const cs = getComputedStyle(el), r = box(el);
        if (r.w === 0 || r.h === 0 || cs.display === 'none') continue;
        if (el.tagName === 'svg') { svgs.push({...r, idx: svgs.length}); el.dataset.svgIdx = svgs.length-1; items.push({k:'svg', ...r, idx: svgs.length-1}); continue; }
        const bg = col(cs.backgroundColor), bw = parseFloat(cs.borderTopWidth), bc = col(cs.borderTopColor);
        const bl = parseFloat(cs.borderLeftWidth), blc = col(cs.borderLeftColor);
        const rad = parseFloat(cs.borderTopLeftRadius) || 0;
        const sides = ['Top','Right','Bottom','Left'].map(k => parseFloat(cs['border'+k+'Width']));
        const full = sides.every(v => v > 0) && bc;
        if (bg || full) items.push({k:'rect', ...r, fill: bg, line: full ? bc : null, lw: full ? bw : 0, r: rad});
        if (!full && sides[0] > 0 && bc) items.push({k:'rect', x:r.x, y:r.y, w:r.w, h:sides[0], fill: bc, line:null, lw:0, r:0});
        if (!full && bl > 0 && blc) items.push({k:'rect', x:r.x, y:r.y, w:bl, h:r.h, fill: blc, line:null, lw:0, r:0});
        if (consumed.has(el)) continue;
        const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (!hasText) continue;
        // Eén tekstvak per blok, inline kinderen worden runs
        const runs = [];
        const st = (e) => { const c = getComputedStyle(e); return {font: c.fontFamily.split(',')[0].replace(/"/g,'').trim(),
          size: parseFloat(c.fontSize), bold: +c.fontWeight >= 600, color: col(c.color).hex, upper: c.textTransform === 'uppercase'}; };
        const walk = (node, owner) => { for (const n of node.childNodes) {
          if (n.nodeType === 3) { const t = n.textContent.replace(/\s+/g,' '); if (t.trim() || runs.length) runs.push({t, ...st(owner)}); }
          else if (n.nodeType === 1 && getComputedStyle(n).display.startsWith('inline') && n.tagName !== 'svg') { consumed.add(n); walk(n, n); }
          else if (n.nodeType === 1 && getComputedStyle(n).display === 'block' && n.tagName === 'B') { consumed.add(n); runs.push({t:'\n', ...st(n)}); walk(n, n); runs.push({t:'\n', ...st(n)}); }
        } };
        walk(el, el);
        const range = document.createRange(); range.selectNodeContents(el); const tr = range.getBoundingClientRect();
        const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2;
        items.push({k:'text', x: tr.left, y: tr.top, w: Math.max(tr.width, 1), h: tr.height, blockW: r.w, runs,
                    align: cs.textAlign === 'right' ? 'right' : cs.textAlign === 'center' ? 'center' : 'left', lh,
                    ls: parseFloat(cs.letterSpacing) || 0});
      }
      return {items, svgs, dark: document.body.classList.contains('dark')};
    });
    for (const s of data.svgs) {
      const el = (await p.$$('svg'))[s.idx];
      const f = `svg-${i}-${s.idx}.png`;
      await el.screenshot({path: f, omitBackground: true});
      s.file = f;
    }
    data.items.forEach(it => { if (it.k === 'svg') it.file = data.svgs[it.idx].file; });
    out.push({dark: data.dark, items: data.items, nr: parseInt(path.basename(file)) || i + 1});
    await p.close();
  }
  fs.writeFileSync('layout.json', JSON.stringify(out));
  await b.close();
})();
