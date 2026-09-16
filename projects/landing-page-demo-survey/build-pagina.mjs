/* Bouwt pagina.html: afgewerkte secties in kleur, de rest als wireframe.
   CSS van elk stuk wordt gescoped onder een wrapper-class, zodat .card en .h2
   uit verschillende secties elkaar niet overschrijven. */
import { readFileSync, writeFileSync } from 'node:fs';

const grab = (file) => {
  const s = readFileSync(file, 'utf8');
  const css = s.slice(s.indexOf('<style>') + 7, s.indexOf('</style>'));
  const body = s.slice(s.indexOf('<body>') + 6, s.indexOf('<div class="notes">') > -1 ? s.indexOf('<div class="notes">') : s.indexOf('</body>'));
  return { css, body };
};

/* scope: zet `.scope ` voor elke selector, behalve globals en keyframes */
function scopeCss(css, scope) {
  const out = [];
  let i = 0;
  while (i < css.length) {
    // commentaar
    if (css.startsWith('/*', i)) { const e = css.indexOf('*/', i); out.push(css.slice(i, e + 2)); i = e + 2; continue; }
    const brace = css.indexOf('{', i);
    if (brace === -1) { out.push(css.slice(i)); break; }
    const sel = css.slice(i, brace).trim();
    // blok met haakjes vinden
    let depth = 0, j = brace;
    for (; j < css.length; j++) { if (css[j] === '{') depth++; else if (css[j] === '}') { depth--; if (!depth) break; } }
    const block = css.slice(brace + 1, j);
    if (sel.startsWith('@media') || sel.startsWith('@supports')) {
      out.push(`\n${sel} {${scopeCss(block, scope)}}`);
    } else if (sel.startsWith('@') || sel === ':root' || /^(html|body|\*|\*,)/.test(sel)) {
      // globals ongemoeid laten, behalve body-achtige die we neutraliseren
      if (sel === ':root' || sel.startsWith('@')) out.push(`\n${sel} {${block}}`);
    } else {
      const scoped = sel.split(',').map(s => `${scope} ${s.trim()}`).join(', ');
      out.push(`\n${scoped} {${block}}`);
    }
    i = j + 1;
  }
  return out.join('');
}

const wf = readFileSync('wireframe.html', 'utf8');
const wfCss = wf.slice(wf.indexOf('<style>') + 7, wf.indexOf('</style>'));
const wfSection = (from, to) => wf.slice(wf.indexOf(from), to ? wf.indexOf(to) : wf.indexOf('<div class="foot">'));

const hero = grab('proef-hero.html');
const pijn = grab('proef-pijn.html');
const bewijs = grab('proef-bewijsblok.html');

const parts = [
  { id: 'hero',   klaar: true,  css: hero.css,   html: hero.body },
  { id: 'pijn',   klaar: true,  css: pijn.css,   html: pijn.body },
  { id: 'hoe',    klaar: false, html: wfSection('<!-- 3 HOW', '<!-- 4 PROOF') },
  { id: 'bewijs', klaar: true,  css: bewijs.css, html: bewijs.body },
  { id: 'prod',   klaar: false, html: wfSection('<!-- 5 PRODUCTS', '<!-- 6 FIT') },
  { id: 'fit',    klaar: false, html: wfSection('<!-- 6 FIT', '<!-- 7 FAQ') },
  { id: 'faq',    klaar: false, html: wfSection('<!-- 7 FAQ', '<!-- 8 BOOK') },
  { id: 'book',   klaar: false, html: wfSection('<!-- 8 BOOK') },
];

const css = parts.filter(p => p.klaar).map(p => scopeCss(p.css, `.s-${p.id}`)).join('\n')
  + '\n' + scopeCss(wfCss, '.s-wire');

const body = parts.map(p => {
  const label = p.klaar ? '' : `<div class="wire-flag"><span>Wireframe</span> nog niet uitgewerkt</div>`;
  return `<div class="${p.klaar ? 's-' + p.id : 's-wire'}" data-sec="${p.id}">\n${label}\n${p.html}\n</div>`;
}).join('\n\n');

const page = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Eduface landingspagina, samengesteld</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700;800&family=Inter:wght@400;450;500;600;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; scroll-behavior: smooth; }
body { font-family: "Inter", ui-sans-serif, system-ui, sans-serif; background: #f3f7f8; color: #002333; }
img { display: block; max-width: 100%; }
a { text-decoration: none; color: inherit; }
:focus-visible { outline: 2px solid #00e075; outline-offset: 3px; }
[data-sec] { position: relative; }
.wire-flag { position: absolute; top: 14px; right: 18px; z-index: 40; display: inline-flex; align-items: center; gap: 8px; background: #002333; color: #fff; border-radius: 999px; padding: 6px 14px; font-size: 12px; }
.wire-flag span { font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #00e075; }
${css}
</style>
</head>
<body>
${body}
</body>
</html>`;

writeFileSync('pagina.html', page);
console.log('pagina.html gebouwd,', page.length, 'tekens');
