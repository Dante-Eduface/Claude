"""Leest de berichtbestanden en bouwt de Lemlist-leads voor campagne cam_kM7vngvjiuG7Wda8i.
Gebruik: python3 bouw_import.py > leads.json   (controleert ook lengte en verboden tekens)"""
import re, json, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(BASE, "..", "..")
LINK = "https://events.teams.microsoft.com/event/4239b958-f045-4d0c-8367-96a44223b992@b817b3d1-ef29-4188-b513-db36a036f9b1?source=copyLinkOneEventsShareDialog"
FIELDS = ["linkedInConnectionRequest", "linkedInMessage", "firstEmailSubject", "firstEmail", "Call_script"]

# bron: (bestand, kopprefix). Kop = de regel die met "## " begint en dit prefix bevat.
LEADS = [
 dict(first="Barry", last="O'Mahony", company="Abu Dhabi University", domain="adu.ac.ae", li="https://www.linkedin.com/in/professor-barry-o-mahony-2b62501b/", email="", phone="", src=("aacsb-proef/lemlist-velden.md", "1. Barry O'Mahony")),
 dict(first="Simon", last="Mercado", company="ESCP Business School", domain="escp.eu", li="https://linkedin.com/in/simon-anthony-mercado-35ab6118", email="smercado@escp.eu", phone="+44 7795 602920", src=("aacsb-proef/lemlist-velden.md", "3. Simon Mercado")),
 dict(first="Karin", last="Barac", company="University of Pretoria", domain="up.ac.za", li="https://www.linkedin.com/in/karin-barac-87042170/", email="", phone="+27 12 420 5439", src=("aacsb-proef/lemlist-velden.md", "4. Karin Barac")),
 dict(first="Bendik", last="Samuelsen", company="BI Norwegian Business School", domain="bi.no", li="https://www.linkedin.com/in/bendik-meling-samuelsen-7b3bb/", email="bendik.samuelsen@bi.no", phone="+47 464 10 561", src=("aacsb-proef/lemlist-velden.md", "10. Bendik Samuelsen")),
 dict(first="Elvira", last="Bolat", company="Bournemouth University", domain="bournemouth.ac.uk", li="https://www.linkedin.com/in/elvirabolat/", email="ebolat@bournemouth.ac.uk", phone="01202 968755", src=("aacsb-proef/lemlist-velden.md", "7. Elvira Bolat")),
 dict(first="Dominic", last="Finn", company="University of Strathclyde", domain="strath.ac.uk", li="https://uk.linkedin.com/in/dominic-finn-a273b312", email="dominic.finn@strath.ac.uk", phone="0141 548 3621", src=("aacsb-proef/lemlist-velden.md", "2. Dominic Finn")),
 dict(first="Kirsteen", last="Daly", company="University of Glasgow", domain="gla.ac.uk", li="https://www.linkedin.com/in/kirsteen-daly-cmgr-mcmi-0863388a/", email="Kirsteen.Daly@glasgow.ac.uk", phone="0141 330 4666", src=("aacsb-proef/lemlist-velden.md", "8. Kirsteen Daly")),
 dict(first="Rose", last="White", company="Lancaster University Management School", domain="lancaster.ac.uk", li="https://www.linkedin.com/in/rosewhite1/", email="r.c.white@lancaster.ac.uk", phone="+44 1524 510743", src=("aacsb-roster/berichten/batch-07.md", "a023")),
 dict(first="Qionglei", last="Yu", company="Newcastle University Business School", domain="ncl.ac.uk", li="https://uk.linkedin.com/in/dr-qionglei-lei-yu-686255a5", email="qionglei.yu@ncl.ac.uk", phone="", src=("aacsb-roster/berichten/batch-09.md", "a038")),
]
EXTRA = os.path.join(BASE, "extra_leads.json")   # de rest, aangevuld zodra agent 4 klaar is
if os.path.exists(EXTRA):
    LEADS += [dict(x, src=tuple(x["src"])) for x in json.load(open(EXTRA))]

def section(path, prefix):
    txt = open(os.path.join(ROOT, path), encoding="utf-8").read()
    parts = re.split(r"(?m)^## ", txt)
    for p in parts:
        if p.startswith(prefix) or p.split("\n")[0].startswith(prefix):
            return p
    raise SystemExit(f"niet gevonden: {prefix} in {path}")

def field(sec, name):
    m = re.search(r"\*\*" + re.escape(name) + r"\*\*[^\n]*\n(.*?)(?=\n\*\*[^\n*]+\*\*|\n---|\Z)", sec, re.S)
    if not m: return ""
    v = m.group(1).strip()
    v = "\n".join(l[2:] if l.startswith("> ") else ("" if l.strip()==">" else l) for l in v.split("\n")).strip()
    return v

def meta(sec, key):
    head = sec.split("\n**")[0]
    if key == "email":
        m = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", head); return m.group(0) if m else ""
    if key == "phone":
        m = re.search(r"(\+?\d[\d ]{8,}\d)", head); return m.group(1) if m else ""

out, fouten = [], []
for L in LEADS:
    sec = section(*L["src"])
    cv = {f: field(sec, f) for f in FIELDS}
    cv = {k: v.replace("[link]", LINK) for k, v in cv.items()}
    name = f'{L["first"]} {L["last"]}'
    n = len(cv["linkedInConnectionRequest"])
    if not (0 < n <= 300): fouten.append(f"{name}: verzoek {n} tekens")
    for k, v in cv.items():
        body = re.sub(r"\d{1,2}:\d{2}", "", v.replace(LINK, ""))
        if k != "Call_script" and ":" in body: fouten.append(f"{name}: dubbele punt in {k}")
        if "—" in v or re.search(r"\bJisc\b|\bALT\b", v): fouten.append(f"{name}: verboden in {k}")
    if "geen adres" in cv["firstEmail"].lower() or not cv["firstEmail"]: cv.pop("firstEmail"); cv.pop("firstEmailSubject", None)
    if "firstEmail" in cv:
        cv["firstEmail"] = cv["firstEmail"].replace("\n\n", "<br><br>").replace("\n", "<br>")
    cv["Call_script"] = cv["Call_script"].replace("\n", "<br>")
    email = L["email"] if L["email"] is not None else meta(sec, "email")
    phone = L["phone"] if L["phone"] is not None else meta(sec, "phone")
    lead = dict(firstName=L["first"], lastName=L["last"], companyName=L["company"], companyDomain=L["domain"], linkedinUrl=L["li"], customVariables={k: v for k, v in cv.items() if v})
    if email: lead["email"] = email
    if phone: lead["phone"] = phone
    out.append(lead)
print(json.dumps(out, ensure_ascii=False, indent=1))
print(f"{len(out)} leads, fouten: {fouten or 'geen'}", file=sys.stderr)
