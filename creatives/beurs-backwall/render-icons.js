const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2400, height: 1700 } });
  await p.goto('file://' + path.resolve(__dirname, 'icons.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.locator('#sheet').screenshot({ path: 'icons.png' }); await b.close(); })();
