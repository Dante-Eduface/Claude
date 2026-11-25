// Gebruik: node render.js [uitvoer.png]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2] || 'backwall.png';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2954, height: 2520 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(__dirname, 'backwall.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.locator('#wall').screenshot({ path: out });
  await browser.close();
})();
