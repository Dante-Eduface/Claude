#!/usr/bin/env python3
"""
pipeline.py - de enige schrijver van het master-document van de SHIFT-opleiderspijplijn.

Twee tabellen in GTM/ICP/shift/master/ (sinds 10-09-2026 internationaal, de markt is
een variabele: --markt <code>, SHIFT_MARKT, anders nl. Profielen in GTM/ICP/shift/markets/):
  orgs.csv     een rij per organisatie   (agent 1)
  people.csv   een rij per persoon       (agent 2/3/4/5)
  journal.csv  append-only audit van elke veldwijziging

Geen stage-kolom: de stage wordt afgeleid uit de data, zodat hij nooit uit de pas loopt.

Stdlib only, python 3.9+.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone

csv.field_size_limit(10 * 1024 * 1024)

# ---------------------------------------------------------------- paden

# Twee geldige lay-outs voor dezelfde pipeline.py: genest onder GTM/ICP/shift/
# (de Claud AE-hoofdmap) of plat op de repo-root (de losgetrokken shift-agent-
# repo voor Jeroen, sinds 16-09-2026). Kies wat er echt staat, gok niet vast.
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_GENEST = os.path.join(REPO, "projects", "shift")
SHIFT = _GENEST if os.path.isdir(os.path.join(_GENEST, "master")) else REPO
MASTER = os.path.join(SHIFT, "master")
MARKETS = os.path.join(SHIFT, "markets")
ORGS = os.path.join(MASTER, "orgs.csv")
PEOPLE = os.path.join(MASTER, "people.csv")
JOURNAL = os.path.join(MASTER, "journal.csv")
LOCK = os.path.join(MASTER, ".lock")
DOSSIERS = os.path.join(MASTER, "dossiers")

# ---------------------------------------------------------------- dossiers
#
# Het master-document bewaart de STAND, het dossier bewaart de INHOUD.
# Reden: het onderzoek van agent 3 past niet in vier CSV-cellen (dat was ~1.050
# tekens per persoon) en een cel van 3.000 tekens maakt `queue --table` onleesbaar.
# Je leest een dossier per persoon, of met --sectie zelfs maar een stuk ervan.

PERSOON_SECTIES = [
    "Waarom deze persoon",   # agent 2
    "Bronnen",               # agent 3
    "Citaten",
    "Toetsprogramma",
    "Getallen",
    "Rare details",
    "Persoon",
    "Onzekerheden",
    "Berichten",             # agent 4
]

ORG_SECTIES = [
    "Status", "Bekostiging", "Aanbod", "Beoordeling", "De pijn",
    "Onderwijsvisie", "Organogram", "LMS", "Rechtsvorm", "Studentenaantal",
]

# Wie draagt de last in de bron. Zonder dit label is een citaat een halve
# observatie: bij THIM (13-08-2026) ging een NVAO-citaat over de STUDENT en
# maakte het bericht er de last van de DOCENT van. Zie Platform/onderwijs-vaktermen.md.
DRAGERS = ["student", "beoordelaar", "organisatie", "panel"]

DOSSIER_MAX_REGELS = 250

# De vier velden die vroeger het onderzoek droegen. Ze blijven bestaan als
# samenvatting voor de wachtrij, de lading zit in het dossier.
TEASER_VELDEN = ["opvallend", "haakje", "toetsprogramma", "schrijfwerk"]
TEASER_MAX = 200

# ---------------------------------------------------------------- schema

ORG_COLS = [
    "org_id", "markt", "naam", "naam_aliassen", "moeder_org_id", "categorie", "domein",
    "beoordeelt_zelf", "bewijs_citaat", "bewijs_url", "particulier", "bron_particulier",
    "omvang_medewerkers", "lerenden_per_jaar", "lerenden_diploma", "lerenden_diploma_bron",
    "aantal_opleidingen", "cursusprijs",
    "omzet_indicatie", "geschatte_jaarwaarde", "segment_omvang",
    "omvang_niveau", "omvang_citaat", "omvang_url",
    "icp_status", "blokkade_reden", "close_lead_id", "close_gecheckt_op",
    "contact_zoekpoging", "notities", "laatst_bijgewerkt", "bijgewerkt_door",
]

# ---------------------------------------------------------------- prijsmodel
#
# Sinds 16-09-2026: prijs per student per maand, geen staffel meer. Besluit
# Dante, zie GTM/Pricing/. Drie per student per maand in elke markt,
# in de valuta van die markt: 3 EUR, 3 GBP, 3 USD. Geen omrekening, hetzelfde
# getal, want het is een prijspunt en geen wisselkoers.
#
# Wat hiermee verdween: de staffel A-E, de toolfee per opleiding, en de
# betaalbaarheidstoets op de programma-omzet. De dealwaarde is nu recht
# evenredig met het aantal lerenden, dus aantal_opleidingen en cursusprijs
# zijn wel nuttige context maar bepalen de prijs niet meer.

PRIJS_PER_STUDENT_MAAND = 3
MAANDEN_PER_JAAR = 12

# De vloer waaronder een opleider buiten de outreach blijft. Op 16-09-2026
# stond dit even in lerenden (300, in elke markt hetzelfde getal), maar dat
# bleek zelf een vergissing: bij hetzelfde prijspunt (3 per student, plat
# bedrag per valuta) is 300 lerenden in GBP/USD meer omzet waard dan in EUR,
# dus een koppendrempel benadeelt de sterkere valuta's. Teruggedraaid op
# 17-09-2026 naar een omzetdrempel: 10.000 in de valuta van de markt, plat
# bedrag, geen wisselkoers, net als de prijs zelf.
DREMPEL_JAARWAARDE = 10000

# ---------------------------------------------------------------- markten
#
# Sinds 10-09-2026 is de markt een variabele. Alles wat per markt verschilt
# staat in GTM/ICP/shift/markets/<code>/: profiel.json voor de harde waarden
# waar dit script mee rekent, profiel.md voor de kennis die de agents lezen.
# De constanten hierboven zijn de NL-waarden en blijven de default, zodat
# dashboard.py (importeert de module zonder main()) gewoon blijft werken.
# Een markt is een segment met eigen koopgedrag, meestal valt dat samen met
# een land, maar dat hoeft niet.

VALUTAS = ["EUR", "GBP", "USD"]          # de enige drie, besluit Dante 10-09-2026
KANALEN = ["linkedin", "email"]

# De veertien slots die een markt compleet maken. Dit zijn de koppen in profiel.md.
# Ontbreekt er een, dan weigert `queue` en zegt `doctor` welke.
PROFIEL_SLOTS = [
    ("Registers", "waar agent 1 aanbieders vindt, met URL per register"),
    ("Toezichtregime", "wie panelrapporten publiceert die de beoordeling bekritiseren, en waar die staan"),
    ("Poort-0-afvallers", "archetypes die normen stellen of examineren in plaats van zelf te beoordelen"),
    ("Poort-0-vocabulaire", "woorden die op een site verraden dat ze zelf beoordelen, plus de externe examinatoren"),
    ("Student-signaal", "het citeerbare getal per aanbieder over beoordeling en feedback, en waar het staat"),
    ("Doorlooptijdnorm", "de gangbare of gepubliceerde termijn tussen inleveren en feedback"),
    ("Vaktermen", "termen met een vaste drager (student / beoordelaar / organisatie / panel)"),
    ("Programmaduur", "hoe je poort 0b meet: de eenheid en de grens"),
    ("Prijsmodel", "valuta, prijs per student per maand en de omzetdrempel in woorden; de harde waarden staan in profiel.json"),
    ("Titelrangorde", "welke functietitels hoger staan; de regexes staan in profiel.json"),
    ("Taal en register", "taalcode, aanhef, toon, wat je niet zegt"),
    ("Klantnamen", "welke klanten als bewijs genoemd mogen worden; 'geen' is ook een antwoord"),
    ("Kanaal", "linkedin, email of beide, en wat agent 4 dus per persoon oplevert"),
    ("Seizoen", "wanneer outreach landt en wanneer niet"),
]

# Sleutels in profiel.json. Alles verplicht behalve lemlist_campagne_id (waarschuwing).
PROFIEL_JSON_VELDEN = ["code", "naam", "valuta", "taal", "kanaal",
                       "prijs_per_student_maand", "drempel_jaarwaarde", "titel_rang",
                       "klantnamen", "lemlist_campagne_id"]

MARKT = "nl"
PROFIEL = {}
VALUTA = "EUR"


def markt_pad(code):
    return os.path.join(MARKETS, code)


def markten():
    if not os.path.isdir(MARKETS):
        return []
    return sorted(d for d in os.listdir(MARKETS)
                  if os.path.isdir(os.path.join(MARKETS, d)) and not d.startswith("."))


def profiel_laden(code):
    pad = os.path.join(markt_pad(code), "profiel.json")
    if not os.path.exists(pad):
        return None
    with open(pad, encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError as e:
            die("profiel.json van markt %s is geen geldige JSON: %s" % (code, e))


def _leeg(v):
    return v in (None, "", [], {})


def profiel_klachten(code):
    """(fouten, waarschuwingen) over het profiel van een markt. Geen fouten = compleet."""
    fouten, waarschuwingen = [], []
    if code not in markten():
        return ["markt '%s' bestaat niet. Wel: %s. Nieuw aanmaken: pipeline.py markt --nieuw %s"
                % (code, ", ".join(markten()) or "(geen)", code)], []
    prof = profiel_laden(code)
    if prof is None:
        fouten.append("profiel.json ontbreekt")
    else:
        for k in PROFIEL_JSON_VELDEN:
            if k not in prof:
                fouten.append("profiel.json mist sleutel '%s'" % k)
        v = prof.get("valuta")
        if _leeg(v):
            fouten.append("profiel.json: valuta is leeg (kies uit %s)" % "/".join(VALUTAS))
        elif v not in VALUTAS:
            fouten.append("profiel.json: valuta '%s' mag niet, alleen %s" % (v, "/".join(VALUTAS)))
        if _leeg(prof.get("naam")):
            fouten.append("profiel.json: naam is leeg (bijv. 'Verenigd Koninkrijk, particuliere opleiders')")
        if _leeg(prof.get("taal")):
            fouten.append("profiel.json: taal is leeg (bijv. en-GB)")
        k = prof.get("kanaal")
        if _leeg(k):
            fouten.append("profiel.json: kanaal is leeg (kies uit %s)" % "/".join(KANALEN))
        elif not isinstance(k, list) or not set(k) <= set(KANALEN):
            fouten.append("profiel.json: kanaal %r mag niet, alleen %s" % (k, "/".join(KANALEN)))
        if _leeg(prof.get("prijs_per_student_maand")):
            fouten.append("profiel.json: prijs_per_student_maand is leeg (bijv. 3, in de valuta van de markt)")
        if _leeg(prof.get("drempel_jaarwaarde")):
            fouten.append("profiel.json: drempel_jaarwaarde is leeg (bijv. 10000, in de valuta van de markt)")
        if _leeg(prof.get("titel_rang")):
            fouten.append("profiel.json: titel_rang is leeg ([[regex, score], ...])")
        if "klantnamen" in prof and not isinstance(prof["klantnamen"], list):
            fouten.append("profiel.json: klantnamen moet een lijst zijn, leeg mag")
        if _leeg(prof.get("lemlist_campagne_id")):
            waarschuwingen.append("profiel.json: lemlist_campagne_id is leeg, stap 5 kan pas als de campagne bestaat")
    pad_md = os.path.join(markt_pad(code), "profiel.md")
    if not os.path.exists(pad_md):
        fouten.append("profiel.md ontbreekt")
    else:
        with open(pad_md, encoding="utf-8") as f:
            tekst = re.sub(r"(?s)<!--.*?-->", "", f.read())
        gevuld = {k: bool(v.strip()) for k, v in dossier_secties(tekst).items() if k}
        for kop, uitleg in PROFIEL_SLOTS:
            if kop not in gevuld:
                fouten.append("profiel.md mist kop '## %s' (%s)" % (kop, uitleg))
            elif not gevuld[kop]:
                fouten.append("profiel.md: '## %s' is leeg (%s)" % (kop, uitleg))
    for bestand in ("WERKVOORRAAD.md", "GATEN.md"):
        if not os.path.exists(os.path.join(markt_pad(code), bestand)):
            waarschuwingen.append("%s ontbreekt in de marktmap" % bestand)
    return fouten, waarschuwingen


def activeer_markt(code):
    """Zet de actieve markt en laad de harde waarden uit het profiel.

    Ontbreekt het profiel (nieuwe markt), dan blijven de NL-defaults staan;
    `doctor` en `queue` zeggen dan zelf wat er mist.
    """
    global MARKT, PROFIEL, VALUTA, PRIJS_PER_STUDENT_MAAND, MAANDEN_PER_JAAR
    global DREMPEL_JAARWAARDE, SEGMENT_GRENZEN, TITEL_RANG
    MARKT = code
    prof = profiel_laden(code) or {}
    PROFIEL = prof
    if prof.get("valuta"):
        VALUTA = prof["valuta"]
    if prof.get("prijs_per_student_maand") is not None:
        PRIJS_PER_STUDENT_MAAND = prof["prijs_per_student_maand"]
    if prof.get("maanden_per_jaar") is not None:
        MAANDEN_PER_JAAR = prof["maanden_per_jaar"]
    if prof.get("drempel_jaarwaarde") is not None:
        DREMPEL_JAARWAARDE = prof["drempel_jaarwaarde"]
    if prof.get("segment_grenzen"):
        SEGMENT_GRENZEN = [(g, naam) for g, naam in prof["segment_grenzen"]]
    if prof.get("titel_rang"):
        TITEL_RANG = [(pat, score) for pat, score in prof["titel_rang"]]


def eis_profiel_compleet():
    fouten, _ = profiel_klachten(MARKT)
    if fouten:
        die("markt '%s' is niet compleet, dus geen wachtrij:\n  - %s\n"
            "Vul GTM/ICP/shift/markets/%s/ aan en controleer met: pipeline.py --markt %s doctor"
            % (MARKT, "\n  - ".join(fouten), MARKT, MARKT))


def org_markt(o):
    return (o.get("markt") or "").strip()


def load_markt():
    """orgs en people van de actieve markt, voor wachtrij en tellingen.

    Commando's op id (show, set, dossier, exists, history) gebruiken load(),
    want die moeten over markten heen werken: exists is juist de dedup-poort
    voor concerns die in meer dan een markt zitten.
    """
    orgs = [o for o in load(ORGS, ORG_COLS) if org_markt(o) == MARKT]
    ids = {o["org_id"] for o in orgs}
    people = [p for p in load(PEOPLE, PERSON_COLS) if p.get("org_id") in ids]
    return orgs, people


def bereken_jaarwaarde(lerenden, opleidingen=None):
    """Jaarwaarde in de valuta van de markt, of None als het aantal ontbreekt.

    Sinds het PSU-model is dit een vermenigvuldiging: lerenden maal de prijs per
    student per maand maal het aantal maanden. `opleidingen` doet niet meer mee
    en blijft alleen in de signatuur staan zodat bestaande aanroepen werken.
    """
    lerenden = getal(lerenden)
    if lerenden is None or lerenden <= 0:
        return None
    return int(round(lerenden * PRIJS_PER_STUDENT_MAAND * MAANDEN_PER_JAAR))


def omvang_oordeel(o, drempel=None, aandeel=None):
    """Poort 0d in een functie, zodat de agent niet zelf zit te rekenen.

    Geeft (oordeel, reden) terug. Drie uitkomsten:
      groot_genoeg  jaarwaarde boven de drempel, een deal die de moeite waard is
      te_klein      bewezen onder de drempel, buiten de outreach
      onbekend      geen lerendenaantal gevonden, blijft gewoon in de pijplijn

    Sinds 17-09-2026 (teruggedraaid vanaf de 300-lerenden-drempel van
    16-09-2026, zie de constante hierboven) toetst dit op de berekende
    jaarwaarde (lerenden maal de prijs per student) tegen `drempel`, in de
    valuta van de markt, niet meer op een kaal lerendenaantal. Dat betekent
    dat een toekomstige prijswijziging vanzelf meerekent zonder dat de
    drempel opnieuw omgezet hoeft te worden naar een lerendenaantal.
    `aandeel` staat er alleen nog voor oude aanroepen; de betaalbaarheidstoets
    is vervallen, want bij een prijs per student schaalt de rekening vanzelf
    mee met de omvang van de klant.
    """
    drempel = DREMPEL_JAARWAARDE if drempel is None else drempel
    lerenden = getal(o.get("lerenden_per_jaar"))
    if lerenden is None:
        return "onbekend", "geen lerenden per jaar gevonden, dus niets te toetsen"
    # bereken_jaarwaarde() parst zelf ook met getal(): geef het RUWE veld door,
    # niet de hier al geparste `lerenden` — getal() is niet idempotent op een
    # float (str(246.0) -> "246.0" -> decimaalpunt wordt gestript als was het
    # een duizendtalscheiding -> 2460). Zie ook regel bij _afgeleid_org.
    waarde = bereken_jaarwaarde(o.get("lerenden_per_jaar"))
    if waarde < drempel:
        return "te_klein", "%d lerenden per jaar, ongeveer %d %s per jaar, onder de drempel van %d %s" % (
            lerenden, waarde, VALUTA, drempel, VALUTA)
    return "groot_genoeg", "%d lerenden per jaar, ongeveer %d %s per jaar" % (
        lerenden, waarde, VALUTA)


def getal(v):
    """Leest een getal uit een cel. Leeg of onleesbaar wordt None, niet 0."""
    if v is None:
        return None
    s = str(v).strip().replace(".", "").replace(",", ".")
    s = re.sub(r"[^0-9.]", "", s)
    if not s or s == ".":
        return None
    try:
        return float(s)
    except ValueError:
        return None

PERSON_COLS = [
    # identiteit
    "person_id", "org_id", "dubbel_van",
    # stap 2 - contact-sourcing-nl
    "naam", "voornaam", "achternaam", "functie", "functie_niveau",
    "linkedin_url", "email", "email_status", "telefoon",
    "rol", "waarom_deze_persoon", "functie_bron", "in_functie_sinds",
    "functie_geverifieerd_op", "waarom_afgevallen",
    # stap 3 - shift-research
    "opvallend", "haakje", "haakje_bron_url", "haakje_bron_type", "haakje_gevonden_op",
    "haakje_gaat_over", "haakje_niveau", "haakje_trap", "toetsprogramma", "schrijfwerk",
    "type_instelling", "alternatief_hoger_in_boom", "onderzoek_status",
    # stap 4 - linkedin-outreach
    "connectieverzoek", "opvolgmail_onderwerp", "opvolgmail", "reminder", "twijfels",
    "afgevallen_openers", "waarom_dit_bericht", "bericht_status", "bericht_status_toelichting",
    "gepauzeerd_tot",
    # stap 5 - lemlist-import-nl
    "lemlist_status", "lemlist_campagne_id", "lemlist_lead_id",
    # wat er daadwerkelijk gebeurd is
    "verzonden_linkedin", "verzonden_email", "cold_call", "linkedin_geaccepteerd_op",
    "reactie_gekregen_op", "reactie_tekst", "uitkomst", "uitkomst_reden", "uitkomst_datum",
    # systeem
    "notities", "laatst_bijgewerkt", "bijgewerkt_door",
]

# Wat elke kolom betekent, in gewone taal. `pipeline.py uitleg` drukt dit af,
# zodat je nooit hoeft te raden hoe een veld heet of welke waarden erin mogen.
UITLEG = {
    # organisatie
    "org_id": "Vast kenmerk van de organisatie. Verandert nooit, ook niet als de naam wijzigt.",
    "markt": "In welke markt deze organisatie meedoet (nl, uk, ...). Personen erven dit van hun organisatie. Zie pipeline.py markt.",
    "naam": "Naam van de organisatie of de persoon.",
    "naam_aliassen": "Andere schrijfwijzen van de organisatienaam, gescheiden door een |.",
    "moeder_org_id": "De org_id van het moederbedrijf, leeg als die er niet is.",
    "categorie": "Type opleider, zoals agent 1 hem heeft ingedeeld.",
    "domein": "Website-domein, nodig voor Lemlist.",
    "beoordeelt_zelf": "Beoordeelt deze opleider zelf het werk van lerenden? Dat is poort 0.",
    "bewijs_citaat": "Het letterlijke citaat waarmee poort 0 is beantwoord.",
    "bewijs_url": "De pagina waar dat citaat vandaan komt.",
    "particulier": "Is het een particuliere opleider (dus niet bekostigd)?",
    "bron_particulier": "Waar dat vandaan komt (NRTO, CRKBO, eigen site).",
    "omvang_medewerkers": "Aantal medewerkers, als we het weten. Zwakste omvangssignaal: opleiders draaien veel op freelancers, dus dit getal is bijna altijd te laag.",
    "lerenden_per_jaar": "Hoeveel lerenden er per jaar starten. Sinds het PSU-model is dit HET getal: de prijs is lerenden maal de prijs per student per maand, en de drempel van poort 0d is een minimum aantal lerenden. Zonder dit veld is er geen dealwaarde en geen segment.",
    "lerenden_diploma": "Hoeveel van die lerenden in een meerjarig of diplomagericht traject zitten, dus niet in een losse cursus of training. Dit is het getal waarop we op omvang sorteren, drempel 3.000.",
    "lerenden_diploma_bron": "De pagina waar het diploma-aantal vandaan komt. Ander veld dan omvang_url, omdat het totaal en het diploma-deel vaak uit verschillende bronnen komen.",
    "aantal_opleidingen": "Hoeveel opleidingen van langer dan een jaar ze aanbieden. Sinds het PSU-model bepaalt dit de prijs niet meer; het blijft nuttig om te zien hoe breed een uitrol kan worden.",
    "cursusprijs": "Wat een deelnemer betaalt voor de opleiding, in de valuta van de markt. Sinds het PSU-model geen poort meer, wel context voor het gesprek.",
    "omzet_indicatie": "Lerenden per jaar maal cursusprijs. Ruwe omzet van dat programma. Wordt zelf berekend en is sinds het PSU-model alleen nog context.",
    "geschatte_jaarwaarde": "Wat deze opleider per jaar waard zou zijn: lerenden maal de prijs per student per maand maal twaalf. Wordt zelf berekend, je vult hem niet met de hand.",
    "segment_omvang": "Grootteklasse van de organisatie, waarop we meten of het werkt. Zelf berekend uit lerenden_per_jaar. Een aantal lerenden is in elke markt hetzelfde getal, dus NL, UK en US zijn zonder omrekening vergelijkbaar. Je vult hem niet met de hand.",
    "omvang_niveau": "Hoe hard het omvangsgetal is. Voorkomt dat een schatting later als feit wordt gelezen.",
    "omvang_citaat": "Het letterlijke citaat waar het omvangsgetal vandaan komt.",
    "omvang_url": "De pagina waar dat omvangscitaat staat.",
    "icp_status": "Waar staat deze organisatie in de kwalificatie.",
    "blokkade_reden": "Waarom er geen koude outreach mag, bijvoorbeeld: loopt al via Close.",
    "close_lead_id": "De lead-id in Close, als de organisatie daar al staat.",
    "close_gecheckt_op": "Datum waarop agent 1 Close heeft gecontroleerd.",
    "contact_zoekpoging": "Wat agent 2 al geprobeerd heeft en niet vond. Voorkomt dubbel zoekwerk.",
    # persoon, identiteit
    "person_id": "Vast kenmerk van de persoon, gebaseerd op zijn LinkedIn-adres.",
    "dubbel_van": "Staat deze persoon dubbel, dan wijst dit naar het record dat blijft gelden.",
    "voornaam": "Voornaam, afgeleid uit naam.",
    "achternaam": "Achternaam, afgeleid uit naam.",
    "functie": "Functietitel zoals op LinkedIn.",
    "functie_niveau": "De functietitel teruggebracht tot een handvol niveaus, waarop we meten of het werkt. Afgeleid uit de titelrangorde van de markt, dus een nieuwe titel valt vanzelf op de goede plek. Je vult hem niet met de hand.",
    "linkedin_url": "Het LinkedIn-profiel. Dit is het belangrijkste veld, hier hangt alles aan.",
    "email": "E-mailadres.",
    "email_status": "Hoe zeker we zijn van dat e-mailadres.",
    "telefoon": "Telefoonnummer, als je het toevallig tegenkomt op een profiel- of staffpagina. Geen aparte zoekactie zoals bij email, puur bijvangst tijdens agent 2 of agent 3.",
    "rol": "Wat deze persoon voor ons is binnen zijn organisatie.",
    "waarom_deze_persoon": "De onderbouwing van agent 2: waarom is dit de juiste ingang.",
    "functie_bron": "Waar de functietitel vandaan komt.",
    "in_functie_sinds": "Sinds wanneer die persoon deze functie heeft.",
    "functie_geverifieerd_op": "Datum waarop is gecheckt dat hij er nog werkt. Leeg = niet gecheckt.",
    "waarom_afgevallen": "Waarom deze persoon niet de ingang is.",
    # persoon, onderzoek
    "opvallend": "Wat er opvalt aan deze persoon of organisatie, ruwe observatie.",
    "haakje": "Het haakje: het concrete ding waar het bericht op aanhaakt.",
    "haakje_bron_url": "De pagina waar het haakje staat. Zonder dit mag er geen bericht uit.",
    "haakje_bron_type": "Soort bron: interview, publicatie, teampagina, jaarverslag, enzovoort.",
    "haakje_gevonden_op": "Datum waarop het haakje is gevonden.",
    "haakje_gaat_over": "Gaat het haakje over de persoon zelf of over de organisatie.",
    "haakje_niveau": "Hoe ORIGINEEL het haakje is, op de ladder uit .claude/skills/outreach/haakje-zoeken.md (1 citeren-en-pitchen, 2 zelf een gevolg trekken, 2b eerlijke non-sequitur, 3 iets bouwen en weggeven). Vanaf 2 mag er een bericht op.",
    "haakje_trap": "Welke stap van de ZOEKLADDER (.claude/skills/person-research/SKILL.md) het haakje opleverde: 1 websearch, 2 LinkedIn-profiel, 3 teampagina/eigen site, 4 de instelling (visie/jaarverslag/rapport), 5 hun echte werk, 6 vakbladen/podcasts, 7 Apify. Niet hetzelfde als haakje_niveau: dit is WAAR je het vond, dat is hoe ORIGINEEL het is.",
    "toetsprogramma": "Wat lerenden inleveren, hoeveel, en wie het nakijkt.",
    "schrijfwerk": "Is schrijfwerk kern of bijzaak in de opleiding.",
    "type_instelling": "Wat voor opleider dit precies is.",
    "alternatief_hoger_in_boom": "Iemand hoger in de organisatie, mocht deze route stuklopen.",
    "onderzoek_status": "Hoe ver het haakje-onderzoek is.",
    # persoon, bericht
    "connectieverzoek": "Het LinkedIn-connectieverzoek. Maximaal 300 tekens.",
    "opvolgmail_onderwerp": "Onderwerpregel van de opvolgmail.",
    "opvolgmail": "De opvolgmail zelf.",
    "reminder": "De korte herinnering die als reply in dezelfde mailthread gaat. Alleen als het kanaal van de markt email bevat.",
    "twijfels": "Waar de agent zelf niet zeker over is. Komt op de reviewkaart te staan.",
    "afgevallen_openers": "Openingen die zijn overwogen en afgevallen, met de reden.",
    "waarom_dit_bericht": "Hoe de agent tot dit bericht kwam: gekozen insteek en waarom die.",
    "bericht_status": "Waar het bericht staat in de goedkeuring.",
    "bericht_status_toelichting": "Vrije tekst bij die status, inclusief de oude omschrijving.",
    "gepauzeerd_tot": "Datum waarop dit bericht weer opgepakt mag worden.",
    # persoon, verzending en uitkomst
    "lemlist_status": "Staat deze persoon in een Lemlist-campagne.",
    "lemlist_campagne_id": "Welke Lemlist-campagne.",
    "lemlist_lead_id": "De lead-id binnen Lemlist.",
    "verzonden_linkedin": "Datum waarop het connectieverzoek de deur uit ging.",
    "verzonden_email": "Datum waarop de mail de deur uit ging.",
    "cold_call": "Datum waarop er gebeld is.",
    "linkedin_geaccepteerd_op": "Datum waarop het connectieverzoek is geaccepteerd.",
    "reactie_gekregen_op": "Datum waarop er een reactie kwam.",
    "reactie_tekst": "De eerste regels van wat hij terugschreef, zoals Lemlist het geeft. Een feit, geen oordeel: wat het betekende zet je in uitkomst en uitkomst_reden.",
    "uitkomst": "Wat het uiteindelijk werd. Hier leg je 'geen interesse' vast.",
    "uitkomst_reden": "In zijn eigen woorden waarom. Dit is later opvraagbaar.",
    "uitkomst_datum": "Wanneer die uitkomst duidelijk werd.",
    # systeem
    "notities": "Losse aantekeningen en wat er bij samenvoegen is bewaard.",
    "laatst_bijgewerkt": "Datum van de laatste wijziging.",
    "bijgewerkt_door": "Welke agent of persoon die wijziging deed.",
}

# wie mag wat schrijven. --actor wordt hiertegen gecontroleerd.
# markt zet alleen de mens of het systeem, nooit een agent: een organisatie
# verhuist niet van markt omdat een sourcing-ronde dat handig vindt.
# De afgeleide velden horen niet bij een agent: die volgen uit andere velden en
# worden door _afgeleid_org() en doctor gezet. Een agent die ze zelf invult
# zorgt voor twee waarheden, en de handmatige wint dan tot de volgende doctor.
_ORG_AFGELEID = {"omzet_indicatie", "geschatte_jaarwaarde", "segment_omvang"}
_ORG_AGENT = set(ORG_COLS) - {"markt"} - _ORG_AFGELEID
OWNER = {
    "lead-sourcing-nl": _ORG_AGENT | {
        "person_id", "org_id", "naam", "voornaam", "achternaam", "functie", "linkedin_url",
        "email", "rol", "waarom_deze_persoon", "notities",
    },
    "contact-sourcing-nl": {
        "person_id", "org_id", "naam", "voornaam", "achternaam", "functie", "linkedin_url",
        "email", "email_status", "rol", "waarom_deze_persoon", "functie_bron",
        "in_functie_sinds", "functie_geverifieerd_op", "waarom_afgevallen", "dubbel_van",
        "notities", "contact_zoekpoging",
    },
    "shift-research": {
        "opvallend", "haakje", "haakje_bron_url", "haakje_bron_type", "haakje_gevonden_op",
        "haakje_gaat_over", "haakje_niveau", "haakje_trap", "toetsprogramma", "schrijfwerk",
        "type_instelling", "alternatief_hoger_in_boom", "onderzoek_status", "notities",
        "twijfels",
    },
    "linkedin-outreach": {
        "connectieverzoek", "opvolgmail_onderwerp", "opvolgmail", "reminder", "twijfels",
        "afgevallen_openers", "waarom_dit_bericht", "bericht_status",
        "bericht_status_toelichting", "gepauzeerd_tot", "notities",
    },
    "lemlist-import-nl": {
        "lemlist_status", "lemlist_campagne_id", "lemlist_lead_id", "bericht_status",
        "bericht_status_toelichting", "email", "email_status", "notities",
    },
    "dante": set(ORG_COLS) | set(PERSON_COLS),   # de mens mag alles
    "migratie": set(ORG_COLS) | set(PERSON_COLS),
    "system": set(ORG_COLS) | set(PERSON_COLS),
}
# Marktloze namen sinds 10-09-2026. Dezelfde rechten; de -nl namen blijven
# geldig zodat lopende chats en journaalregels niet breken.
OWNER["lead-sourcing"] = OWNER["lead-sourcing-nl"]
OWNER["contact-sourcing"] = OWNER["contact-sourcing-nl"]
OWNER["outreach"] = OWNER["linkedin-outreach"]
OWNER["lemlist-import"] = OWNER["lemlist-import-nl"]
# Jeroen is mens, geen agent, maar mag alleen zijn eigen schakel: agent 4
# (de berichten en de goedkeuring erop), niet sourcing of onderzoek. Zie
# werkverdeling in CLAUDE.md. Dante blijft de enige met volledige rechten.
OWNER["jeroen"] = OWNER["outreach"]
# de terugschrijf-stap. Mag alleen de feiten vastleggen die Lemlist kent:
# een datum, geen oordeel. Wat de reactie betekende zet Dante met `uitkomst`.
OWNER["lemlist-sync"] = {
    "linkedin_geaccepteerd_op", "reactie_gekregen_op", "reactie_tekst", "verzonden_linkedin",
    "verzonden_email", "lemlist_lead_id", "lemlist_status", "lemlist_campagne_id",
    "bericht_status", "notities",
}

# Elke toegestane waarde met uitleg erbij. ENUMS wordt hieruit afgeleid.
WAARDEN = {
    "icp_status": {
        "kandidaat": "gevonden, nog niet gekwalificeerd op poort 0",
        "gekwalificeerd": "beoordeelt zelf werk van lerenden, mag de pijplijn in",
        "afgevallen": "valt buiten de ICP",
        "geblokkeerd": "geen koude outreach, bijvoorbeeld omdat het al via Close loopt",
        "te_klein": "past qua fit, maar er komt geen deal boven de drempel van de markt uit; blijft staan, buiten de outreach tot de drempel zakt",
    },
    "omvang_niveau": {
        "": "nog niet vastgesteld",
        "hard": "getal met citaat uit een bron van de opleider zelf",
        "afgeleid": "zelf geteld of gerekend, bijvoorbeeld opleidingen uit de catalogus",
        "geschat": "proxy zoals een medewerkersband op LinkedIn",
        "onbekend": "gezocht en niets gevonden, niet gegokt",
    },
    "segment_omvang": {
        "": "nog niet uitgerekend",
        "onbekend": "geen lerenden per jaar bekend, dus geen klasse",
        "micro": "onder de drempel van de markt, standaard 300 lerenden per jaar",
        "klein": "300 tot 1.000 lerenden per jaar",
        "midden": "1.000 tot 3.000 lerenden per jaar",
        "groot": "3.000 lerenden per jaar of meer",
    },
    "functie_niveau": {
        "": "nog niet afgeleid",
        "onbekend": "geen functietitel, of een titel die de rangorde van de markt niet kent",
        "bestuur": "bestuur, CEO, algemeen directeur, eigenaar of oprichter",
        "directie": "directeur, ook de functionele directeuren",
        "onderwijsleiding": "hoofd of manager van onderwijs, opleidingen of kwaliteit, plus lector en decaan",
        "manager": "manager of teamleider zonder onderwijs in de titel",
        "uitvoerend": "adviseur, cordinator, docent of trainer",
    },
    "beoordeelt_zelf": {"Ja": "", "Nee": "", "Onbekend": ""},
    "particulier": {"Ja": "", "Nee": "", "Onbekend": ""},
    "rol": {
        "aangewezen": "dit is de persoon die we benaderen, er is er maar een per organisatie",
        "tweede_kandidaat": "goede reserve, komt aan de beurt als de eerste niet reageert",
        "doorverwijzing": "door iemand anders naar ons doorverwezen",
        "al_in_close": "staat al in Close, niet koud benaderen",
        "afgevallen": "onderzocht en niet de juiste ingang, met reden in waarom_afgevallen",
        "achtergrond": "wel bekend bij de organisatie, maar geen kandidaat",
    },
    # De originaliteitsladder uit .claude/skills/outreach/haakje-zoeken.md is
    # hier leidend (17-09-2026 rechtgetrokken: deze woordenlijst omschreef
    # daarvoor een ANDERE maatlat onder dezelfde labels, wat het systeem
    # onbedoeld vaag maakte).
    "haakje_niveau": {
        "1": "citeren en dan pitchen; iedereen kan dit, niet goed genoeg om te versturen",
        "2": "je ziet iets in hun situatie dat zij niet zelf hebben gezegd; de ondergrens om te schrijven",
        "2b": "de eerlijke non-sequitur: iets menselijks en zichtbaars van hun profiel, erken dat het niks met de reden te maken heeft, dan de vraag",
        "3": "je doet iets met hun eigen materiaal en geeft het weg, krediet volledig naar hen",
        "onbeoordeeld": "onderzoek is gedaan maar er is nooit een niveau toegekend",
    },
    # De zoekladder uit .claude/skills/person-research/SKILL.md (waar je het
    # haakje vond), niet te verwarren met haakje_niveau (hoe origineel het is).
    "haakje_trap": {
        "1": "websearch op \"naam\" + instelling, of \"naam\" interview",
        "2": "LinkedIn-profiel: headline, about, functiebeschrijvingen",
        "3": "teampagina / over-ons / instituutpagina van de eigen site",
        "4": "de instelling: AI-pagina, visiestuk, handboek, jaarverslag, toezichthouder-rapport, nieuws",
        "5": "hun echte werk: publicaties, scriptie, lectorale rede, papers, repositories",
        "6": "vakbladen, congresprogramma's, podcasts, brancheorganisatie",
        "7": "Apify (linkedin-profile-scraper)",
    },
    "onderzoek_status": {
        "open": "nog niet onderzocht",
        "gevonden": "haakje gevonden",
        "geen_haakje": "gezocht en niets bruikbaars gevonden",
        "geparkeerd": "twijfelgeval, later opnieuw bekijken",
    },
    "haakje_gaat_over": {
        "": "nog niet bepaald",
        "persoon": "over de persoon zelf",
        "organisatie": "over de organisatie",
        "persoon + organisatie": "allebei",
    },
    "bericht_status": {
        "": "nog geen bericht geschreven",
        "concept": "geschreven, wacht op jouw oordeel",
        "goedgekeurd": "door jou goedgekeurd, mag naar Lemlist",
        "afgekeurd": "door jou afgekeurd, met reden in de toelichting",
        "verstuurd": "de deur uit, wordt automatisch gezet zodra er een verzenddatum staat",
        "vervallen": "gaat niet meer door, met reden in de toelichting",
        "gepauzeerd": "tijdelijk stil, zie gepauzeerd_tot",
    },
    "lemlist_status": {
        "": "nog niet aan de orde",
        "nvt": "gaat niet naar Lemlist",
        "klaar": "klaar om te importeren",
        "geimporteerd": "staat in een campagne",
        "fout": "import mislukt",
    },
    "email_status": {
        "": "onbekend",
        "geverifieerd": "gecontroleerd adres",
        "gegokt": "afgeleid van het patroon van de organisatie",
        "niet gevonden": "geen adres te vinden",
        "bounce": "kwam terug",
    },
    "uitkomst": {
        "": "nog geen uitkomst",
        "geen_interesse": "expliciet nee gezegd, reden in uitkomst_reden",
        "interesse": "wil verder praten",
        "gesprek_gepland": "er staat een afspraak",
        "doorverwezen": "verwijst ons door naar iemand anders",
        "later_terugkomen": "nu niet, later wel",
        "geen_reactie": "nooit iets teruggehoord",
    },
}

ENUMS = {k: list(v.keys()) for k, v in WAARDEN.items()}

TOUCH_VELD = {"linkedin": "verzonden_linkedin", "email": "verzonden_email", "call": "cold_call"}

# titelrangorde voor de tiebreak, hoger getal = hoger in de boom
TITEL_RANG = [
    # Volgorde telt, eerste hit wint. De onderwijstak staat boven de bedrijfsvoeringstak:
    # een commercieel of financieel directeur gaat niet over het beoordelen van werk.
    (r"college van bestuur|\bcvb\b|bestuursvoorzitter|\bbestuurder\b", 100),
    (r"\b(ceo|algemeen\s*directeur|directeur[- ]bestuurder|managing\s*director)\b", 96),
    (r"\b(eigenaar|oprichter|founder|mede-oprichter|co-?founder)\b", 94),
    (r"\bdirect(eur|ie)\s*(van\s*)?(onderwijs|opleidingen|academy|kwaliteit|studie)", 92),
    (r"\b(directie|directielid)\b", 88),
    (r"\b(commercieel|financieel|marketing|hr|operationeel)\s*directeur\b", 82),
    (r"\bdirecteur\b", 86),
    (r"\bhoofd\s*(onderwijs|opleidingen|academy|kwaliteit)", 80),
    (r"\bhoofd\b", 75),
    (r"\b(lector|decaan|dean)\b", 72),
    (r"manager\s*(onderwijs|opleidingen|academy|kwaliteit)", 68),
    (r"\b(onderwijsmanager|opleidingsmanager|programmamanager)\b", 66),
    (r"\bmanager\b", 60),
    (r"\b(teamleider|team\s*lead)\b", 55),
    (r"\b(adviseur|advisor|specialist|expert|onderwijskundige)\b", 45),
    (r"\b(cordinator|coordinator|cordinatie)\b", 40),
    (r"\b(docent|trainer|lecturer)\b", 20),
]

# ---------------------------------------------------------------- helpers


def slug(s):
    """ascii-fold, lowercase, alles niet [a-z0-9] wordt een streepje."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.encode("ascii", "ignore").decode("ascii").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def norm(s):
    """normaliseer vrije tekst voor vergelijking."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"\s+", " ", s).strip()


def li_slug(url):
    """haal de /in/<slug> eruit, url-decode, lowercase. Leeg als het geen profiel-URL is."""
    if not url:
        return ""
    u = str(url).strip()
    m = re.search(r"/in/([^/?#\s]+)", u, re.I)
    if not m:
        return ""
    raw = m.group(1)
    try:
        from urllib.parse import unquote
        raw = unquote(raw)
    except Exception:
        pass
    return slug(raw)


def org_id_for(naam):
    return "org_" + slug(naam) if naam else ""


def person_id_for(naam, linkedin, org_naam=""):
    s = li_slug(linkedin)
    if s:
        return "p_" + s
    return "p_" + slug(org_naam) + "--" + slug(naam)


_TITEL_CACHE = {}


def titel_rang_van_markt(code):
    """De titelrangorde van een markt, niet van de actieve markt.

    Zonder dit knipt een backfill vanuit markt nl de Britse titels met de
    Nederlandse regexes, en heet elke 'Director' opeens onbekend.
    """
    if not code or code == MARKT:
        return TITEL_RANG
    if code not in _TITEL_CACHE:
        prof = profiel_laden(code) or {}
        rang = prof.get("titel_rang")
        _TITEL_CACHE[code] = [(p, sc) for p, sc in rang] if rang else TITEL_RANG
    return _TITEL_CACHE[code]


def titel_score(functie, markt=None):
    """De score uit de titelrangorde van de markt, of None als geen enkele regex past.

    Het verschil met titel_rang() telt: die geeft 50 terug bij geen treffer,
    wat prima is voor een tiebreak maar niet voor een segment. Een onbekende
    titel is "onbekend", geen middenmoter.
    """
    f = norm(functie)
    for pat, score in titel_rang_van_markt(markt):
        if re.search(pat, f):
            return score
    return None


def titel_rang(functie, markt=None):
    score = titel_score(functie, markt)
    return 50 if score is None else score


# ---------------------------------------------------------------- segmenten
#
# Twee afgeleide velden waarop we meten of de outreach werkt. Allebei berekend,
# nooit met de hand gezet, want een handmatig segment loopt binnen een maand uit
# de pas met het veld waar het uit volgt.
#
# Waarom afgeleid en niet een eigen oordeel per record: `categorie` en `functie`
# zijn vrije tekst en daar zit geen segmentatie in te krijgen (16-09-2026: 126
# lege categorieen, en bijna net zoveel unieke functietitels als personen).

# Grenzen in lerenden per jaar, als absolute getallen. Dat kan sinds het
# PSU-model: een aantal studenten is in elke markt hetzelfde getal, dus NL, UK
# en US zijn zonder omrekening vergelijkbaar. De onderste grens is de drempel.
# Een markt die anders ligt zet zijn eigen lijst in profiel.json onder
# segment_grenzen.
SEGMENT_GRENZEN = [(300, "micro"), (1000, "klein"), (3000, "midden")]
SEGMENT_BOVEN = "groot"

# De titelscore geknipt in niveaus. De grenzen volgen de sprongen die al in de
# titelrangorde zitten: 94 is waar eigenaar/oprichter begint, 82 waar de
# functionele directeuren beginnen, 66 waar de onderwijstak onder directie zit.
FUNCTIE_NIVEAUS = [(94, "bestuur"), (82, "directie"), (66, "onderwijsleiding"),
                   (55, "manager"), (0, "uitvoerend")]

_GRENZEN_CACHE = {}


def segment_grenzen_van_markt(code):
    """De segmentgrenzen van een markt, niet van de actieve markt.

    Nodig omdat `set` op een org uit een andere markt dan de actieve gewoon mag,
    en het segment dan met de verkeerde grenzen geknipt zou worden.
    """
    if not code or code == MARKT:
        return SEGMENT_GRENZEN
    if code not in _GRENZEN_CACHE:
        prof = profiel_laden(code) or {}
        g = prof.get("segment_grenzen")
        _GRENZEN_CACHE[code] = [(x, naam) for x, naam in g] if g else SEGMENT_GRENZEN
    return _GRENZEN_CACHE[code]


def segment_omvang_van(o):
    """Grootteklasse van een organisatie, uit het aantal lerenden per jaar."""
    lerenden = getal(o.get("lerenden_per_jaar"))
    if lerenden is None:
        return "onbekend"
    for grens, naam in segment_grenzen_van_markt(org_markt(o)):
        if lerenden < grens:
            return naam
    return SEGMENT_BOVEN


def functie_niveau_van(functie, markt=None):
    """Functietitel -> een van de vijf niveaus, of onbekend."""
    score = titel_score(functie, markt)
    if score is None:
        return "onbekend"
    for ondergrens, naam in FUNCTIE_NIVEAUS:
        if score >= ondergrens:
            return naam
    return "onbekend"


def now_iso():
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")


def stamp():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def split_naam(naam):
    parts = (naam or "").strip().split()
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])


# ---------------------------------------------------------------- io


class Lock:
    def __init__(self, timeout=120):
        self.timeout = timeout

    def __enter__(self):
        os.makedirs(MASTER, exist_ok=True)
        wachtte = 0.0
        while True:
            try:
                fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, ("%d %s\n" % (os.getpid(), stamp())).encode())
                os.close(fd)
                return self
            except FileExistsError:
                try:
                    age = time.time() - os.path.getmtime(LOCK)
                except OSError:
                    age = 0
                if age > self.timeout:
                    os.unlink(LOCK)          # verlopen slot, opruimen
                    continue
                if wachtte > self.timeout:
                    die("lock vast: %s" % LOCK)
                time.sleep(0.25)
                wachtte += 0.25

    def __exit__(self, *a):
        try:
            os.unlink(LOCK)
        except OSError:
            pass


def load(path, cols):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for c in cols:
            r.setdefault(c, "")
            if r[c] is None:
                r[c] = ""
        r.pop(None, None)
    return rows


def save(path, cols, rows):
    """atomair: schrijf naar .tmp en hernoem."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: (r.get(c) or "") for c in cols})
    os.replace(tmp, path)


