#!/usr/bin/env python3
"""Bouwt het pijplijn-dashboard: agents 1-4 visueel plus de echte cijfers.

Rekent niets zelf uit wat pipeline.py al kan. Importeert dat script en
gebruikt stage_van() als enige waarheid voor de fase.

    python3 .claude/scripts/dashboard.py [--out PAD]

Schrijft standaard naar projects/targetlijst-nl/pijplijn-dashboard.html.
"""

import argparse
import csv
import datetime
import importlib.util
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))


def laad_pipeline():
    pad = os.path.join(HIER, "pipeline.py")
    spec = importlib.util.spec_from_file_location("pipeline", pad)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pipeline"] = mod
    spec.loader.exec_module(mod)
    return mod


P = laad_pipeline()

# ---------------------------------------------------------------- de keten

STAPPEN = [
    {
        "n": "1",
        "agent": "lead-sourcing-nl",
        "titel": "Organisaties zoeken",
        "stage": "1",
        "in": "Bronbakken: NRTO, opleidingsgroepen, particuliere hogescholen, CRKBO, CPION",
        "uit": "Rij in orgs.csv met icp_status",
        "poorten": [
            ["Poort 0 &mdash; ICP", "Beoordeelt die zelf werk van lerenden? Eigen docenten of examencommissie is Ja, extern examenbureau is Nee."],
            ["Bewijsregel", "Elk Ja heeft een letterlijk citaat plus URL. Geen citaat, geen Ja."],
            ["Poort 0d &mdash; omvang", "Zit er 10k in? Cascade lerenden &rarr; opleidingen &rarr; medewerkers. Jaarfee mag niet boven 10% van de cursusomzet."],
            ["Close-check", "Staat de org of de moeder al in Close, dan geblokkeerd en geen koude outreach."],
        ],
        "klaar": "icp_status = gekwalificeerd en nog geen aangewezen persoon",
    },
    {
        "n": "2",
        "agent": "contact-sourcing-nl",
        "titel": "De juiste persoon",
        "stage": "2",
        "in": "Gekwalificeerde orgs zonder contact",
        "uit": "Een persoon met rol = aangewezen",
        "poorten": [
            ["Organigram eerst", "Volg de tak onderwijs of onderzoek, niet bedrijfsvoering."],
            ["Mandaat", "Hoogste autoriteit over onderwijs of AI. Nooit de examencommissie. Docent of teamco&ouml;rdinator is een ongeldige uitkomst."],
            ["Werkt die er nog?", "LinkedIn is beslissend, einddatum in de ervaring. Vertrokken is afgevallen."],
            ["Klopt de titel?", "Verifieren via LinkedIn, functie_bron en datum invullen."],
            ["Dedup", "pipeline.py exists op de LinkedIn-URL voor je aanwijst."],
        ],
        "klaar": "rol = aangewezen, onderzoek nog niet gedaan",
    },
    {
        "n": "3",
        "agent": "shift-research",
        "titel": "Haakje zoeken",
        "stage": "3",
        "in": "Aangewezen personen zonder onderzoek",
        "uit": "Haakje met bron en niveau, plus het dossier",
        "poorten": [
            ["Toetsprogramma eerst", "Wat leveren lerenden in, hoeveel, wie kijkt het na. Met bron."],
            ["Brontoets", "Splits FEIT en GEVOLG. Nooit begrippen invullen die de bron niet noemt, zoals nakijklast of tijdsdruk."],
            ["Tegenspraaktoets", "Zoek een zin in de bron die je haakje onderuithaalt."],
            ["Drager-toets", "Elk citaat krijgt student, beoordelaar, organisatie of panel. Een last bij de student is geen haakje voor ons."],
            ["Teaser-limiet", "De velden blijven onder 200 tekens, de lading hoort in het dossier."],
        ],
        "klaar": "niveau 2, 2b of 3 toegekend",
        "extra": {"stage": "3r", "label": "3r &middot; onderzocht, niveau ontbreekt"},
    },
    {
        "n": "4",
        "agent": "linkedin-outreach",
        "titel": "Bericht schrijven",
        "stage": "4",
        "in": "Personen met een bruikbaar haakje",
        "uit": "Connectieverzoek plus opvolgmail, status concept",
        "poorten": [
            ["Koud-check", "Close en Gmail op persoon en org. Lopende cold call is vervallen, recent benaderde collega is gepauzeerd."],
            ["Afgemaakte rij", "Toetsprogramma en schrijfwerk staan bevestigd in het dossier. Onbekend gaat terug naar agent 3, niet zelf googelen."],
            ["Niveau-poort", "Alleen 2, 2b en 3 krijgen een bericht. Niveau 1 gaat naar Dante."],
            ["Omkeertoets", "Vervang het detail door iets anders. Klopt de zin nog steeds, dan is de brug vals."],
            ["Lengte", "Het connectieverzoek blijft onder 300 tekens, het script weigert langer."],
        ],
        "klaar": "Dante zet bericht_status op goedgekeurd",
    },
    {
        "n": "5",
        "agent": "lemlist-import-nl",
        "titel": "Naar Lemlist",
        "stage": "5",
        "in": "Goedgekeurde berichten",
        "uit": "Lead in de campagne, klaar om te versturen",
        "poorten": [
            ["E&eacute;n per organisatie", "Maximaal een verstuurmoment per org, de hoogste in de boom."],
            ["E&eacute;n kanaal", "Loopt er al een cold call, dan geen LinkedIn-verzoek erbovenop."],
            ["Dedupe", "Op LinkedIn-URL, plus e-mail en domein."],
            ["br-fix", "De opvolgmail moet HTML-breaks hebben, anders valt de opmaak weg in Lemlist."],
        ],
        "klaar": "Dante verstuurt zelf, daarna stage klaar",
    },
]

