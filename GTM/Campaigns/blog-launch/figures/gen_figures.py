import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fig')
FONTS=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts')
CSS="""
@font-face{font-family:Inter;src:url('file://FONTDIR/Inter-var.woff2') format('woff2');font-weight:100 900}
@font-face{font-family:'League Spartan';src:url('file://FONTDIR/LeagueSpartan-Bold.ttf');font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;font-family:Inter,sans-serif;color:#002333}
#fig{width:1200px;background:#f3f7f8;border-radius:20px;padding:56px}
h1{font-family:'League Spartan';font-weight:700;font-size:40px;line-height:1.15;margin-bottom:8px}
.sub{font-size:22px;color:#2c4a57;margin-bottom:40px;line-height:1.4}
.card{background:#fff;border:2px solid #e7eef0;border-radius:12px;padding:24px}
.lab{font-size:18px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.t{font-size:24px;line-height:1.35}
.s{font-size:20px;line-height:1.4;color:#2c4a57}
.ex{display:inline-block;font-size:16px;font-weight:700;letter-spacing:.1em;color:#5b7480;border:2px solid #cdd9de;border-radius:6px;padding:4px 10px}
.foot{margin-top:32px;font-size:20px;color:#2c4a57;line-height:1.4}
.row{display:flex;gap:24px}
.num{width:48px;height:48px;border-radius:50%;background:#002333;color:#fff;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center;flex:none}
.ok{background:#e6f4ee;color:#007b54}.warn{background:#fbf1e3;color:#8a5200}.bad{background:#fbeceb;color:#b3261e}
.neutral{background:#e7eef0;color:#002333}
.chip{display:inline-flex;align-items:center;gap:10px;border-radius:9999px;padding:8px 18px;font-weight:700;font-size:20px}
.arrow{color:#5b7480;font-size:32px;display:flex;align-items:center;justify-content:center}
""".replace("FONTDIR",FONTS)
def page(body): return "<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body><div id='fig'>"+body+"</div></body></html>"
F={}
# ---------- Blog 51 ----------
def col(cls,icon,title,items):
    li="".join(f"<div class='card' style='padding:18px 20px;margin-top:14px'><div class='t' style='font-size:22px'>{i}</div></div>" for i in items)
    return f"<div style='flex:1'><div class='chip {cls}'>{icon} {title}</div>{li}</div>"
F['51-f1-reliable-vs-drifts']=("Where ChatGPT is reliable, and where it drifts",
 "<h1>Where ChatGPT is reliable, and where it drifts</h1><div class='sub'>Grading tasks, ordered from reading text to making a judgement.</div>"
 "<div class='row'>"+col('ok','✓','Reliable',["Summarize the thesis","Find passages for a descriptor","Check citation format","Draft feedback from your notes"])
 +col('warn','!','Needs checking',["Score a single criterion","Name the weakest section","Suggest a level between two descriptors"])
 +col('bad','×','Drifts',["Overall grade on a fluent but weak essay","Same grade on a second run","Weighting criteria the way your rubric does","Quotes copied exactly"])+"</div>"
 "<div style='margin-top:36px;height:14px;border-radius:9999px;background:linear-gradient(90deg,#cdd9de,#002333)'></div>"
 "<div class='row' style='justify-content:space-between;margin-top:12px'><div class='s'>Reading text</div><div class='s' style='font-weight:700;color:#002333'>The further right, the more you review →</div></div>")
