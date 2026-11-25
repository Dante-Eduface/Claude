const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/redesign.html');
  await p.waitForTimeout(400);
  const m = await p.evaluate(() => ({ sh: document.querySelector('.canvas').scrollHeight, gaps: [...document.querySelectorAll('.canvas > *')].map(e => [Math.round(e.getBoundingClientRect().top), Math.round(e.getBoundingClientRect().bottom)]) }));
  console.log(JSON.stringify(m));
  await p.screenshot({ path: 'eduface-redesign.png' });
  await b.close();
})();
