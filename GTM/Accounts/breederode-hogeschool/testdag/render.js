const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/kalibreren-werkwijze.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: 'kalibreren-werkwijze.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '18mm', bottom: '16mm', left: '16mm', right: '16mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.4pt;color:#5b7480;padding:0 16mm;display:flex;justify-content:space-between;">
      <span>Eduface &middot; kalibreren</span>
      <span>pagina <span class="pageNumber"></span> van <span class="totalPages"></span></span></div>`,
  });
  await b.close();
})();
