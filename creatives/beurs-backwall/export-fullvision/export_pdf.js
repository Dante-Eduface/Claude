// Rendert een drukvariant (1 px = 1 mm) naar een PDF op 25% schaal. Gebruik: node export_pdf.js <html> <b_mm> <h_mm> <uit.pdf>
// Zachte schaduwen worden eerst als PNG met alfakanaal gerenderd en als gewone afbeelding ingevoegd, zodat het PDF geen
// luminosity-softmasks bevat (die tonen sommige programma's als grijze vlakken).
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const [,, file, Wmm, Hmm, out] = process.argv; const W = +Wmm, H = +Hmm; const S = 0.25; const url = 'file://' + path.resolve(file);
  const b = await chromium.launch(); const tmp = path.join(path.dirname(out), 'schaduw'); fs.mkdirSync(tmp, { recursive: true });
  const hasShadows = fs.readFileSync(file, 'utf8').includes('box-shadow');
  const layers = {};
  if (hasShadows) {
    const BASE = '*{background:transparent!important;color:transparent!important;border-color:transparent!important;outline-color:transparent!important;filter:none!important}' +
                 'img,svg{visibility:hidden!important} html,body,.wall{background:transparent!important}';
    const shots = { A: '.m1,.m2{box-shadow:none!important}', B: '.pl,.pr,.ai{box-shadow:none!important}' };
    const q = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
    for (const [k, css] of Object.entries(shots)) {
      await q.goto(url); await q.evaluate(() => document.fonts.ready);
      await q.addStyleTag({ content: BASE + css });
      const f = path.join(tmp, `laag_${k}.png`); await q.screenshot({ path: f, omitBackground: true, clip: { x: 0, y: 0, width: W, height: H } }); layers[k] = f;
    }
    await q.close();
  }
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto(url); await p.evaluate(() => document.fonts.ready);
  if (hasShadows) {
    await p.addStyleTag({ content: '.pl,.pr,.ai,.m1,.m2{box-shadow:none!important}' });
    await p.evaluate(({ A, B }) => {
      const mk = (src, l, t) => { const i = document.createElement('img'); i.src = src; i.style.cssText = `position:absolute;left:${l}px;top:${t}px;width:${innerWidth}px;height:${innerHeight}px;pointer-events:none;z-index:0`; return i; };
      const lc = document.getElementById('layer-content'); lc.style.position = 'relative'; lc.insertBefore(mk(A, 0, 0), lc.firstChild);   // laag A: onder de grote vlakken
      const mock = document.querySelector('.mock'); const r = mock.getBoundingClientRect();
      mock.style.position = 'relative'; mock.insertBefore(mk(B, -r.left, -r.top), mock.firstChild);                                   // laag B: onder de kaartjes in het reviewscherm
      document.querySelectorAll('.m1,.m2').forEach(e => { e.style.position = 'relative'; e.style.zIndex = 1; });
    }, { A: 'file://' + layers.A, B: 'file://' + layers.B });
    await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))));
  }
  const k = S * 96 / 25.4;      // CSS-pixels per ontwerp-mm bij 25%
  await p.pdf({ path: out, width: `${W * S}mm`, height: `${H * S}mm`, scale: k, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
  await b.close();
})();
