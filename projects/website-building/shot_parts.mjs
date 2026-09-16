/* Screenshot losse secties, na eerst helemaal doorgescrold te hebben zodat
   alle in-view reveals al gespeeld hebben. Gebruik:
   node shot_parts.mjs "<selector>" naam  [meer selector/naam paren]
   Bestanden komen in ./temporary screenshots/part-<naam>.png */
import puppeteer from 'puppeteer';
import { mkdir } from 'node:fs/promises';
import { join } from 'node:path';

const args = process.argv.slice(2);
const dir = join(process.cwd(), 'temporary screenshots');
await mkdir(dir, { recursive: true });

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto('http://localhost:3000', { waitUntil: 'networkidle0' });

await page.evaluate(async () => {
  const step = 400;
  for (let y = 0; y < document.body.scrollHeight; y += step) {
    window.scrollTo(0, y);
    await new Promise((r) => setTimeout(r, 60));
  }
  window.scrollTo(0, 0);
});
await new Promise((r) => setTimeout(r, 1600));

for (let i = 0; i < args.length; i += 2) {
  const sel = args[i];
  const name = args[i + 1] || `part-${i}`;
  const el = await page.$(sel);
  if (!el) { console.log(`niet gevonden: ${sel}`); continue; }
  const out = join(dir, `part-${name}.png`);
  await el.screenshot({ path: out });
  console.log(`Saved: ${out}`);
}

await browser.close();
