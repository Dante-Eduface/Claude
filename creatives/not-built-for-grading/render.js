// PNG-preview (2x) + vector-PDF op echte maat 2954 x 2520 mm
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1477, height: 1260 }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/redesign.html');
  await p.waitForTimeout(400);
  console.log(JSON.stringify(await p.evaluate(() => ({ sh: document.querySelector('.canvas').scrollHeight, sections: [...document.querySelectorAll('.canvas > *')].map(e => [Math.round(e.getBoundingClientRect().top), Math.round(e.getBoundingClientRect().bottom)]) }))));
  await p.screenshot({ path: 'eduface-redesign.png' });
  if (process.argv[2] === 'pdf') {
    await p.addStyleTag({ content: 'html{zoom:7.5594} @page{margin:0}' });
    await p.pdf({ path: 'eduface-redesign-2954x2520mm.pdf', width: '2954mm', height: '2520mm', printBackground: true, pageRanges: '1' });
  }
  await b.close();
})();
