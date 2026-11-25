// Meet de fascia-drukvariant uit en rendert de achtergrond (verloop + stippen) zonder tekst en logo.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3020, height: 350 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(__dirname, '..', 'facade-print.html')); await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => { const q = s => [...document.querySelectorAll(s)].map(e => { const b = e.getBoundingClientRect(); return [b.x, b.y, b.width, b.height]; });
    return { logo: q('.logo')[0], sep: q('.sep'), h: q('.h')[0], l: q('.stand .l')[0], n: q('.stand .n')[0] }; });
  fs.writeFileSync(path.join(__dirname, 'measured_facade.json'), JSON.stringify(r, null, 1));
  await p.addStyleTag({ content: '.row{visibility:hidden!important}' });
  await p.locator('#f').screenshot({ path: path.join(__dirname, 'assets3', 'gevel-bg.png'), clip: { x: 0, y: 0, width: 3020, height: 350 } });
  await b.close(); console.log(JSON.stringify(r));
})();