ZIJUITGANGEN = [
    ["gepauzeerd", "Gepauzeerd", "Collega bij dezelfde org is korter dan twee weken geleden benaderd."],
    ["reserve", "Tweede kandidaat", "Goede reserve, komt aan de beurt als de eerste niets doet."],
    ["buiten", "Buiten", "Afgevallen, achtergrond, al in Close, geen haakje, of niveau 1."],
    ["geblokkeerd", "Geblokkeerd", "De organisatie zelf is afgevallen, geblokkeerd of te klein."],
]

LADDER = [
    "Is de organisatie afgevallen, geblokkeerd of te klein? Dan <b>geblokkeerd</b>.",
    "Is de rol afgevallen, achtergrond, al in Close of doorverwijzing? Dan <b>buiten</b>.",
    "Staat er een Lemlist-import of een verzenddatum, of is het bericht verstuurd? Dan <b>klaar</b>.",
    "Is het bericht vervallen of afgekeurd? Dan <b>buiten</b>.",
    "Is het bericht gepauzeerd? Dan <b>gepauzeerd</b>.",
    "Is het bericht goedgekeurd? Dan <b>stage 5</b>, klaar voor Lemlist.",
    "Is de rol niet aangewezen? Dan <b>reserve</b>.",
    "Is het onderzoek leeg, open of geparkeerd? Dan <b>stage 3</b>, haakje zoeken.",
    "Is het onderzoek geen_haakje? Dan <b>buiten</b>.",
    "Is het haakje-niveau leeg of onbeoordeeld? Dan <b>stage 3r</b>, alleen nog een niveau toekennen.",
    "Is het niveau 2, 2b of 3 en er is nog geen bericht? Dan <b>stage 4</b>, bericht schrijven.",
    "Is het niveau 1? Dan <b>buiten</b>.",
]

COMMANDOS = [
    ["status [--doel N]", "Trechtertelling. Met --doel een plan hoeveel er uit 3r, 3 en 2 moet komen."],
    ["queue --stage 2|3|3r|4|5", "De werkvoorraad van een stap, met de velden die die stap nodig heeft."],
    ["show &lt;id&gt; [--full]", "Alles van een org of persoon, inclusief afgeleide stage en dossierpad."],
    ["dossier &lt;id&gt; [--sectie X]", "Het onderzoeksdossier lezen of schrijven, per sectie."],
    ["uitleg [veld]", "Wat een veld betekent en welke waarden mogen. Nooit gokken."],
    ["exists --linkedin URL", "Zit deze persoon al in de keten, in welke stage, is er al iets verstuurd."],
    ["omvang --toets ORG", "Poort 0d: groot genoeg, te klein of onbekend."],
    ["touch &lt;id&gt; --kanaal linkedin", "Verzenddatum vastleggen, zet bericht_status zelf op verstuurd."],
    ["uitkomst &lt;id&gt; --status ...", "Wat er uit een lead kwam, met de reden in hun eigen woorden."],
    ["promote &lt;id&gt;", "Tweede kandidaat wordt de aangewezene, de vorige zakt terug."],
    ["doctor [--fix-safe]", "Controle op dubbele id's, foute enums, te lange berichten, ontbrekende dossiers."],
    ["export lemlist --out PAD", "De stage-5-wachtrij als CSV in Lemlist-kolommen."],
]

