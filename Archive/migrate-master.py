#!/usr/bin/env python3
"""
migrate-master.py - voegt de losse pijplijnbestanden samen tot het master-document.

Bronnen (worden alleen gelezen, nooit aangeraakt):
  targetlijst-nl.csv           organisaties        (agent 1)
  contacten-linkedin-nl.csv    personen            (agent 2)
  haakjes-nl.csv               onderzoek           (agent 3)
  berichten-nl.csv             berichten           (agent 4)
  contacten-nl.csv             legacy, levert e-mailadressen
  contacten-onderwijs-nl.csv   legacy, levert aantekeningen

Doel: master/orgs.csv + master/people.csv

Draaien:
  migrate-master.py --dry-run     schrijft niets, levert een HTML-rapport
  migrate-master.py --run         schrijft de master (idempotent, mag opnieuw)
  migrate-master.py --verify      vergelijkt de master terug tegen de bronnen

Stdlib only, python 3.9+.
"""

import argparse
import csv
import html
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pipeline import (  # noqa: E402
    ORG_COLS, PERSON_COLS, ORGS, PEOPLE, MASTER, REPO,
    slug, norm, li_slug, org_id_for, person_id_for, titel_rang, split_naam,
    now_iso, save, load, doctor,
)

T = os.path.join(REPO, "projects", "targetlijst-nl")
csv.field_size_limit(10 * 1024 * 1024)

RAPPORT = os.path.join(T, "migratie-rapport.html")

# ---------------------------------------------------------------- mapping

# Laag -> rol_type. Volgorde telt, eerste hit wint.
LAAG_MAP = [
    ("GEEN CONTACT", "afgevallen"),
    ("NIET GEVONDEN", "afgevallen"),
    ("EXAMENCOMMISSIE", "afgevallen"),
    ("EB / TE HOOG", "afgevallen"),
    ("DUBBEL", "afgevallen"),
    ("docent", "afgevallen"),
    ("IN CLOSE", "al_in_close"),
    ("TWEEDE KANDIDAAT", "tweede_kandidaat"),
    ("AANGEWEZEN", "aangewezen"),
    ("TITEL NIET GEVERIFIEERD", "aangewezen"),
]

# Handmatige beslissingen van Dante, na het nalopen van de tiebreaks op 14-08-2026.
# Deze winnen altijd van de automatische tiebreak, en overleven een herhaalde migratie.
# Sleutel = de naam van de organisatie, waarde = wie de aangewezen persoon wordt.
DANTE_KIEST = {
    "NewCare College": ("Maaike Nijboer",
                        "Dante wil de onderwijstak, niet de commercieel directeur"),
    "SPV B.V.": ("Armand van Bercheycke",
                 "Dante wil de moeder (SeSa Groep), niet de dochter"),
    "TMO Fashion Business School": ("Marit van Daal",
                                    "twee identieke titels, Dante kiest wie het verst is in "
                                    "het onderzoek (23 gevulde velden, bericht al goedgekeurd)"),
}

# Personen die dubbel in de bronbestanden staan. Sleutel = de rij die verdwijnt als
# zelfstandige kandidaat, waarde = de naam van het record dat blijft gelden.
DANTE_DUBBEL = {
    ("Thim van der Laan", "Thim van der Laan"): "Thim van der Laan (jr.)",
}

# Organisaties die Dante met rust wil laten. De hele lead gaat op slot, dus ook de
# tweede kandidaten verdwijnen uit elke wachtrij.
DANTE_ORG_OP_SLOT = {
    "Thim van der Laan": "Thim van der Laan (jr.) heeft per mail nee gezegd 13-08-2026. "
                         "Dante wil de hele lead met rust laten, dus ook geen tweede "
                         "kandidaat benaderen.",
}

# Uitkomsten die Dante zelf heeft doorgegeven en die nergens in de bronbestanden stonden.
DANTE_UITKOMSTEN = [
    {
        "org": "Thim van der Laan", "naam": "Thim van der Laan (jr.)",
        "uitkomst": "geen_interesse", "datum": "2026-08-13", "kanaal": "email",
        "reden": "Reageerde per mail op de opvolgmail: het NVAO-citaat ging over de "
                 "studeerbaarheid voor de student, terwijl Eduface de organisatie in "
                 "efficientie ondersteunt. In zijn woorden: \"Dit is de studeerbaarheid voor "
                 "de student. De oplossing die jij aanbiedt probeert meer de organisatie in "
                 "efficientie e.d. te ondersteunen. Dat zijn twee verschillende dingen.\" "
                 "Dit is de aanleiding geweest voor de drager-toets in de brontoets.",
    },
]

# Bij een dubbele rij wint de sterkste rol, niet de laatste.
ROL_KRACHT = {"": 0, "achtergrond": 1, "afgevallen": 2, "al_in_close": 3, "doorverwijzing": 4,
              "tweede_kandidaat": 5, "aangewezen": 6}

BRON_TYPE_MAP = {
    "": "", "organisatie": "organisatie", "webresearch": "webresearch",
    "teampagina": "teampagina", "eigen site": "eigen site", "interview": "interview",
    "publicatie": "publicatie", "vakblad": "vakblad",
}


def status_naar_enum(s):
    """De 30 prosastatussen worden 6 waarden. De originele tekst blijft bewaard."""
    n = norm(s)
    if not n:
        return "", ""
    if n.startswith("gedropt") or n.startswith("vervallen"):
        return "vervallen", s
    if "gepauzeerd" in n:
        return "gepauzeerd", s
    if n.startswith("verstuurd") or "verstuurd, bevestigd" in n:
        return "verstuurd", s
    if "in lemlist-campagne" in n:
        return "goedgekeurd", s
    if n.startswith("goedgekeurd"):
        return "goedgekeurd", s
    if n.startswith("klaar") or n.startswith("groen licht"):
        return "goedgekeurd", s
    if n.startswith("concept") or n.startswith("herzien") or n.startswith("twijfelgeval") \
            or n.startswith("voorgelegd"):
        return "concept", s
    return "concept", s


def gepauzeerd_tot(s):
    m = re.search(r"(20\d\d-\d\d-\d\d)", s or "")
    return m.group(1) if m and "gepauzeerd" in norm(s) else ""


