"""Rendert alle benodigde icons als transparante PNG, per kleurtoon."""
import subprocess, os
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TONES = {'amber': 'E07B00', 'green': '007B54', 'navy': '002333'}

ICONS = {
 'verschillen': '<path d="M3 6h12M3 12h18M3 18h8"/>',
 'variatie':    '<path d="M4 20V11M10 20V4M16 20v-6M22 20V8"/>',
 'wisselend':   '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/><path d="M12 9v4M12 17h.01"/>',
 'ongelijk':    '<path d="M4 9h16M4 15h16"/><path d="m19 4-14 16"/>',
 'check':       '<path d="M20 6 9 17l-5-5"/>',
 'studenten':   '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>',
 'docenten':    '<path d="M2 3h20v12H2z"/><path d="M12 15v6M8 21h8"/><path d="m7 11 3-3 2 2 4-4"/>',
 'inleveren':   '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="M12 18v-6M9 15l3-3 3 3"/>',
 'voorstel':    '<path d="m12 3 1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9Z"/><path d="M19 15v4M17 17h4"/>',
 'aftekenen':   '<path d="M3 17c3-6 6 3 9-3s5 1 9-5"/><path d="M4 21h16"/>',
 'model':       '<path d="M12 3a4 4 0 0 0-4 4 3 3 0 0 0-1 5.8V17a4 4 0 0 0 8 0v-4.2A3 3 0 0 0 16 7a4 4 0 0 0-4-4Z"/><path d="M12 8v9"/>',
 'rubric':      '<path d="M4 5h16M4 12h16M4 19h16"/><path d="m6 5 1 1 2-2M6 12l1 1 2-2M6 19l1 1 2-2"/>',
 'aanbieder':   '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
 'instelling':  '<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>',
 'cijfers':     '<path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h3M8 16h3M15 12v4M13 14h4"/>',
 'iama':        '<path d="M9 3h6v3H9z"/><path d="M6 5H5a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1"/><path d="m8 14 2 2 5-5"/>',
 'pilot':       '<path d="M5 19c0-4 3-9 9-11 3-1 5-1 5-1s0 2-1 5c-2 6-7 9-11 9Z"/><path d="M9 15a3 3 0 0 1 0-4"/><path d="M5 19s-1 1-1 2 2 0 2 0"/>',
 'gesprek':     '<path d="M21 12a8 8 0 0 1-8 8H7l-4 3V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8Z"/><path d="M9 11h6M9 15h4"/>',
}

os.makedirs('assets', exist_ok=True)
for name, paths in ICONS.items():
    for tone, hexc in TONES.items():
        out = f'assets/icon-{name}-{tone}.png'
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
print(f'{len(ICONS)*len(TONES)} icons gerenderd')

# Windesheim-logo op wit en op navy
for naam, bg in [('windesheim', 'transparent'), ('windesheim-wit', '#002333')]:
    tmp = 'assets/_wh.html'
    open(tmp, 'w').write(
        f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:{bg}}}'
        'img{display:block;height:240px;width:auto}</style></head><body><img src="../windesheim.svg"></body></html>')
    subprocess.run([CHROME, '--headless', '--disable-gpu', f'--screenshot=assets/{naam}.png',
                    '--window-size=520,240', '--default-background-color=00000000',
                    '--hide-scrollbars', '--virtual-time-budget=2500', tmp], capture_output=True)
    os.remove(tmp)
print('logo-varianten gerenderd')
