"""Rendert de extra logo's en de nieuwe icons naar transparante PNG."""
import subprocess, os
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TONES = {'amber': 'E07B00', 'green': '007B54', 'navy': '002333'}

NIEUW = {
 'data':     '<path d="M3 5c0-1.1 4-2 9-2s9 .9 9 2-4 2-9 2-9-.9-9-2Z"/><path d="M3 5v6c0 1.1 4 2 9 2s9-.9 9-2V5"/><path d="M3 11v6c0 1.1 4 2 9 2s9-.9 9-2v-6"/>',
 'pen':      '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
 'boek':     '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/><path d="M9 7h7"/>',
 'filepen':  '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h5"/><path d="M14 2v6h6"/><path d="M18.4 13.6a1.7 1.7 0 0 1 2.4 2.4L16 21l-3 .8.8-3Z"/>',
 'lagen':    '<path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/>',
 'usercheck':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m16 11 2 2 4-4"/>',
 'lamp':     '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V18h8v-3.3A7 7 0 0 0 12 2Z"/>',
 'historie': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l3 2"/>',
 'klok':     '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}

for name, paths in NIEUW.items():
    for tone, hexc in TONES.items():
        out = f'assets/icon-{name}-{tone}.png'
        if os.path.exists(out):
            continue
        tmp = f'assets/_{name}.html'
        open(tmp, 'w').write(
            '<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}svg{display:block;width:296px;height:296px}'
            '</style></head><body>'
            f'<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#{hexc}" '
            f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{paths}</svg></body></html>')
        subprocess.run([CHROME, '--headless', '--disable-gpu', f'--screenshot={out}',
                        '--window-size=296,296', '--default-background-color=00000000',
                        '--hide-scrollbars', '--virtual-time-budget=1500', tmp], capture_output=True)
        os.remove(tmp)
print('icons klaar')

for svg, hoogte, breedte in [('bath-spa', 200, 700), ('leiden', 200, 700), ('radboud', 200, 700)]:
    tmp = 'assets/_logo.html'
    open(tmp, 'w').write(
        f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:transparent}}'
        f'img{{display:block;height:{hoogte}px;width:auto}}</style></head><body>'
        f'<img src="{svg}.svg"></body></html>')
    subprocess.run([CHROME, '--headless', '--disable-gpu', f'--screenshot=assets/{svg}.png',
                    f'--window-size={breedte},{hoogte}', '--default-background-color=00000000',
                    '--hide-scrollbars', '--virtual-time-budget=2500', tmp],
                   capture_output=True, cwd='assets')
    os.remove(tmp)
print('logos klaar')