VERDELINGEN = [
    ("orgs", "icp_status", "Organisaties: ICP-status"),
    ("orgs", "beoordeelt_zelf", "Organisaties: beoordeelt zelf"),
    ("people", "rol", "Personen: rol"),
    ("people", "onderzoek_status", "Personen: onderzoek"),
    ("people", "haakje_niveau", "Personen: haakje-niveau"),
    ("people", "bericht_status", "Personen: bericht"),
    ("people", "lemlist_status", "Personen: Lemlist"),
    ("people", "uitkomst", "Personen: uitkomst"),
]


def verdeling(rows, veld):
    telling = {}
    for r in rows:
        v = (r.get(veld) or "").strip()
        telling[v] = telling.get(v, 0) + 1
    paren = sorted(telling.items(), key=lambda kv: -kv[1])
    uitleg = P.WAARDEN.get(veld, {})
    return [
        {
            "waarde": k if k else "(leeg)",
            "aantal": v,
            "uitleg": uitleg.get(k, ""),
        }
        for k, v in paren
    ]


def journaal_activiteit(dagen=45):
    """Per dag hoeveel wijzigingen, en per actor het totaal. Streamt het bestand."""
    if not os.path.exists(P.JOURNAL):
        return {"per_dag": [], "per_actor": []}
    grens = (datetime.date.today() - datetime.timedelta(days=dagen)).isoformat()
    per_dag, per_actor = {}, {}
    with open(P.JOURNAL, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        for rij in r:
            if len(rij) < 2:
                continue
            dag = rij[0][:10]
            if dag < grens:
                continue
            per_dag[dag] = per_dag.get(dag, 0) + 1
            actor = rij[1] or "onbekend"
            per_actor[actor] = per_actor.get(actor, 0) + 1
    if per_dag:
        eerste = datetime.date.fromisoformat(min(per_dag))
        vandaag = datetime.date.today()
        d = eerste
        while d <= vandaag:
            per_dag.setdefault(d.isoformat(), 0)
            d += datetime.timedelta(days=1)
    return {
        "per_dag": [{"dag": d, "aantal": n} for d, n in sorted(per_dag.items())],
        "per_actor": [{"actor": a, "aantal": n} for a, n in sorted(per_actor.items(), key=lambda kv: -kv[1])],
    }


def verzamel():
    orgs, people = P.load_markt()      # alleen de actieve markt (--markt), sinds 10-09-2026
    by_id = {o["org_id"]: o for o in orgs}

    stages = {}
    for p in people:
        s = P.stage_van(p, by_id)
        stages.setdefault(s, []).append(p)

    def persoonrij(p):
        org = by_id.get(p.get("org_id", ""), {})
        return {
            "id": p.get("person_id", ""),
            "naam": p.get("naam", ""),
            "functie": p.get("functie", ""),
            "org": org.get("naam", p.get("org_id", "")),
            "niveau": p.get("haakje_niveau", ""),
            "onderzoek": p.get("onderzoek_status", ""),
            "bericht": p.get("bericht_status", ""),
            "bijgewerkt": (p.get("laatst_bijgewerkt", "") or "")[:10],
        }

    def orgrij(o):
        return {
            "id": o.get("org_id", ""),
            "naam": o.get("naam", ""),
            "functie": o.get("categorie", ""),
            "org": o.get("domein", ""),
            "niveau": "",
            "onderzoek": o.get("beoordeelt_zelf", ""),
            "bericht": "",
            "bijgewerkt": (o.get("laatst_bijgewerkt", "") or "")[:10],
        }

    stage2 = P.orgs_stage2(orgs, people)

    lijsten = {
        "1": [orgrij(o) for o in orgs if o.get("icp_status") == "kandidaat"],
        "2": [orgrij(o) for o in stage2],
    }
    for s in ["3", "3r", "4", "5", "gepauzeerd", "reserve", "buiten", "geblokkeerd", "klaar"]:
        lijsten[s] = [persoonrij(p) for p in stages.get(s, [])]
    for k in lijsten:
        lijsten[k].sort(key=lambda r: (r["org"].lower(), r["naam"].lower()))

    tellingen = {"2": len(stage2)}
    for s in ["3", "3r", "4", "5", "gepauzeerd", "reserve", "buiten", "geblokkeerd", "klaar"]:
        tellingen[s] = len(stages.get(s, []))
    tellingen["1"] = sum(1 for o in orgs if o.get("icp_status") == "kandidaat")

    in_bewerking = tellingen["2"] + tellingen["3"] + tellingen["3r"] + tellingen["4"] + tellingen["5"]

    return {
        "gegenereerd": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        "kpi": {
            "orgs": len(orgs),
            "orgs_gekwalificeerd": sum(1 for o in orgs if o.get("icp_status") == "gekwalificeerd"),
            "personen": len(people),
            "benaderd": tellingen["klaar"],
            "in_bewerking": in_bewerking,
        },
        "tellingen": tellingen,
        "lijsten": lijsten,
        "stappen": STAPPEN,
        "zijuitgangen": [
            {"sleutel": k, "titel": t, "uitleg": u, "aantal": tellingen.get(k, 0)}
            for k, t, u in ZIJUITGANGEN
        ],
        "verdelingen": [
            {"titel": titel, "veld": veld, "items": verdeling(orgs if bron == "orgs" else people, veld)}
            for bron, veld, titel in VERDELINGEN
        ],
        "ladder": LADDER,
        "commandos": COMMANDOS,
        "activiteit": journaal_activiteit(),
    }


# ---------------------------------------------------------------- sjabloon

SJABLOON = r"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Pijplijn NL</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  color-scheme:light;
  --navy:#002333; --green:#00e075; --green-deep:#007b54; --green-700:#006754;
  --ground:#f3f7f8; --card:#ffffff; --ink:#002333; --ink-soft:#2c4a57;
  --muted:#5b7480; --line:#d6e2e7; --line-soft:#e7eef0;
  --shadow:0 1px 2px rgba(0,35,51,.06), 0 4px 16px rgba(0,35,51,.06);
  --sans:"Inter",ui-sans-serif,system-ui,-apple-system,sans-serif;
  --display:"League Spartan",var(--sans);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:48px 24px 96px}