def eerste_datum(s):
    m = re.search(r"(20\d\d-\d\d-\d\d)", s or "")
    return m.group(1) if m else ""


PSEUDO_NAMEN = {"geen contact", "niet gevonden", "geen", "nvt", "n.v.t.", "-", "?", "onbekend",
                "geen contact opgeleverd", "dubbel", "examencommissie"}


def is_persoonsnaam(naam):
    """'GEEN CONTACT' in de naamkolom is geen persoon maar een aantekening."""
    n = norm(naam)
    if not n or n in PSEUDO_NAMEN:
        return False
    if naam.strip().isupper() and len(naam.split()) <= 3:
        return False
    return True


def splits_bewijs(tekst):
    """'citaat (bron: https://...)' -> (citaat, url)"""
    t = (tekst or "").strip()
    urls = re.findall(r"https?://[^\s,;)\]\"']+", t)
    url = urls[0].rstrip(".,;)") if urls else ""
    citaat = t
    if url:
        citaat = t.replace(url, "").strip()
        citaat = re.sub(r"[\s(\[]*bron\s*:?\s*[)\]]*\s*$", "", citaat, flags=re.I).strip()
        citaat = citaat.strip(" ()[]-,;")
    return citaat, url


def beste_linkedin(a, b):
    """Zelfde profiel, andere schrijfwijze. Kies de schoonste URL."""
    def score(u):
        u = (u or "").strip()
        if not u or "/in/" not in u:
            return -1
        s = 0
        if u.startswith("https://www.linkedin.com/in/"):
            s += 4
        if "%" not in u:
            s += 3                       # geen percent-encoding
        if " " not in u and "(" not in u:
            s += 2                       # geen aantekening in het veld
        if u.rstrip("/").count("/") == 4:
            s += 1
        return s
    return a if score(a) >= score(b) else b


def domein_uit(url):
    m = re.search(r"https?://(?:www\.)?([^/\s]+)", url or "")
    return m.group(1).lower() if m else ""


# ---------------------------------------------------------------- laden


def lees(naam):
    pad = os.path.join(T, naam)
    if not os.path.exists(pad):
        return []
    with open(pad, newline="", encoding="utf-8") as f:
        return [dict(r) for r in csv.DictReader(f)]


class Log:
    def __init__(self):
        self.secties = defaultdict(list)
        self.tellers = {}

    def add(self, sectie, **kw):
        self.secties[sectie].append(kw)

    def tel(self, k, v):
        self.tellers[k] = v


# ---------------------------------------------------------------- orgs


def bouw_orgs(log):
    orgs = {}          # org_id -> rij
    alias_index = {}   # genormaliseerde naam -> org_id

    def registreer_alias(naam, oid):
        n = norm(naam)
        if n and n not in alias_index:
            alias_index[n] = oid

    for r in lees("targetlijst-nl.csv"):
        naam = (r.get("Aanbieder") or "").strip()
        if not naam:
            continue
        # "Salta Group (moeder)" -> basisnaam + alias
        basis = re.sub(r"\s*\([^)]*\)\s*$", "", naam).strip() or naam
        oid = org_id_for(basis)
        citaat, url = splits_bewijs(r.get("Bewijs (citaat + bron)"))
        beoordeelt = (r.get("Beoordeelt zelf werk van lerenden") or "").strip() or "Onbekend"
        beoordeelt = {"Ja": "Ja", "Nee": "Nee"}.get(beoordeelt, "Onbekend")
        part = (r.get("Particulier") or "").strip() or "Onbekend"
        part = {"Ja": "Ja", "Nee": "Nee"}.get(part, "Onbekend")

        if oid in orgs:
            o = orgs[oid]
            if naam != basis and naam not in o["naam_aliassen"].split("|"):
                o["naam_aliassen"] = "|".join(filter(None, [o["naam_aliassen"], naam]))
            log.add("org_samengevoegd", org_id=oid, naam=naam, met=o["naam"])
        else:
            o = {c: "" for c in ORG_COLS}
            o.update({
                "org_id": oid, "naam": basis,
                "naam_aliassen": naam if naam != basis else "",
                "moeder_org_id": "", "categorie": (r.get("Categorie") or "").strip(),
                "domein": domein_uit(url),
                "beoordeelt_zelf": beoordeelt, "bewijs_citaat": citaat, "bewijs_url": url,
                "particulier": part,
                "bron_particulier": (r.get("Bron particulier") or "").strip(),
                "icp_status": "gekwalificeerd" if beoordeelt == "Ja" else "kandidaat",
                "laatst_bijgewerkt": now_iso(), "bijgewerkt_door": "migratie",
            })
            orgs[oid] = o
        registreer_alias(naam, oid)
        registreer_alias(basis, oid)
        # moeder onthouden, pas koppelen als alle orgs bestaan
        m = (r.get("Moeder / groep") or "").strip()
        if m and norm(m) != norm(basis):
            o["notities"] = ("moeder-tekst: " + m) if not o["notities"] else o["notities"]
            o["_moeder_tekst"] = m

    # moeders koppelen (lijst pakken, want orgs kan er onderweg bij krijgen)
    for o in list(orgs.values()):
        m = o.pop("_moeder_tekst", "")
        if not m:
            continue
        mb = re.sub(r"\s*\([^)]*\)\s*$", "", m).strip()
        moid = alias_index.get(norm(mb)) or alias_index.get(norm(m))
        if moid and moid != o["org_id"]:
            o["moeder_org_id"] = moid
        elif mb:
            # moeder staat niet zelf op de targetlijst: aanmaken als kandidaat
            moid = org_id_for(mb)
            if moid not in orgs:
                n = {c: "" for c in ORG_COLS}
                n.update({"org_id": moid, "naam": mb, "icp_status": "kandidaat",
                          "beoordeelt_zelf": "Onbekend", "particulier": "Onbekend",
                          "notities": "afgeleid uit de kolom Moeder / groep, niet zelf gekwalificeerd",
                          "laatst_bijgewerkt": now_iso(), "bijgewerkt_door": "migratie"})
                orgs[moid] = n
                alias_index[norm(mb)] = moid
                log.add("org_uit_moederkolom", org_id=moid, naam=mb)
            o["moeder_org_id"] = moid
    return orgs, alias_index


