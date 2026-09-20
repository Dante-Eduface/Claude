import puppeteer from 'puppeteer';
const OUT = process.argv[2];
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto('https://habitline-wbs.framer.website/', { waitUntil: 'networkidle0', timeout: 60000 });
await new Promise(r => setTimeout(r, 1000));

// scroll down slowly to trigger scroll-reveal animations
const height = await page.evaluate(() => document.body.scrollHeight);
let y = 0;
while (y < height) {
  await page.evaluate((yy) => window.scrollTo(0, yy), y);
  await new Promise(r => setTimeout(r, 350));
  y += 500;
}
await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
await new Promise(r => setTimeout(r, 800));
await page.evaluate(() => window.scrollTo(0, 0));
await new Promise(r => setTimeout(r, 500));

await page.screenshot({ path: `${OUT}/full2.png`, fullPage: true });
const dims = await page.evaluate(() => ({ h: document.body.scrollHeight, w: document.body.scrollWidth }));
console.log(JSON.stringify(dims));
await browser.close();
