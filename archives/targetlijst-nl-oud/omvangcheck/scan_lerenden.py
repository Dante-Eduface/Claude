import sys,re,subprocess,html,json,os,concurrent.futures as cf
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def get(u,t=12):
    try:
        r=subprocess.run(["curl","-sL","--max-time",str(t),"-A",UA,u],capture_output=True)
        return r.stdout.decode("utf-8","replace")
    except Exception: return ""
def clean(t):
    t=re.sub(r'(?is)<(script|style|svg|head)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?s)<[^>]+>',' ',t)
    return re.sub(r'[ \t\xa0]+',' ',html.unescape(t))
def urls(dom):
    us=set()
    for p in ["/sitemap.xml","/sitemap_index.xml","/wp-sitemap.xml"]:
        for l in re.findall(r'<loc>(.*?)</loc>',get("https://"+dom+p))[:250]:
            if l.endswith('.xml'): us.update(re.findall(r'<loc>(.*?)</loc>',get(l))[:700])
            else: us.add(l)
        if us: break
    if not us:
        for h in re.findall(r'href="([^"]+)"',get("https://"+dom)):
            if h.startswith('/'): h="https://"+dom+h
            if h.startswith('http') and dom in h: us.add(h)
    return us
LEER=[re.compile(p,re.I) for p in [
 r"(?:ruim|meer dan|ongeveer|circa|zo'?n|bijna|jaarlijks|per jaar|inmiddels|al|reeds)\s*([\d][\d.]{1,6})\s*\+?\s*(studenten|cursisten|deelnemers|leerlingen|professionals)",
 r"([\d][\d.]{1,6})\s*\+?\s*(studenten|cursisten|deelnemers|leerlingen)\s*(?:per jaar|jaarlijks|volgen|hebben|zijn|gingen)",
 r"(?:opleiden|opgeleid|bedienen|begeleiden|verwelkomen)[^.]{0,25}?([\d][\d.]{1,6})\s*(studenten|cursisten|deelnemers|professionals|mensen)",
]]
PRIJS=re.compile(r"(?:€|EUR)\s*([\d][\d.,]{2,9})|([\d][\d.,]{2,9})\s*euro",re.I)
OPLPG=re.compile(r'/(opleiding|opleidingen|leergang|leergangen|studie|studies|mbo|hbo|cursus|cursussen)/[^/]{3,}/?$',re.I)
KWO=re.compile(r'over-ons|overons|about|organisatie|jaarverslag|wie-zijn|feiten|cijfers|onze-school|historie',re.I)
def work(line):
  q=line.split('|')
  r={"pid":q[0],"oid":q[1],"naam":q[2],"dom":q[3],"rank":int(q[4]),"duur_grond":q[5],
     "lerenden":[],"lerenden_url":"","prijzen":[],"prijs_url":"","opl_paginas":0,"fout":""}
  try:
    if not r["dom"]: r["fout"]="geen domein"; return r
    us=urls(r["dom"])
    if not us: r["fout"]="geen urls"; return r
    r["opl_paginas"]=sum(1 for u in us if OPLPG.search(u))
    for u in ["https://"+r["dom"]]+sorted([x for x in us if KWO.search(x)],key=len)[:5]:
        t=clean(get(u))
        for pat in LEER:
            for m in pat.finditer(t):
                s=' '.join(m.group(0).split())
                if s not in r["lerenden"]:
                    r["lerenden"].append(s); r["lerenden_url"]=r["lerenden_url"] or u
        if len(r["lerenden"])>=4: break
    for u in sorted([x for x in us if OPLPG.search(x)],key=len)[:3]:
        t=clean(get(u))
        for m in PRIJS.finditer(t):
            v=(m.group(1) or m.group(2) or "").replace('.','').replace(',','.')
            try: f=float(v)
            except: continue
            if 200<=f<=25000:
                s=' '.join(m.group(0).split())
                if s not in r["prijzen"]: r["prijzen"].append(s); r["prijs_url"]=r["prijs_url"] or u
        if r["prijzen"]: break
    r["lerenden"]=r["lerenden"][:4]; r["prijzen"]=r["prijzen"][:4]
  except Exception as e:
    r["fout"]=str(e)[:60]
  return r
lines=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out=[]
with cf.ThreadPoolExecutor(6) as ex:
    for i,x in enumerate(ex.map(work,lines)):
        out.append(x)
        json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
print("klaar:",len(out))
