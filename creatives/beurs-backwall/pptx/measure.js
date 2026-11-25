// Meet de huidige backwall.html uit (posities in wandpixels = mm) en rendert de plaatjes voor de pptx.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const out = {}; const A = (n) => path.join(__dirname, 'assets2', n);
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 2954, height: 2520 }, deviceScaleFactor: 3 });
  await page.goto('file://' + path.resolve(__dirname, '..', 'backwall.html')); await page.evaluate(() => document.fonts.ready);
  const sel = ['.q','.e','.q .it','.q .qt','.q .who','.q .qb','.tools .lab','.redbox','.tl','.tl img','.x','.e .it','.e .eh','.arrow','.own','.own .top','.own .top img','.own .top .ai','.own .n','.own .l','.own .d','.lms .lab','.lms img','.logo'];
  out.rects = await page.evaluate((sel) => { const r = {}; for (const s of sel) r[s] = [...document.querySelectorAll(s)].map(e => { const b = e.getBoundingClientRect(); return [b.x, b.y, b.width, b.height]; }); return r; }, sel);
  // transparant maken zodat alleen het icoon zelf in beeld komt
  await page.addStyleTag({ content: 'html,body,.wall,.q,.e,.it,.own,.redbox,.tl{background:transparent!important;box-shadow:none!important;border:none!important}' });
  const shoot = async (loc, name) => { await loc.screenshot({ path: A(name), omitBackground: true }); };
  for (const [i, el] of (await page.locator('.q .it svg').all()).entries()) await shoot(el, `q-icon-${i+1}.png`);
  for (const [i, el] of (await page.locator('.e .it svg').all()).entries()) await shoot(el, `e-icon-${i+1}.png`);
  for (const [i, el] of (await page.locator('.tl img').all()).entries()) await shoot(el, `tool-${i+1}.png`);
  await shoot(page.locator('.x').first(), 'x.png');
  await shoot(page.locator('.arrow'), 'arrow.png');
  for (const [i, el] of (await page.locator('.lms img').all()).entries()) await shoot(el, `lms-${i+1}.png`);
  fs.writeFileSync(path.join(__dirname, 'measured.json'), JSON.stringify(out, null, 1));
  await b.close();
  console.log(Object.entries(out.rects).map(([k, v]) => `${k}: ${v.length}`).join('\n'));
})();
