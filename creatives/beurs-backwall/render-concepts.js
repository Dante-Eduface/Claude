const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2954, height: 2520 } });
  for (const n of [1,2,3,4,5]) {
    await p.goto('file://' + path.resolve(__dirname, 'concepts.html') + '?c=' + n);
    await p.evaluate(() => document.fonts.ready);
    await p.locator('#wall').screenshot({ path: `concept-${n}.png` });
  }
  await b.close(); })();