def vind_org(naam, orgs, alias_index, log, herkomst):
    """Zoek een org op naam. Maakt er een aan als hij niet bestaat."""
    n = norm(naam)
    if not n:
        return ""
    if n in alias_index:
        return alias_index[n]
    basis = norm(re.sub(r"\s*\([^)]*\)\s*$", "", naam).strip())
    if basis in alias_index:
        alias_index[n] = alias_index[basis]
        return alias_index[basis]
    # deelstring, langste match wint (Salta Group (dekt 8 merken) -> Salta Group)
    kandidaten = [(len(k), v) for k, v in alias_index.items()
                  if len(k) > 4 and (k in n or n in k)]
    if kandidaten:
        oid = max(kandidaten)[1]
        alias_index[n] = oid
        log.add("org_deelstring", gezocht=naam, gekoppeld_aan=orgs[oid]["naam"], bron=herkomst)
        return oid
    oid = org_id_for(naam)
    o = {c: "" for c in ORG_COLS}
    o.update({"org_id": oid, "naam": naam.strip(), "icp_status": "kandidaat",
              "beoordeelt_zelf": "Onbekend", "particulier": "Onbekend",
              "notities": "afgeleid uit %s, niet gekwalificeerd door agent 1" % herkomst,
              "laatst_bijgewerkt": now_iso(), "bijgewerkt_door": "migratie"})
    orgs[oid] = o
    alias_index[n] = oid
    log.add("org_nieuw_uit_contact", org_id=oid, naam=naam, bron=herkomst)
    return oid


# ---------------------------------------------------------------- personen


class PersoonIndex:
    """Matchvolgorde: LinkedIn-slug -> (org, naam) -> naam binnen dezelfde moederboom."""

    def __init__(self, orgs):
        self.rows = {}          # person_id -> rij
        self.by_li = {}
        self.by_orgnaam = {}
        self.by_naam = defaultdict(list)
        self.orgs = orgs

    def _boom(self, oid):
        o = self.orgs.get(oid, {})
        return o.get("moeder_org_id") or oid

    def zoek(self, org_id, naam, linkedin):
        s = li_slug(linkedin)
        if s and s in self.by_li:
            return self.by_li[s], "linkedin"
        k = (org_id, norm(naam))
        if k in self.by_orgnaam:
            return self.by_orgnaam[k], "org+naam"
        # Alleen bij een echte voor+achternaam. Twee mensen met dezelfde volledige naam
        # binnen een groep is vrijwel uitgesloten, bij een enkel woord niet.
        if len(norm(naam).split()) >= 2:
            for pid in self.by_naam.get(norm(naam), []):
                if self._boom(self.rows[pid]["org_id"]) == self._boom(org_id):
                    return pid, "naam-in-moederboom"
        return None, ""

    def voeg_toe(self, rij):
        pid = rij["person_id"]
        self.rows[pid] = rij
        s = li_slug(rij["linkedin_url"])
        if s:
            self.by_li[s] = pid
        self.by_orgnaam[(rij["org_id"], norm(rij["naam"]))] = pid
        self.by_naam[norm(rij["naam"])].append(pid)

    def herindexeer(self, pid):
        rij = self.rows[pid]
        s = li_slug(rij["linkedin_url"])
        if s:
            self.by_li[s] = pid
        self.by_orgnaam[(rij["org_id"], norm(rij["naam"]))] = pid


def vul(rij, veld, waarde, log, pid, bron, overschrijf=False):
    """Vul een veld. Standaard alleen als het leeg is; conflicten worden gelogd."""
    w = (waarde or "").strip()
    if not w:
        return
    oud = (rij.get(veld) or "").strip()
    if veld == "linkedin_url" and oud and oud != w:
        rij[veld] = beste_linkedin(oud, w)
        log.add("conflict", person_id=pid, veld=veld, behouden=rij[veld][:80],
                weggezet=(w if rij[veld] == oud else oud)[:80], bron=bron)
        return
    if not oud:
        rij[veld] = w
    elif oud != w:
        if overschrijf:
            rij[veld] = w
            rij["notities"] = "; ".join(filter(None, [rij.get("notities"),
                                                      "%s (was): %s" % (veld, oud[:200])]))
            log.add("conflict", person_id=pid, veld=veld, behouden=w[:80], weggezet=oud[:80],
                    bron=bron)
        else:
            log.add("conflict", person_id=pid, veld=veld, behouden=oud[:80], weggezet=w[:80],
                    bron=bron)


