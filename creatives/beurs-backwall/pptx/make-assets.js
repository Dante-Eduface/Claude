// Rendert de plaatjes die in de pptx als afbeelding blijven: achtergrond, witte logo's, iconen, chevron.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const root = path.resolve(__dirname, '..');
const N='#002333', G='#00e075', W='#fff';
const sv=(inner)=>`<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">${inner}</svg>`;
const icons = {
 'icon-teacher': sv(`<circle cx="150" cy="108" r="64" fill="none" stroke="${W}" stroke-width="30"/><path d="M36,340 C36,236 264,236 264,340" fill="none" stroke="${W}" stroke-width="30" stroke-linecap="round"/><circle cx="312" cy="294" r="62" fill="${G}"/><polyline points="282,294 304,316 342,270" fill="none" stroke="${N}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>`),
 'icon-bubbles': sv(`<rect x="30" y="34" width="230" height="104" rx="38" fill="none" stroke="${W}" stroke-width="26"/><rect x="60" y="68" width="110" height="18" rx="9" fill="${W}"/><rect x="140" y="156" width="230" height="104" rx="38" fill="rgba(255,255,255,.14)" stroke="${W}" stroke-width="26"/><rect x="172" y="190" width="150" height="18" rx="9" fill="${W}"/><rect x="30" y="278" width="230" height="104" rx="38" fill="none" stroke="${W}" stroke-width="26"/><rect x="60" y="312" width="84" height="18" rx="9" fill="${G}"/>`),
 'icon-sheets': sv(`<rect x="130" y="24" width="220" height="270" rx="30" fill="none" stroke="${W}" stroke-width="22" opacity=".4"/><rect x="90" y="64" width="220" height="270" rx="30" fill="none" stroke="${W}" stroke-width="22" opacity=".7"/><rect x="44" y="108" width="220" height="270" rx="30" fill="${N}" stroke="${W}" stroke-width="26"/>${[160,222,284].map(y=>`<polyline points="76,${y} 92,${y+16} 118,${y-14}" fill="none" stroke="${G}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><rect x="134" y="${y-8}" width="98" height="14" rx="7" fill="${W}"/>`).join('')}`),
 'chevron': `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 30 30"><polyline points="7,11 15,20 23,11" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>`
};
for (const f of ['openai','googlegemini','claude']) {
  const s = fs.readFileSync(path.join(root,'assets/logos',f+'.svg'),'utf8').replace(/fill="#[0-9a-fA-F]+"/,'fill="#ffffff"').replace('<svg ','<svg width="400" height="400" ');
  icons['logo-'+f] = s;
}
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 400, height: 400 } });
  for (const [n, svg] of Object.entries(icons)) {
    await p.setContent(`<body style="margin:0;background:transparent">${svg}</body>`);
    await p.screenshot({ path: path.join(__dirname,'assets',n+'.png'), omitBackground: true, clip:{x:0,y:0,width:400,height:400} });
  }
  // achtergrond: alleen de verloop, op volle wandmaat
  const q = await b.newPage({ viewport: { width: 2954, height: 2520 } });
  await q.setContent(`<body style="margin:0"><div id="w" style="width:2954px;height:2520px;background:radial-gradient(ellipse 80% 45% at 90% 52%, #f9f8f7 0%, rgba(249,248,247,0) 100%),linear-gradient(180deg,#dce7ee 0%,#e2edf1 20%,#ecf3f5 40%,#f4f6f6 55%,#eff3f3 70%,#e4edf1 90%,#dde8ee 100%)"></div></body>`);
  await q.locator('#w').screenshot({ path: path.join(__dirname,'assets','bg.png') });
  await b.close();
})();
