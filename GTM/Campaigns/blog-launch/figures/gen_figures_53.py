import os, figs
from figs import page, OUT
F={}
A="<div class='arrow' style='font-size:26px'>→</div>"
def band(lbl,dec,own,sty,tag=""):
    return f"<div class='card' style='display:flex;gap:24px;align-items:flex-start;{sty}'><div style='width:300px'><div class='t' style='font-weight:700'>{lbl}</div>{tag}</div><div style='flex:1.3'><div class='lab' style='font-size:15px;opacity:.7'>Decides</div><div class='s' style='font-size:19px;color:inherit;margin-top:4px'>{dec}</div></div><div style='flex:1'><div class='lab' style='font-size:15px;opacity:.7'>Owner</div><div class='s' style='font-size:19px;color:inherit;margin-top:4px'>{own}</div></div></div>"
F['53-f1-three-layers']=("Three layers of a college AI policy",
 "<h1>A college AI policy has three layers</h1><div class='sub'>Each layer works inside the one below it, and each has its own owner.</div>"
 +band("Layer 3 · Staff use of AI in teaching and grading","Which tools staff may use, what happens to student work, review of every AI-suggested grade, what students are told","Dean or head of quality, with privacy","background:#fbf1e3;border:3px dashed #b26a00;color:#002333","<div class='chip warn' style='font-size:15px;margin-top:10px;padding:5px 12px'>the layer many policies leave out</div>")
 +"<div style='height:14px'></div>"+band("Layer 2 · Course and syllabus statement","What students may do with AI, per assignment, and how they declare it","Program director and instructor","")
 +"<div style='height:14px'></div>"+band("Layer 1 · Institution policy","Governance, approved tools, data rules, integrity procedure, review date","Academic board or provost, with privacy and IT","background:#002333;border-color:#002333;color:#fff")
 +"<div class='s' style='margin-top:18px;font-weight:600'>↑ Each layer works inside the one below it.</div>")
def cell(t,kind):
    sty={"yes":"background:#e6f4ee;color:#007b54;font-weight:700","part":"background:#f3f7f8;color:#002333","no":"background:#f3f7f8;color:#5b7480;font-style:italic"}[kind]
    return f"<div style='flex:1;border-radius:8px;padding:14px 16px;font-size:19px;{sty}'>{t}</div>"
rows=[("Minnesota Duluth syllabus statements",[("links to conduct code","part"),("✓ three stances","yes"),("not on this page","no")]),
("Nebraska Omaha faculty principles",[("vetted enterprise tools","part"),("✓ statement per course","yes"),("✓ disclose, consent, human alternative","yes")]),
("Utah AI-in-grading guidelines",[("approved tools, contracts","part"),("disclose in syllabus","part"),("✓ full guidelines","yes")])]
grid="<div class='row' style='gap:10px;margin-bottom:10px'><div style='width:280px'></div>"+"".join(f"<div class='lab' style='flex:1;font-size:15px'>{h}</div>" for h in ["Layer 1 · Institution","Layer 2 · Syllabus","Layer 3 · Staff grading"])+"</div>"
grid+="".join("<div class='row' style='gap:10px;margin-top:10px;align-items:stretch'><div class='t' style='width:280px;font-size:20px;font-weight:700'>"+n+"</div>"+"".join(cell(t,k) for t,k in cs)+"</div>" for n,cs in rows)
F['53-f2-coverage-grid']=("What three published college AI policies cover, by layer",
 "<h1>What three published sources cover</h1><div class='sub'>Read October 2026. Three sources, not a survey of all colleges.</div>"
 f"<div class='card'>{grid}</div>"
 "<div class='card' style='margin-top:20px;display:flex;gap:28px;align-items:center'><div style=\"font-family:'League Spartan';font-size:52px;font-weight:700\">39%</div><div class='s'>of institutions had an AI acceptable use policy in the 2025 EDUCAUSE AI Landscape Study. <b style='color:#002333'>9%</b> said their privacy and security policies were adequate for AI.</div></div>")