def migreer(log):
    orgs, alias_index = bouw_orgs(log)
    log.tel("orgs_uit_targetlijst", len(orgs))
    idx = PersoonIndex(orgs)

    def haal_of_maak(org_naam, naam, linkedin, bron):
        oid = vind_org(org_naam, orgs, alias_index, log, bron)
        pid, hoe = idx.zoek(oid, naam, linkedin)
        if pid:
            if hoe != "linkedin":
                log.add("gematcht", person_id=pid, naam=naam, org=org_naam, methode=hoe, bron=bron)
            return idx.rows[pid], False
        pid = person_id_for(naam, linkedin, orgs[oid]["naam"])
        if pid in idx.rows:                       # zelfde id, andere org: hou het bij elkaar
            return idx.rows[pid], False
        rij = {c: "" for c in PERSON_COLS}
        rij.update({"person_id": pid, "org_id": oid, "naam": (naam or "").strip(),
                    "linkedin_url": (linkedin or "").strip(),
                    "laatst_bijgewerkt": now_iso(), "bijgewerkt_door": "migratie"})
        rij["voornaam"], rij["achternaam"] = split_naam(rij["naam"])
        idx.voeg_toe(rij)
        return rij, True

    # ---- contacten-linkedin-nl.csv (agent 2) --------------------------------
    bron_rijen = {}
    n_in = 0
    for r in lees("contacten-linkedin-nl.csv"):
        naam = (r.get("Naam") or "").strip()
        if not is_persoonsnaam(naam):
            # Rij zonder naam is geen persoon maar een aantekening op de organisatie:
            # "GEEN CONTACT: site noemt geen namen". Die hoort op de org, anders doet
            # agent 2 dezelfde zoektocht nog een keer.
            org_naam = (r.get("Organisatie") or "").strip()
            waarom = (r.get("Waarom deze persoon") or "").strip()
            if not org_naam:
                continue
            oid = vind_org(org_naam, orgs, alias_index, log, "contacten (rij zonder naam)")
            o = orgs[oid]
            laag_of_naam = (r.get("Laag") or naam or "onbekend").strip()
            tekst = "%s: %s" % (laag_of_naam, waarom) if waarom else laag_of_naam
            if tekst:
                o["contact_zoekpoging"] = "; ".join(
                    filter(None, [o.get("contact_zoekpoging"), tekst]))[:2000]
            if "GEBLOKKEERD" in waarom.upper() or "geen koude outreach" in norm(waarom):
                o["icp_status"] = "geblokkeerd"
                o["blokkade_reden"] = waarom[:300]
                log.add("org_geblokkeerd", naam=org_naam, reden=waarom[:160])
            log.add("zoekpoging_zonder_naam", org=org_naam,
                    laag=(r.get("Laag") or "").strip(), waarom=waarom[:160])
            continue
        n_in += 1
        rij, nieuw = haal_of_maak(r.get("Organisatie"), naam, r.get("LinkedIn"), "contacten")
        pid = rij["person_id"]
        laag = (r.get("Laag") or "").strip()
        waarom = (r.get("Waarom deze persoon") or "").strip()

        rol = None
        for sleutel, waarde in LAAG_MAP:
            if laag == sleutel:
                rol = waarde
                break
        if rol is None:
            if laag == "kern" and waarom:
                rol = "aangewezen"                       # de 12
                log.add("kern_met_onderbouwing", person_id=pid, naam=naam,
                        org=r.get("Organisatie"), waarom=waarom[:120])
            else:
                rol = "achtergrond"
        if waarom.upper().startswith("DOORVERWIJZING"):
            rol = "doorverwijzing"
        if rol == "afgevallen":
            vul(rij, "waarom_afgevallen", laag, log, pid, "contacten")

        # Staat dezelfde persoon twee keer in het bestand, dan wint de sterkste rol.
        # Niet de laatste rij, want die volgorde is willekeurig.
        if ROL_KRACHT[rol] > ROL_KRACHT.get(rij["rol"], -1):
            if rij["rol"] and rij["rol"] != rol:
                log.add("rol_sterkste_wint", person_id=pid, naam=naam, org=r.get("Organisatie"),
                        gekozen=rol, ook_gezien=rij["rol"])
            rij["rol"] = rol
        elif rij["rol"] != rol:
            log.add("rol_sterkste_wint", person_id=pid, naam=naam, org=r.get("Organisatie"),
                    gekozen=rij["rol"], ook_gezien=rol)
        vul(rij, "functie", r.get("Functie"), log, pid, "contacten")
        vul(rij, "functie_bron", r.get("Bron"), log, pid, "contacten")
        vul(rij, "in_functie_sinds", r.get("In functie sinds"), log, pid, "contacten")
        vul(rij, "waarom_deze_persoon", waarom, log, pid, "contacten")
        vul(rij, "haakje", r.get("Haakje"), log, pid, "contacten")
        if laag == "TITEL NIET GEVERIFIEERD":
            rij["functie_geverifieerd_op"] = ""
            rij["notities"] = "; ".join(filter(None, [rij["notities"], "titel niet geverifieerd"]))
        rij["notities"] = "; ".join(filter(None, [rij["notities"], "Laag(oud)=%s" % laag]))
        bron_rijen.setdefault("contacten", []).append(pid)
    log.tel("contacten_ingelezen", n_in)

    # ---- haakjes-nl.csv (agent 3) ------------------------------------------
    n_in = 0
    for r in lees("haakjes-nl.csv"):
        naam = (r.get("Naam") or "").strip()
        if not naam:
            continue
        n_in += 1
        rij, nieuw = haal_of_maak(r.get("Organisatie"), naam, r.get("LinkedIn"), "haakjes")
        pid = rij["person_id"]
        if nieuw:
            log.add("orphan", person_id=pid, naam=naam, org=r.get("Organisatie"), bron="haakjes")
            rij["rol"] = "aangewezen"
        vul(rij, "linkedin_url", r.get("LinkedIn"), log, pid, "haakjes")
        idx.herindexeer(pid)
        vul(rij, "functie", r.get("Functie"), log, pid, "haakjes")
        vul(rij, "opvallend", r.get("Opvallend"), log, pid, "haakjes")
        vul(rij, "haakje", r.get("Haakje"), log, pid, "haakjes", overschrijf=True)
        vul(rij, "haakje_bron_url", r.get("Bron-URL"), log, pid, "haakjes")
        vul(rij, "haakje_bron_type", BRON_TYPE_MAP.get((r.get("Bron-type") or "").strip(),
                                                       (r.get("Bron-type") or "").strip()),
            log, pid, "haakjes")
        vul(rij, "haakje_gevonden_op", eerste_datum(r.get("Datum haakje")), log, pid, "haakjes")
        ho = norm(r.get("Haakje over"))
        if ho.startswith("persoon + organisatie") or "gemengd" in ho or "/" in ho:
            ho = "persoon + organisatie"
        elif ho.startswith("organisatie"):
            ho = "organisatie"
        elif ho.startswith("persoon"):
            ho = "persoon"
        else:
            ho = ""
        vul(rij, "haakje_gaat_over", ho, log, pid, "haakjes")
        vul(rij, "haakje_trap", (r.get("Trap") or "").strip(), log, pid, "haakjes")
        vul(rij, "toetsprogramma", r.get("Toetsprogramma"), log, pid, "haakjes")
        vul(rij, "schrijfwerk", r.get("Schrijfwerk"), log, pid, "haakjes")
        vul(rij, "type_instelling", r.get("Type instelling"), log, pid, "haakjes")
        vul(rij, "alternatief_hoger_in_boom",
            r.get("Alternatief (hoger in de boom, haakje nog te zoeken)"), log, pid, "haakjes")

        gevonden = (r.get("Gevonden") or "").strip()
        niveau = (r.get("Niveau") or "").strip()
        if gevonden.startswith("Ja"):
            rij["onderzoek_status"] = "gevonden"
            rij["haakje_niveau"] = niveau if niveau in ("1", "2", "2b", "3") else "onbeoordeeld"
            if not niveau:
                log.add("niveau_onbeoordeeld", person_id=pid, naam=naam,
                        org=r.get("Organisatie"), haakje=(r.get("Haakje") or "")[:100])
        elif gevonden.startswith("Twijfel"):
            rij["onderzoek_status"] = "geparkeerd"
            rij["haakje_niveau"] = niveau if niveau in ("1", "2", "2b", "3") else "onbeoordeeld"
        elif gevonden.startswith("Nee"):
            rij["onderzoek_status"] = "geen_haakje"
            rij["haakje_niveau"] = niveau if niveau in ("1", "2", "2b", "3") else "onbeoordeeld"
            if len(gevonden) > 3:
                rij["notities"] = "; ".join(filter(None, [rij["notities"], gevonden]))
        else:
            rij["onderzoek_status"] = rij["onderzoek_status"] or "open"
            rij["haakje_niveau"] = niveau if niveau in ("1", "2", "2b", "3") else "onbeoordeeld"
        bron_rijen.setdefault("haakjes", []).append(pid)
    log.tel("haakjes_ingelezen", n_in)

    # ---- berichten-nl.csv (agent 4) ----------------------------------------
    n_in = 0
    for r in lees("berichten-nl.csv"):
        naam = (r.get("Naam") or "").strip()
        if not naam:
            continue
        n_in += 1
        rij, nieuw = haal_of_maak(r.get("Organisatie"), naam, r.get("LinkedIn"), "berichten")
        pid = rij["person_id"]
        if nieuw:
            log.add("orphan", person_id=pid, naam=naam, org=r.get("Organisatie"), bron="berichten")
            rij["rol"] = "aangewezen"
            rij["onderzoek_status"] = "gevonden"
        vul(rij, "linkedin_url", r.get("LinkedIn"), log, pid, "berichten")
        idx.herindexeer(pid)
        vul(rij, "functie", r.get("Functie"), log, pid, "berichten")
        vul(rij, "haakje", r.get("Haakje"), log, pid, "berichten")
        vul(rij, "haakje_bron_url", r.get("Bron-URL"), log, pid, "berichten")
        vul(rij, "connectieverzoek", r.get("Connectieverzoek"), log, pid, "berichten")
        vul(rij, "opvolgmail_onderwerp", r.get("Opvolgmail onderwerp"), log, pid, "berichten")
        vul(rij, "opvolgmail", r.get("Opvolgbericht"), log, pid, "berichten")
        vul(rij, "twijfels", r.get("Twijfels"), log, pid, "berichten")
        niveau = (r.get("Niveau") or "").strip()
        if niveau in ("1", "2", "2b", "3") and rij["haakje_niveau"] in ("", "onbeoordeeld"):
            rij["haakje_niveau"] = niveau
        if not rij["haakje_niveau"]:
            rij["haakje_niveau"] = "onbeoordeeld"
        if not rij["onderzoek_status"]:
            rij["onderzoek_status"] = "gevonden" if rij["haakje"] else "open"

        st, ruw = status_naar_enum(r.get("Status"))
        rij["bericht_status"] = st
        rij["bericht_status_toelichting"] = ruw
        p = gepauzeerd_tot(r.get("Status"))
        if p:
            rij["gepauzeerd_tot"] = p
        lem = (r.get("Lemlist") or "").strip()
        if lem == "Ja":
            rij["lemlist_status"] = "geimporteerd"
        elif lem.startswith("Nee"):
            rij["lemlist_status"] = "nvt"
            rij["notities"] = "; ".join(filter(None, [rij["notities"], "Lemlist: " + lem]))
        for kol, veld in (("LinkedIn connectieverzoek verzonden", "verzonden_linkedin"),
                          ("Email verstuurd", "verzonden_email"),
                          ("Cold call gedaan", "cold_call")):
            d = eerste_datum(r.get(kol))
            if d:
                rij[veld] = d
        if any(rij[v] for v in ("verzonden_linkedin", "verzonden_email", "cold_call")):
            if rij["bericht_status"] not in ("gepauzeerd", "vervallen"):
                rij["bericht_status"] = "verstuurd"
        bron_rijen.setdefault("berichten", []).append(pid)
    log.tel("berichten_ingelezen", n_in)

    # ---- legacy: e-mailadressen en aantekeningen redden ---------------------
    gered_mail = 0
    for r in lees("contacten-nl.csv"):
        naam = (r.get("Naam") or "").strip()
        if not naam:
            continue
        oid = vind_org(r.get("Organisatie"), orgs, alias_index, log, "contacten-nl")
        pid, _ = idx.zoek(oid, naam, r.get("LinkedIn"))
        if not pid:
            continue
        rij = idx.rows[pid]
        mail = (r.get("E-mail") or "").strip()
        if mail and "@" in mail and not rij["email"]:
            rij["email"] = mail
            rij["email_status"] = ""
            gered_mail += 1
        for kol in ("Opmerking", "Kijkt zelf na", "Teamgrootte"):
            v = (r.get(kol) or "").strip()
            if v:
                rij["notities"] = "; ".join(filter(None, [rij["notities"], "%s: %s" % (kol, v)]))
    log.tel("emailadressen_gered", gered_mail)

    gered_notitie = 0
    for r in lees("contacten-onderwijs-nl.csv"):
        naam = (r.get("Naam") or "").strip()
        if not naam:
            continue
        oid = vind_org(r.get("Organisatie"), orgs, alias_index, log, "contacten-onderwijs")
        pid, _ = idx.zoek(oid, naam, r.get("LinkedIn"))
        if not pid:
            continue
        rij = idx.rows[pid]
        for kol in ("Waar gaat die over", "Let op"):
            v = (r.get(kol) or "").strip()
            if v:
                rij["notities"] = "; ".join(filter(None, [rij["notities"], "%s: %s" % (kol, v)]))
                gered_notitie += 1
    log.tel("aantekeningen_gered", gered_notitie)

    # ---- dubbele personen die Dante heeft aangewezen -----------------------
    op_naam = defaultdict(list)
    for rij in idx.rows.values():
        op_naam[(norm(orgs[rij["org_id"]]["naam"]), norm(rij["naam"]))].append(rij)
    for (org_n, naam_n), blijft_naam in DANTE_DUBBEL.items():
        verdwijnt = op_naam.get((norm(org_n), norm(naam_n)), [])
        blijft = next((r for r in idx.rows.values()
                       if norm(r["naam"]) == norm(blijft_naam)
                       and norm(orgs[r["org_id"]]["naam"]) == norm(org_n)), None)
        if not blijft:
            log.add("dubbel_niet_gevonden", org=org_n, gezocht=blijft_naam)
            continue
        for r in verdwijnt:
            if r is blijft:
                continue
            r["dubbel_van"] = blijft["person_id"]
            r["rol"] = "achtergrond"
            r["waarom_afgevallen"] = "dubbel record, geldt als %s" % blijft["person_id"]
            # onderzoek dat alleen op deze rij stond overzetten naar het record dat blijft
            for veld in ("haakje", "haakje_bron_url", "haakje_bron_type", "toetsprogramma",
                         "schrijfwerk", "type_instelling", "opvallend"):
                if r.get(veld) and not blijft.get(veld):
                    blijft[veld] = r[veld]
            log.add("dubbel_samengevoegd", org=org_n, verdwijnt=r["naam"],
                    blijft=blijft["naam"], blijft_id=blijft["person_id"])

    # ---- uitkomsten die Dante heeft doorgegeven ----------------------------
    for u in DANTE_UITKOMSTEN:
        doel = next((r for r in idx.rows.values()
                     if norm(r["naam"]) == norm(u["naam"])
                     and norm(orgs[r["org_id"]]["naam"]) == norm(u["org"])), None)
        if not doel:
            log.add("uitkomst_niet_gevonden", org=u["org"], naam=u["naam"])
            continue
        doel["uitkomst"] = u["uitkomst"]
        doel["uitkomst_reden"] = u["reden"]
        doel["uitkomst_datum"] = u["datum"]
        doel["reactie_gekregen_op"] = u["datum"]
        if u.get("kanaal") == "email" and not doel["verzonden_email"]:
            doel["verzonden_email"] = u["datum"]
        if u["uitkomst"] in ("geen_interesse", "later_terugkomen"):
            doel["bericht_status"] = "vervallen"
            doel["bericht_status_toelichting"] = "%s (%s): %s" % (
                u["uitkomst"], u["datum"], u["reden"][:200])
        log.add("uitkomst_vastgelegd", naam=u["naam"], org=u["org"],
                uitkomst=u["uitkomst"], reden=u["reden"][:120])

    # ---- organisaties die Dante met rust wil laten -------------------------
    for org_naam, reden in DANTE_ORG_OP_SLOT.items():
        oid = alias_index.get(norm(org_naam))
        if not oid:
            log.add("slot_niet_gevonden", org=org_naam)
            continue
        orgs[oid]["icp_status"] = "geblokkeerd"
        orgs[oid]["blokkade_reden"] = reden
        log.add("org_op_slot", naam=orgs[oid]["naam"], reden=reden)

    # ---- tiebreak: een aangewezen per org ----------------------------------
    per_org = defaultdict(list)
    for rij in idx.rows.values():
        if rij["rol"] == "aangewezen":
            per_org[rij["org_id"]].append(rij)

    def verstuurd(p):
        return any((p.get(v) or "").strip() for v in
                   ("verzonden_linkedin", "verzonden_email", "cold_call"))

    for oid, lijst in per_org.items():
        if len(lijst) < 2:
            continue
        gesorteerd = sorted(lijst, key=lambda p: (verstuurd(p), titel_rang(p["functie"])),
                            reverse=True)
        winnaar = gesorteerd[0]
        reden = "al benaderd" if verstuurd(winnaar) else \
            "hoogste titel (rang %d)" % titel_rang(winnaar["functie"])
        # handmatige keuze van Dante wint altijd
        keuze = DANTE_KIEST.get(orgs[oid]["naam"])
        if keuze:
            gekozen = next((p for p in lijst if norm(p["naam"]) == norm(keuze[0])), None)
            if gekozen:
                gesorteerd = [gekozen] + [p for p in lijst if p is not gekozen]
                winnaar = gekozen
                reden = "KEUZE DANTE: " + keuze[1]
            else:
                log.add("keuze_niet_gevonden", org=orgs[oid]["naam"], gezocht=keuze[0])
        for p in gesorteerd[1:]:
            p["rol"] = "tweede_kandidaat"
        log.add("tiebreak", org=orgs[oid]["naam"], winnaar=winnaar["naam"],
                functie=winnaar["functie"][:50], reden=reden,
                verloren=", ".join("%s (%s)" % (p["naam"], p["functie"][:30])
                                   for p in gesorteerd[1:]))

    # ---- afronden ----------------------------------------------------------
    for rij in idx.rows.values():
        if not rij["voornaam"]:
            rij["voornaam"], rij["achternaam"] = split_naam(rij["naam"])
        if rij["rol"] == "aangewezen" and not rij["onderzoek_status"]:
            rij["onderzoek_status"] = "open"
        if rij["onderzoek_status"] in ("gevonden", "geparkeerd", "geen_haakje") \
                and not rij["haakje_niveau"]:
            rij["haakje_niveau"] = "onbeoordeeld"
        if rij["haakje_bron_type"] and rij["haakje_bron_type"] not in BRON_TYPE_MAP.values():
            pass  # vrije tekst mag hier, geen woordenlijst

    log.tel("orgs_totaal", len(orgs))
    log.tel("personen_totaal", len(idx.rows))
    return orgs, idx


