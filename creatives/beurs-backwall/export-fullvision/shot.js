const { chromium } = require('playwright'); const path = require('path');
(async () => { const [,, file, W, H, out] = process.argv; const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +W, height: +H } });
  await p.goto('file://' + path.resolve(file)); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: +W, height: +H } }); await b.close(); })();