parts=[("1","Stance","One sentence on the course’s position on AI","#002333"),("2","Per-assignment rule","Weekly quiz: No AI · Research paper: AI allowed with declaration · Final presentation: No AI, live Q&amp;A","#2c4a57"),
("3","Allowed uses","Brainstorming, grammar checks, explaining a concept","#2c4a57"),("4","Not allowed","Submitting AI-generated text as your own; AI-written code without a declaration","#b26a00"),
("5","How to declare","Tool, what you used it for, what you changed, attached to the submission","#5b7480"),("6","If unsure / consequences","Ask before you submit; undeclared use goes to the integrity procedure","#a9bcc4")]
rws="".join(f"<div class='row' style='gap:20px;margin-top:14px;align-items:stretch'><div style='width:10px;border-radius:6px;background:{c}'></div><div class='num' style='width:40px;height:40px;font-size:20px'>{n}</div><div class='t' style='width:270px;font-weight:700'>{a}</div><div class='t' style='flex:1;color:#2c4a57;font-size:22px'>{b}</div></div>" for n,a,b,c in parts)
F['53-f3-syllabus-anatomy']=("Anatomy of a syllabus AI statement",
 "<h1>Anatomy of a syllabus AI statement</h1><div class='sub'>Six parts. The per-assignment rule and the declaration are what students actually use.</div>"
 f"<div class='card' style='padding:28px 32px'>{rws}<div style='margin-top:22px;border-top:2px dashed #cdd9de;padding-top:16px' class='t'><b>One card per course, rules per assignment.</b></div></div>")
def q(t): return f"<div class='card' style='background:#002333;border-color:#002333;color:#fff;padding:18px 22px'><div class='t' style='font-size:22px;font-weight:700'>{t}</div></div>"
def out(t,cls): return f"<div class='card {cls}' style='padding:14px 20px;border:none'><div class='s' style='font-size:19px;color:#002333'>{t}</div></div>"
def br(l,c): return f"<div class='row' style='align-items:center;gap:14px;margin-top:10px;margin-left:48px'><div class='lab' style='width:56px;color:#5b7480'>{l}</div><div style='flex:1'>{c}</div></div>"
F['53-f4-statement-decision']=("Decision tree: which AI statement for this assignment",
 "<h1>Which AI statement for this assignment?</h1><div class='sub'>Supervision and purpose decide most cases.</div>"
 +q("1 · Is the work done under supervision (in class, exam room, live)?")
 +br("Yes",q("2 · Is the outcome about doing it without AI?").replace("background:#002333;border-color:#002333;color:#fff","background:#2c4a57;border-color:#2c4a57;color:#fff"))
 +"<div style='margin-left:118px'>"+br("Yes",out("<b>Template 2:</b> AI not allowed","neutral"))+br("No",out("<b>Template 3 or 4</b>, even when supervised","neutral"))+"</div>"
 +"<div style='margin-top:18px'>"+q("3 · Unsupervised: is using AI part of what the assignment teaches?")+"</div>"+br("Yes",out("<b>Template 4:</b> encouraged with conditions, graded on the process","neutral"))
 +"<div style='margin-top:18px'>"+q("4 · Can you see drafts, checkpoints or a short oral?")+"</div>"+br("Yes",out("<b>Template 3:</b> allowed with declaration","ok"))+br("No",out("<b>Redesign first:</b> add a checkpoint or an oral, then choose Template 3","warn"))
 +"<div class='card' style='margin-top:24px'><div class='t'><b>A “no AI” rule on unsupervised work is a request, not a control.</b></div></div>")
steps=[("Approved tool only","On the college list, under an agreement","You"),("Prepare the work","Identifiers removed if the tool requires it","You"),("AI drafts","Per-criterion scores and comments against the rubric","AI"),("Instructor reviews","Reads the work, checks the evidence, fixes what is wrong","You"),("Instructor approves","Only now does the grade reach the student","You"),("Record","Tool, version, what AI did, final grade","You"),("Student can ask","Explanation, full human review on request","Student")]
def sc(i,s):
    a,b,who=s; ai=who=="AI"
    st="background:#002333;border-color:#002333" if ai else ""
    return f"<div class='card' style='flex:1;padding:18px;{st}'><div class='row' style='justify-content:space-between;align-items:center'><div class='num' style='width:40px;height:40px;font-size:20px;{'background:#fff;color:#002333' if ai else ''}'>{i}</div><div class='chip' style='font-size:14px;padding:4px 10px;background:{'#fff' if ai else '#e7eef0'};color:#002333'>{ {'You':'Instructor','AI':'AI drafts','Student':'Student'}[who]}</div></div><div class='t' style='font-size:21px;font-weight:700;margin-top:12px;{'color:#fff' if ai else ''}'>{a}</div><div class='s' style='font-size:17px;margin-top:6px;{'color:rgba(255,255,255,.75)' if ai else ''}'>{b}</div></div>"
