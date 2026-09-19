"""Iconenset voor pitch-slides.

Lijn-iconen op een 24x24 viewBox, stroke 1.9, geen fills. Ze worden op aanvraag
naar transparante PNG gerenderd met headless Chrome, want python-pptx kan geen SVG.

    python3 icons.py verschillen variatie wisselend --tint amber

Bestaat het PNG al, dan wordt het overgeslagen. Nieuw icoon nodig? Zet het paadje
in ICONS en render het, dan staat het er voor het hele deck.
"""
import os, subprocess, sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TINTS = {"amber": "E07B00", "green": "007B54", "navy": "002333", 'mint': '00E075'}

ICONS = {
    'gebouwen': '<path d="M2.6 20.8h18.8"/><path d="M5 20.8V6.6l6-2.9v17.1"/>'
                '<path d="M11 20.8V10.6l7 3v7.2"/>'
                '<path d="M7.4 9.2h1.1M7.4 12.6h1.1M7.4 16h1.1M14 15.2h1.1M14 17.9h1.1"/>',
    'usermin': '<circle cx="9.5" cy="8" r="3.4"/>'
               '<path d="M3.2 20.3v-1.1a5.3 5.3 0 0 1 5.3-5.3h2a5.3 5.3 0 0 1 4 1.8"/>'
               '<path d="M16.2 18.4h5.2"/>',
    # -- toegevoegd bij het UTI-deck, september 2026
    'oogdicht': '<path d="M10.7 5.1A11 11 0 0 1 12 5c5 0 9 4.5 9 7a12.6 12.6 0 0 1-2.2 3.3"/>'
                '<path d="M6.6 6.6C4.2 8.1 3 10.3 3 12c0 2.5 4 7 9 7a9.6 9.6 0 0 0 4.8-1.4"/>'
                '<path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/><path d="M3 3l18 18"/>',
    'sleutel': '<path d="M14.6 6.3a1 1 0 0 0 0 1.4l1.7 1.7a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9'
               'l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z"/>',
    'tandwiel': '<circle cx="12" cy="12" r="3.2"/><path d="M19.1 14.4a1.5 1.5 0 0 0 .3 1.7l.1.1a1.9 1.9 0 1 1-2.6 2.6'
                'l-.1-.1a1.5 1.5 0 0 0-1.7-.3 1.5 1.5 0 0 0-.9 1.4v.2a1.9 1.9 0 0 1-3.8 0v-.1a1.5 1.5 0 0 0-1-1.4'
                ' 1.5 1.5 0 0 0-1.7.3l-.1.1a1.9 1.9 0 1 1-2.6-2.6l.1-.1a1.5 1.5 0 0 0 .3-1.7 1.5 1.5 0 0 0-1.4-.9h-.2'
                'a1.9 1.9 0 0 1 0-3.8h.1a1.5 1.5 0 0 0 1.4-1 1.5 1.5 0 0 0-.3-1.7l-.1-.1a1.9 1.9 0 1 1 2.6-2.6l.1.1'
                'a1.5 1.5 0 0 0 1.7.3h.1a1.5 1.5 0 0 0 .9-1.4v-.2a1.9 1.9 0 0 1 3.8 0v.1a1.5 1.5 0 0 0 .9 1.4'
                ' 1.5 1.5 0 0 0 1.7-.3l.1-.1a1.9 1.9 0 1 1 2.6 2.6l-.1.1a1.5 1.5 0 0 0-.3 1.7v.1a1.5 1.5 0 0 0 1.4.9h.2'
                'a1.9 1.9 0 0 1 0 3.8h-.1a1.5 1.5 0 0 0-1.4.9z"/>',
    'prijs': '<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2.5 12V3.5H11l9.6 9.1a1.9 1.9 0 0 1 0 2.8z"/>'
             '<circle cx="7.2" cy="7.2" r="1.1"/>',
 'aanbieder': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
 'aftekenen': '<path d="M3 17c3-6 6 3 9-3s5 1 9-5"/><path d="M4 21h16"/>',
 'boek': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/><path d="M9 7h7"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'cijfers': '<path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h3M8 16h3M15 12v4M13 14h4"/>',
 'code': '<path d="m8 6-6 6 6 6"/><path d="m16 6 6 6-6 6"/>',
 'data': '<path d="M3 5c0-1.1 4-2 9-2s9 .9 9 2-4 2-9 2-9-.9-9-2Z"/><path d="M3 5v6c0 1.1 4 2 9 2s9-.9 9-2V5"/><path d="M3 11v6c0 1.1 4 2 9 2s9-.9 9-2v-6"/>',
 'docenten': '<path d="M2 3h20v12H2z"/><path d="M12 15v6M8 21h8"/><path d="m7 11 3-3 2 2 4-4"/>',
 'filepen': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h5"/><path d="M14 2v6h6"/><path d="M18.4 13.6a1.7 1.7 0 0 1 2.4 2.4L16 21l-3 .8.8-3Z"/>',
 'gesprek': '<path d="M21 12a8 8 0 0 1-8 8H7l-4 3V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8Z"/><path d="M9 11h6M9 15h4"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18Z"/>',
 'groep': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'historie': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l3 2"/>',
 'iama': '<path d="M9 3h6v3H9z"/><path d="M6 5H5a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1"/><path d="m8 14 2 2 5-5"/>',
 'inleveren': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="M12 18v-6M9 15l3-3 3 3"/>',
 'instelling': '<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>',
 'kar': '<circle cx="9" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.6L21 7H6"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'kolf': '<path d="M9 3v6L4 19a2 2 0 0 0 1.8 3h12.4A2 2 0 0 0 20 19l-5-10V3"/><path d="M8 3h8M7 14h10"/>',
 'lagen': '<path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/>',
 'lamp': '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V18h8v-3.3A7 7 0 0 0 12 2Z"/>',
 'mail': '<path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
 'microfoon': '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
 'model': '<path d="M12 3a4 4 0 0 0-4 4 3 3 0 0 0-1 5.8V17a4 4 0 0 0 8 0v-4.2A3 3 0 0 0 16 7a4 4 0 0 0-4-4Z"/><path d="M12 8v9"/>',
 'ongelijk': '<path d="M4 9h16M4 15h16"/><path d="m19 4-14 16"/>',
 'pan': '<path d="M4 11h16v3a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6v-3Z"/><path d="M20 12h2a2 2 0 0 1 0 4h-2"/><path d="M8 7c0-1.5 1-1.5 1-3M12 7c0-1.5 1-1.5 1-3M16 7c0-1.5 1-1.5 1-3"/>',
 'pen': '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
 'pilot': '<path d="M5 19c0-4 3-9 9-11 3-1 5-1 5-1s0 2-1 5c-2 6-7 9-11 9Z"/><path d="M9 15a3 3 0 0 1 0-4"/><path d="M5 19s-1 1-1 2 2 0 2 0"/>',
 'rubric': '<path d="M4 5h16M4 12h16M4 19h16"/><path d="m6 5 1 1 2-2M6 12l1 1 2-2M6 19l1 1 2-2"/>',
 'schoolbord': '<path d="M3 4h18v11H3z"/><path d="M12 15v5M9 20h6"/><path d="m7 11 3-3 2 2 4-4"/>',
 'studenten': '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>',
 'trend': '<path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 'usercheck': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m16 11 2 2 4-4"/>',
 'variatie': '<path d="M4 20V11M10 20V4M16 20v-6M22 20V8"/>',
 'verschillen': '<path d="M3 6h12M3 12h18M3 18h8"/>',
 'vliegtuig': '<path d="M17.8 19.2 16 11l3.5-3.5a2.1 2.1 0 0 0-3-3L13 8 4.8 6.2a1 1 0 0 0-.9 1.7l6 3.4-2.6 2.6-2.6-.6-1 1 3 1.8 1.8 3 1-1-.6-2.6 2.6-2.6 3.4 6a1 1 0 0 0 1.7-.9Z"/>',
 'voorstel': '<path d="m12 3 1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9Z"/><path d="M19 15v4M17 17h4"/>',
 'weegschaal': '<path d="M12 3v18M7 21h10"/><path d="m5 7 7-2 7 2"/><path d="M5 7 2 14a3.5 3.5 0 0 0 6 0Z"/><path d="m19 7 3 7a3.5 3.5 0 0 1-6 0Z"/>',
 'winkel': '<path d="M3 9h18l-1-5H4L3 9Z"/><path d="M5 9v11h14V9"/><path d="M9 20v-6h6v6"/>',
 'wisselend': '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/><path d="M12 9v4M12 17h.01"/>',
 'zorg': '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
}


