import json, csv
d = json.load(open("leads.json"))
cols = ["firstName","lastName","email","phone","companyName","companyDomain","linkedinUrl",
        "linkedInConnectionRequest","linkedInMessage","firstEmailSubject","firstEmail","Call_script"]
with open("leads.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(cols)
    for l in d:
        cv = l["customVariables"]
        w.writerow([l.get(c, cv.get(c, "")) for c in cols])
print(len(d), "rijen")
