const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/onvoldoende-voorbeeld-cat-poh.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({
    path: 'onvoldoende-voorbeeld-cat-poh.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '15mm', bottom: '16mm', left: '15mm', right: '15mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:Arial,sans-serif;font-size:7.6pt;color:#4F6269;padding:0 15mm;display:flex;justify-content:space-between;">
      <span>CAT Praktijkondersteuner Huisartsenzorg &middot; 30 september 2026 &middot; Dante Torbed, Eduface</span>
      <span>pagina <span class="pageNumber"></span> van <span class="totalPages"></span></span></div>`,
  });
  await b.close();
})();