h1,h2,h3{font-family:var(--display);letter-spacing:-.01em;margin:0}
h1{font-size:2.4rem;font-weight:700;line-height:1.1}
h2{font-size:1.35rem;font-weight:600}
.eyebrow{font-size:.7rem;font-weight:600;letter-spacing:.13em;text-transform:uppercase;
  color:var(--green-deep);margin-bottom:10px}
.lede{color:var(--muted);margin:12px 0 0;max-width:62ch}
header{margin-bottom:40px}
section{margin-top:48px}
.sec-head{margin-bottom:18px}
.sec-head p{color:var(--muted);margin:6px 0 0;max-width:70ch;font-size:.9rem}

.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;
  box-shadow:var(--shadow)}
.kpi .num{font-family:var(--display);font-size:2.3rem;font-weight:700;line-height:1;
  color:var(--navy)}
.kpi .lbl{font-size:.78rem;color:var(--muted);margin-top:8px;text-transform:uppercase;
  letter-spacing:.08em;font-weight:600}
.kpi .sub{font-size:.8rem;color:var(--muted);margin-top:4px}

.chain{display:grid;grid-template-columns:repeat(5,1fr);gap:0;align-items:stretch}
@media (max-width:1000px){.chain{grid-template-columns:1fr;gap:14px}}
.step{position:relative;padding-right:22px}
@media (max-width:1000px){.step{padding-right:0}}
.step:last-child{padding-right:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 16px 18px;
  box-shadow:var(--shadow);height:100%;display:flex;flex-direction:column;
  cursor:pointer;transition:border-color .12s,transform .12s}
.card:hover{border-color:var(--green-deep);transform:translateY(-1px)}
.card.actief{border-color:var(--green-deep);box-shadow:0 0 0 2px rgba(0,123,84,.16),var(--shadow)}
.badge{width:26px;height:26px;border-radius:8px;background:var(--navy);color:var(--green);
  font-family:var(--display);font-weight:700;font-size:.85rem;display:flex;align-items:center;
  justify-content:center;margin-bottom:10px}
.card h3{font-size:1rem;font-weight:600}
.agent{font-size:.72rem;color:var(--muted);font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  margin-top:3px;word-break:break-all}
.wacht{margin:12px 0;display:flex;align-items:baseline;gap:7px}
.wacht b{font-family:var(--display);font-size:1.9rem;font-weight:700;line-height:1;
  color:var(--green-deep)}
