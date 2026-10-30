"""Losse pagina Risicoanalyse voor het Academica-voorstel (30-10-2026). Nog niet in het document.

Gebruik: python3 risicoanalyse.py <werkmap>
"""
import sys, os
sys.path.insert(0, '/home/user/Claude/.claude/skills/business-case-design/motor')
from bouwstenen import *

MAP = sys.argv[1]

def meter(niveau):
    # Drie stappen: laag, middel, hoog. "Laag tot middel" vult de tweede half.
    stappen = {'Laag': ['on', '', ''], 'Laag tot middel': ['on', 'half', '']}[niveau]
    return '<div class="meter">' + ''.join(f'<i class="{c}">{"<b></b>" if c == "half" else ""}</i>' for c in stappen) + f'<span>Restrisico {niveau.lower()}</span></div>'

def risk(titel, maatregelen, niveau, soort='tertiary'):
    return f'<section class="risk {soort}"><div><h2>{titel}</h2>{meter(niveau)}</div>{lst(maatregelen)}</section>'

page(MAP, '7-risicoanalyse', f'''
<h1>Risicoanalyse</h1>
<p class="lead">Welke risico's instellingen benoemen bij het gebruik van Eduface en welke maatregelen ze nemen, op basis van onze samenwerkingen en hun DPIA's.</p>
<div class="stack" style="margin-top:8mm">
''' + risk('Persoonsgegevens in opdrachten', [
    'Verwerkersovereenkomst over persoonsgegevens.',
    'Alleen betrokken docenten zien de opdrachten.',
    'Inzendingen worden niet onderling vergeleken.'], 'Laag')
+ risk('Onjuiste of eenzijdige feedback', [
    'Docent is eindverantwoordelijk en past alles aan.',
    'Training voor docenten in het werken met Eduface.',
    'Tweede beoordeling of moderatie waar nodig.'], 'Laag')
+ risk('Gebruik voor andere doelen', [
    'Opdrachten worden niet gebruikt voor training.',
    'Geen verzameling van inzendingen.',
    'Vastgelegd in de licentieovereenkomst.'], 'Laag')
+ risk('Verwerking buiten de EU', [
    'Alle opslag en verwerking binnen de EER.',
    'Geen doorgifte naar landen buiten de EER.',
    'Vastgelegd in de verwerkersovereenkomst.'], 'Laag')
+ risk('Datalek of onvoldoende beveiliging', [
    'Versleuteld opgeslagen en verzonden, in de EU.',
    'Een datalek wordt binnen 48 uur gemeld.',
    'Beveiligingscheck door eigen IT vooraf.'], 'Laag')
+ risk('Nieuwe AI-wetgeving', [
    'AI Act: hoog risico, verplichtingen vanaf eind 2027.',
    'Menselijke controle op elke beoordeling.',
    'AI-geletterdheid docenten, verplicht sinds feb. 2025.',
    'Documentatie en ondersteuning vanuit Eduface.'], 'Laag tot middel', 'secondary')
+ '\n</div>')
