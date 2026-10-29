// node shoot.js a.html a.png [b.html b.png ...] : screenshot plus overloopcheck
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const a = process.argv.slice(2), b = await chromium.launch();
  const pg = await b.newPage({viewport: {width: 1920, height: 1080}});
  for (let i = 0; i < a.length; i += 2) {
    await pg.goto('file://' + path.resolve(a[i]), {waitUntil: 'networkidle'});
    await pg.evaluate(() => document.fonts.ready);
    const over = await pg.evaluate(() => [...document.querySelectorAll('.slide div')]
      .filter(d => d.textContent && d.scrollHeight > d.clientHeight + 2)
      .map(d => d.textContent.slice(0, 40)));
    if (over.length) console.log(a[i + 1], 'OVERLOOP:', over);
    await pg.screenshot({path: a[i + 1]});
  }
  await b.close();
})();