.wacht span{font-size:.75rem;color:var(--muted)}
.sub-wacht{font-size:.74rem;color:var(--muted);background:var(--line-soft);border-radius:7px;
  padding:6px 9px;margin:-4px 0 10px;cursor:pointer}
.sub-wacht:hover{color:var(--green-deep)}
.sub-wacht b{color:var(--green-deep);font-weight:600}
.io{font-size:.78rem;color:var(--muted);border-top:1px solid var(--line-soft);padding-top:10px;
  margin-top:auto}
.io div+div{margin-top:5px}
.io b{color:var(--ink-soft);font-weight:600}
.arrow{position:absolute;right:0;top:64px;width:22px;height:2px;background:var(--line)}
.arrow:after{content:"";position:absolute;right:0;top:-4px;border-left:7px solid var(--line);
  border-top:5px solid transparent;border-bottom:5px solid transparent}
@media (max-width:1000px){.arrow{display:none}}

.poorten{margin-top:12px;border-top:1px solid var(--line-soft);padding-top:10px}
.poort{font-size:.78rem;margin-top:8px}
.poort b{display:block;color:var(--ink);font-weight:600;font-size:.76rem}
.poort span{color:var(--muted)}

.exits{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.exit{background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:15px 17px;
  cursor:pointer;transition:border-color .12s}
.exit:hover,.exit.actief{border-color:var(--green-deep);border-style:solid}
.exit .num{font-family:var(--display);font-size:1.7rem;font-weight:700;line-height:1;color:var(--muted)}
.exit h3{font-size:.9rem;margin-top:6px}
.exit p{font-size:.76rem;color:var(--muted);margin:5px 0 0}

.paneel{margin-top:22px;background:var(--card);border:1px solid var(--line);border-radius:12px;
  box-shadow:var(--shadow);overflow:hidden}
.paneel-kop{padding:14px 18px;border-bottom:1px solid var(--line-soft);display:flex;
  justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.paneel-kop h3{font-size:.95rem}
.paneel-kop .telling{font-size:.8rem;color:var(--muted)}
.scroll{overflow-x:auto;max-height:460px;overflow-y:auto}
table{border-collapse:collapse;width:100%;font-size:.83rem}
th{text-align:left;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;
  color:var(--muted);font-weight:600;padding:10px 14px;border-bottom:1px solid var(--line);
  position:sticky;top:0;background:var(--card)}
td{padding:9px 14px;border-bottom:1px solid var(--line-soft);vertical-align:top}
tr:last-child td{border-bottom:none}
td.org{font-weight:600}
td.dim{color:var(--muted)}
.leeg{padding:26px 18px;color:var(--muted);font-size:.85rem}

.verdelingen{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.vak{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;
  box-shadow:var(--shadow)}
.vak h3{font-size:.85rem;margin-bottom:12px}
.rij{margin-top:9px}
.rij-kop{display:flex;justify-content:space-between;font-size:.78rem;gap:10px}
.rij-kop b{font-weight:500}
.rij-kop span{color:var(--muted);font-variant-numeric:tabular-nums}
.bar{height:6px;background:var(--line-soft);border-radius:99px;margin-top:4px;overflow:hidden}
.barfill{height:100%;background:var(--green-deep);border-radius:99px}
.rij small{display:block;color:var(--muted);font-size:.7rem;margin-top:3px}

ol.ladder{counter-reset:l;list-style:none;padding:0;margin:0}
ol.ladder li{counter-increment:l;position:relative;padding:9px 0 9px 40px;font-size:.86rem;
  border-bottom:1px solid var(--line-soft)}
ol.ladder li:last-child{border-bottom:none}
ol.ladder li:before{content:counter(l);position:absolute;left:0;top:8px;width:24px;height:24px;
  border-radius:7px;background:var(--line-soft);color:var(--ink-soft);font-size:.72rem;
  font-weight:600;display:flex;align-items:center;justify-content:center}
ol.ladder b{color:var(--green-deep)}

table.cmd td:first-child{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.78rem;
  white-space:nowrap;color:var(--green-deep)}

.spark{display:flex;align-items:flex-end;gap:2px;height:56px;margin-top:10px}
.spark div{flex:1;background:var(--green-deep);border-radius:2px 2px 0 0;min-height:2px;opacity:.85}
.spark-as{display:flex;justify-content:space-between;font-size:.7rem;color:var(--muted);margin-top:6px}

footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);font-size:.78rem;
  color:var(--muted)}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.85em;
  background:var(--line-soft);padding:1px 5px;border-radius:4px}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="eyebrow">Targetlijst NL</div>
  <h1>De pijplijn, van organisatie tot bericht</h1>
  <p class="lede">Vijf stappen, elk met eigen poorten. Een record schuift pas door als het de poort haalt.
  De fase staat nergens opgeslagen, die wordt afgeleid uit de data. Klik op een stap voor wie daar wacht.</p>
