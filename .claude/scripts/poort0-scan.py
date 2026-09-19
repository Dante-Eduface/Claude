import sys,re,subprocess,html,os,json,concurrent.futures as cf
# Sinds 10-09-2026 marktafhankelijk: de regexes komen uit GTM/ICP/shift/markets/<code>/profiel.json
# (sleutels poort0_own, poort0_extern, poort0_duur, poort0_url_kw). Markt via SHIFT_MARKT, anders nl.
# Ontbreekt een sleutel, dan geldt de NL-regex hieronder. Gebruik: SHIFT_MARKT=uk python3 poort0-scan.py lijst.txt 0 50
_REPO=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_GENEST=os.path.join(_REPO,"projects","shift")
_SHIFT=_GENEST if os.path.isdir(os.path.join(_GENEST,"master")) else _REPO
_MARKT=(os.environ.get("SHIFT_MARKT") or "nl").strip().lower()
try:
    _PROF=json.load(open(os.path.join(_SHIFT,"markets",_MARKT,"profiel.json"),encoding="utf-8"))
except Exception:
    _PROF={}
def _rx(sleutel,fallback,flags=re.I):
    return re.compile(_PROF.get(sleutel) or fallback,flags)
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
OWN=_rx('poort0_own',r'wordt beoordeeld|worden beoordeeld|beoordeeld door (de |onze |een )?(docent|trainer|opleider|assessor|examinator|examencommissie|begeleider|beoordelaar)|(docent|trainer|assessor|examinator|examencommissie|beoordelaar)\w*[^.]{0,80}beoordeel|onze examencommissie|eigen examencommissie|scriptie|afstudeeropdracht|eindwerkstuk|eindopdracht|eindgesprek|proeve van bekwaamheid|portfolio wordt|beoordelingscriteria|nakijk|feedback op je (opdracht|werk|verslag|essay)|leerverslag')
EXTERN=_rx('poort0_extern',r'\bCBR\b|\bCCV\b|\bTCVT\b|Oranje Kruis|\bIBKI\b|CerTech|\bSVPB\b|\bExTH\b|\bSEU\b|Prometric|Pearson VUE|extern examenbureau|externe examinator|externe examinering|onafhankelijk exameninstituut|onafhankelijk examenbureau|\bLSSA\b|Associatie voor Examinering|Scrum\.org|PeopleCert|APMG|\bEXIN\b|Nedcert|\bSVH\b|SVM ?NIVO|\bTCI\b|Exuive|staatsexamen',0)
DUUR=_rx('poort0_duur',r'\b(\d{1,2})\s*(maanden|jaar)\b|studiebelasting|\b\d{1,3}\s*(EC|ECTS|SBU)\b|lesdagen|opleidingsdagen|bijeenkomsten',0)
def get(u,t=15):
    return subprocess.run(["curl","-sL","--max-time",str(t),"-A",UA,u],capture_output=True,text=True).stdout
def clean(t):
    t=re.sub(r'(?is)<(script|style|nav|footer|svg|head)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?s)<[^>]+>',' ',t); t=html.unescape(t)
    return re.sub(r'[ \t\xa0]+',' ',t)
def urls_for(dom):
    us=set()
    for p in ["/sitemap.xml","/sitemap_index.xml","/wp-sitemap.xml"]:
        locs=re.findall(r'<loc>(.*?)</loc>',get("https://"+dom+p))
        for l in locs[:200]:
            if l.endswith('.xml'): us.update(re.findall(r'<loc>(.*?)</loc>',get(l))[:300])
            else: us.add(l)
        if us: break
    if not us:
        t=get("https://"+dom)
        for h in re.findall(r'href="([^"]+)"',t):
            if h.startswith('/'): h="https://"+dom+h
            if h.startswith('http') and dom in h: us.add(h)
    return us
kw=_rx('poort0_url_kw',r'opleiding|leergang|post-hbo|post-mbo|studiegids|examen|toets|reglement|diploma|certific|beoordel|faq|veelgestelde')
def work(item):
    naam,dom=item.split('|')
    try: us=urls_for(dom)
    except Exception: return None
    sel=sorted([u for u in us if kw.search(u)],key=lambda u:(-len(re.findall(r'examen|toets|reglement|studiegids|beoordel|diploma',u,re.I)),len(u)))[:5]
    own=[]; ext=[]; duur=False
    for u in sel:
        try: t=clean(get(u))
        except Exception: continue
        if DUUR.search(t): duur=True
        for s in re.split(r'(?<=[.!?])\s+|\n',t):
            s=' '.join(s.split())
            if not (30<len(s)<300): continue
            if EXTERN.search(s): ext.append((u,s))
            elif OWN.search(s): own.append((u,s))
    if ext: return f"NEE  {naam} [{dom}]\n     {ext[0][1][:220]}\n     {ext[0][0]}"
    if own and duur:
        o=sorted(own,key=lambda x:-len(x[1]))[:2]
        return f"JA?  {naam} [{dom}]\n"+"\n".join(f"     {s[:230]}\n     {u}" for u,s in o)
    return None
items=[l.strip() for l in open(sys.argv[1]) if l.strip()][int(sys.argv[2]):int(sys.argv[3])]
with cf.ThreadPoolExecutor(10) as ex:
    for r in ex.map(work,items):
        if r: print(r)