def journal(entries):
    """entries: lijst van (record_id, veld, oud, nieuw, actor)"""
    if not entries:
        return
    nieuw = not os.path.exists(JOURNAL)
    os.makedirs(MASTER, exist_ok=True)
    with open(JOURNAL, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nieuw:
            w.writerow(["tijdstip", "actor", "record_id", "veld", "oude_waarde", "nieuwe_waarde"])
        t = stamp()
        for rid, veld, oud, new, actor in entries:
            w.writerow([t, actor, rid, veld, oud, new])


def die(msg, code=1):
    sys.stderr.write("FOUT: %s\n" % msg)
    sys.exit(code)


def out(data, table=False):
    if table:
        print(as_table(data))
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


def as_table(data):
    if isinstance(data, dict):
        return "\n".join("%-24s %s" % (k, v) for k, v in data.items())
    if not data:
        return "(leeg)"
    if not isinstance(data[0], dict):
        return "\n".join(str(x) for x in data)
    cols = list(data[0].keys())

    def cel(r, c):
        return str(r.get(c, ""))[:60].replace("\n", " ")

    breed = {c: max([len(c)] + [len(cel(r, c)) for r in data]) for c in cols}
    lijnen = [" | ".join(c.ljust(breed[c]) for c in cols)]
    lijnen.append("-+-".join("-" * breed[c] for c in cols))
    for r in data:
        lijnen.append(" | ".join(cel(r, c).ljust(breed[c]) for c in cols))
    return "\n".join(lijnen)


# ---------------------------------------------------------------- stages


def stage_van(p, org_by_id):
    """Leidt de stage af uit de data. Geen opgeslagen stage-kolom."""
    org = org_by_id.get(p.get("org_id", ""), {})
    if org.get("icp_status") in ("afgevallen", "geblokkeerd", "te_klein"):
        return "geblokkeerd"
    if p.get("rol") in ("afgevallen", "achtergrond", "al_in_close", "doorverwijzing"):
        return "buiten"
    if p.get("lemlist_status") == "geimporteerd" or p.get("verzonden_linkedin") \
            or p.get("verzonden_email") or p.get("bericht_status") == "verstuurd":
        return "klaar"
    if p.get("bericht_status") in ("vervallen", "afgekeurd"):
        return "buiten"
    if p.get("bericht_status") == "gepauzeerd":
        return "gepauzeerd"
    if p.get("bericht_status") == "goedgekeurd":
        return "5"
    if p.get("rol") != "aangewezen":
        return "reserve"
    if p.get("onderzoek_status") in ("", "open", "geparkeerd"):
        return "3"
    if p.get("onderzoek_status") == "geen_haakje":
        return "buiten"
    if p.get("haakje_niveau") in ("", "onbeoordeeld"):
        return "3r"
    if p.get("haakje_niveau") in ("2", "2b", "3") and not p.get("bericht_status"):
        return "4"
    if p.get("haakje_niveau") == "1":
        return "buiten"
    return "buiten"


def orgs_stage2(orgs, people):
    """orgs die gekwalificeerd zijn en nog geen aangewezen persoon hebben."""
    heeft = {p["org_id"] for p in people if p.get("rol") == "aangewezen"}
    return [o for o in orgs if o.get("icp_status") == "gekwalificeerd" and o["org_id"] not in heeft]


# ---------------------------------------------------------------- validatie


def is_org_id(rid):
    return str(rid).startswith("org_")


def dossier_pad(rid):
    """Afgeleid uit het id, nooit opgeslagen. Namen veranderen, id's niet."""
    if is_org_id(rid):
        return os.path.join(DOSSIERS, "orgs", "%s.md" % rid)
    return os.path.join(DOSSIERS, "%s.md" % rid)


def dossier_relpad(rid):
    return os.path.relpath(dossier_pad(rid), REPO)


def dossier_lees(rid):
    pad = dossier_pad(rid)
    if not os.path.exists(pad):
        return None
    with open(pad, encoding="utf-8") as f:
        return f.read()


def dossier_secties(tekst):
    """{kop: inhoud} in leesvolgorde. Alles voor de eerste ## valt onder ''."""
    res, kop, buf = {}, "", []
    for regel in (tekst or "").splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", regel)
        if m:
            res[kop] = "\n".join(buf).strip()
            kop, buf = m.group(1), []
        else:
            buf.append(regel)
    res[kop] = "\n".join(buf).strip()
    return res


def dossier_sjabloon(rid, naam="", org_naam=""):
    secties = ORG_SECTIES if is_org_id(rid) else PERSOON_SECTIES
    kop = "# %s%s" % (naam or rid, (" — " + org_naam) if org_naam else "")
    regels = [kop, "", "<!-- id: %s -->" % rid, ""]
    for s in secties:
        regels.append("## %s" % s)
        if s == "Citaten":
            regels += [
                "<!-- elk citaat op deze vorm, de drager is verplicht:",
                '> "letterlijk citaat"',
                "  bron: <url of document, pagina> · datum: JJJJ-MM-DD · drager: %s"
                % "|".join(DRAGERS),
                "   Vaktermen hebben een vaste drager, zie de kop Vaktermen in",
                "   GTM/ICP/shift/markets/%s/profiel.md. Lees ze nooit als gewone taal. -->" % MARKT,
            ]
        regels.append("")
    return "\n".join(regels).rstrip() + "\n"


def _citaat_regels(blok):
    """(citaat, metaregel) uit een Citaten-sectie, commentaar overgeslagen."""
    regels = [r for r in (blok or "").splitlines()]
    res, i = [], 0
    in_comment = False
    while i < len(regels):
        r = regels[i]
        if "<!--" in r:
            in_comment = True
        if in_comment:
            if "-->" in r:
                in_comment = False
            i += 1
            continue
        if r.strip().startswith(">") and r.strip(" >").strip():
            meta = regels[i + 1] if i + 1 < len(regels) else ""
            res.append((r.strip(), meta.strip()))
            i += 2
            continue
        i += 1
    return res


def dossier_klachten(rid, tekst):
    """Wat er mis is met dit dossier. Lege lijst = in orde."""
    problemen = []
    secties = dossier_secties(tekst)
    toegestaan = set(ORG_SECTIES if is_org_id(rid) else PERSOON_SECTIES)
    onbekend = [k for k in secties if k and k not in toegestaan]
    if onbekend:
        problemen.append("onbekende kop(pen): %s. Toegestaan: %s"
                         % (", ".join(onbekend), ", ".join(sorted(toegestaan))))
    n = len((tekst or "").splitlines())
    if n > DOSSIER_MAX_REGELS:
        problemen.append("%d regels, de grens is %d. Een dossier dat alles bewaart is "
                         "net zo onbruikbaar als een dossier dat niets bewaart."
                         % (n, DOSSIER_MAX_REGELS))
    if not is_org_id(rid):
        cit = _citaat_regels(secties.get("Citaten", ""))
        for citaat, meta in cit:
            low = meta.lower()
            if "drager:" not in low:
                problemen.append("citaat zonder drager-label: %s" % citaat[:70])
            elif not any(("drager: " + d) in low or ("drager:" + d) in low for d in DRAGERS):
                problemen.append("drager onbekend bij: %s (kies uit %s)"
                                 % (citaat[:60], "/".join(DRAGERS)))
            if "bron:" not in low:
                problemen.append("citaat zonder bron: %s" % citaat[:70])
    return problemen


def doctor(fix_safe=False, verbose=True):
    orgs = load(ORGS, ORG_COLS)
    people = load(PEOPLE, PERSON_COLS)
    fouten, waarschuwingen, fixes = [], [], []
    bekende_markten = markten()

    # het profiel van de actieve markt: zonder compleet profiel geen wachtrij
    prof_f, prof_w = profiel_klachten(MARKT)
    fouten += ["profiel %s: %s" % (MARKT, f) for f in prof_f]
    waarschuwingen += ["profiel %s: %s" % (MARKT, w) for w in prof_w]

    org_ids = set()
    for o in orgs:
        oid = o["org_id"]
        if not oid:
            fouten.append("org zonder org_id: %s" % o.get("naam"))
        if oid in org_ids:
            fouten.append("dubbel org_id: %s" % oid)
        org_ids.add(oid)
        mk = org_markt(o)
        if not mk:
            fouten.append("%s: geen markt. Zet hem met: pipeline.py set %s --set markt=<code> --actor dante"
                          % (oid, oid))
        elif mk not in bekende_markten:
            fouten.append("%s: markt '%s' bestaat niet (wel: %s)"
                          % (oid, mk, ", ".join(bekende_markten) or "geen"))
        for veld in ("icp_status", "beoordeelt_zelf", "particulier", "omvang_niveau",
                     "segment_omvang"):
            v = (o.get(veld) or "").strip()
            if v and v not in ENUMS[veld]:
                fouten.append("%s: %s='%s' hoort niet in de woordenlijst %s"
                              % (oid, veld, v, ENUMS[veld]))
        # afkeuren op omvang mag alleen met het bewijs eronder. Zelfde regel als
        # bij poort 0: geen citaat is geen oordeel.
        if o.get("icp_status") == "te_klein":
            if not (o.get("geschatte_jaarwaarde") or "").strip():
                fouten.append("%s: te_klein zonder geschatte_jaarwaarde" % oid)
            if not (o.get("omvang_citaat") or "").strip():
                fouten.append("%s: te_klein zonder omvang_citaat" % oid)
            if not (o.get("omvang_url") or "").strip():
                waarschuwingen.append("%s: te_klein zonder omvang_url" % oid)
        # een omvangsgetal zonder bron is een gok die later als feit gelezen wordt
        if (o.get("lerenden_per_jaar") or "").strip() and not (o.get("omvang_url") or "").strip():
            waarschuwingen.append("%s: lerenden_per_jaar zonder omvang_url" % oid)
        # de afgeleide velden mogen nooit afwijken van waar ze uit volgen.
        # Alle drie, niet alleen het segment: toen het prijsmodel op 16-09-2026
        # van staffel naar prijs per student ging, bleven de oude jaarwaarden
        # anders gewoon staan en zag niemand het verschil.
        kopie = dict(o)
        _afgeleid_org(kopie)
        for veld in ("omzet_indicatie", "geschatte_jaarwaarde", "segment_omvang"):
            hoort = kopie.get(veld) or ""
            if (o.get(veld) or "") != hoort:
                if fix_safe:
                    o[veld] = hoort
                    fixes.append("%s: %s -> %s" % (oid, veld, hoort or "(leeg)"))
                else:
                    waarschuwingen.append(
                        "%s: %s='%s' maar de getallen zeggen '%s'. "
                        "Herstel met: pipeline.py doctor --fix-safe"
                        % (oid, veld, o.get(veld), hoort))
        m = o.get("moeder_org_id")
        if m and m not in org_ids and m not in {x["org_id"] for x in orgs}:
            fouten.append("%s: moeder_org_id '%s' bestaat niet" % (oid, m))

    p_ids = set()
    aangewezen_per_org = {}
    markt_van_org = {o["org_id"]: org_markt(o) for o in orgs}
    for p in people:
        pid = p["person_id"]
        if not pid:
            fouten.append("persoon zonder person_id: %s" % p.get("naam"))
        if pid in p_ids:
            fouten.append("dubbel person_id: %s" % pid)
        p_ids.add(pid)
        if p.get("org_id") not in org_ids:
            fouten.append("%s: org_id '%s' bestaat niet" % (pid, p.get("org_id")))
        for veld in ("rol", "haakje_niveau", "onderzoek_status", "bericht_status",
                     "lemlist_status", "email_status", "functie_niveau"):
            v = (p.get(veld) or "").strip()
            if v and v not in ENUMS[veld]:
                fouten.append("%s: %s='%s' hoort niet in de woordenlijst %s"
                              % (pid, veld, v, ENUMS[veld]))
        hoort = functie_niveau_van(p.get("functie"), markt_van_org.get(p.get("org_id")))
        if (p.get("functie_niveau") or "") != hoort:
            if fix_safe:
                p["functie_niveau"] = hoort
                fixes.append("%s: functie_niveau -> %s" % (pid, hoort))
            else:
                waarschuwingen.append(
                    "%s: functie_niveau='%s' maar de titel zegt '%s'. "
                    "Herstel met: pipeline.py doctor --fix-safe"
                    % (pid, p.get("functie_niveau"), hoort))
        if p.get("rol") == "aangewezen":
            aangewezen_per_org.setdefault(p["org_id"], []).append(pid)
        # niveau mag niet leeg zijn zodra er onderzoek gedaan is
        if p.get("onderzoek_status") == "gevonden" and not (p.get("haakje_niveau") or "").strip():
            if fix_safe:
                p["haakje_niveau"] = "onbeoordeeld"
                fixes.append("%s: leeg niveau -> onbeoordeeld" % pid)
            else:
                fouten.append("%s: onderzoek_status=gevonden maar haakje_niveau is leeg" % pid)
        # bericht klaar voor review zonder bron of onderbouwing
        if p.get("bericht_status") in ("concept", "goedgekeurd"):
            if not (p.get("haakje_bron_url") or "").strip():
                waarschuwingen.append("%s: bericht zonder haakje_bron_url" % pid)
            if not (p.get("waarom_dit_bericht") or "").strip():
                waarschuwingen.append("%s: bericht zonder waarom_dit_bericht" % pid)
        # uitkomst zonder reden is een half vastgelegd gesprek
        if p.get("uitkomst") in ("geen_interesse", "later_terugkomen") \
                and not (p.get("uitkomst_reden") or "").strip():
            waarschuwingen.append("%s: uitkomst '%s' zonder reden" % (pid, p.get("uitkomst")))
        if p.get("dubbel_van") and p["dubbel_van"] not in p_ids | {
                x["person_id"] for x in people}:
            fouten.append("%s: dubbel_van verwijst naar onbekend record %s"
                          % (pid, p["dubbel_van"]))
        # tekens
        cv = p.get("connectieverzoek") or ""
        if len(cv) > 300:
            fouten.append("%s: connectieverzoek is %d tekens (max 300)" % (pid, len(cv)))
        # verstuurd moet kloppen met de datumvelden
        heeft_datum = any((p.get(v) or "").strip() for v in
                          ("verzonden_linkedin", "verzonden_email", "cold_call"))
        if heeft_datum and p.get("bericht_status") not in ("verstuurd", "gepauzeerd", "vervallen"):
            if fix_safe:
                p["bericht_status"] = "verstuurd"
                fixes.append("%s: verzenddatum aanwezig -> bericht_status=verstuurd" % pid)
            else:
                waarschuwingen.append("%s: verzenddatum aanwezig maar bericht_status='%s'"
                                      % (pid, p.get("bericht_status")))

    # ---- dossiers: het master-document draagt de stand, het dossier de inhoud
    org_by_id = {o["org_id"]: o for o in orgs}
    for p in people:
        pid = p["person_id"]
        for veld in TEASER_VELDEN:
            v = (p.get(veld) or "").strip()
            if len(v) > TEASER_MAX:
                waarschuwingen.append(
                    "%s: %s is %d tekens (max %d). De lading hoort in het dossier, "
                    "dit veld is de samenvatting." % (pid, veld, len(v), TEASER_MAX))
        tekst = dossier_lees(pid)
        st = stage_van(p, org_by_id)
        if tekst is None:
            if st in ("4", "5"):
                waarschuwingen.append(
                    "%s: staat in stap %s maar heeft geen dossier (%s)"
                    % (pid, st, dossier_relpad(pid)))
            continue
        for probleem in dossier_klachten(pid, tekst):
            waarschuwingen.append("%s dossier: %s" % (pid, probleem))
        if st in ("4", "5") and not dossier_secties(tekst).get("Citaten", "").strip():
            waarschuwingen.append(
                "%s dossier: '## Citaten' is leeg, en dat is precies wat agent 4 nodig heeft"
                % pid)

    for oid, lijst in aangewezen_per_org.items():
        if len(lijst) > 1:
            fouten.append("%s heeft %d aangewezen personen: %s" % (oid, len(lijst), lijst))

    # Besluit Dante 17-09-2026: gekwalificeerd en aangewezen horen ten alle
    # tijden gelijk te staan. Een organisatie die de poort door is maar geen
    # contact heeft, is een gat dat agent 2 dezelfde ronde nog moet dichten,
    # geen rustpunt.
    for o in orgs:
        if o.get("icp_status") == "gekwalificeerd" and not aangewezen_per_org.get(o["org_id"]):
            waarschuwingen.append(
                "%s: gekwalificeerd zonder aangewezen contact. Zet agent 2 erop, "
                "of log een gat als er echt niemand te vinden is." % o["org_id"])

    if fix_safe and fixes:
        with Lock():
            save(PEOPLE, PERSON_COLS, people)
            save(ORGS, ORG_COLS, orgs)
        journal([(f.split(":")[0], "doctor", "", f, "system") for f in fixes])

    res = {"fouten": fouten, "waarschuwingen": waarschuwingen, "fixes": fixes,
           "orgs": len(orgs), "personen": len(people), "markt": MARKT,
           "profiel_compleet": not prof_f}
    if verbose:
        n_markt = sum(1 for o in orgs if org_markt(o) == MARKT)
        print("markt: %s   profiel: %s   orgs in deze markt: %d" % (
            MARKT, "compleet" if not prof_f else "%d slot(s) missen" % len(prof_f), n_markt))
        print("orgs: %d   personen: %d   (alle markten)" % (len(orgs), len(people)))
        print("fouten: %d   waarschuwingen: %d" % (len(fouten), len(waarschuwingen)))
        for f in fouten[:60]:
            print("  FOUT  " + f)
        if len(fouten) > 60:
            print("  ... en nog %d" % (len(fouten) - 60))
        for w in waarschuwingen[:30]:
            print("  let op " + w)
        if len(waarschuwingen) > 30:
            print("  ... en nog %d" % (len(waarschuwingen) - 30))
        for f in fixes:
            print("  gefixt " + f)
    return res


# ---------------------------------------------------------------- commando's

QUEUE_FIELDS = {
    "2": ["org_id", "naam", "categorie", "domein", "beoordeelt_zelf", "bewijs_citaat",
          "bewijs_url", "moeder_org_id", "contact_zoekpoging"],
    "3": ["person_id", "org_id", "org_naam", "naam", "functie", "linkedin_url",
          "in_functie_sinds", "waarom_deze_persoon", "toetsprogramma", "bewijs_citaat",
          "dossier_pad"],
    "3r": ["person_id", "org_naam", "naam", "functie", "haakje", "haakje_bron_url",
           "haakje_bron_type", "haakje_gaat_over", "opvallend", "onderzoek_status",
           "dossier_pad"],
    "4": ["person_id", "org_naam", "naam", "functie", "linkedin_url", "haakje_niveau", "haakje_trap",
          "haakje", "haakje_bron_url", "haakje_bron_type", "haakje_gaat_over", "opvallend",
          "toetsprogramma", "schrijfwerk", "alternatief_hoger_in_boom", "dossier_pad"],
    "5": ["person_id", "org_naam", "naam", "voornaam", "achternaam", "functie",
          "linkedin_url", "email", "email_status", "domein", "connectieverzoek",
          "opvolgmail_onderwerp", "opvolgmail", "reminder"],
}


def cmd_queue(a):
    eis_profiel_compleet()
    orgs, people = load_markt()
    by_id = {o["org_id"]: o for o in orgs}

    if a.stage == "2":
        rows = orgs_stage2(orgs, people)
        velden = a.fields.split(",") if a.fields else QUEUE_FIELDS["2"]
        per_org = {}
        for p in people:
            per_org.setdefault(p["org_id"], []).append(p)
        res = []
        for o in rows:
            d = {k: o.get(k, "") for k in velden}
            # wie er al bekend is bij deze org, zodat agent 2 die niet opnieuw aandraagt
            d["al_bekend"] = [
                {"naam": p["naam"], "functie": p["functie"], "rol": p["rol"],
                 "reden": p["waarom_afgevallen"] or p["waarom_deze_persoon"][:80]}
                for p in per_org.get(o["org_id"], [])
            ]
            res.append(d)
    else:
        rows = [p for p in people if stage_van(p, by_id) == a.stage]
        if a.org:
            rows = [p for p in rows if p["org_id"] == a.org]
        velden = a.fields.split(",") if a.fields else QUEUE_FIELDS.get(a.stage, PERSON_COLS)
        res = []
        for p in rows:
            o = by_id.get(p["org_id"], {})
            d = {}
            for k in velden:
                if k == "dossier_pad":
                    # afgeleid, staat niet in het CSV. Leeg = nog geen dossier.
                    d[k] = dossier_relpad(p["person_id"]) \
                        if os.path.exists(dossier_pad(p["person_id"])) else ""
                elif k == "org_naam":
                    d[k] = o.get("naam", "")
                elif k in ("domein", "bewijs_citaat", "bewijs_url", "categorie"):
                    d[k] = o.get(k, "")
                else:
                    d[k] = p.get(k, "")
            res.append(d)
    if a.limit:
        res = res[: a.limit]
    out(res, a.table)


def cmd_show(a):
    orgs = load(ORGS, ORG_COLS)
    people = load(PEOPLE, PERSON_COLS)
    for r in orgs + people:
        if r.get("org_id") == a.id and "person_id" not in r:
            mensen = [{"person_id": p["person_id"], "naam": p["naam"], "functie": p["functie"],
                       "rol": p["rol"], "haakje_niveau": p["haakje_niveau"],
                       "bericht_status": p["bericht_status"],
                       "verzonden_linkedin": p["verzonden_linkedin"]}
                      for p in people if p["org_id"] == a.id]
            d = dict(r)
            d["personen"] = mensen
            return out(d, a.table)
        if r.get("person_id") == a.id:
            d = dict(r)
            org = next((o for o in orgs if o["org_id"] == r["org_id"]), {})
            d["_org_naam"] = org.get("naam", "")
            d["_stage"] = stage_van(r, {o["org_id"]: o for o in orgs})
            d["_dossier"] = dossier_relpad(a.id) if os.path.exists(dossier_pad(a.id)) else ""
            if not a.full:
                d = {k: v for k, v in d.items() if v}
            return out(d, a.table)
    die("niet gevonden: %s" % a.id)


def cmd_dossier(a):
    rid = a.id
    orgs = load(ORGS, ORG_COLS)
    people = load(PEOPLE, PERSON_COLS)
    rec = next((o for o in orgs if o["org_id"] == rid), None) \
        or next((p for p in people if p["person_id"] == rid), None)
    if rec is None:
        die("niet gevonden: %s" % rid)
    org_naam = ""
    if "person_id" in rec:
        org_naam = next((o["naam"] for o in orgs if o["org_id"] == rec["org_id"]), "")

    if a.sjabloon:
        print(dossier_sjabloon(rid, rec.get("naam", ""), org_naam))
        return

    tekst = dossier_lees(rid)

    if a.schrijf:
        _check_actor_bekend(a.actor)
        nieuw = sys.stdin.read() if a.schrijf == "-" else open(a.schrijf, encoding="utf-8").read()
        if a.sectie:
            # alleen die sectie vervangen, de rest blijft staan
            basis = tekst if tekst is not None else dossier_sjabloon(rid, rec.get("naam", ""), org_naam)
            nieuw = _sectie_vervangen(rid, basis, a.sectie, nieuw)
        problemen = dossier_klachten(rid, nieuw)
        if problemen and not a.forceer:
            die("dossier niet weggeschreven:\n  - " + "\n  - ".join(problemen))
        pad = dossier_pad(rid)
        os.makedirs(os.path.dirname(pad), exist_ok=True)
        tmp = pad + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(nieuw if nieuw.endswith("\n") else nieuw + "\n")
        os.replace(tmp, pad)
        journal([(rid, "dossier" + (":" + a.sectie if a.sectie else ""),
                  "%d regels" % len((tekst or "").splitlines()),
                  "%d regels" % len(nieuw.splitlines()), a.actor)])
        out({"ok": True, "id": rid, "pad": dossier_relpad(rid),
             "regels": len(nieuw.splitlines()), "let_op": problemen}, a.table)
        return

    if tekst is None:
        die("nog geen dossier voor %s. Maak er een met:\n"
            "  pipeline.py dossier %s --sjabloon > /tmp/d.md   (invullen)\n"
            "  pipeline.py dossier %s --schrijf /tmp/d.md --actor <skill>" % (rid, rid, rid))

    if a.sectie:
        secties = dossier_secties(tekst)
        treffer = next((k for k in secties if norm(k) == norm(a.sectie)), None)
        if treffer is None:
            die("sectie '%s' bestaat niet. Wel: %s"
                % (a.sectie, ", ".join(k for k in secties if k)))
        print(secties[treffer])
        return

    print(tekst)


def _sectie_vervangen(rid, basis, sectie, inhoud):
    secties = ORG_SECTIES if is_org_id(rid) else PERSOON_SECTIES
    treffer = next((s for s in secties if norm(s) == norm(sectie)), None)
    if treffer is None:
        die("sectie '%s' bestaat niet in het sjabloon. Wel: %s" % (sectie, ", ".join(secties)))
    uit, vervangen, skip = [], False, False
    for regel in basis.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", regel)
        if m:
            skip = norm(m.group(1)) == norm(treffer)
            if skip:
                uit += ["## %s" % treffer, inhoud.strip(), ""]
                vervangen = True
                continue
        if not skip:
            uit.append(regel)
    if not vervangen:
        uit += ["## %s" % treffer, inhoud.strip(), ""]
    return "\n".join(uit).rstrip() + "\n"


def _check_actor_bekend(actor):
    if actor not in OWNER:
        die("onbekende actor '%s'. Kies uit: %s" % (actor, ", ".join(sorted(OWNER))))


def _naam_kern(s):
    """normaliseer een organisatienaam extra agressief voor dedup: geen rechtsvorm,
    geen & vs and, geen lidwoorden. Ruimer dan norm(), speciaal om Ltd/Limited/&
    -varianten van dezelfde organisatie te vangen (zie 15-09-2026: exists --naam
    checkte alleen personen, nooit orgs, en dat leverde die dag zeven dubbele
    organisaties op)."""
    n = norm(s)
    n = n.replace("&", " and ")
    n = re.sub(r"\b(limited|ltd|llp|plc|the|of|and|group|inc|uk)\b", " ", n)
    return re.sub(r"[^a-z0-9]", "", n)


def cmd_exists(a):
    people = load(PEOPLE, PERSON_COLS)
    orgs_lijst = load(ORGS, ORG_COLS)
    orgs = {o["org_id"]: o for o in orgs_lijst}
    hits = []
    org_hits = []
    if a.linkedin:
        s = li_slug(a.linkedin)
        hits = [p for p in people if s and li_slug(p["linkedin_url"]) == s]
    elif a.naam:
        n = norm(a.naam)
        hits = [p for p in people if norm(p["naam"]) == n]
        if a.org:
            o = norm(a.org)
            hits = [p for p in hits
                    if o in norm(orgs.get(p["org_id"], {}).get("naam", "")) or
                    norm(orgs.get(p["org_id"], {}).get("naam", "")) in o]
        # dedup-poort voor organisaties: ook zoeken op orgs.csv, exact EN op de
        # rechtsvorm-vrije kern, plus aliassen. Dit is de check die
        # `add-org` van je verwacht vóór je een nieuwe rij aanmaakt.
        kern = _naam_kern(a.naam)
        for o in orgs_lijst:
            kandidaten = [o["naam"]] + [x for x in (o.get("naam_aliassen") or "").split("|") if x]
            if any(norm(k) == n for k in kandidaten) or any(_naam_kern(k) == kern for k in kandidaten):
                org_hits.append(o)
    res = {"bestaat": bool(hits), "aantal": len(hits), "treffers": [
        {"person_id": p["person_id"], "naam": p["naam"],
         "org": orgs.get(p["org_id"], {}).get("naam", ""), "rol": p["rol"],
         "haakje_niveau": p["haakje_niveau"], "bericht_status": p["bericht_status"],
         "verzonden_linkedin": p["verzonden_linkedin"],
         "stage": stage_van(p, orgs)} for p in hits]}
    if a.naam:
        res["organisatie_bestaat"] = bool(org_hits)
        res["organisatie_treffers"] = [
            {"org_id": o["org_id"], "naam": o["naam"], "markt": o.get("markt", ""),
             "icp_status": o["icp_status"]} for o in org_hits]
        if org_hits:
            res["_let_op"] = ("Deze organisatie(naam) staat al in het systeem. Gebruik "
                              "'set <org_id>', niet 'add-org', tenzij dit aantoonbaar een "
                              "andere organisatie is.")
    out(res, a.table)


def cmd_orgs(a):
    orgs, people = load_markt()
    rows = orgs
    if a.icp_status:
        rows = [o for o in rows if o.get("icp_status") == a.icp_status]
    if a.zonder_contact:
        heeft = {p["org_id"] for p in people if p.get("rol") == "aangewezen"}
        rows = [o for o in rows if o["org_id"] not in heeft]
    if a.met_mensen:
        res = []
        for o in rows:
            d = {"org_id": o["org_id"], "naam": o["naam"], "icp_status": o["icp_status"]}
            d["personen"] = [{"person_id": p["person_id"], "naam": p["naam"],
                              "functie": p["functie"], "rol": p["rol"],
                              "bericht_status": p["bericht_status"],
                              "verzonden_linkedin": p["verzonden_linkedin"],
                              "verzonden_email": p["verzonden_email"],
                              "cold_call": p["cold_call"]}
                             for p in people if p["org_id"] == o["org_id"]]
            res.append(d)
    else:
        res = [{k: o.get(k, "") for k in ("org_id", "naam", "categorie", "icp_status",
                                          "blokkade_reden")} for o in rows]
    if a.limit:
        res = res[: a.limit]
    out(res, a.table)


def _check_actor(actor, velden):
    toegestaan = OWNER.get(actor)
    if toegestaan is None:
        die("onbekende actor '%s'. Kies uit: %s" % (actor, ", ".join(sorted(OWNER))))
    fout = [v for v in velden if v not in toegestaan]
    if fout:
        die("actor '%s' mag deze velden niet schrijven: %s" % (actor, ", ".join(fout)))


def _check_enum(velden):
    for k, v in velden.items():
        if k in ENUMS and (v or "") not in ENUMS[k]:
            die("%s='%s' hoort niet in de woordenlijst: %s" % (k, v, ENUMS[k]))
    mk = velden.get("markt")
    if mk is not None and mk not in markten():
        die("markt '%s' bestaat niet. Wel: %s" % (mk, ", ".join(markten()) or "geen"))
    # harde grenzen, voor het schrijven en niet erna
    cv = velden.get("connectieverzoek")
    if cv is not None and len(cv) > 300:
        die("connectieverzoek is %d tekens, LinkedIn staat er 300 toe. Niet weggeschreven."
            % len(cv))
    for veld in TEASER_VELDEN:
        v = velden.get(veld)
        if v is not None and len(v) > TEASER_MAX:
            die("%s is %d tekens, de grens is %d. Dit veld is de samenvatting voor de "
                "wachtrij, niet de drager van het onderzoek. Zet de inhoud in het dossier:\n"
                "  pipeline.py dossier <id> --schrijf -" % (veld, len(v), TEASER_MAX))
    for veld in ("haakje_gevonden_op", "verzonden_linkedin", "verzonden_email", "cold_call",
                 "gepauzeerd_tot", "uitkomst_datum", "functie_geverifieerd_op",
                 "close_gecheckt_op", "linkedin_geaccepteerd_op", "reactie_gekregen_op"):
        v = (velden.get(veld) or "").strip()
        if v and not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", v):
            die("%s='%s' is geen datum. Gebruik JJJJ-MM-DD (of JJJJ-MM als de dag onbekend is)."
                % (veld, v))


def _parse_sets(sets):
    d = {}
    for s in sets or []:
        if "=" not in s:
            die("--set verwacht veld=waarde, kreeg '%s'" % s)
        k, v = s.split("=", 1)
        d[k.strip()] = v
    return d


def cmd_set(a):
    velden = _parse_sets(a.set)
    if not velden:
        die("niets te zetten")
    _check_actor(a.actor, velden.keys())
    _check_enum(velden)
    is_org = a.id.startswith("org_")
    pad, cols = (ORGS, ORG_COLS) if is_org else (PEOPLE, PERSON_COLS)
    sleutel = "org_id" if is_org else "person_id"
    with Lock():
        rows = load(pad, cols)
        doel = next((r for r in rows if r[sleutel] == a.id), None)
        if doel is None:
            die("niet gevonden: %s" % a.id)
        onbekend = [k for k in velden if k not in cols]
        if onbekend:
            die("onbekende kolom(men): %s" % ", ".join(onbekend))
        entries = []
        for k, v in velden.items():
            if (doel.get(k) or "") != v:
                entries.append((a.id, k, doel.get(k, ""), v, a.actor))
                doel[k] = v
        # afgeleide velden bijwerken
        if is_org:
            _afgeleid_org(doel)
        else:
            _afgeleid(doel, _markt_van_person(doel))
        doel["laatst_bijgewerkt"] = now_iso()
        doel["bijgewerkt_door"] = a.actor
        save(pad, cols, rows)
    journal(entries)
    out({"ok": True, "id": a.id, "gewijzigd": [e[1] for e in entries]}, a.table)
    doctor(verbose=False)


_ORG_MARKT_CACHE = None


def _markt_van_person(p):
    """De markt van de organisatie waar deze persoon bij hoort.

    Eenmalig gecached: zonder cache leest elke `set` op een persoon de hele
    orgs.csv opnieuw, en een nachtronde doet er honderden.
    """
    global _ORG_MARKT_CACHE
    oid = p.get("org_id")
    if not oid:
        return None
    if _ORG_MARKT_CACHE is None:
        _ORG_MARKT_CACHE = {o["org_id"]: org_markt(o) for o in load(ORGS, ORG_COLS)}
    return _ORG_MARKT_CACHE.get(oid)


def _afgeleid_org(o):
    """Omvangsvelden die uit andere velden volgen. Je zet ze nooit met de hand.

    Ontbreekt een van de ingredienten, dan blijft het veld leeg. Een lege cel
    betekent "niet uitgerekend", en dat is iets anders dan nul.
    """
    lerenden = getal(o.get("lerenden_per_jaar"))
    prijs = getal(o.get("cursusprijs"))
    # ook leegmaken als de invoer verdwijnt, anders blijft een oude uitkomst
    # staan bij een getal dat er niet meer is
    o["omzet_indicatie"] = str(int(lerenden * prijs)) \
        if (lerenden is not None and prijs is not None) else ""
    waarde = bereken_jaarwaarde(o.get("lerenden_per_jaar"))
    o["geschatte_jaarwaarde"] = str(waarde) if waarde is not None else ""
    o["segment_omvang"] = segment_omvang_van(o)


def _afgeleid(p, markt=None):
    """velden die uit andere velden volgen, nooit met de hand gezet.

    `markt` is de markt van de organisatie waar deze persoon bij hoort. Laat je
    hem leeg, dan geldt de actieve markt; dat klopt voor `set` en `touch`, maar
    niet voor een ronde over alle records heen.
    """
    if not p.get("voornaam") and p.get("naam"):
        p["voornaam"], p["achternaam"] = split_naam(p["naam"])
    p["functie_niveau"] = functie_niveau_van(p.get("functie"), markt)
    if any((p.get(v) or "").strip() for v in ("verzonden_linkedin", "verzonden_email", "cold_call")):
        if p.get("bericht_status") not in ("gepauzeerd", "vervallen"):
            p["bericht_status"] = "verstuurd"


def cmd_promote(a):
    with Lock():
        people = load(PEOPLE, PERSON_COLS)
        doel = next((p for p in people if p["person_id"] == a.id), None)
        if doel is None:
            die("niet gevonden: %s" % a.id)
        oid = doel["org_id"]
        entries = []
        for p in people:
            if p["org_id"] == oid and p["rol"] == "aangewezen" and p is not doel:
                entries.append((p["person_id"], "rol", "aangewezen", "tweede_kandidaat", a.actor))
                p["rol"] = "tweede_kandidaat"
                p["laatst_bijgewerkt"] = now_iso()
                p["bijgewerkt_door"] = a.actor
        entries.append((doel["person_id"], "rol", doel["rol"], "aangewezen", a.actor))
        doel["rol"] = "aangewezen"
        if not doel.get("onderzoek_status"):
            doel["onderzoek_status"] = "open"
        doel["laatst_bijgewerkt"] = now_iso()
        doel["bijgewerkt_door"] = a.actor
        save(PEOPLE, PERSON_COLS, people)
    journal(entries)
    out({"ok": True, "aangewezen": a.id,
         "teruggezet": [e[0] for e in entries if e[3] == "tweede_kandidaat"]}, a.table)


def cmd_touch(a):
    veld = TOUCH_VELD[a.kanaal]
    with Lock():
        people = load(PEOPLE, PERSON_COLS)
        doel = next((p for p in people if p["person_id"] == a.id), None)
        if doel is None:
            die("niet gevonden: %s" % a.id)
        oud = doel.get(veld, "")
        doel[veld] = a.datum or now_iso()
        _afgeleid(doel)
        doel["laatst_bijgewerkt"] = now_iso()
        doel["bijgewerkt_door"] = a.actor
        save(PEOPLE, PERSON_COLS, people)
    journal([(a.id, veld, oud, doel[veld], a.actor)])
    out({"ok": True, "id": a.id, veld: doel[veld],
         "bericht_status": doel["bericht_status"]}, a.table)


def cmd_add_org(a):
    velden = _parse_sets(a.set)
    velden["naam"] = a.naam
    _check_actor(a.actor, velden.keys())
    _check_enum(velden)
    oid = org_id_for(a.naam)
    if MARKT not in markten():
        die("markt '%s' bestaat niet. Maak hem eerst aan: pipeline.py markt --nieuw %s" % (MARKT, MARKT))
    with Lock():
        orgs = load(ORGS, ORG_COLS)
        if any(o["org_id"] == oid for o in orgs):
            die("bestaat al: %s" % oid)
        if not getattr(a, "forceer_dubbel", False):
            kern = _naam_kern(a.naam)
            n = norm(a.naam)
            for o in orgs:
                kandidaten = [o["naam"]] + [x for x in (o.get("naam_aliassen") or "").split("|") if x]
                if any(norm(k) == n for k in kandidaten) or any(_naam_kern(k) == kern for k in kandidaten):
                    die("lijkt al te bestaan als %s (%s). Gebruik 'set %s' om bij te werken, of "
                        "voeg --forceer-dubbel toe als dit aantoonbaar een andere organisatie is "
                        "(bijv. een dochter met dezelfde naam in een ander land)."
                        % (o["org_id"], o["naam"], o["org_id"]))
        rij = {c: "" for c in ORG_COLS}
        rij.update({k: v for k, v in velden.items() if k in ORG_COLS})
        rij["org_id"] = oid
        rij["markt"] = MARKT
        rij.setdefault("icp_status", "kandidaat")
        if not rij["icp_status"]:
            rij["icp_status"] = "kandidaat"
        _afgeleid_org(rij)
        rij["laatst_bijgewerkt"] = now_iso()
        rij["bijgewerkt_door"] = a.actor
        orgs.append(rij)
        save(ORGS, ORG_COLS, orgs)
    journal([(oid, "aangemaakt", "", a.naam, a.actor)])
    out({"ok": True, "org_id": oid}, a.table)


def cmd_add_person(a):
    velden = _parse_sets(a.set)
    velden["naam"] = a.naam
    if a.linkedin:
        velden["linkedin_url"] = a.linkedin
    _check_actor(a.actor, list(velden.keys()) + ["org_id"])
    _check_enum(velden)
    with Lock():
        orgs = load(ORGS, ORG_COLS)
        org = next((o for o in orgs if o["org_id"] == a.org_id), None)
        if org is None:
            die("onbekende org_id: %s" % a.org_id)
        people = load(PEOPLE, PERSON_COLS)
        pid = person_id_for(a.naam, a.linkedin, org["naam"])
        if any(p["person_id"] == pid for p in people):
            die("bestaat al: %s (gebruik set om bij te werken)" % pid)
        rij = {c: "" for c in PERSON_COLS}
        rij.update({k: v for k, v in velden.items() if k in PERSON_COLS})
        rij["person_id"] = pid
        rij["org_id"] = a.org_id
        if not rij["rol"]:
            rij["rol"] = "achtergrond"
        if rij["rol"] == "aangewezen" and not rij["onderzoek_status"]:
            rij["onderzoek_status"] = "open"
        _afgeleid(rij)
        rij["laatst_bijgewerkt"] = now_iso()
        rij["bijgewerkt_door"] = a.actor
        people.append(rij)
        save(PEOPLE, PERSON_COLS, people)
    journal([(pid, "aangemaakt", "", a.naam, a.actor)])
    out({"ok": True, "person_id": pid}, a.table)
    doctor(verbose=False)


def cmd_status(a):
    orgs, people = load_markt()
    by_id = {o["org_id"]: o for o in orgs}
    telling = {}
    for p in people:
        s = stage_van(p, by_id)
        telling[s] = telling.get(s, 0) + 1
    res = {
        "markt": MARKT,
        "orgs_totaal": len(orgs),
        "orgs_gekwalificeerd": sum(1 for o in orgs if o["icp_status"] == "gekwalificeerd"),
        "orgs_kandidaat": sum(1 for o in orgs if o["icp_status"] == "kandidaat"),
        "orgs_geblokkeerd": sum(1 for o in orgs if o["icp_status"] == "geblokkeerd"),
        "orgs_te_klein": sum(1 for o in orgs if o["icp_status"] == "te_klein"),
        "personen_totaal": len(people),
        "stage_2_orgs_zonder_contact": len(orgs_stage2(orgs, people)),
        "stage_3_onderzoek": telling.get("3", 0),
        "stage_3r_niveau_ontbreekt": telling.get("3r", 0),
        "stage_4_bericht_schrijven": telling.get("4", 0),
        "stage_5_klaar_voor_lemlist": telling.get("5", 0),
        "gepauzeerd": telling.get("gepauzeerd", 0),
        "klaar_benaderd": telling.get("klaar", 0),
        "reserve_tweede_kandidaten": telling.get("reserve", 0),
        "buiten_scope": telling.get("buiten", 0) + telling.get("geblokkeerd", 0),
    }
    if a.doel:
        klaar = res["stage_4_bericht_schrijven"]
        tekort = max(0, a.doel - klaar)
        plan = []
        if tekort == 0:
            plan.append("stage 4 heeft %d klaarstaande records: genoeg voor %d." % (klaar, a.doel))
        else:
            plan.append("stage 4 heeft er %d, nodig %d extra." % (klaar, tekort))
            rest = tekort
            for naam, sleutel in (("stage 3r (alleen niveau toekennen)", "stage_3r_niveau_ontbreekt"),
                                  ("stage 3 (onderzoek)", "stage_3_onderzoek"),
                                  ("stage 2 (contact zoeken)", "stage_2_orgs_zonder_contact")):
                if rest <= 0:
                    break
                n = min(rest, res[sleutel])
                if n:
                    plan.append("  pak %d uit %s (voorraad %d)" % (n, naam, res[sleutel]))
                    rest -= n
            if rest > 0:
                plan.append("  komt %d tekort, agent 1 moet nieuwe organisaties zoeken." % rest)
        res["plan"] = plan
    out(res, a.table)


# ---------------------------------------------------------------- lemlist
#
# De terugschrijf-stap: wat er in de campagne gebeurde terug het master-document
# in. Zonder deze stap staat er wel "verstuurd" maar nooit een acceptatie, en is
# elk segmentrapport leeg.
#
# DIT SCRIPT PRAAT NIET MET LEMLIST. Besluit Dante 16-09-2026: alle
# Lemlist-verkeer loopt via de claude.ai-connector, nooit via de REST API. De
# API-sleutel geeft op elk endpoint 403 (error 1010) omdat het account geen
# REST-toegang heeft, terwijl de connector prima werkt. Een script dat het toch
# via HTTP probeert, faalt dus altijd en kost alleen tijd.
#
# De werkverdeling die daaruit volgt:
#   1. Claude haalt de leads op met de Lemlist-connector:
#        search_campaign_leads(campaignId=..., include=["activities"], limit=100)
#   2. Claude zet de `leads`-array in een JSON-bestand.
#   3. Dit commando leest dat bestand en schrijft de feiten weg.
# Zo blijft pipeline.py de enige schrijver van het master-document, en blijft
# het netwerk buiten dit bestand.

# Lemlist levert `activities` als een string, een regel per gebeurtenis:
#   [2026-07-30] linkedinInviteAccepted: linkedinInviteAccepted
#   [2026-07-30] linkedinReplied: Hi Dante, I am happy to be connected, but ...
# Vandaar een regexparser en geen JSON-pad.
_ACT_REGEL = re.compile(r"^\[(\d{4}-\d{2}-\d{2})\]\s*([A-Za-z]+)\s*:\s*(.*)$")

# Welk gebeurtenistype welk veld zet. Lemlist heeft zijn typenamen eerder
# hernoemd, dus we matchen op een stuk van de naam in plaats van op de hele
# string, en een type dat we niet kennen wordt gemeld in plaats van genegeerd.
LEMLIST_EVENTS = [
    ("inviteaccepted", "linkedin_geaccepteerd_op"),
    ("linkedinreplied", "reactie_gekregen_op"),
    ("emailsreplied", "reactie_gekregen_op"),
    ("invitedone", "verzonden_linkedin"),
    ("linkedinsent", "verzonden_linkedin"),
    ("emailssent", "verzonden_email"),
    ("aircalldone", "cold_call"),
]
# Types die niets over de prospect zeggen of al in het master-document staan.
# outofoffice staat er bewust bij: een automatisch antwoord is geen reactie, en
# als je hem meetelt lijkt elke afwezigheidsmelding een gesprek.
LEMLIST_NEGEER = ("conditionchosen", "skipped", "paused", "resumed", "visitdone",
                  "opened", "clicked", "bounced", "failed", "unsubscribed",
                  "outofoffice", "interested", "notinterested", "hooked",
                  "attracted", "custom")

# Een reactie waarvan de tekst bewaard wordt, zodat Dante hem kan duiden
# zonder Lemlist te openen. Let op het verschil: bij LinkedIn levert Lemlist de
# echte tekst, bij mail alleen de onderwerpregel ("Re: ...").
LEMLIST_REACTIE_TYPES = ("linkedinreplied", "emailsreplied")


def _act_regels(lead):
    """(datum, type, tekst) per gebeurtenis, oudste eerst."""
    ruw = lead.get("activities") or ""
    if isinstance(ruw, list):                      # voor het geval Lemlist ooit JSON gaat leveren
        uit = []
        for a in ruw:
            d = str(a.get("createdAt") or a.get("date") or "")[:10]
            uit.append((d, norm(a.get("type")).replace(" ", ""), str(a.get("text") or "")))
        return sorted(uit)
    uit = []
    for regel in str(ruw).splitlines():
        m = _ACT_REGEL.match(regel.strip())
        if m:
            uit.append((m.group(1), norm(m.group(2)).replace(" ", ""), m.group(3).strip()))
    return sorted(uit)


# De peiling: een goedkope poort voor een dure operatie.
#
# Het ophalen van alle leads met hun activiteiten kost ongeveer een kwart
# miljoen tokens, vooral door het aantal aanroepen. De meeste dagen is er
# niets veranderd. `get_campaigns_stats` is een enkele kleine aanroep die de
# totalen geeft; is die gelijk aan de vorige keer, dan hoeft de rest niet.
PEILING = os.path.join(MASTER, ".lemlist-peiling.json")


def cmd_peiling(a):
    """Vergelijk de tellingen van Lemlist met die van de vorige sync.

    Claude draait get_campaigns_stats en geeft de drie totalen door. Dit
    commando zegt of het de moeite waard is om alles op te halen.
    """
    nu = {"verstuurd": a.verstuurd, "geaccepteerd": a.geaccepteerd, "gereageerd": a.gereageerd}
    vorig = {}
    if os.path.exists(PEILING):
        try:
            with open(PEILING, encoding="utf-8") as f:
                vorig = json.load(f).get(MARKT, {})
        except ValueError:
            pass

    verschil = {k: nu[k] - vorig.get(k, 0) for k in nu}
    nodig = any(v != 0 for v in verschil.values()) or not vorig

    if a.leg_vast:
        alles = {}
        if os.path.exists(PEILING):
            try:
                with open(PEILING, encoding="utf-8") as f:
                    alles = json.load(f)
            except ValueError:
                pass
        alles[MARKT] = dict(nu, gepeild_op=stamp())
        with open(PEILING, "w", encoding="utf-8") as f:
            json.dump(alles, f, ensure_ascii=False, indent=2)

    out({"markt": MARKT, "nu": nu, "vorige_sync": vorig or None, "verschil": verschil,
         "ophalen_nodig": nodig,
         "advies": ("haal de leads op, er is iets veranderd" if nodig else
                    "sla het ophalen over, de tellingen zijn gelijk aan de vorige sync"),
         "vastgelegd": bool(a.leg_vast)}, a.table)


def cmd_sync_lemlist(a):
    """Leest een export van de Lemlist-connector en zet de feiten in het master-document.

    Zet bewust GEEN uitkomst. Een reactie kan een ja, een nee of een
    doorverwijzing zijn, en `uitkomst` hoort de reden in zijn eigen woorden te
    dragen. De tekst van de reactie wordt wel bewaard, zodat het duiden een
    kwestie van lezen is en niet van Lemlist erbij pakken.
    """
    if not os.path.exists(a.invoer):
        die("bestand niet gevonden: %s\n"
            "Laat Claude de leads eerst ophalen met de Lemlist-connector:\n"
            "  search_campaign_leads(campaignId=\"cam_...\", include=[\"activities\"], limit=100)\n"
            "en de `leads`-array als JSON in dat bestand zetten." % a.invoer)
    with open(a.invoer, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = data.get("leads") or data.get("data") or []
    if not isinstance(data, list):
        die("%s bevat geen lijst met leads" % a.invoer)

    people = load(PEOPLE, PERSON_COLS)
    op_leadid = {p["lemlist_lead_id"]: p for p in people if p.get("lemlist_lead_id")}
    op_email = {norm(p["email"]): p for p in people if p.get("email")}
    op_li = {li_slug(p["linkedin_url"]): p for p in people if li_slug(p.get("linkedin_url"))}

    wijzigingen, onbekend_type, niet_gevonden = [], {}, []
    for lead in data:
        p = (op_leadid.get(lead.get("_id") or lead.get("id"))
             or op_li.get(li_slug(lead.get("linkedinUrl")))
             or op_email.get(norm(lead.get("email"))))
        if p is None:
            niet_gevonden.append(lead.get("email") or lead.get("linkedinUrl") or lead.get("_id"))
            continue
        for datum, typ, tekst in _act_regels(lead):
            veld = next((v for stuk, v in LEMLIST_EVENTS if stuk in typ), None)
            if veld is None:
                if not any(n in typ for n in LEMLIST_NEGEER):
                    onbekend_type[typ] = onbekend_type.get(typ, 0) + 1
                continue
            # de eerste keer telt: een tweede mail maakt de eerste verzenddatum niet ongedaan
            oud = (p.get(veld) or "").strip()
            if not oud or datum < oud:
                wijzigingen.append((p, veld, oud, datum))
                if not a.droog:
                    p[veld] = datum
            if any(r in typ for r in LEMLIST_REACTIE_TYPES) and tekst:
                kort = tekst[:TEASER_MAX]
                if (p.get("reactie_tekst") or "") != kort:
                    wijzigingen.append((p, "reactie_tekst", p.get("reactie_tekst", ""), kort))
                    if not a.droog:
                        p["reactie_tekst"] = kort
        if not a.droog:
            lid = lead.get("_id") or lead.get("id")
            if lid and not p.get("lemlist_lead_id"):
                p["lemlist_lead_id"] = lid
            cid = lead.get("campaignId")
            if cid and not p.get("lemlist_campagne_id"):
                p["lemlist_campagne_id"] = cid
            if wijzigingen and wijzigingen[-1][0] is p:
                _afgeleid(p, _markt_van_person(p))
                p["laatst_bijgewerkt"] = now_iso()
                p["bijgewerkt_door"] = "lemlist-sync"

    if wijzigingen and not a.droog:
        with Lock():
            save(PEOPLE, PERSON_COLS, people)
        journal([(p["person_id"], veld, oud, nieuw, "lemlist-sync")
                 for p, veld, oud, nieuw in wijzigingen])

    res = {
        "markt": MARKT, "droog": bool(a.droog), "leads_gelezen": len(data),
        "bijgewerkt": len(wijzigingen),
        "acceptaties": sum(1 for _, v, _, _ in wijzigingen if v == "linkedin_geaccepteerd_op"),
        "reacties": sum(1 for _, v, _, _ in wijzigingen if v == "reactie_gekregen_op"),
        "lead_niet_in_master": len(niet_gevonden),
        "records": ["%s %s=%s" % (p["person_id"], v, n)
                    for p, v, _, n in wijzigingen if v != "reactie_tekst"][:40],
    }
    if niet_gevonden:
        res["niet_gevonden"] = niet_gevonden[:15]
    if onbekend_type:
        res["onbekende_types"] = onbekend_type
        res["let_op"] = ("Lemlist stuurde types die dit script niet kent. Kijk of er een "
                         "acceptatie of reactie tussen zit en vul LEMLIST_EVENTS aan.")
    out(res, a.table)


# ---------------------------------------------------------------- rapport
#
# Onder deze grens zegt het rapport geen percentage maar "te weinig volume".
# Reden: op 16-09-2026 waren er 45 berichten de deur uit over vier segmenten
# verdeeld. Een reply-percentage op zes leads is ruis die eruitziet als een
# conclusie, en daar wordt vervolgens een segment op afgeschreven.
MIN_VOOR_CONCLUSIE = 30

# De assen waarop we kijken of het werkt. Elke as is een veld dat al bestaat,
# geen nieuw oordeel per record.
RAPPORT_ASSEN = {
    "omvang": ("segment_omvang", "org"),
    "functie": ("functie_niveau", "persoon"),
    "haakje": ("haakje_niveau", "persoon"),
    "markt": ("markt", "org"),
}


def _rapport_rijen(as_naam, alle_markten=False):
    veld, waar = RAPPORT_ASSEN[as_naam]
    orgs = load(ORGS, ORG_COLS)
    if not alle_markten:
        orgs = [o for o in orgs if org_markt(o) == MARKT]
    org_by_id = {o["org_id"]: o for o in orgs}
    people = [p for p in load(PEOPLE, PERSON_COLS) if p.get("org_id") in org_by_id]

    groepen = {}
    for p in people:
        if p.get("rol") != "aangewezen":
            continue
        org = org_by_id.get(p["org_id"], {})
        sleutel = (org.get(veld) if waar == "org" else p.get(veld)) or "(leeg)"
        g = groepen.setdefault(sleutel, dict(segment=sleutel, aangewezen=0, verstuurd=0,
                                             geaccepteerd=0, gereageerd=0, positief=0, nee=0))
        g["aangewezen"] += 1
        if any((p.get(v) or "").strip() for v in ("verzonden_linkedin", "verzonden_email", "cold_call")):
            g["verstuurd"] += 1
        if (p.get("linkedin_geaccepteerd_op") or "").strip():
            g["geaccepteerd"] += 1
        if (p.get("reactie_gekregen_op") or "").strip():
            g["gereageerd"] += 1
        if p.get("uitkomst") in ("interesse", "gesprek_gepland", "doorverwezen"):
            g["positief"] += 1
        if p.get("uitkomst") == "geen_interesse":
            g["nee"] += 1

    rijen = []
    for g in sorted(groepen.values(), key=lambda x: -x["verstuurd"]):
        n = g["verstuurd"]
        if g["segment"] in ("onbekend", "(leeg)"):
            # geen segment maar een gat in de data. Een percentage hierop leest
            # als een bevinding over een groep, en die groep bestaat niet.
            g["accept"] = "-"
            g["reactie"] = "-"
            g["oordeel"] = "geen segment, hier ontbreekt het veld"
        elif n >= MIN_VOOR_CONCLUSIE:
            # acceptatie apart, want dat is de eerste poort en de enige die
            # alleen over de openingszin gaat. Een bericht dat niet geaccepteerd
            # wordt is nooit gelezen, dus een lage reactiegraad daaronder zegt
            # niets over de inhoud.
            g["accept"] = "%.0f%%" % (g["geaccepteerd"] * 100.0 / n)
            g["reactie"] = "%.0f%%" % (g["gereageerd"] * 100.0 / n)
            g["oordeel"] = ""
        else:
            g["accept"] = "-"
            g["reactie"] = "-"
            g["oordeel"] = "te weinig volume (%d van %d)" % (n, MIN_VOOR_CONCLUSIE)
        rijen.append(g)
    return rijen


def cmd_rapport(a):
    """Werkt het, en voor wie. Vier assen, en een rem op te kleine aantallen."""
    assen = [a.as_] if a.as_ else list(RAPPORT_ASSEN)
    people = load(PEOPLE, PERSON_COLS)
    verstuurd = sum(1 for p in people if any((p.get(v) or "").strip() for v in
                                             ("verzonden_linkedin", "verzonden_email", "cold_call")))
    gemeten = sum(1 for p in people if (p.get("linkedin_geaccepteerd_op") or "").strip()
                  or (p.get("reactie_gekregen_op") or "").strip())
    # sync-lemlist zet alleen de datum. Wat de reactie betekende is mensenwerk,
    # en zolang dat niet gebeurd is telt hij nergens als resultaat mee.
    teduiden = [p for p in people if (p.get("reactie_gekregen_op") or "").strip()
                and not (p.get("uitkomst") or "").strip()]

    if a.table:
        print("markt: %s   verstuurd: %d   waarvan een uitkomst geregistreerd: %d"
              % (MARKT, verstuurd, gemeten))
        if verstuurd and gemeten < verstuurd * 0.25:
            print("LET OP: van %d verstuurde berichten is er %d met een acceptatie of reactie "
                  "teruggeschreven. Een laag percentage hieronder betekent dus vooral dat de "
                  "meetlus leeg is, niet dat niemand reageerde. Vul hem: "
                  "pipeline.py --markt %s sync-lemlist" % (verstuurd, gemeten, MARKT))
        for naam in assen:
            print("\n== %s ==" % naam)
            print(as_table(_rapport_rijen(naam, alle_markten=(naam == "markt"))))
        if teduiden:
            print("\n%d reactie(s) wachten op een duiding. Zolang die leeg is telt de reactie "
                  "nergens als resultaat:" % len(teduiden))
            for p in teduiden[:10]:
                print("  pipeline.py uitkomst %s --status <interesse|geen_interesse|...> "
                      "--reden \"<in zijn eigen woorden>\"" % p["person_id"])
        return

    out({"markt": MARKT, "verstuurd": verstuurd, "uitkomst_geregistreerd": gemeten,
         "minimum_voor_conclusie": MIN_VOOR_CONCLUSIE,
         "reacties_zonder_duiding": [p["person_id"] for p in teduiden],
         "assen": {naam: _rapport_rijen(naam, alle_markten=(naam == "markt")) for naam in assen}})


def cmd_cockpit(a):
    """Alles wat de cockpit-pagina laat zien, in een JSON.

    De pagina is een Artifact en leest deze export; hij praat niet zelf met het
    master-document. Zo blijft pipeline.py de enige die de stand kent, en kan de
    pagina in een andere sessie gebouwd worden zonder de CSV's te openen.

    Vier blokken, een per scherm:
      stand      de trechter, en wat er per as gemeten is
      goedkeuren de concepten die op Jeroen wachten, met haakje en bron erbij
      reacties   wie er antwoordde, met de tekst, en of de uitkomst nog ontbreekt
      agents     hoeveel elke agent opleverde en waar hij op vastliep
    """
    orgs_l, people = load_markt()
    orgs = {o["org_id"]: o for o in orgs_l}

    def org_van(p):
        return orgs.get(p.get("org_id"), {})

    # ---- stand
    telling = {}
    for p in people:
        st = stage_van(p, orgs)
        telling[st] = telling.get(st, 0) + 1
    assen = {naam: _rapport_rijen(naam, alle_markten=(naam == "markt"))
             for naam in RAPPORT_ASSEN}

    # ---- goedkeuren: precies de wachtrij van stap 5-in-wording
    goedkeuren = []
    for p in people:
        if p.get("bericht_status") != "concept":
            continue
        o = org_van(p)
        goedkeuren.append({
            "person_id": p["person_id"], "naam": p["naam"], "functie": p["functie"],
            "functie_niveau": p["functie_niveau"], "linkedin_url": p["linkedin_url"],
            "organisatie": o.get("naam", ""), "segment_omvang": o.get("segment_omvang", ""),
            "lerenden_per_jaar": o.get("lerenden_per_jaar", ""),
            "haakje": p["haakje"], "haakje_bron_url": p["haakje_bron_url"],
            "haakje_bron_type": p["haakje_bron_type"], "haakje_niveau": p["haakje_niveau"],
            "toetsprogramma": p["toetsprogramma"], "opvallend": p["opvallend"],
            "connectieverzoek": p["connectieverzoek"],
            "opvolgmail_onderwerp": p["opvolgmail_onderwerp"], "opvolgmail": p["opvolgmail"],
            "reminder": p["reminder"],
            "waarom_dit_bericht": p["waarom_dit_bericht"], "twijfels": p["twijfels"],
            "afgevallen_openers": p["afgevallen_openers"],
            "dossier": dossier_relpad(p["person_id"]),
        })

    # ---- reacties: alles waar iemand op antwoordde
    reacties = []
    for p in people:
        if not (p.get("reactie_gekregen_op") or "").strip():
            continue
        o = org_van(p)
        reacties.append({
            "person_id": p["person_id"], "naam": p["naam"], "functie": p["functie"],
            "organisatie": o.get("naam", ""), "linkedin_url": p["linkedin_url"],
            "reactie_gekregen_op": p["reactie_gekregen_op"],
            "reactie_tekst": p["reactie_tekst"],
            "connectieverzoek": p["connectieverzoek"],
            "opvolgmail_onderwerp": p["opvolgmail_onderwerp"],
            "haakje": p["haakje"], "haakje_bron_url": p["haakje_bron_url"],
            "uitkomst": p["uitkomst"], "uitkomst_reden": p["uitkomst_reden"],
            "geduid": bool((p.get("uitkomst") or "").strip()),
        })
    reacties.sort(key=lambda r: (r["geduid"], r["reactie_gekregen_op"]))

    # ---- agents: wat leverde elke stap op, en waar bleef het liggen
    agents = [
        {"nr": 1, "naam": "lead-sourcing", "levert": "organisaties met bewijs",
         "voorraad": sum(1 for o in orgs_l if o["icp_status"] == "kandidaat"),
         "klaar": sum(1 for o in orgs_l if o["icp_status"] == "gekwalificeerd"),
         "gat": sum(1 for o in orgs_l if o["icp_status"] == "gekwalificeerd"
                    and not (o.get("lerenden_per_jaar") or "").strip()),
         "gat_uitleg": "gekwalificeerd zonder lerendenaantal, dus zonder dealwaarde en zonder segment"},
        {"nr": 2, "naam": "contact-sourcing", "levert": "een aangewezen persoon per organisatie",
         "voorraad": len(orgs_stage2(orgs_l, people)),
         "klaar": sum(1 for p in people if p.get("rol") == "aangewezen"),
         "gat": sum(1 for p in people if p.get("rol") == "aangewezen"
                    and p.get("functie_niveau") == "onbekend"),
         "gat_uitleg": "aangewezen met een functietitel die de rangorde van de markt niet kent"},
        {"nr": 3, "naam": "shift-research", "levert": "een haakje met bron",
         "voorraad": telling.get("3", 0) + telling.get("3r", 0),
         "klaar": sum(1 for p in people if p.get("onderzoek_status") == "gevonden"),
         "gat": sum(1 for p in people if p.get("onderzoek_status") == "geen_haakje"),
         "gat_uitleg": "onderzocht en niets bruikbaars gevonden"},
        {"nr": 4, "naam": "outreach", "levert": "de drie berichten",
         "voorraad": telling.get("4", 0),
         "klaar": sum(1 for p in people if p.get("bericht_status") in ("concept", "goedgekeurd", "verstuurd")),
         "gat": sum(1 for p in people if p.get("bericht_status") == "afgekeurd"),
         "gat_uitleg": "door Dante of Jeroen afgekeurd"},
        {"nr": 5, "naam": "lemlist-import", "levert": "leads in de campagne",
         "voorraad": telling.get("5", 0),
         "klaar": sum(1 for p in people if p.get("lemlist_status") == "geimporteerd"),
         "gat": sum(1 for p in people if p.get("lemlist_status") == "fout"),
         "gat_uitleg": "import mislukt"},
    ]

    verstuurd = [p for p in people if any((p.get(v) or "").strip() for v in
                                          ("verzonden_linkedin", "verzonden_email", "cold_call"))]
    res = {
        "markt": MARKT,
        "gemaakt_op": stamp(),
        "prijsmodel": {"per_student_per_maand": PRIJS_PER_STUDENT_MAAND,
                       "valuta": VALUTA, "maanden": MAANDEN_PER_JAAR,
                       "drempel_jaarwaarde": DREMPEL_JAARWAARDE},
        "stand": {
            "orgs_totaal": len(orgs_l),
            "orgs_gekwalificeerd": sum(1 for o in orgs_l if o["icp_status"] == "gekwalificeerd"),
            "orgs_kandidaat": sum(1 for o in orgs_l if o["icp_status"] == "kandidaat"),
            "personen_aangewezen": sum(1 for p in people if p.get("rol") == "aangewezen"),
            "stage_2": len(orgs_stage2(orgs_l, people)),
            "stage_3": telling.get("3", 0) + telling.get("3r", 0),
            "stage_4": telling.get("4", 0),
            "stage_5": telling.get("5", 0),
            "verstuurd": len(verstuurd),
            "geaccepteerd": sum(1 for p in people if (p.get("linkedin_geaccepteerd_op") or "").strip()),
            "gereageerd": len(reacties),
            "reacties_ongeduid": sum(1 for r in reacties if not r["geduid"]),
            "pijplijnwaarde": sum(getal(o.get("geschatte_jaarwaarde")) or 0
                                  for o in orgs_l if o["icp_status"] == "gekwalificeerd"),
        },
        "minimum_voor_conclusie": MIN_VOOR_CONCLUSIE,
        "assen": assen,
        "goedkeuren": goedkeuren,
        "reacties": reacties,
        "agents": agents,
    }
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        print("cockpit-export naar %s: %d te keuren, %d reacties, %d ongeduid"
              % (a.out, len(goedkeuren), len(reacties), res["stand"]["reacties_ongeduid"]))
        return
    out(res, a.table)


def cmd_omvang(a):
    """De omkeerknop op poort 0d.

    Zonder --drempel toont hij wie er op te_klein staat en waarom. Met een
    lagere --drempel (in de valuta van de markt) zie je wie er terugkomt als
    je de lat verlaagt, en met --herzien zet je die groep in een keer terug
    op gekwalificeerd.
    """
    drempel = a.drempel if a.drempel is not None else DREMPEL_JAARWAARDE
    aandeel = None                       # vervallen met het PSU-model
    orgs, _ = load_markt()

    # --toets: het oordeel over een organisatie opvragen in plaats van zelf rekenen
    if a.toets:
        doel = next((o for o in orgs if o["org_id"] == a.toets), None)
        if doel is None:
            die("niet gevonden: %s" % a.toets)
        oordeel, reden = omvang_oordeel(doel, drempel, aandeel)
        out({"org_id": doel["org_id"], "naam": doel["naam"], "oordeel": oordeel,
             "reden": reden, "lerenden_per_jaar": doel.get("lerenden_per_jaar", ""),
             "geschatte_jaarwaarde": doel.get("geschatte_jaarwaarde", ""),
             "segment_omvang": doel.get("segment_omvang", ""),
             "omvang_niveau": doel.get("omvang_niveau", ""),
             "actie": {"groot_genoeg": "laat icp_status staan",
                       "te_klein": "zet icp_status=te_klein, met omvang_citaat en omvang_url erbij",
                       "onbekend": "laat staan, omvang is geen afwijsgrond"}[oordeel]}, a.table)
        return

    klein = [o for o in orgs if o.get("icp_status") == "te_klein"]
    rijen = []
    for o in sorted(klein, key=lambda x: -(getal(x.get("lerenden_per_jaar")) or 0)):
        oordeel, reden = omvang_oordeel(o, drempel, aandeel)
        rijen.append({
            "org_id": o["org_id"],
            "naam": o["naam"],
            "geschatte_jaarwaarde": o.get("geschatte_jaarwaarde", ""),
            "omzet_indicatie": o.get("omzet_indicatie", ""),
            "lerenden_per_jaar": o.get("lerenden_per_jaar", ""),
            "aantal_opleidingen": o.get("aantal_opleidingen", ""),
            "omvang_niveau": o.get("omvang_niveau", ""),
            "komt_terug": "ja" if oordeel != "te_klein" else "nee",
            "reden": reden,
        })

    if not a.herzien:
        out({"drempel_jaarwaarde": drempel, "te_klein": len(klein),
             "komt_terug_bij_deze_drempel": sum(1 for r in rijen if r["komt_terug"] == "ja"),
             "orgs": rijen}, a.table)
        return

    if a.drempel is None:
        die("--herzien vraagt om een expliciete --drempel, "
            "anders herzie je op precies de lat waarop ze zijn afgevallen")
    terug = [r["org_id"] for r in rijen if r["komt_terug"] == "ja"]
    if not terug:
        out({"ok": True, "drempel_jaarwaarde": drempel, "herzien": []}, a.table)
        return
    entries = []
    with Lock():
        orgs = load(ORGS, ORG_COLS)      # alles laden, want save() schrijft alles terug
        for o in orgs:
            if o["org_id"] in terug:
                entries.append((o["org_id"], "icp_status", "te_klein", "gekwalificeerd", a.actor))
                o["icp_status"] = "gekwalificeerd"
                o["laatst_bijgewerkt"] = now_iso()
                o["bijgewerkt_door"] = a.actor
        save(ORGS, ORG_COLS, orgs)
    journal(entries)
    out({"ok": True, "drempel_jaarwaarde": drempel, "herzien": terug}, a.table)


def cmd_uitleg(a):
    """Wat elk veld betekent en welke waarden erin mogen. Zodat je nooit hoeft te raden."""
    if a.veld:
        treffers = [k for k in list(ORG_COLS) + PERSON_COLS if a.veld.lower() in k.lower()]
        if not treffers:
            die("geen veld gevonden dat lijkt op '%s'" % a.veld)
    else:
        treffers = None

    def blok(titel, kolommen):
        print("\n== %s ==" % titel)
        for k in kolommen:
            if treffers and k not in treffers:
                continue
            print("  %-28s %s" % (k, UITLEG.get(k, "(nog geen uitleg)")))
            if k in WAARDEN:
                for w, u in WAARDEN[k].items():
                    label = w if w else "(leeg)"
                    print("      %-20s %s" % (label, u))

    if not treffers:
        print("Elk veld in het master-document, met de toegestane waarden eronder.")
        print("Actieve markt: %s (valuta %s). Andere markt: --markt <code>. Overzicht: pipeline.py markt"
              % (MARKT, VALUTA))
        print("Zoeken kan ook: pipeline.py uitleg niveau")
    blok("ORGANISATIE (master/orgs.csv)", ORG_COLS)
    blok("PERSOON, wie is het (stap 2)", PERSON_COLS[:16])
    blok("PERSOON, het onderzoek (stap 3)", PERSON_COLS[16:29])
    blok("PERSOON, het bericht (stap 4)", PERSON_COLS[29:39])
    blok("PERSOON, verzending en uitkomst (stap 5 en daarna)", PERSON_COLS[39:-3])
    blok("SYSTEEM", PERSON_COLS[-3:])
    if not treffers:
        print("\n== DE STAPPEN (worden afgeleid, staan nergens opgeslagen) ==")
        for s, u in (
            ("stap 2", "organisatie gekwalificeerd, nog geen aangewezen persoon"),
            ("stap 3", "aangewezen persoon, haakje nog niet gevonden"),
            ("stap 3r", "haakje gevonden maar nooit een niveau gekregen, reparatiewachtrij"),
            ("stap 4", "haakje op niveau 2, 2b of 3, nog geen bericht geschreven"),
            ("stap 5", "bericht goedgekeurd, klaar om naar Lemlist te gaan"),
        ):
            print("  %-8s %s" % (s, u))


def cmd_uitkomst(a):
    """Leg vast hoe het afliep, met de reden in zijn eigen woorden."""
    if a.status not in ENUMS["uitkomst"]:
        die("uitkomst '%s' bestaat niet. Kies uit:\n%s" % (
            a.status, "\n".join("  %-18s %s" % (k, v) for k, v in WAARDEN["uitkomst"].items())))
    with Lock():
        people = load(PEOPLE, PERSON_COLS)
        doel = next((p for p in people if p["person_id"] == a.id), None)
        if doel is None:
            die("niet gevonden: %s" % a.id)
        entries = [(a.id, "uitkomst", doel["uitkomst"], a.status, a.actor)]
        doel["uitkomst"] = a.status
        if a.reden:
            entries.append((a.id, "uitkomst_reden", doel["uitkomst_reden"], a.reden, a.actor))
            doel["uitkomst_reden"] = a.reden
        doel["uitkomst_datum"] = a.datum or now_iso()
        if a.kanaal:
            doel[TOUCH_VELD[a.kanaal]] = doel[TOUCH_VELD[a.kanaal]] or (a.datum or now_iso())
        if not doel["reactie_gekregen_op"] and a.status != "geen_reactie":
            doel["reactie_gekregen_op"] = a.datum or now_iso()
        # een uitkomst sluit de outreach af, dus geen nieuwe berichten meer
        if a.status in ("geen_interesse", "later_terugkomen"):
            doel["bericht_status"] = "vervallen"
            doel["bericht_status_toelichting"] = "%s: %s" % (a.status, a.reden or "")
        _afgeleid(doel)
        doel["laatst_bijgewerkt"] = now_iso()
        doel["bijgewerkt_door"] = a.actor
        save(PEOPLE, PERSON_COLS, people)
    journal(entries)
    out({"ok": True, "id": a.id, "naam": doel["naam"], "uitkomst": doel["uitkomst"],
         "reden": doel["uitkomst_reden"], "datum": doel["uitkomst_datum"],
         "bericht_status": doel["bericht_status"]}, a.table)


def cmd_uitkomsten(a):
    """Alle vastgelegde uitkomsten teruglezen. 'Wie zei ook alweer nee, en waarom?'"""
    orgs_l, people = load_markt()
    orgs = {o["org_id"]: o for o in orgs_l}
    rows = [p for p in people if p["uitkomst"]]
    if a.status:
        rows = [p for p in rows if p["uitkomst"] == a.status]
    rows.sort(key=lambda p: p["uitkomst_datum"], reverse=True)
    out([{"datum": p["uitkomst_datum"], "naam": p["naam"],
          "org": orgs.get(p["org_id"], {}).get("naam", ""), "functie": p["functie"],
          "uitkomst": p["uitkomst"], "reden": p["uitkomst_reden"],
          "person_id": p["person_id"]} for p in rows], a.table)


def cmd_doctor(a):
    r = doctor(fix_safe=a.fix_safe, verbose=True)
    sys.exit(1 if r["fouten"] else 0)


def cmd_history(a):
    if not os.path.exists(JOURNAL):
        return out([], a.table)
    with open(JOURNAL, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["record_id"] == a.id]
    out(rows[-(a.limit or 50):], a.table)


def cmd_export(a):
    if a.wat != "lemlist":
        die("alleen 'lemlist' is nu ondersteund")
    orgs_l, people = load_markt()
    orgs = {o["org_id"]: o for o in orgs_l}
    # exact de stap-5-wachtrij, dus niemand die al benaderd is gaat opnieuw de deur uit
    rows = [p for p in people if stage_van(p, orgs) == "5"]
    kolommen = ["Voornaam Achternaam", "Organisatie", "Domein", "Email", "EmailStatus",
                "linkedInUrl", "linkedInConnectionRequest", "firstEmailSubject", "firstEmail",
                "reminder1", "person_id"]
    uit = []
    for p in rows:
        org = orgs.get(p["org_id"], {})
        uit.append({
            "Voornaam Achternaam": p["naam"],
            "Organisatie": org.get("naam", ""),
            "Domein": org.get("domein", ""),
            "Email": p["email"],
            "EmailStatus": p["email_status"],
            "linkedInUrl": p["linkedin_url"],
            "linkedInConnectionRequest": p["connectieverzoek"],
            "firstEmailSubject": p["opvolgmail_onderwerp"],
            # Lemlist slikt geen echte newlines, die moeten <br> worden
            "firstEmail": (p["opvolgmail"] or "").replace("\r\n", "\n").replace("\n", "<br>"),
            "reminder1": (p["reminder"] or "").replace("\r\n", "\n").replace("\n", "<br>"),
            "person_id": p["person_id"],
        })
    if a.out:
        with open(a.out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=kolommen)
            w.writeheader()
            w.writerows(uit)
        print("%d rijen naar %s" % (len(uit), a.out))
    else:
        out(uit, a.table)


def _profiel_md_skelet(code):
    regels = ["# Marktprofiel %s" % code, "",
              "<!-- Veertien slots. Elke kop moet inhoud hebben, anders weigert `queue`.",
              "     Elk feit met bron (URL + datum). Niet gevonden = zeg dat, verzin niets.",
              "     De harde waarden (valuta, prijs, titelrangorde) staan in profiel.json. -->", ""]
    for kop, uitleg in PROFIEL_SLOTS:
        regels += ["## %s" % kop, "<!-- %s -->" % uitleg, ""]
    return "\n".join(regels)


def cmd_markt(a):
    """Markten tonen, of een nieuwe aanmaken met alle veertien slots leeg."""
    if a.nieuw:
        code = a.nieuw.strip().lower()
        if not re.fullmatch(r"[a-z][a-z0-9-]{1,15}", code):
            die("marktcode '%s' mag niet: kleine letters, cijfers en streepjes, 2 tot 16 tekens" % code)
        pad = markt_pad(code)
        if os.path.exists(pad):
            die("markt %s bestaat al: %s" % (code, os.path.relpath(pad, REPO)))
        os.makedirs(pad)
        skelet = {
            "code": code, "naam": "", "valuta": "", "taal": "", "kanaal": [],
            "prijs_per_student_maand": None, "maanden_per_jaar": 12,
            "drempel_jaarwaarde": None, "segment_grenzen": [],
            "titel_rang": [], "klantnamen": [], "lemlist_campagne_id": "",
            "_uitleg": {
                "valuta": "een van %s" % "/".join(VALUTAS),
                "taal": "taalcode van de berichten, bijv. en-GB of en-US",
                "kanaal": "lijst uit %s" % "/".join(KANALEN),
                "prijs_per_student_maand": "prijs per student per maand in de valuta van de markt, nu 3",
                "maanden_per_jaar": "waarmee we de jaarwaarde rekenen, standaard 12",
                "drempel_jaarwaarde": "vloer voor poort 0d in de valuta van de markt, nu 10000, plat bedrag zonder wisselkoers",
                "segment_grenzen": "[[bovengrens lerenden, naam], ...] bijv. [[300,'micro'],[1000,'klein'],[3000,'midden']]; leeg = de standaard",
                "titel_rang": "[[regex op de functietitel, score 0-100], ...], eerste treffer wint",
                "klantnamen": "klanten die als bewijs genoemd mogen worden, lege lijst mag",
                "lemlist_campagne_id": "cam_... van de campagne voor deze markt, leeg tot die bestaat",
            },
        }
        with open(os.path.join(pad, "profiel.json"), "w", encoding="utf-8") as f:
            json.dump(skelet, f, ensure_ascii=False, indent=2)
            f.write("\n")
        with open(os.path.join(pad, "profiel.md"), "w", encoding="utf-8") as f:
            f.write(_profiel_md_skelet(code))
        with open(os.path.join(pad, "WERKVOORRAAD.md"), "w", encoding="utf-8") as f:
            f.write("# Werkvoorraad %s: welke bronnen zijn af, welke niet\n\n"
                    "Stand van zaken voor agent 1. Bijwerken na elke ronde.\n\n"
                    "Laatst bijgewerkt: %s\n\n## Open\n\n(nog niets)\n\n## Af\n\n(nog niets)\n"
                    % (code, now_iso()))
        with open(os.path.join(pad, "GATEN.md"), "w", encoding="utf-8") as f:
            f.write("# Gaten %s: gekwalificeerde organisaties zonder contact\n\n"
                    "| Datum | org_id | Organisatie | Categorie | Waarom het gat viel | Status |\n"
                    "|---|---|---|---|---|---|\n" % code)
        with open(os.path.join(pad, "UITGESLOTEN.md"), "w", encoding="utf-8") as f:
            f.write("# Uitgesloten %s: afvallers met reden en citaat\n\n"
                    "Agent 1 schrijft hier wie er afviel en waarom, zodat de volgende ronde ze niet opnieuw onderzoekt.\n\n"
                    "| Datum | Organisatie | Waarom | Citaat | URL |\n|---|---|---|---|---|\n" % code)
        with open(os.path.join(pad, "UITGESLOTEN.md"), "w", encoding="utf-8") as f:
            f.write("# Uitgesloten %s: afvallers met reden en citaat\n\n"
                    "Zodat de volgende ronde ze niet opnieuw onderzoekt.\n\n"
                    "| Datum | Organisatie | Reden | Citaat | URL |\n|---|---|---|---|---|\n" % code)
        journal([(code, "markt", "", "aangemaakt", a.actor)])
        fouten, _ = profiel_klachten(code)
        out({"ok": True, "markt": code, "pad": os.path.relpath(pad, REPO),
             "slots_leeg": len(fouten),
             "volgende_stap": "vul profiel.json en de 14 koppen in profiel.md, controleer met: "
                              "pipeline.py --markt %s doctor" % code}, a.table)
        return
    rijen = []
    orgs = load(ORGS, ORG_COLS)
    for code in markten():
        f, w = profiel_klachten(code)
        prof = profiel_laden(code) or {}
        rijen.append({"markt": code, "naam": prof.get("naam", ""), "valuta": prof.get("valuta", ""),
                      "taal": prof.get("taal", ""), "kanaal": ",".join(prof.get("kanaal") or []),
                      "compleet": "ja" if not f else "nee, %d slot(s)" % len(f),
                      "orgs": sum(1 for o in orgs if org_markt(o) == code),
                      "actief": "ja" if code == MARKT else ""})
    if not rijen:
        print("nog geen markten. Nieuw: pipeline.py markt --nieuw <code>")
        return
    out(rijen, a.table)


# ---------------------------------------------------------------- cli


def main():
    ap = argparse.ArgumentParser(prog="pipeline.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table", action="store_true", help="leesbare tabel in plaats van JSON")
    ap.add_argument("--markt", default=None,
                    help="de markt (nl, uk, ...). Anders SHIFT_MARKT, anders nl")

    # --table en --markt mogen ook achter het subcommando, want dat typ je nu eenmaal zo
    gedeeld = argparse.ArgumentParser(add_help=False)
    gedeeld.add_argument("--table", action="store_true",
                         help="leesbare tabel in plaats van JSON")
    gedeeld.add_argument("--markt", default=argparse.SUPPRESS,
                         help="de markt (nl, uk, ...). Anders SHIFT_MARKT, anders nl")

    _add = ap.add_subparsers(dest="cmd", required=True).add_parser

    class sub:
        @staticmethod
        def add_parser(naam, **kw):
            kw.setdefault("parents", [gedeeld])
            return _add(naam, **kw)

    p = sub.add_parser("queue", help="de werkvoorraad van een stage")
    p.add_argument("--stage", required=True, choices=["2", "3", "3r", "4", "5"])
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--org")
    p.add_argument("--fields")
    p.set_defaults(fn=cmd_queue)

    p = sub.add_parser("show", help="een org of persoon tonen")
    p.add_argument("id")
    p.add_argument("--full", action="store_true", help="ook lege velden")
    p.set_defaults(fn=cmd_show)

    p = sub.add_parser("dossier", help="het onderzoeksdossier van een persoon of organisatie")
    p.add_argument("id")
    p.add_argument("--sectie", help="alleen deze kop, bijv. Citaten. Scheelt tokens.")
    p.add_argument("--schrijf", metavar="PAD",
                   help="inhoud wegschrijven, '-' leest van stdin. Met --sectie alleen die kop.")
    p.add_argument("--sjabloon", action="store_true", help="lege kopstructuur om te vullen")
    p.add_argument("--actor", default="dante")
    p.add_argument("--forceer", action="store_true",
                   help="wegschrijven ondanks klachten. Doe dit niet zomaar.")
    p.set_defaults(fn=cmd_dossier)

    p = sub.add_parser("exists", help="dedup-poort: zit deze persoon al in de keten?")
    p.add_argument("--linkedin")
    p.add_argument("--naam")
    p.add_argument("--org")
    p.set_defaults(fn=cmd_exists)

    p = sub.add_parser("orgs", help="organisaties filteren")
    p.add_argument("--icp-status", dest="icp_status")
    p.add_argument("--zonder-contact", action="store_true")
    p.add_argument("--met-mensen", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    p.set_defaults(fn=cmd_orgs)

    p = sub.add_parser("add-org")
    p.add_argument("--naam", required=True)
    p.add_argument("--set", action="append")
    p.add_argument("--actor", default="lead-sourcing-nl")
    p.add_argument("--forceer-dubbel", dest="forceer_dubbel", action="store_true",
                   help="voeg toch toe ook al lijkt de naam op een bestaande org")
    p.set_defaults(fn=cmd_add_org)

    p = sub.add_parser("add-person")
    p.add_argument("--org-id", dest="org_id", required=True)
    p.add_argument("--naam", required=True)
    p.add_argument("--linkedin")
    p.add_argument("--set", action="append")
    p.add_argument("--actor", default="contact-sourcing-nl")
    p.set_defaults(fn=cmd_add_person)

    p = sub.add_parser("set", help="velden bijwerken op een bestaand record")
    p.add_argument("id")
    p.add_argument("--set", action="append", required=True)
    p.add_argument("--actor", required=True)
    p.set_defaults(fn=cmd_set)

    p = sub.add_parser("promote", help="tweede kandidaat wordt de aangewezen persoon")
    p.add_argument("id")
    p.add_argument("--actor", default="dante")
    p.set_defaults(fn=cmd_promote)

    p = sub.add_parser("touch", help="verzenddatum vastleggen")
    p.add_argument("id")
    p.add_argument("--kanaal", required=True, choices=["linkedin", "email", "call"])
    p.add_argument("--datum")
    p.add_argument("--actor", default="dante")
    p.set_defaults(fn=cmd_touch)

    p = sub.add_parser("uitleg", help="welke velden en welke waarden bestaan er")
    p.add_argument("veld", nargs="?", help="zoek op een deel van een veldnaam")
    p.set_defaults(fn=cmd_uitleg)

    p = sub.add_parser("uitkomst", help="leg vast hoe het afliep, met de reden")
    p.add_argument("id")
    p.add_argument("--status", required=True,
                   help=" | ".join(ENUMS["uitkomst"][1:]))
    p.add_argument("--reden", help="in zijn eigen woorden waarom")
    p.add_argument("--kanaal", choices=["linkedin", "email", "call"])
    p.add_argument("--datum")
    p.add_argument("--actor", default="dante")
    p.set_defaults(fn=cmd_uitkomst)

    p = sub.add_parser("uitkomsten", help="alle vastgelegde uitkomsten teruglezen")
    p.add_argument("--status")
    p.set_defaults(fn=cmd_uitkomsten)

    p = sub.add_parser("omvang", help="wie staat er op te_klein, en wie komt terug bij een lagere drempel")
    p.add_argument("--drempel", type=int,
                   help="minimum jaarwaarde in de valuta van de markt, standaard %d" % DREMPEL_JAARWAARDE)
    p.add_argument("--toets", metavar="ORG_ID",
                   help="vraag het oordeel over een organisatie op, in plaats van zelf te rekenen")
    p.add_argument("--herzien", action="store_true",
                   help="zet iedereen boven die drempel terug op gekwalificeerd")
    p.add_argument("--actor", default="dante")
    p.set_defaults(fn=cmd_omvang)

    p = sub.add_parser("sync-lemlist",
                       help="lees een export van de Lemlist-connector en schrijf de feiten terug")
    p.add_argument("--invoer", required=True, metavar="PAD",
                   help="JSON met de leads uit search_campaign_leads(include=['activities'])")
    p.add_argument("--droog", action="store_true", help="laat zien wat er zou veranderen, schrijf niets")
    p.set_defaults(fn=cmd_sync_lemlist)

    p = sub.add_parser("peiling",
                       help="is het de moeite om alle leads op te halen? goedkope poort voor sync-lemlist")
    p.add_argument("--verstuurd", type=int, required=True, help="messageMetrics.sent, opgeteld over de campagnes")
    p.add_argument("--geaccepteerd", type=int, required=True, help="channelMetrics.linkedinInvitationAccepted")
    p.add_argument("--gereageerd", type=int, required=True, help="messageMetrics.replied")
    p.add_argument("--leg-vast", dest="leg_vast", action="store_true",
                   help="sla deze telling op als nieuwe ijkwaarde, doe dit NA een geslaagde sync")
    p.set_defaults(fn=cmd_peiling)

    p = sub.add_parser("cockpit", help="alles wat de cockpit-pagina toont, als JSON")
    p.add_argument("--out", metavar="PAD", help="wegschrijven in plaats van afdrukken")
    p.set_defaults(fn=cmd_cockpit)

    p = sub.add_parser("rapport", help="werkt het, en voor wie: conversie per segment")
    p.add_argument("--as", dest="as_", choices=sorted(RAPPORT_ASSEN),
                   help="een enkele as, anders alle vier")
    p.set_defaults(fn=cmd_rapport)

    p = sub.add_parser("status", help="stand van de trechter")
    p.add_argument("--doel", type=int)
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("doctor", help="validatie")
    p.add_argument("--fix-safe", dest="fix_safe", action="store_true")
    p.set_defaults(fn=cmd_doctor)

    p = sub.add_parser("history", help="journaal van een record")
    p.add_argument("id")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(fn=cmd_history)

    p = sub.add_parser("export")
    p.add_argument("wat", choices=["lemlist"])
    p.add_argument("--out")
    p.set_defaults(fn=cmd_export)

    p = sub.add_parser("markt", help="markten tonen, of een nieuwe aanmaken (--nieuw <code>)")
    p.add_argument("--nieuw", metavar="CODE", help="maak een lege markt aan met alle 14 slots leeg")
    p.add_argument("--actor", default="dante")
    p.set_defaults(fn=cmd_markt)

    a = ap.parse_args()
    activeer_markt((getattr(a, "markt", None) or os.environ.get("SHIFT_MARKT") or "nl").strip().lower())
    a.fn(a)


if __name__ == "__main__":
    main()