def render(naam, tint="navy", map="assets"):
    """Rendert een icoon naar assets/icon-<naam>-<tint>.png en geeft het pad terug."""
    if naam not in ICONS:
        raise KeyError(f"onbekend icoon {naam!r}, kies uit: {', '.join(sorted(ICONS))}")
    os.makedirs(map, exist_ok=True)
    uit = f"{map}/icon-{naam}-{tint}.png"
    if os.path.exists(uit):
        return uit
    tmp = f"{map}/_{naam}.html"
    with open(tmp, "w") as f:
        f.write(
            "<!DOCTYPE html><html><head><meta charset='utf-8'><style>"
            "html,body{margin:0;padding:0;background:transparent}"
            "svg{display:block;width:296px;height:296px}</style></head><body>"
            f"<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg' fill='none' "
            f"stroke='#{TINTS[tint]}' stroke-width='1.9' stroke-linecap='round' "
            f"stroke-linejoin='round'>{ICONS[naam]}</svg></body></html>")
    subprocess.run([CHROME, "--headless", "--disable-gpu", f"--screenshot={uit}",
                    "--window-size=296,296", "--default-background-color=00000000",
                    "--hide-scrollbars", "--virtual-time-budget=1500", tmp],
                   capture_output=True)
    os.remove(tmp)
    return uit


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tint = "navy"
    if "--tint" in sys.argv:
        tint = sys.argv[sys.argv.index("--tint") + 1]
        args = [a for a in args if a != tint]
    for naam in (args or sorted(ICONS)):
        print(render(naam, tint))