F['53-f5-grading-flow']=("AI-assisted grading under a college policy, seven steps",
 "<h1>AI-assisted grading under the staff clause</h1><div class='sub'>The AI drafts in step 3. Steps 4 to 7 keep the instructor responsible and the grade explainable.</div>"
 "<div class='row' style='gap:10px;align-items:stretch'>"+sc(1,steps[0])+A+sc(2,steps[1])+A+sc(3,steps[2])+A+sc(4,steps[3])+"</div>"
 "<div class='arrow' style='justify-content:flex-end;padding-right:120px;margin:8px 0'>↓</div>"
 "<div class='row' style='gap:10px;align-items:stretch;flex-direction:row-reverse;padding-left:260px'>"+sc(5,steps[4])+"<div class='arrow' style='font-size:26px'>←</div>"+sc(6,steps[5])+"<div class='arrow' style='font-size:26px'>←</div>"+sc(7,steps[6])+"</div>")
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
intakes={"Jan","Mar","May","Jul","Sep","Nov"}
def seg(lbl,n,sty): return f"<div style='flex:{n};border-radius:8px;padding:14px 16px;font-size:19px;font-weight:700;{sty}'>{lbl}</div>"
F['53-f6-intake-versions']=("Policy versions tied to intakes, example calendar",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Policy versions by intake</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Six start dates a year. The version in force at enrollment is the one a student is held to.</div>"
 "<div class='row' style='gap:8px'>"+seg("v1.0",4,"background:#e7eef0;color:#002333")+seg("v1.1 · tool list updated",4,"background:#2c4a57;color:#fff")+seg("v2.0 · staff clause added",4,"background:#002333;color:#fff")+"</div>"
 "<div class='row' style='gap:0;margin-top:14px'>"+"".join(f"<div style='flex:1;text-align:center'><div style='height:{'28px' if m in intakes else '12px'};border-left:3px solid {'#002333' if m in intakes else '#cdd9de'};width:0;margin:0 auto'></div><div class='s' style='font-size:17px;{'font-weight:700;color:#002333' if m in intakes else ''}'>{m}</div>{'<div class=s style=font-size:14px>intake</div>' if m in intakes else ''}</div>" for m in months)+"</div>"
 "<div class='card' style='margin-top:26px'><div class='t'><b>Transition rule:</b> students who started under v1.1 keep v1.1 rules for courses already under way.</div></div>")
ph=[("1–2","Inventory","Tools in use, existing rules, assignment types",2,"background:#e7eef0;color:#002333"),("3–5","Layer 1","Policy text, governance group, tool list and data rules approved",3,"background:#002333;color:#fff"),("6–8","Layer 2","Statement set, declaration, assignment mapping",3,"background:#2c4a57;color:#fff"),("9–11","Layer 3","Staff clause; calibration pilot on one course",3,"background:#fbf1e3;color:#002333"),("12–15","Roll out","Train all instructors incl. adjuncts; templates in course shell; publish; first intake on v1.0",4,"background:#5b7480;color:#fff")]
F['53-f7-rollout']=("One-term rollout of a college AI policy, example timeline",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>A one-term rollout</h1><span class='ex'>EXAMPLE · 15 WEEKS</span></div><div class='sub'>Tools and data rules come first. The staff clause is piloted before it applies everywhere.</div>"
 "<div class='row' style='gap:8px;align-items:stretch'>"+"".join(f"<div style='flex:{n};border-radius:10px;padding:18px;{sty}'><div class='lab' style='font-size:14px;opacity:.8'>Weeks {w}</div><div class='t' style='font-size:22px;font-weight:700;margin-top:6px'>{t}</div><div style='font-size:17px;line-height:1.4;margin-top:6px;opacity:.9'>{d}</div></div>" for w,t,d,n,sty in ph)+"</div>"
 "<div class='card' style='margin-top:24px;display:flex;gap:16px;align-items:center'><div style='width:22px;height:22px;transform:rotate(45deg);background:#002333'></div><div class='t'><b>Week 15:</b> set the review date for the end of the next term.</div></div>")
for k,(alt,body) in F.items():
    open(os.path.join(OUT,k+'.html'),'w').write(page(body)); open(os.path.join(OUT,k+'.alt'),'w').write(alt)
print(len(F))