</header>

<section style="margin-top:32px">
  <div class="kpis" id="kpis"></div>
</section>

<section>
  <div class="sec-head">
    <h2>De keten</h2>
    <p>Het grote getal per kaart is wat er nu wacht. Onder elke kaart staan de poorten die de agent moet halen voor hij mag doorschuiven.</p>
  </div>
  <div class="chain" id="chain"></div>
</section>

<section>
  <div class="sec-head">
    <h2>Zijuitgangen</h2>
    <p>Niet alles gaat de keten door. Dit is waar records blijven liggen of afvallen.</p>
  </div>
  <div class="exits" id="exits"></div>
</section>

<section>
  <div class="paneel">
    <div class="paneel-kop">
      <h3 id="paneel-titel">Wachtrij</h3>
      <div class="telling" id="paneel-telling"></div>
    </div>
    <div class="scroll" id="paneel-body"></div>
  </div>
</section>

<section>
  <div class="sec-head">
    <h2>Verdelingen</h2>
    <p>Wat er in de kolommen staat. Onder elke waarde de betekenis uit <code>pipeline.py uitleg</code>.</p>
  </div>
  <div class="verdelingen" id="verdelingen"></div>
</section>

<section>
  <div class="sec-head">
    <h2>Activiteit</h2>
    <p>Wijzigingen per dag uit het journaal, laatste 45 dagen.</p>
  </div>
  <div class="vak">
    <div class="spark" id="spark"></div>
    <div class="spark-as" id="spark-as"></div>
    <div id="actors" style="margin-top:18px"></div>
  </div>
</section>

<section>
  <div class="sec-head">
    <h2>Hoe de fase bepaald wordt</h2>
    <p>Er is geen fase-kolom. Deze twaalf vragen worden op volgorde gesteld, de eerste die klopt bepaalt de fase.</p>
  </div>
  <div class="vak"><ol class="ladder" id="ladder"></ol></div>
</section>

<section>
  <div class="sec-head">
    <h2>Commando's</h2>
    <p>Alles draait via <code>python3 .claude/scripts/pipeline.py</code>. Veldnaam kwijt? <code>uitleg</code> vertelt het.</p>
  </div>
  <div class="paneel"><div class="scroll" style="max-height:none"><table class="cmd"><tbody id="cmd"></tbody></table></div></div>
</section>

<footer id="footer"></footer>
</div>

