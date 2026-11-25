// Gebruik: node render.js [uitvoer.png] [indeling: 1 of 2, leeg = alleen logo]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2] || 'backwall.png';
  const v = process.argv[3] || '';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2954, height: 2520 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(__dirname, 'backwall.html') + (v ? '?v=' + v : ''));
  await page.evaluate(() => document.fonts.ready);
  await page.locator('#wall').screenshot({ path: out });
  await browser.close();
})();