# ---------------------------------------------------------------- rapport

CSS = """
body{font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
 margin:0;background:#f6f8f9;color:#12232b}
.wrap{max-width:1100px;margin:0 auto;padding:32px 20px 80px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:19px;margin:34px 0 10px;
 padding-top:18px;border-top:1px solid #dde4e7}
.sub{color:#5b6f78;margin:0 0 26px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:18px 0}
.card{background:#fff;border:1px solid #e2e8eb;border-radius:10px;padding:14px 16px}
.card .n{font-size:24px;font-weight:600}
.card .l{color:#5b6f78;font-size:13px;margin-top:2px}
.ok{color:#137a4c}.warn{color:#8a5a00}.bad{color:#b3261e}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #e2e8eb;
 border-radius:10px;overflow:hidden;font-size:13.5px}
th{background:#eef3f5;text-align:left;padding:8px 10px;font-weight:600;white-space:nowrap}
td{padding:7px 10px;border-top:1px solid #edf1f3;vertical-align:top}
tr:hover td{background:#fafcfc}
.scroll{overflow-x:auto;margin:10px 0 4px}
details{margin:10px 0}summary{cursor:pointer;color:#0b6ea8;font-weight:500}
.n0{color:#5b6f78}
"""


def rapport(log, orgs, idx, pad):
    def tabel(rijen, kolommen=None, max_rijen=400):
        if not rijen:
            return '<p class="n0">geen</p>'
        kolommen = kolommen or list(rijen[0].keys())
        h = ['<div class="scroll"><table><tr>' +
             "".join("<th>%s</th>" % html.escape(k) for k in kolommen) + "</tr>"]
        for r in rijen[:max_rijen]:
            h.append("<tr>" + "".join(
                "<td>%s</td>" % html.escape(str(r.get(k, ""))[:300]) for k in kolommen) + "</tr>")
        h.append("</table></div>")
        if len(rijen) > max_rijen:
            h.append('<p class="n0">... en nog %d rijen</p>' % (len(rijen) - max_rijen))
        return "".join(h)

    s = log.secties
    t = log.tellers
    people = list(idx.rows.values())
    rol = defaultdict(int)
    for p in people:
        rol[p["rol"]] += 1
    niv = defaultdict(int)
    for p in people:
        niv[p["haakje_niveau"] or "(leeg)"] += 1

    in_totaal = t.get("contacten_ingelezen", 0) + t.get("haakjes_ingelezen", 0) + \
        t.get("berichten_ingelezen", 0)
    balans_ok = t.get("personen_totaal", 0) <= in_totaal

    h = ['<!doctype html><meta charset="utf-8"><title>Migratie-rapport</title>',
         "<style>%s</style><div class=wrap>" % CSS,
         "<h1>Migratie-rapport</h1>",
         '<p class="sub">Van 4 losse CSV\'s naar het master-document. '
         'Dit is een droogloop: er is nog niets weggeschreven. %s</p>' % now_iso()]

    h.append('<div class="grid">')
    for label, waarde, klasse in [
        ("organisaties", t.get("orgs_totaal", 0), ""),
        ("personen", t.get("personen_totaal", 0), ""),
        ("rijen ingelezen", in_totaal, ""),
        ("orphans gered", len(s["orphan"]), "ok" if s["orphan"] else ""),
        ("conflicten", len(s["conflict"]), "warn" if s["conflict"] else "ok"),
        ("tiebreaks", len(s["tiebreak"]), "warn" if s["tiebreak"] else ""),
        ("balans", "klopt" if balans_ok else "FOUT", "ok" if balans_ok else "bad"),
    ]:
        h.append('<div class="card"><div class="n %s">%s</div><div class="l">%s</div></div>'
                 % (klasse, waarde, label))
    h.append("</div>")

    h.append("<h2>Verdeling</h2>")
    h.append(tabel([{"rol": k, "aantal": v} for k, v in
                    sorted(rol.items(), key=lambda x: -x[1])]))
    h.append(tabel([{"niveau": k, "aantal": v} for k, v in
                    sorted(niv.items(), key=lambda x: -x[1])]))
    h.append(tabel([{"bron": k, "rijen": v} for k, v in sorted(t.items())]))

    h.append("<h2>Orphans: stonden in haakjes of berichten maar niet in de contactenlijst</h2>")
    h.append("<p>Deze zijn niet weggegooid, ze zijn als nieuw record aangemaakt en op "
             "<code>aangewezen</code> gezet.</p>")
    h.append(tabel(s["orphan"], ["naam", "org", "bron", "person_id"]))

    h.append("<h2>De 12 die 'kern' heetten maar wel een onderbouwing hadden</h2>")
    h.append("<p>Op <code>aangewezen</code> gezet. Loop deze na, dit is de enige interpretatie "
             "in de migratie waar ik van je afwijk als je het er niet mee eens bent.</p>")
    h.append(tabel(s["kern_met_onderbouwing"], ["naam", "org", "waarom"]))

    h.append("<h2>Tiebreaks: twee aangewezen personen bij een organisatie</h2>")
    h.append("<p>Regel: wie al benaderd is wint, anders wie het hoogst in de boom staat. "
             "De verliezer is <code>tweede_kandidaat</code>, niet verwijderd.</p>")
    h.append(tabel(s["tiebreak"], ["org", "winnaar", "functie", "reden", "verloren"]))

    h.append("<h2>Onderzoek zonder niveau (de reparatiewachtrij)</h2>")
    h.append("<p>Haakje gevonden, maar nooit een niveau toegekend. Deze vallen in stage 3r: "
             "agent 3 kent alleen een niveau toe, hij doet geen nieuw onderzoek.</p>")
    h.append(tabel(s["niveau_onbeoordeeld"], ["naam", "org", "haakje"]))

    h.append("<h2>Organisaties die niet op de targetlijst stonden</h2>")
    h.append("<p>Afgeleid uit de contact- of berichtbestanden. Staan op "
             "<code>kandidaat</code> en komen bovenaan agent 1's wachtrij.</p>")
    h.append(tabel(s["org_nieuw_uit_contact"] + s["org_uit_moederkolom"],
                   ["naam", "org_id", "bron"]))

    h.append("<h2>Zoekpogingen zonder naam: agent 2 heeft gezocht en niets gevonden</h2>")
    h.append("<p>Deze 37 rijen in de contactenlijst waren geen personen maar aantekeningen. "
             "Ze staan nu in het veld <code>contact_zoekpoging</code> op de organisatie, zodat "
             "agent 2 diezelfde zoektocht niet nog een keer doet.</p>")
    h.append(tabel(s["zoekpoging_zonder_naam"], ["org", "laag", "waarom"]))

    if s["org_geblokkeerd"]:
        h.append("<h2>Organisaties geblokkeerd op basis van een aantekening</h2>")
        h.append(tabel(s["org_geblokkeerd"], ["naam", "reden"]))

    h.append("<h2>Naamvarianten die op een bestaande organisatie zijn gekoppeld</h2>")
    h.append(tabel(s["org_deelstring"], ["gezocht", "gekoppeld_aan", "bron"]))

    h.append("<h2>Personen die niet op LinkedIn maar op naam gematcht zijn</h2>")
    h.append("<p>Hier zit het risico op een verkeerde koppeling. Steekproef nemen.</p>")
    h.append(tabel(s["gematcht"], ["naam", "org", "methode", "bron", "person_id"]))

    if s["uitkomst_vastgelegd"] or s["dubbel_samengevoegd"]:
        h.append("<h2>Handmatige beslissingen van Dante</h2>")
        h.append("<p>Deze staan in het script vastgelegd en overleven een herhaalde "
                 "migratie.</p>")
        h.append(tabel(s["dubbel_samengevoegd"], ["org", "verdwijnt", "blijft", "blijft_id"]))
        h.append(tabel(s["uitkomst_vastgelegd"], ["naam", "org", "uitkomst", "reden"]))

    if s["rol_sterkste_wint"]:
        h.append("<h2>Dubbele rijen met een verschillende rol</h2>")
        h.append("<p>Dezelfde persoon stond twee keer in de contactenlijst met een ander label. "
                 "De sterkste rol wint (aangewezen boven tweede kandidaat boven afgevallen), "
                 "niet de laatste rij.</p>")
        h.append(tabel(s["rol_sterkste_wint"], ["naam", "org", "gekozen", "ook_gezien"]))

    h.append("<h2>Conflicten: twee bestanden zeiden iets anders</h2>")
    h.append("<p>De behouden waarde staat links. De weggezette waarde is bewaard in "
             "<code>notities</code> of hieronder terug te lezen.</p>")
    h.append(tabel(s["conflict"], ["person_id", "veld", "behouden", "weggezet", "bron"]))

    if s["org_samengevoegd"]:
        h.append("<h2>Organisaties samengevoegd op naamvariant</h2>")
        h.append(tabel(s["org_samengevoegd"], ["naam", "met", "org_id"]))

    h.append("</div>")
    with open(pad, "w", encoding="utf-8") as f:
        f.write("".join(h))


