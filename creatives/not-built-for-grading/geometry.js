const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + process.cwd() + '/redesign.html');
  await p.waitForTimeout(300);
  const g = await p.evaluate(() => {
    const r = e => { const b = e.getBoundingClientRect(); return [b.left, b.top, b.width, b.height].map(v => Math.round(v * 10) / 10); };
    const all = s => [...document.querySelectorAll(s)].map(r);
    return { h1: r(document.querySelector('h1')), names: r(document.querySelector('.names')),
      q: all('.q'), who: all('.who'), tick: all('.tick'), arrow: all('.arrow svg'), a: all('.a > span:last-child'),
      proof: r(document.querySelector('.proof')), kicker: r(document.querySelector('.kicker')), num: r(document.querySelector('.num')),
      cap: r(document.querySelector('.cap')), dev: r(document.querySelector('.dev')), lbl: r(document.querySelector('.lbl')),
      lms: r(document.querySelector('img.lms')), logo: r(document.querySelector('img.logo')) };
  });
  require('fs').writeFileSync('geometry.json', JSON.stringify(g, null, 1));
  console.log(JSON.stringify(g));
  await b.close();
})();