steps=[("Check the account","Approved for student data? Identifiers removed?","You"),("Turn the rubric into a prompt","Criteria, levels, evidence rule, fixed format","You"),("Calibrate","3 to 5 essays you already graded","You"),("Grade one essay per fresh chat","Same prompt every time","ChatGPT drafts"),("Test consistency","3 runs on a sample","You"),("Review and record","You decide; the gradebook holds your grade","You")]
def stepcard(i,s):
    a,b,who=s; gpt=who!="You"
    style="background:#002333;border-color:#002333" if gpt else ""
    tc="color:#fff" if gpt else ""
    chip=f"<div class='chip' style='background:{'#fff' if gpt else '#e7eef0'};color:#002333;font-size:16px;padding:6px 14px'>{who}</div>"
    n=f"<div class='num' style='{'background:#fff;color:#002333' if gpt else ''}'>{i}</div>"
    return f"<div class='card' style='flex:1;{style}'><div class='row' style='justify-content:space-between;align-items:center'>{n}{chip}</div><div class='t' style='font-weight:700;margin-top:18px;{tc}'>{a}</div><div class='s' style='margin-top:8px;{'color:rgba(255,255,255,.75)' if gpt else ''}'>{b}</div></div>"
F['51-f2-six-steps']=("Six steps to grade essays with ChatGPT",
 "<h1>Grading essays with ChatGPT: six steps</h1><div class='sub'>ChatGPT drafts in one step. The instructor controls the other five.</div>"
 "<div class='row'>"+stepcard(1,steps[0])+"<div class='arrow'>→</div>"+stepcard(2,steps[1])+"<div class='arrow'>→</div>"+stepcard(3,steps[2])+"</div>"
 "<div class='arrow' style='justify-content:flex-end;padding-right:150px;margin:10px 0'>↓</div>"
 "<div class='row' style='flex-direction:row-reverse'>"+stepcard(4,steps[3])+"<div class='arrow'>←</div>"+stepcard(5,steps[4])+"<div class='arrow'>←</div>"+stepcard(6,steps[5])+"</div>")
parts=[("Setup","Role","“You are a careful second reader, not the final grader.”","#002333"),("Setup","Context","Assignment prompt and learning outcomes","#002333"),
("Standard","Rubric","Criteria, weights, descriptors for every level","#2c4a57"),("Standard","Scale","Points per criterion and grade boundaries","#2c4a57"),
("Checks","Evidence rule","“Quote 1 to 3 passages per criterion, word for word.”","#5b7480"),("Checks","No-invent rule","“Do not invent quotes, sources or facts.”","#5b7480"),
("Checks","Tie-break rule","“Between two levels, choose the lower and explain.”","#5b7480"),("Format","Output format","Fixed table plus TOTAL, WEAKEST CRITERION, CHECK THESE","#a9bcc4")]
rows="".join(f"<div class='row' style='align-items:stretch;gap:20px;margin-top:12px'><div style='width:10px;border-radius:6px;background:{c}'></div><div style='width:120px' class='lab' >{g}</div><div style='width:220px' class='t'><b>{n}</b></div><div class='t' style='flex:1;color:#2c4a57'>{x}</div></div>" for g,n,x,c in parts)
F['51-f3-prompt-anatomy']=("Anatomy of a ChatGPT grading prompt",
 "<h1>Anatomy of a grading prompt</h1><div class='sub'>Eight parts. The evidence and no-invent rules are what let you check the output.</div>"
 f"<div class='card' style='padding:28px 32px'>{rows}<div style='margin-top:24px;border-top:2px dashed #cdd9de;padding-top:18px' class='t'><b>Last: the essay</b> <span style='color:#2c4a57'>with the student’s name and ID removed</span></div></div>")
