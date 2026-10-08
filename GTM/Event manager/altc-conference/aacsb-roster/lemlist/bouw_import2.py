"""Ronde 2+: leest berichten/set-*.md, bouwt leads2.json en leads2.csv voor cam_kM7vngvjiuG7Wda8i.
Gebruik: python3 bouw_import2.py set-c set-d ...   (zonder argumenten: alle set-*.md)"""
import re, json, csv, sys, os, glob
B = os.path.dirname(os.path.abspath(__file__)); BER = os.path.join(B, "..", "berichten")
LINK = "https://events.teams.microsoft.com/event/4239b958-f045-4d0c-8367-96a44223b992@b817b3d1-ef29-4188-b513-db36a036f9b1?source=copyLinkOneEventsShareDialog"
F = ["linkedInConnectionRequest", "linkedInMessage", "firstEmailSubject", "firstEmail", "Call_script"]
gedaan = {r["naam"].lower() for r in csv.DictReader(open(os.path.join(B, "geimporteerd.csv")))}
files = [os.path.join(BER, a + ".md") for a in sys.argv[1:]] or sorted(glob.glob(os.path.join(BER, "set-*.md")))

def field(sec, name):
    m = re.search(r"\*\*" + re.escape(name) + r"\*\*[^\n]*\n(.*?)(?=\n\*\*[^\n*]+\*\*|\n---|\n## |\Z)", sec, re.S)
    if not m: return ""
    v = "\n".join(l[2:] if l.startswith("> ") else ("" if l.strip() == ">" else l) for l in m.group(1).strip().split("\n")).strip()
    return "" if re.match(r"(?i)^(geen|n\.?v\.?t|-)\b", v) else v

out, fout, skip = [], [], []
for fp in files:
    txt = open(fp, encoding="utf-8").read()
    for sec in re.split(r"(?m)^## ", txt)[1:]:
        head = sec.split("\n")[0]; meta = sec.split("\n")[1] if "\n" in sec else ""
        m = re.match(r"(a\d{3}\s+)?([^,]+),(.*)", head)
        if not m or "AFGEVALLEN" in sec[:300]: skip.append(head[:60]); continue
        name = m.group(2).strip(); org = m.group(3).split(",")[-1].strip()
        if name.lower() in gedaan: skip.append(name + " (al in campagne)"); continue
        li = re.search(r"https?://[\w.]*linkedin\.com/in/[^\s)·]+", meta)
        segs = [x.strip() for x in meta.split("·")]
        emseg = next((x for x in segs if "@" in x), "")
        em = None if re.search(r"(?i)geen|alleen|niet", emseg.split("@")[0]) else re.search(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", emseg)
        telseg = segs[-1] if len(segs) >= 3 else ""
        num = re.search(r"(\+?\(?\d[\d ()]{8,}\d)", telseg)
        algemeen = bool(re.search(r"(?i)centrale|algeme|switchboard", telseg))
        ph = num if (num and not algemeen) else None
        cv = {k: field(sec, k).replace("[link]", LINK) for k in F}
        n = len(cv["linkedInConnectionRequest"])
        if not 0 < n <= 300: fout.append(f"{name}: verzoek {n}")
        for k, v in cv.items():
            body = re.sub(r"\d{1,2}[:.]\d{2}", "", v.replace(LINK, ""))
            if k not in ("Call_script",) and ":" in body: fout.append(f"{name}: ':' in {k}")
            if re.search(r"—|\bJisc\b|\bALT\b|Dante|Jeroen", v): fout.append(f"{name}: verboden woord in {k}")
        if re.search(r"(?i)(best|groet|regards|cheers|met vriendelijke)[^<\n]{0,15}$", cv["firstEmail"].strip()): fout.append(f"{name}: afsluiting in mail")
        if not cv["firstEmail"]: cv.pop("firstEmail"); cv.pop("firstEmailSubject", None)
        else: cv["firstEmail"] = cv["firstEmail"].replace("\n\n", "<br><br>").replace("\n", "<br>")
        cv["Call_script"] = cv["Call_script"].replace("\n", "<br>")
        parts = name.split(" ", 1)
        lead = dict(firstName=parts[0], lastName=parts[1] if len(parts) > 1 else "", companyName=org,
                    customVariables={k: v for k, v in cv.items() if v})
        if li: lead["linkedinUrl"] = li.group(0).rstrip(".,")
        if em: lead["email"] = em.group(0); lead["companyDomain"] = em.group(0).split("@")[1].lower()
        if ph: lead["phone"] = ph.group(1).strip()
        if not (li or em or ph):
            if num: lead["phone"] = num.group(1).strip(); lead["customVariables"]["Call_script"] = "(Algemeen nummer, vraag naar " + name + ")<br>" + lead["customVariables"].get("Call_script", "")
            else: skip.append(name + " (geen kanaal)"); continue
        out.append(lead)
json.dump(out, open(os.path.join(B, "leads2.json"), "w"), ensure_ascii=False, indent=1)
cols = ["firstName","lastName","email","phone","companyName","companyDomain","linkedinUrl"] + F
with open(os.path.join(B, "leads2.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(cols)
    for l in out: w.writerow([l.get(c, l["customVariables"].get(c, "")) for c in cols])
print(f"{len(out)} leads | fouten: {fout or 'geen'} | overgeslagen: {skip}", file=sys.stderr)
for l in out: print(l["firstName"], l["lastName"], "|", l["companyName"][:30], "| LI" if "linkedinUrl" in l else "| -", "| mail" if "email" in l else "| -", "| tel" if "phone" in l else "| -", file=sys.stderr)