# ---------------------------------------------------------------- verify


def verify():
    orgs = {o["org_id"]: o for o in load(ORGS, ORG_COLS)}
    people = load(PEOPLE, PERSON_COLS)
    by_li = {li_slug(p["linkedin_url"]): p for p in people if li_slug(p["linkedin_url"])}
    by_naam = defaultdict(list)
    for p in people:
        by_naam[norm(p["naam"])].append(p)

    naam_van_org = {}
    for o in orgs.values():
        naam_van_org[norm(o["naam"])] = o
        for a in (o["naam_aliassen"] or "").split("|"):
            if a.strip():
                naam_van_org[norm(a)] = o

    ontbreekt, als_notitie = [], 0
    for bestand, naamkol in (("contacten-linkedin-nl.csv", "Naam"),
                             ("haakjes-nl.csv", "Naam"),
                             ("berichten-nl.csv", "Naam")):
        for r in lees(bestand):
            naam = (r.get(naamkol) or "").strip()
            org_naam = (r.get("Organisatie") or "").strip()
            if not is_persoonsnaam(naam):
                # hoort als aantekening op de organisatie te staan
                o = naam_van_org.get(norm(org_naam))
                if o and (o.get("contact_zoekpoging") or o.get("blokkade_reden")):
                    als_notitie += 1
                elif org_naam:
                    ontbreekt.append({"bestand": bestand, "naam": naam or "(leeg)",
                                      "org": org_naam, "reden": "aantekening niet geland"})
                continue
            s = li_slug(r.get("LinkedIn"))
            if s and s in by_li:
                continue
            if by_naam.get(norm(naam)):
                continue
            ontbreekt.append({"bestand": bestand, "naam": naam, "org": org_naam,
                              "reden": "persoon niet gevonden"})

    print("orgs in master: %d" % len(orgs))
    print("personen in master: %d" % len(people))
    print("aantekeningen op organisatieniveau geland: %d" % als_notitie)
    print("bronrijen niet terug te vinden: %d" % len(ontbreekt))
    for o in ontbreekt[:40]:
        print("   ONTBREEKT %(bestand)s | %(naam)s | %(org)s | %(reden)s" % o)
    return 1 if ontbreekt else 0


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true", help="schrijf niets, maak alleen het rapport")
    g.add_argument("--run", action="store_true", help="schrijf de master weg")
    g.add_argument("--verify", action="store_true", help="master terugvergelijken met de bronnen")
    ap.add_argument("--rapport", default=RAPPORT)
    a = ap.parse_args()

    if a.verify:
        sys.exit(verify())

    log = Log()
    orgs, idx = migreer(log)
    rapport(log, orgs, idx, a.rapport)
    print("rapport: %s" % a.rapport)
    for k, v in sorted(log.tellers.items()):
        print("  %-28s %s" % (k, v))
    print("  %-28s %d" % ("orphans", len(log.secties["orphan"])))
    print("  %-28s %d" % ("conflicten", len(log.secties["conflict"])))
    print("  %-28s %d" % ("tiebreaks", len(log.secties["tiebreak"])))
    print("  %-28s %d" % ("niveau onbeoordeeld", len(log.secties["niveau_onbeoordeeld"])))

    if a.run:
        os.makedirs(MASTER, exist_ok=True)
        save(ORGS, ORG_COLS, sorted(orgs.values(), key=lambda o: o["naam"].lower()))
        save(PEOPLE, PERSON_COLS,
             sorted(idx.rows.values(), key=lambda p: (p["org_id"], p["naam"].lower())))
        print("\ngeschreven: %s" % ORGS)
        print("geschreven: %s" % PEOPLE)
        print()
        doctor(verbose=True)
    else:
        print("\n(droogloop, er is niets weggeschreven)")


if __name__ == "__main__":
    main()