F['51-f4-annotated-output']=("Annotated example of a structured ChatGPT grading output",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Reading the output: what to check</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Structured output turns review into checking.</div>"
 "<div class='row' style='align-items:flex-start'><div class='card' style='flex:1.5;padding:0;overflow:hidden'>"
 "<div class='row' style='background:#002333;color:#fff;padding:16px 20px;gap:12px;font-weight:700;font-size:18px'><div style='width:150px'>CRITERION</div><div style='width:100px'>POINTS</div><div style='flex:1'>EVIDENCE</div><div style='width:110px'>CONF.</div></div>"
 "<div class='row' style='padding:18px 20px;gap:12px;font-size:20px'><div style='width:150px;font-weight:700'>Thesis</div><div style='width:100px'>16 / 20</div><div style='flex:1'>“Social media changes how teens form friendships…”</div><div style='width:110px'>High</div></div>"
 "<div class='row warn' style='padding:18px 20px;gap:12px;font-size:20px;color:#002333'><div style='width:150px;font-weight:700'>Use of evidence <span style='color:#8a5200'>①</span></div><div style='width:100px'>12 / 25</div><div style='flex:1'>“Studies show social media is bad for teens”</div><div style='width:110px'>Medium <span style='color:#8a5200'>②</span></div></div>"
 "<div class='row' style='padding:18px 20px;gap:12px;font-size:20px;background:#f3f7f8'><div style='width:150px;font-weight:700'>Organization <span style='color:#5b7480'>③</span></div><div style='width:100px'>9 / 15</div><div style='flex:1;color:#5b7480;font-style:italic'>No evidence found</div><div style='width:110px'>Low</div></div></div>"
 "<div style='flex:1'>"
 "<div class='card' style='margin-bottom:14px'><div class='lab' style='color:#8a5200'>① Search the quote</div><div class='s' style='margin-top:6px'>Ctrl+F it in the essay. Found? Keep. Not found? Discard the whole row.</div></div>"
 "<div class='card' style='margin-bottom:14px'><div class='lab' style='color:#8a5200'>② Read the confidence</div><div class='s' style='margin-top:6px'>Medium or Low means you read this criterion yourself.</div></div>"
 "<div class='card'><div class='lab' style='color:#5b7480'>③ An honest gap</div><div class='s' style='margin-top:6px'>“No evidence found” is the prompt working, not failing.</div></div></div></div>")
def bar(label,val,color,note=""):
    w=val/10*560
    return f"<div class='row' style='align-items:center;gap:16px;margin-top:12px'><div class='s' style='width:130px;color:#002333;font-weight:600'>{label}</div><div style='width:560px;background:#e7eef0;border-radius:6px;height:40px;position:relative'><div style='width:{w}px;height:40px;border-radius:6px;background:{color}'></div><div style='position:absolute;left:{5.5/10*560}px;top:-6px;bottom:-6px;border-left:2px dashed #b3261e'></div></div><div class='t' style='font-weight:700;width:56px'>{val}</div><div class='s' style='flex:1;font-size:18px'>{note}</div></div>"
F['51-f5-test-results']=("ChatGPT against the lecturer's grade on two papers",
 "<h1>ChatGPT against the lecturer’s grade</h1><div class='sub'>Dutch 10-point scale. The dashed line is the pass mark (5.5).</div>"
 "<div class='row' style='align-items:flex-start'><div style='flex:1'>"
 "<div class='lab' style='margin-top:4px'>Psychology case study</div>"+bar("Lecturer",6.5,"#002333")+bar("ChatGPT",8.1,"#a9bcc4","praised the weakest section")+
 "<div class='lab' style='margin-top:36px'>Constitutional law essay</div>"+bar("Lecturer",4.4,"#002333","below a pass")+bar("ChatGPT",7.1,"#a9bcc4")+bar("Eduface",5.5,"#5b7480")+
 "</div></div><div class='card' style='margin-top:32px;display:flex;gap:24px;align-items:center'><div style=\"font-family:'League Spartan';font-size:56px;font-weight:700\">0.9</div><div class='s'>points from the lecturer, on average, across five psychology papers. The average looked fine; the misses were on the weakest papers.</div></div>"
 "<div class='foot'>Two students, eight tools, six papers with known lecturer grades. Directional, not a ranking.</div>")