<script type="application/json" id="data">__DATA__</script>
<script>
(function(){
  var D = JSON.parse(document.getElementById('data').textContent);
  var $ = function(id){ return document.getElementById(id); };
  var esc = function(s){ var d=document.createElement('div'); d.textContent=s==null?'':String(s); return d.innerHTML; };

  // KPI's
  var k = D.kpi;
  $('kpis').innerHTML = [
    ['Organisaties', k.orgs, k.orgs_gekwalificeerd + ' gekwalificeerd', ''],
    ['Personen', k.personen, 'in people.csv', ''],
    ['Benaderd', k.benaderd, 'verstuurd of ge&iuml;mporteerd', 'klaar'],
    ['In bewerking', k.in_bewerking, 'stap 2 tot en met 5', '']
  ].map(function(r){
    var attr = r[3] ? ' data-stage="'+r[3]+'" style="cursor:pointer"' : '';
    return '<div class="kpi"'+attr+'><div class="num">'+r[1]+'</div><div class="lbl">'+r[0]+'</div><div class="sub">'+r[2]+'</div></div>';
  }).join('');

  // Keten
  $('chain').innerHTML = D.stappen.map(function(s){
    var n = D.tellingen[s.stage] || 0;
    var poorten = s.poorten.map(function(p){
      return '<div class="poort"><b>'+p[0]+'</b><span>'+p[1]+'</span></div>';
    }).join('');
    return '<div class="step">'+
      '<div class="card" data-stage="'+s.stage+'">'+
        '<div class="badge">'+s.n+'</div>'+
        '<h3>'+esc(s.titel)+'</h3>'+
        '<div class="agent">'+esc(s.agent)+'</div>'+
        '<div class="wacht"><b>'+n+'</b><span>wacht hier</span></div>'+
        (s.extra ? '<div class="sub-wacht" data-stage="'+s.extra.stage+'"><b>'+(D.tellingen[s.extra.stage]||0)+'</b> '+s.extra.label+'</div>' : '')+
        '<div class="poorten">'+poorten+'</div>'+
        '<div class="io"><div><b>In:</b> '+esc(s.in)+'</div><div><b>Uit:</b> '+esc(s.uit)+'</div>'+
        '<div><b>Door als:</b> '+esc(s.klaar)+'</div></div>'+
      '</div>'+
      '<div class="arrow"></div>'+
    '</div>';
  }).join('');

  // Zijuitgangen
  $('exits').innerHTML = D.zijuitgangen.map(function(e){
    return '<div class="exit" data-stage="'+e.sleutel+'">'+
      '<div class="num">'+e.aantal+'</div><h3>'+esc(e.titel)+'</h3><p>'+esc(e.uitleg)+'</p></div>';
  }).join('');

  // Paneel
  var LABELS = {'1':'Stap 1 &mdash; kandidaten, nog niet gekwalificeerd','2':'Stap 2 &mdash; organisaties zonder contact','3':'Stap 3 &mdash; haakje zoeken',
    '3r':'Stap 3r &mdash; alleen niveau toekennen','4':'Stap 4 &mdash; bericht schrijven',
    '5':'Stap 5 &mdash; klaar voor Lemlist','gepauzeerd':'Gepauzeerd','reserve':'Tweede kandidaten',
    'buiten':'Buiten de keten','geblokkeerd':'Geblokkeerd','klaar':'Benaderd'};

  function toon(stage){
    var rows = D.lijsten[stage] || [];
    $('paneel-titel').innerHTML = LABELS[stage] || stage;
    $('paneel-telling').textContent = rows.length + (rows.length === 1 ? ' record' : ' records');
    if(!rows.length){
      $('paneel-body').innerHTML = '<div class="leeg">Niets in deze wachtrij.</div>';
    } else {
      var isOrg = (stage === '2');
      var head = isOrg
        ? '<tr><th>Organisatie</th><th>Categorie</th><th>Domein</th><th>Beoordeelt zelf</th><th>Bijgewerkt</th></tr>'
        : '<tr><th>Organisatie</th><th>Persoon</th><th>Functie</th><th>Niveau</th><th>Status</th><th>Bijgewerkt</th></tr>';
      var body = rows.map(function(r){
        if(isOrg){
          return '<tr><td class="org">'+esc(r.naam)+'</td><td class="dim">'+esc(r.functie)+
            '</td><td class="dim">'+esc(r.org)+'</td><td>'+esc(r.onderzoek)+
            '</td><td class="dim">'+esc(r.bijgewerkt)+'</td></tr>';
        }
        var status = r.bericht || r.onderzoek || '';
        return '<tr><td class="org">'+esc(r.org)+'</td><td>'+esc(r.naam)+
          '</td><td class="dim">'+esc(r.functie)+'</td><td>'+esc(r.niveau)+
          '</td><td class="dim">'+esc(status)+'</td><td class="dim">'+esc(r.bijgewerkt)+'</td></tr>';
      }).join('');
      $('paneel-body').innerHTML = '<table><thead>'+head+'</thead><tbody>'+body+'</tbody></table>';
    }
    var alle = document.querySelectorAll('.card,.exit');
    for(var i=0;i<alle.length;i++){
      alle[i].classList.toggle('actief', alle[i].getAttribute('data-stage') === stage);
    }
  }

  document.addEventListener('click', function(e){
    var el = e.target.closest ? e.target.closest('[data-stage]') : null;
    if(el){ toon(el.getAttribute('data-stage')); }
  });

  // eerste paneel: de grootste wachtrij in de keten
  var eerste = ['2','3','3r','4','5'].sort(function(a,b){
    return (D.tellingen[b]||0) - (D.tellingen[a]||0);
  })[0];
  toon(eerste);

  // Verdelingen
  $('verdelingen').innerHTML = D.verdelingen.map(function(v){
    var max = Math.max.apply(null, v.items.map(function(i){ return i.aantal; })) || 1;
    var rijen = v.items.map(function(i){
      return '<div class="rij"><div class="rij-kop"><b>'+esc(i.waarde)+'</b><span>'+i.aantal+'</span></div>'+
        '<div class="bar"><div class="barfill" style="width:'+Math.round(i.aantal/max*100)+'%"></div></div>'+
        (i.uitleg ? '<small>'+esc(i.uitleg)+'</small>' : '')+'</div>';
    }).join('');
    return '<div class="vak"><h3>'+esc(v.titel)+'</h3>'+rijen+'</div>';
  }).join('');

  // Activiteit
  var dagen = D.activiteit.per_dag;
  if(dagen.length){
    var maxd = Math.max.apply(null, dagen.map(function(d){ return d.aantal; })) || 1;
    $('spark').innerHTML = dagen.map(function(d){
      return '<div style="height:'+Math.max(2, Math.round(d.aantal/maxd*56))+'px" title="'+d.dag+': '+d.aantal+'"></div>';
    }).join('');
    $('spark-as').innerHTML = '<span>'+dagen[0].dag+'</span><span>'+dagen[dagen.length-1].dag+' &middot; piek '+maxd+'</span>';
  } else {
    $('spark').innerHTML = '';
    $('spark-as').innerHTML = '<span>geen activiteit in deze periode</span>';
  }
  var maxa = Math.max.apply(null, D.activiteit.per_actor.map(function(a){ return a.aantal; })) || 1;
  $('actors').innerHTML = D.activiteit.per_actor.map(function(a){
    return '<div class="rij"><div class="rij-kop"><b>'+esc(a.actor)+'</b><span>'+a.aantal+'</span></div>'+
      '<div class="bar"><div class="barfill" style="width:'+Math.round(a.aantal/maxa*100)+'%"></div></div></div>';
  }).join('');

  // Ladder en commando's
  $('ladder').innerHTML = D.ladder.map(function(l){ return '<li>'+l+'</li>'; }).join('');
  $('cmd').innerHTML = D.commandos.map(function(c){
    return '<tr><td>'+c[0]+'</td><td>'+c[1]+'</td></tr>';
  }).join('');

  $('footer').innerHTML = 'Stand van ' + esc(D.gegenereerd) +
    '. Verversen: <code>python3 .claude/scripts/dashboard.py</code>. ' +
    'Bron: projects/shift/master/, fase afgeleid met stage_van() uit pipeline.py.';
})();
</script>
</body>
</html>
"""


def kaal(html):
    """Zelfde pagina zonder doctype, html, head en body.

    Een Artifact zet die skeletregels zelf om de inhoud heen, dus ze mogen er
    niet nog een keer in staan. Titel, fontlink, stijl en scripts blijven.
    """
    kop = html.split("<title>", 1)[1]
    kop = "<title>" + kop.split("</style>", 1)[0] + "</style>"
    romp = html.split("<body>", 1)[1].rsplit("</body>", 1)[0]
    return kop + "\n" + romp.strip() + "\n"


def main():
    ap = argparse.ArgumentParser(description="Bouwt het pijplijn-dashboard.")
    ap.add_argument("--out", default=os.path.join(P.REPO, "projects", "targetlijst-nl",
                                                  "pijplijn-dashboard.html"))
    ap.add_argument("--artifact", nargs="?", const=os.path.join(
        P.REPO, "projects", "targetlijst-nl", "pijplijn-dashboard-artifact.html"),
        help="schrijf ook de variant zonder html/head/body, om te publiceren")
    ap.add_argument("--markt", default=None, help="de markt (nl, uk, ...). Anders SHIFT_MARKT, anders nl")
    a = ap.parse_args()
    P.activeer_markt((a.markt or os.environ.get("SHIFT_MARKT") or "nl").strip().lower())

    data = verzamel()
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = SJABLOON.replace("__DATA__", blob)

    with open(a.out, "w", encoding="utf-8") as f:
        f.write(html)

    if a.artifact:
        with open(a.artifact, "w", encoding="utf-8") as f:
            f.write(kaal(html))
        print("artifact-variant: %s" % a.artifact)

    t = data["tellingen"]
    print("geschreven: %s" % a.out)
    print("orgs %d  personen %d  |  stap2 %d  stap3 %d  stap3r %d  stap4 %d  stap5 %d"
          % (data["kpi"]["orgs"], data["kpi"]["personen"], t["2"], t["3"], t["3r"], t["4"], t["5"]))
    print("gepauzeerd %d  reserve %d  klaar %d  buiten %d  geblokkeerd %d"
          % (t["gepauzeerd"], t["reserve"], t["klaar"], t["buiten"], t["geblokkeerd"]))


if __name__ == "__main__":
    main()
