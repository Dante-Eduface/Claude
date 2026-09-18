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
    # Vizier in plaats van drie ringen: op 48px liepen de ringen tegen elkaar.
    'doel':       '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.6"/>'
                  '<path d="M12 2v3.5M12 18.5V22M2 12h3.5M18.5 12H22"/>',
    # Tandwiel in plaats van moersleutel: de sleutel viel op klein formaat uiteen.
    'sleutel':    '<circle cx="12" cy="12" r="3.2"/>'
                  '<path d="M12 2.5v3M12 18.5v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1'
                  'M2.5 12h3M18.5 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
    # Instellingsgebouw, geen woonhuis: dit gaat over campussen, niet over thuis.
    'instelling': '<path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/>'
                  '<path d="M9 21v-5h6v5"/><path d="M9 9h2M13 9h2M9 12.5h2M13 12.5h2"/>',
    'schuifjes':  '<path d="M21 4h-7M10 4H3M21 12h-9M8 12H3M21 20h-5M12 20H3"/>'
                  '<path d="M14 2v4M8 10v4M16 18v4"/>',
    # bewijs
    'check':      '<path d="M20 6 9 17l-5-5"/>',
    'bestand':    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/>'
                  '<path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/>',
    'klok':       '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    # bevindingen en risico
    # Gelijkteken in een kader: exact-match. Het was een ongelijkteken, en dat
    # zei letterlijk het tegenovergestelde van wat er op de slide staat.
    'exact':      '<rect x="3" y="3" width="18" height="18" rx="3.5"/>'
                  '<path d="M8 10h8M8 14h8"/>',
    'onzichtbaar': '<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/>'
                  '<path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/>'
                  '<path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/>'
                  '<path d="m2 2 20 20"/>',
    'trend':      '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    'mensen':     '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
                  '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    # model en baten
    'bericht':    '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
                  '<path d="M7 9h10M7 13h6"/>',
    'weegschaal': '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/>'
                  '<path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/>'
                  '<path d="M7 21h10M12 3v18M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    'ontkoppeld': '<path d="M9 17H7A5 5 0 0 1 7 7h2"/><path d="M15 7h2a5 5 0 0 1 3.9 8.1"/>'
                  '<path d="m2 2 20 20"/>',
    # aanbod en vervolg
    'prijs':      '<circle cx="12" cy="12" r="9"/><path d="M12 7v10"/>'
                  '<path d="M14.8 9.6a2.3 2.3 0 0 0-2.1-1.4h-1.2a2.2 2.2 0 0 0 0 4.4h1a2.2 2.2 0 0 1 0 4.4h-1.2a2.3 2.3 0 0 1-2.1-1.4"/>',
    'route':      '<circle cx="6" cy="19" r="3"/>'
                  '<path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/>'
                  '<circle cx="18" cy="5" r="3"/>',
    'vlag':       '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><path d="M4 22v-7"/>',
    'kalender':   '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'globe':      '<circle cx="12" cy="12" r="9"/>'
                  '<path d="M12 3a15.3 15.3 0 0 1 4 9 15.3 15.3 0 0 1-4 9 15.3 15.3 0 0 1-4-9 15.3 15.3 0 0 1 4-9z"/>'
                  '<path d="M3 12h18"/>',
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
            f'stroke="#{hexc}" stroke-width="2.2" stroke-linecap="round" '
            f'stroke-linejoin="round">{paths}</svg></body></html>')
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                        f'--screenshot={out}', '--window-size=296,296',
                        '--default-background-color=00000000',
                        '--hide-scrollbars', '--virtual-time-budget=1500', tmp],
                       capture_output=True)
        os.remove(tmp)

print(f'{len(ICONS) * len(TONES)} icons gerenderd')