runs=[[16,18,19,12,8,73],[17,21,22,12,8,80],[16,17,20,13,9,75]]
crit=[("Thesis",20),("Evidence",25),("Analysis",30),("Organization",15),("Mechanics",10)]
def runcard(i,r):
    rows="".join(f"<div class='row {'warn' if c in ('Evidence','Analysis') else ''}' style='justify-content:space-between;padding:8px 12px;border-radius:6px;font-size:20px;color:#002333'><span>{c}</span><span><b>{v}</b> / {m}</span></div>" for (c,m),v in zip(crit,r))
    return f"<div class='card' style='flex:1'><div class='lab'>Run {i}</div><div style='margin-top:12px'>{rows}</div><div class='row' style='justify-content:space-between;margin-top:14px;border-top:2px solid #e7eef0;padding-top:12px'><span class='t' style='font-weight:700'>TOTAL</span><span style=\"font-family:'League Spartan';font-size:36px;font-weight:700\">{r[5]}</span></div></div>"
F['51-f6-three-runs']=("Same essay graded three times by ChatGPT",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Same essay, three runs, three grades</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Same prompt, fresh chat each time.</div>"
 "<div class='row'>"+"".join(runcard(i+1,r) for i,r in enumerate(runs))+"</div>"
 "<div class='card' style='margin-top:24px'><div class='lab'>Spread per criterion</div><div class='row' style='margin-top:12px;flex-wrap:wrap;gap:12px'>"
 +"".join(f"<div class='chip {'warn' if c in ('Evidence','Analysis') else ''}' style='{'' if c in ('Evidence','Analysis') else 'background:#e7eef0;color:#002333'}'>{c} {s}</div>" for c,s in [("Thesis",1),("Evidence",4),("Analysis",3),("Organization",1),("Mechanics",1)])
 +"</div><div class='t' style='margin-top:16px'><b>Total spread: 7 points</b>, from a C to a B-. The spread sits in the criteria that need judgement.</div></div>")
def node(t,s="",style=""): return f"<div class='card' style='flex:1;padding:16px 18px;{style}'><div class='t' style='font-size:21px;font-weight:700'>{t}</div>{f'<div class=s style=font-size:17px;margin-top:4px>{s}</div>' if s else ''}</div>"
A="<div class='arrow' style='font-size:26px'>→</div>"
F['51-f7-data-flow']=("Where a student essay goes when you paste it into ChatGPT",
 "<h1>Where an essay goes when you paste it</h1><div class='sub'>The plan decides whether an agreement covers the essay.</div>"
 "<div class='lab'>Personal account (Free, Plus, Pro)</div><div class='row' style='gap:10px;margin-top:12px;align-items:stretch'>"
 +node("Essay in your LMS")+f"<div class='arrow' style='flex-direction:column;font-size:16px;color:#b3261e;font-weight:700;width:120px;text-align:center'>leaves college control<br><span style='font-size:26px'>→</span></div>"+node("Pasted under your personal login")+A+node("Kept in your chat history")+A+node("Training on by default","unless you opt out",style="border-color:#b3261e")+"</div>"
 "<div class='s' style='margin-top:10px'><span style='color:#b3261e;font-weight:700'>×</span> No agreement between your college and OpenAI.</div>"
 "<div class='lab' style='margin-top:36px'>College-licensed plan (Edu, Enterprise, Business)</div><div class='row' style='gap:10px;margin-top:12px;align-items:stretch'>"
 +node("Essay in your LMS")+A+node("Pasted into a workspace your college administers")+A+node("No training by default","per OpenAI")+A+node("Retention and access","set by your college’s agreement",style="border-color:#007b54")+"</div>"
 "<div class='s' style='margin-top:10px'><span style='color:#007b54;font-weight:700'>✓</span> Covered by an agreement your college signed.</div>"
 "<div class='card' style='margin-top:32px;background:#002333;border-color:#002333;color:#fff'><div class='t'><b>Both lanes end the same way:</b> the grade still has to be copied into your gradebook by hand.</div></div>")
