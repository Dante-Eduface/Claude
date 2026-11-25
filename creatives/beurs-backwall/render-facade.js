const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3020, height: 350 } });
  await p.goto('file://' + path.resolve(__dirname, 'facade.html')); await p.evaluate(() => document.fonts.ready);
  await p.locator('#f').screenshot({ path: 'facade.png' }); await b.close(); })();
