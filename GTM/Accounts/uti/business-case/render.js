// Usage: node render.js <input.html> <output.pdf>
const { chromium } = require('playwright');
(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + input, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: output, format: 'Letter', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