def ac(lbl,val,sty=""): return f"<div class='card' style='flex:1;text-align:center;{sty}'><div class='lab' style='font-size:16px;min-height:44px'>{lbl}</div><div style=\"font-family:'League Spartan';font-weight:700;font-size:88px;margin-top:10px\">{val}</div></div>"
F['51-f8-anchoring']=("Anchoring: how an AI suggestion pulls an instructor's grade",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Anchoring, in one essay</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>When the suggestion comes first, it becomes the starting point.</div>"
 "<div class='row' style='align-items:stretch'>"+ac("1 · Your first read, no AI",72)+A+ac("2 · ChatGPT’s suggestion",84,"background:#fbf1e3;border-color:#f0d7ae")+A+ac("3 · Your grade after seeing it",78)+"</div>"
 "<div class='chip warn' style='margin-top:24px'>Pulled 6 points toward the suggestion</div>"
 "<div class='card' style='margin-top:24px'><div class='t'><b>The fix:</b> grade first, then open the output. Do it for the borderline essays, the likely fails and one at random in every batch.</div></div>")
def q(t): return f"<div class='card' style='background:#002333;border-color:#002333;color:#fff;padding:18px 22px'><div class='t' style='font-size:22px;font-weight:700'>{t}</div></div>"
def out(t,cls,icon): return f"<div class='card {cls}' style='padding:16px 20px;border:none'><div class='s' style='font-size:19px;color:#002333'><b>{icon}</b> {t}</div></div>"
def br(lbl,content): return f"<div class='row' style='align-items:center;gap:14px;margin-top:10px;margin-left:48px'><div class='lab' style='width:56px;color:#5b7480'>{lbl}</div><div style='flex:1'>{content}</div></div>"
F['51-f9-decision-tree']=("Decision tree: should you use ChatGPT to grade this assignment?",
 "<h1>Should you use ChatGPT for this assignment?</h1><div class='sub'>Four questions. Stakes and data decide most cases.</div>"
 +q("1 · Does the result count toward a recorded grade?")+br("No",out("Formative comments: Prompt 2 on de-identified drafts, approved account","ok","✓"))
 +"<div style='margin-top:18px'>"+q("2 · Has your college approved this ChatGPT plan for student work?")+"</div>"+br("No",out("Keep essays out. Use ChatGPT for rubric drafting and model answers only","bad","×"))
 +"<div style='margin-top:18px'>"+q("3 · More than about 30 essays, or more than one grader or section?")+"</div>"+br("Yes",out("A dedicated grading tool earns its place: calibration, audit trail, gradebook return","neutral","→"))
 +"<div style='margin-top:18px'>"+q("4 · Did your consistency test pass your thresholds?")+"</div>"+br("Yes",out("Prompt 1, one essay per chat, full review","ok","✓"))+br("No",out("Grade by hand this term; fix the rubric before the next","warn","!")))
def tb(label,h,maxh,parts,note):
    w=h/maxh*620
    return f"<div class='row' style='align-items:center;gap:16px;margin-top:14px'><div class='s' style='width:190px;color:#002333;font-weight:600'>{label}</div><div style='width:{w}px;height:40px;border-radius:6px;background:{parts}'></div><div class='t' style='font-weight:700'>{h} h</div></div><div class='s' style='margin-left:206px;font-size:16px;margin-top:4px'>{note}</div>"
F['51-f10-time-comparison']=("Time to grade 30 and 300 essays: by hand, ChatGPT workflow, dedicated tool",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>What it costs in hours</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Example assumptions, except the 3-minute review time, which comes from the June 2026 Bath Spa University pilot.</div>"
 "<div class='lab'>30 essays, one class</div>"+tb("By hand",10,100,"#a9bcc4","30 × 20 min")+tb("ChatGPT workflow",6.75,100,"#5b7480","setup, calibration, consistency test, 10 min per essay")+tb("Dedicated tool",5.25,100,"#002333","setup 2 h, 25 × 3 min review, 5 full reads, 1 h return")+
 "<div class='lab' style='margin-top:36px'>300 essays, six sections</div>"+tb("By hand",100,100,"#a9bcc4","300 × 20 min")+tb("ChatGPT workflow",52,100,"#5b7480","same setup, 300 × 10 min")+tb("Dedicated tool",22.5,100,"#002333","setup 2 h, 270 × 3 min review, 30 full reads, 1 h return")+
 "<div class='card' style='margin-top:28px'><div class='t'><b>At 30 essays the gap is about 1.5 hours. At 300 it is about 30.</b></div></div>")
