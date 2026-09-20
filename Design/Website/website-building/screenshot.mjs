import puppeteer from 'puppeteer';
import { mkdir, readdir } from 'node:fs/promises';
import { join } from 'node:path';

const url = process.argv[2];
const label = process.argv[3];

if (!url) {
  console.error('Usage: node screenshot.mjs <url> [label]');
  process.exit(1);
}
if (!url.includes('localhost') && !url.includes('127.0.0.1')) {
  console.error('Refusing to screenshot a non-localhost URL. Serve the page first with `node serve.mjs`.');
  process.exit(1);
}

const dir = join(process.cwd(), 'temporary screenshots');
await mkdir(dir, { recursive: true });

const existing = await readdir(dir).catch(() => []);
const nums = existing
  .map((f) => f.match(/^screenshot-(\d+)/))
  .filter(Boolean)
  .map((m) => parseInt(m[1], 10));
const n = (nums.length ? Math.max(...nums) : 0) + 1;

const filename = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;
const filePath = join(dir, filename);

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto(url, { waitUntil: 'networkidle0' });
await page.screenshot({ path: filePath, fullPage: true });
await browser.close();

console.log(`Saved: ${filePath}`);
