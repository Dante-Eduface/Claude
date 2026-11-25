// Rendert een drukvariant (1 px = 1 mm) naar een PDF op 25% schaal. Gebruik: node export_pdf.js <html> <b_mm> <h_mm> <uit.pdf>
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [,, file, Wmm, Hmm, out] = process.argv; const W = +Wmm, H = +Hmm; const S = 0.25;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.resolve(file)); await p.evaluate(() => document.fonts.ready);
  const k = S * 96 / 25.4;      // CSS-pixels per ontwerp-mm bij 25%
  await p.pdf({ path: out, width: `${W * S}mm`, height: `${H * S}mm`, scale: k, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
  await b.close();
})();