# ---------- Blog 52 ----------
def box(t,s="",sty=""): return f"<div class='card' style='padding:18px 22px;{sty}'><div class='t' style='font-size:22px;font-weight:700'>{t}</div>{f'<div class=s style=font-size:18px;margin-top:4px>{s}</div>' if s else ''}</div>"
D="<div class='arrow' style='font-size:26px;margin:6px 0'>↓</div>"
F['52-f1-cba-loop']=("The competency-based assessment loop",
 "<h1>Competency-based assessment is a loop</h1><div class='sub'>The feedback after “not yet” is part of the assessment, not an extra.</div>"
 "<div class='row' style='gap:12px;align-items:stretch'>"+box("1 · Competency","What the student can do","flex:1")+A+box("2 · Criteria","A rubric with levels","flex:1")+A+box("3 · Evidence task","Project, task, knowledge check, portfolio","flex:1")+"</div>"
 "<div class='arrow' style='justify-content:flex-end;padding-right:150px;font-size:26px;margin:8px 0'>↓</div>"
 "<div class='card' style='background:#002333;border-color:#002333;color:#fff;padding:22px 26px'><div class='t' style='font-weight:700'>4 · Evaluation against each criterion</div><div style='font-size:19px;color:rgba(255,255,255,.75);margin-top:4px'>The evaluator decides</div></div>"
 "<div class='row' style='margin-top:20px;align-items:stretch'>"
 "<div style='flex:1'>"+box("✓ Competent","Recorded, the student moves on","background:#e6f4ee;border:none;color:#007b54;height:100%")+"</div>"
 "<div style='flex:1.6'><div class='row' style='gap:12px;align-items:stretch'>"+box("! Not yet","Criterion-level feedback","flex:1;background:#fbf1e3;border:none;color:#8a5200")+A+box("Student revises and resubmits","","flex:1")+"</div>"
 "<div class='s' style='margin-top:12px;font-weight:700;color:#002333'>↺ back to step 4: evaluated again against each criterion</div></div></div>")
seq=[("Attempt 1 submitted","Student"),("AI drafts a level and comment per criterion, with highlighted passages","AI"),("Evaluator edits one comment, approves “Not yet”","Evaluator"),("Criterion-level feedback the same day","Student"),("Attempt 2 submitted","Student"),("AI drafts again","AI"),("Evaluator changes criterion 3 from Exceeds to Competent","Evaluator"),("Evaluator signs off the competency","Evaluator")]
def seqrow(i,t,who):
    sty={"AI":"background:#e7eef0;color:#002333","Evaluator":"background:#002333;color:#fff","Student":"background:#fff;color:#002333;border:2px solid #cdd9de"}[who]
    return f"<div class='row' style='align-items:center;gap:18px;margin-top:12px'><div class='num'>{i}</div><div class='chip' style='width:150px;justify-content:center;font-size:17px;{sty}'>{who}</div><div class='card' style='flex:1;padding:14px 18px'><div class='t' style='font-size:21px'>{t}</div></div></div>"
F['52-f2-two-attempts']=("Two attempts at one competency with AI-assisted evaluation",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Two attempts, one competency</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>The AI drafts each evaluation. The evaluator decides each criterion and signs off.</div>"
 +"".join(seqrow(i+1,t,w) for i,(t,w) in enumerate(seq)))
for k,(alt,body) in F.items():
    open(os.path.join(OUT,k+'.html'),'w').write(page(body))
    open(os.path.join(OUT,k+'.alt'),'w').write(alt)
print(len(F),"figures")
