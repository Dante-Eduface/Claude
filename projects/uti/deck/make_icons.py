"""Rendert de icons voor het UTI-deck als transparante PNG, per merktoon.

Zelfde aanpak als het Windesheim-deck: één SVG-pad per begrip, in elke toon
uitgerend. Zo kan hetzelfde icoon op wit (navy) en op navy (wit of groen)
staan zonder dat er ergens een los bestandje bij gemaakt hoeft te worden.
"""
import subprocess, os

CHROME = os.environ.get('CHROME_PATH', '/opt/pw-browsers/chromium')
TONES = {'navy': '002333', 'white': 'FFFFFF',
         'green': '00E075', 'greendeep': '007B54'}

ICONS = {
    # capabilities
    'doel':       '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/>'
                  '<circle cx="12" cy="12" r="1.4"/>',
    'sleutel':    '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77'
                  'a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91'
                  'a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    'instelling': '<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>',
    'schuifjes':  '<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3"/>'
                  '<path d="M14 2v4M8 10v4M16 18v4"/>',
    # bewijs
    'check':      '<path d="M20 6 9 17l-5-5"/>',
    'bestand':    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/>'
                  '<path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/>',
    'klok':       '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}

os.makedirs('assets', exist_ok=True)
for name, paths in ICONS.items():
    for tone, hexc in TONES.items():
        out = f'assets/icon-{name}-{tone}.png'
        tmp = f'assets/_{name}.html'
        open(tmp, 'w').write(
            '<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            'svg{display:block;width:296px;height:296px}'
            '</style></head><body>'
            f'<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="none" '
            f'stroke="#{hexc}" stroke-width="1.9" stroke-linecap="round" '
            f'stroke-linejoin="round">{paths}</svg></body></html>')
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                        f'--screenshot={out}', '--window-size=296,296',
                        '--default-background-color=00000000',
                        '--hide-scrollbars', '--virtual-time-budget=1500', tmp],
                       capture_output=True)
        os.remove(tmp)

print(f'{len(ICONS) * len(TONES)} icons gerenderd')
