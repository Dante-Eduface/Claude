import os, figs
from figs import page, OUT
F={}
A="<div class='arrow' style='font-size:24px'>→</div>"
def box(t,sub="",sty="",tsz=20): return f"<div class='card' style='padding:14px 16px;{sty}'><div class='t' style='font-size:{tsz}px;font-weight:700'>{t}</div>{f'<div style=font-size:16px;line-height:1.35;margin-top:5px;opacity:.85>{sub}</div>' if sub else ''}</div>"
DARK="background:#002333;border-color:#002333;color:#fff"
def q(t,lvl=0):
    cols=["#002333","#2c4a57","#5b7480"]; c=cols[min(lvl,2)]
    return f"<div class='card' style='background:{c};border-color:{c};color:#fff;padding:15px 22px'><div class='t' style='font-size:21px;font-weight:700'>{t}</div></div>"
def leaf(t,k="n"):
    st={"g":"background:#e6f4ee","b":"background:#e7eef0","a":"background:#fbf1e3","n":"background:#002333;color:#fff","x":"background:#f3f7f8;border:2px solid #e7eef0"}[k]
    return f"<div class='card' style='padding:12px 18px;border:none;{st}'><div style='font-size:19px;line-height:1.35'>{t}</div></div>"
def br(l,c,ind=48): return f"<div class='row' style='align-items:center;gap:14px;margin:9px 0 0 {ind}px'><div class='lab' style='width:52px;color:#5b7480;font-size:16px'>{l}</div><div style='flex:1'>{c}</div></div>"
def sbar(lbl,segs,scale,unit,total,note="",legend=None):
    s=""
    for m,c,t in segs:
        w=m*scale
        s+=f"<div style='width:{w}px;height:46px;background:{c};color:{'#002333' if c in ('#cdd9de','#e7eef0') else '#fff'};font-size:16px;display:flex;align-items:center;justify-content:center;border-right:2px solid #f3f7f8;overflow:hidden'>{t if w>=90 else ''}</div>"
    leg=legend if legend is not None else " · ".join(f"{t} {m:g}" for m,c,t in segs)
    return f"<div style='margin-top:18px'><div class='row' style='align-items:center;gap:14px'><div class='s' style='width:230px;color:#002333;font-weight:600;font-size:19px'>{lbl}</div><div class='row' style='gap:0;border-radius:6px;overflow:hidden'>{s}</div><div class='t' style='font-weight:700;white-space:nowrap'>{total} {unit}</div></div><div class='s' style='margin-left:244px;font-size:15px;margin-top:4px'>{leg}{(' · '+note) if note and legend is None else ''}</div></div>"
# ---------- 56 ----------
F['56-f1-gradebook-to-graded']=("From the Gradebook to a graded submission in Blackboard Ultra, schematic",
 "<h1>From the Gradebook to a graded submission</h1><div class='sub'>Schematic click path. Every route ends on the same Submissions page.</div>"
 "<div class='row' style='gap:8px;align-items:stretch'>"+A.join(f"<div style='flex:1'>{box(t,n,DARK if i==4 else '',19)}</div>" for i,(t,n) in enumerate([("Course → Gradebook","Grid view opens by default"),("Needs Grading icon under the assignment column","Opens Submissions, filtered to Needs Grading"),("Submissions page: select a student name","Grading Status filter, Students panel"),("Grading page","Bb Annotate, rubric, feedback panel; saves as you work"),("Post Grades","Students see grade and feedback only after this")]))+"</div>"
 "<div class='card' style='margin-top:22px;border:2px dashed #a9bcc4;background:transparent'><div class='lab' style='font-size:15px'>Other routes in</div><div class='t' style='font-size:20px;margin-top:6px'>Activity Stream alert · Grades in the left-hand navigation · assignment name → View submissions</div></div>")
F['56-f2-grading-page-zones']=("The three zones of the Blackboard Ultra grading page, schematic",
 "<h1>The grading page: three zones</h1><div class='sub'>Schematic, not a replica of Blackboard. Who is next, the submission, and the panel where scores and feedback live.</div>"
 "<div class='row' style='gap:14px;align-items:stretch'>"
 "<div class='card' style='width:250px'><div class='lab' style='font-size:14px'>Students panel</div><div class='chip' style='background:#e7eef0;color:#002333;font-size:15px;margin:10px 0'>Needs Grading</div>"+"".join(f"<div style='padding:10px;border-radius:8px;background:#f3f7f8;margin-top:8px;font-size:18px'>Student {i}{tag}</div>" for i,tag in [(1,"  <span style='background:#e6e0f4;color:#4a3a8a;border-radius:9999px;padding:2px 8px;font-size:13px'>accommodations</span>"),(2,"  <span style='background:#fbeceb;color:#b3261e;border-radius:9999px;padding:2px 8px;font-size:13px'>late</span>"),(3,"")])+"</div>"
 "<div class='card' style='flex:1.5'><div class='lab' style='font-size:14px'>Submission</div><div style='margin:10px 0;padding:8px 12px;background:#002333;color:#fff;border-radius:8px;font-size:16px'>Bb Annotate tools</div><div class='row' style='gap:6px;font-size:16px'><span style='border-bottom:3px solid #002333;font-weight:700;padding:4px 8px'>File 1</span><span style='padding:4px 8px;color:#5b7480'>File 2</span></div>"+"".join(f"<div style='height:12px;border-radius:6px;background:#e7eef0;margin-top:12px;width:{w}%'></div>" for w in (100,92,97,70,95,88,60))+"</div>"
 "<div class='card' style='flex:1'><div class='lab' style='font-size:14px'>Feedback and rubrics panel</div><div class='row' style='margin:10px 0;align-items:center;gap:10px'><div class='chip' style='background:#e7eef0;color:#002333;font-size:16px;padding:6px 14px'>Grade pill</div><div style='font-size:15px;color:#5b7480'>rubric icon</div></div>"+"".join(f"<div style='border:2px solid #e7eef0;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:16px'>Criterion {i}<span style='float:right;font-weight:700'>Level {l}</span></div>" for i,l in [(1,2),(2,1),(3,3)])+"<div style='margin-top:12px;font-size:16px;font-weight:700'>Overall feedback</div><div class='chip' style='background:#e7eef0;color:#002333;font-size:14px;padding:4px 12px;margin-top:4px'>Audio / Video</div><div style='margin-top:10px;font-size:15px;color:#5b7480'>Grader Notes (private)</div></div></div>"
 "<div class='foot' style='font-weight:700;color:#002333'>→ Scores and feedback save as you select them.</div>")
F['56-f3-feedback-channel']=("Decision tree: which feedback channel for which comment in Blackboard Ultra",
 "<h1>Which feedback channel for which comment?</h1><div class='sub'>Our suggestion, not Anthology’s rule.</div>"
 +q("1 · Is the comment about one passage?")+br("Yes",leaf("Bb Annotate comment or Content Library comment","g"))
 +"<div style='margin-top:14px'>"+q("2 · Is it about a criterion every student is scored on?",1)+"</div>"+br("Yes",leaf("Rubric criterion text box, only when the level descriptor does not already say it","b"))
 +"<div style='margin-top:14px'>"+q("3 · Does it need tone, nuance or more than about 60 seconds of explanation?",1)+"</div>"+br("Yes",leaf("Audio or video: 5 minutes maximum without a Video Studio license","a"))+br("No",leaf("Overall feedback: two or three sentences, one next step","x"))
 +"<div class='card' style='margin-top:20px;background:#002333;border-color:#002333;color:#fff'><div class='t' style='font-size:20px'><b>Always:</b> record why you changed a grade in Grader Notes. Students cannot see them.</div></div>")
F['56-f4-sixty-submissions']=("Example: grading 60 submissions by hand versus a faster Ultra workflow",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Grading 60 submissions</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Minutes per submission. Reading time stays at 6 minutes in both bars.</div>"
 +sbar("By hand: no rubric, typed comments",[(1.5,"#a9bcc4","find"),(6,"#cdd9de","read and mark up"),(5,"#5b7480","write comments"),(1.5,"#2c4a57","score, enter")],55,"min",14,"840 min, 14 h")
 +sbar("Faster Ultra workflow",[(0.5,"#a9bcc4","find"),(6,"#cdd9de","read, annotate"),(3,"#5b7480","rubric, notes"),(1.5,"#2c4a57","audio")],55,"min",11,"660 min + 40 setup + 5 posting = 11.75 h")
 +"<div class='card' style='margin-top:26px'><div class='t' style='font-size:20px'><b>About 2.25 hours saved on 60 papers, roughly 16 percent.</b> The reading is the floor. All numbers are example assumptions: time your first five papers.</div></div>")
steps5=[("1","Before anyone submits","Select Hide student names in assignment settings","only possible now","#e6f4ee","#007b54"),("2","Students submit","A banner tells them not to include a name","","#f3f7f8","#5b7480"),("3","You grade","Names show as Anonymous Student plus a number, in random order","a name inside the file defeats anonymity","#e7eef0","#002333"),("4","Post all grades","Names are revealed","cannot be undone","#fbeceb","#b3261e"),("5","After the reveal","You can still update posted grades and grade late submissions","","#f3f7f8","#5b7480")]
F['56-f5-anonymous-timeline']=("Anonymous grading in Blackboard Ultra from setup to reveal, schematic",
 "<h1>Anonymous grading, from setup to reveal</h1><div class='sub'>Schematic. Anonymity is set before submission and ends at one irreversible click.</div>"
 "<div class='row' style='gap:8px;align-items:stretch'>"+A.join(f"<div class='card' style='flex:1;padding:14px;background:{bg};border:none'><div class='num' style='width:34px;height:34px;font-size:17px'>{n}</div><div class='t' style='font-size:19px;font-weight:700;margin-top:10px'>{t}</div><div style='font-size:16px;line-height:1.4;margin-top:6px;color:#2c4a57'>{d}</div>{f'<div class=chip style=font-size:13px;padding:4px 10px;margin-top:10px;background:#fff;color:{fg}>{tag}</div>' if tag else ''}</div>" for n,t,d,tag,bg,fg in steps5)+"</div>"
 "<div class='foot' style='font-weight:700;color:#002333'>Plan any grade review before you post.</div>")
F['56-f6-cannot-see-grade']=("Decision tree: a student says they cannot see their grade in Blackboard Ultra",
 "<h1>“I can’t see my grade”</h1><div class='sub'>Four checks resolve most of these emails. The first is almost always the post step.</div>"
 +q("1 · Does the grade show Posted in your Gradebook?")+br("No",leaf("Post it: Post grade on the submission, or Post all grades on the item","g"))
 +"<div style='margin-top:12px'>"+q("2 · Is the assignment anonymous?",1)+"</div>"+br("Yes",leaf("Names and grades are released only after Post all grades. Check that you posted all.","b"))
 +"<div style='margin-top:12px'>"+q("3 · Is it a test with results timed to release later?",1)+"</div>"+br("Yes",leaf("Check Assessment results timing: after due date, after all grades are posted, or a set date","a"))
 +"<div style='margin-top:12px'>"+q("4 · Is it a parallel-graded item?",2)+"</div>"+br("Yes",leaf("The reconciler decides the final grade and posts it","x"))+br("No",leaf("Compare with the student view of the item, then ask your administrator","x")))
F['56-f7-two-systems']=("One assignment across Blackboard Ultra and Eduface, schematic",
 "<h1>One assignment, two systems</h1><div class='sub'>Blackboard keeps the submission and the gradebook. Eduface drafts in between. The instructor approves.</div>"
 "<div class='row' style='gap:8px;align-items:stretch'><div style='flex:1'>"+box("Blackboard Ultra","Students submit as usual","background:#e7eef0;border:none")+"</div>"+A+"<div style='flex:1.5'>"+box("Eduface","Paper Grader reads each submission, scores each criterion against your rubric with an explainable breakdown, annotates the text, flags uncertainty",DARK,20)+"</div>"+A+"<div style='flex:1.2'>"+box("You review and approve","Each suggestion, in the Eduface interface. Nothing returns until you approve.","background:#e6f4ee;border:none")+"</div>"+A+"<div style='flex:1'>"+box("Blackboard gradebook","Approved grade returns via LTI Grade Services","background:#e7eef0;border:none")+"</div></div>"
 "<div class='card' style='margin-top:22px'><div class='lab' style='font-size:14px'>Formative feedback on drafts · the Paper Grader’s formative feedback</div><div class='t' style='font-size:20px;margin-top:6px'>Style chosen by the instructor. Shown to the student only after approval, if you choose that setting.</div></div>")
F['56-f8-three-ways']=("Example: the 60-submission assignment, three ways, in total hours",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>The 60-submission assignment, three ways</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Total hours. Only the 3-minute review time comes from a pilot (Bath Spa University, June 2026: 2 to 3 minutes per submission).</div>"
 +sbar("By hand",[(14,"#a9bcc4","")],55,"h",14.0,legend="60 × 20 min")
 +sbar("Faster Ultra workflow",[(11.75,"#5b7480","")],55,"h",11.75,legend="from the previous figure: 660 min + 40 setup + 5 posting")
 +sbar("Ultra plus Eduface",[(2.0,"#a9bcc4","setup"),(2.7,"#2c4a57","54 reviews"),(1.2,"#5b7480","6 full reads"),(0.5,"#cdd9de","")],55,"h",6.4,legend="setup and calibration 2.0 · 54 routine reviews at 3 min 2.7 · 6 full reads at 12 min 1.2 · final checks 0.5")
 +"<div class='card' style='margin-top:26px'><div class='t' style='font-size:20px'>For one 60-paper class, setup is about a third of the Eduface bar. It amortizes over repeat use and extra sections.</div></div>")
# ---------- 58 ----------
def col(h,chips,sty,hs):
    return f"<div class='card' style='flex:1;padding:0;overflow:hidden;{sty}'><div style='padding:12px 16px;font-weight:700;font-size:19px;{hs}'>{h}</div><div style='padding:14px'>{chips}</div></div>"
def ch(t,sty="background:#e7eef0;color:#002333"): return f"<div class='chip' style='{sty};font-size:16px;padding:7px 14px;margin:0 6px 8px 0;border-radius:10px;display:flex'>{t}</div>"
F['58-f1-assessment-cycle']=("Where Blackboard AI touches the assessment cycle in Ultra, schematic",
 "<h1>Where Blackboard AI touches the cycle</h1><div class='sub'>Schematic. The documented AI sits before and after scoring. The middle step stays with the instructor.</div>"
 "<div class='row' style='gap:12px;align-items:stretch'>"+col("Build",ch("Rubric draft")+ch("Assignment prompt")+ch("Test questions and question banks")+"<div class='s' style='font-size:15px'>AI Design Assistant</div>","","background:#002333;color:#fff")
 +col("Practice",ch("AI Conversation: Socratic, Role-play")+ch("Pulse Quiz (AVA license)"),"","background:#002333;color:#fff")
 +"<div class='card' style='flex:1;padding:0;overflow:hidden;border:3px dashed #b26a00;background:#fbf1e3'><div style='padding:12px 16px;font-weight:700;font-size:19px;background:#b26a00;color:#fff'>Score the submission</div><div style='padding:18px;font-size:19px;font-weight:600'>No documented Blackboard AI feature</div></div>"
 +col("Word the feedback",ch("Summarize rubric feedback")+ch("Rewrite")+"<div class='s' style='font-size:15px'>AVA</div>","","background:#002333;color:#fff")+"</div>"
 "<div class='row' style='margin-top:18px;gap:14px'><div class='card' style='flex:3;background:#e7eef0;border:none'><div class='t' style='font-size:19px'><b>Blackboard AI helps here:</b> build, practice, word the feedback.</div></div><div class='card' style='flex:1;background:#fbf1e3;border:none'><div class='t' style='font-size:19px'><b>Instructor today.</b> Or a dedicated tool via LTI 1.3.</div></div></div>")
sm=[("Rate each criterion","Instructor judgment",0),("Add criterion comments","Instructor text",0),("Select Summarize rubric feedback","Inputs: criteria, selected levels, descriptions, your comments, existing feedback",1),("Suggested overall feedback","With an AI-generated banner",1),("Accept, reject or regenerate","Instructor decides",0),("Edit if needed","Instructor text",0),("Post grades","Students see it now",0)]
def sc(i,a,b,ai):
    return f"<div class='card' style='flex:1;padding:12px;{'background:#002333;border-color:#002333;color:#fff' if ai else ''}'><div class='num' style='width:30px;height:30px;font-size:15px;{'background:#fff;color:#002333' if ai else ''}'>{i}</div><div class='t' style='font-size:17px;font-weight:700;margin-top:8px'>{a}</div><div style='font-size:14px;line-height:1.35;margin-top:5px;{'color:rgba(255,255,255,.78)' if ai else 'color:#2c4a57'}'>{b}</div></div>"
F['58-f2-summarize-flow']=("The Summarize workflow in Flexible Grading, schematic",
 "<h1>The Summarize workflow</h1><div class='sub'>Schematic. The judgment about the work happens before the AI step, and the instructor decides what students see.</div>"
 "<div class='row' style='gap:5px;align-items:stretch'>"+"<div class='arrow' style='font-size:18px'>→</div>".join(sc(i+1,a,b,ai) for i,(a,b,ai) in enumerate(sm))+"</div>"
 "<div class='foot'>Dark cards: where the AI is involved.</div>")
mk=[("Jul 15, 2025","AVA announced as a free trial for current customers","#5b7480"),("Jun 30, 2026","Trial period ends","#b3261e"),("Jul 1, 2026","AVA becomes a premium capability that needs a specific license","#b3261e"),("Sep 23, 2026","Anthology restates the license requirement; Pulse Quiz, Virtual Assistant and Formative Feedback announced for AVA institutions","#5b7480"),("End of 2026","Test and stage access to AVA ends for institutions without a license","#5b7480")]
F['58-f3-ava-licensing']=("Blackboard AVA licensing timeline as documented, schematic, not to scale",
 "<h1>AVA licensing, as documented</h1><div class='sub'>Schematic, not to scale. The June 30, 2026 date belongs to AVA.</div>"
 "<div style='position:relative;height:6px;background:#cdd9de;border-radius:3px;margin:34px 0 0'></div><div class='row' style='gap:10px;margin-top:-20px'>"+"".join(f"<div style='flex:1'><div style='width:30px;height:30px;border-radius:50%;background:{c};border:4px solid #f3f7f8'></div><div class='t' style='font-size:20px;font-weight:700;margin-top:12px'>{d}</div><div style='font-size:16px;line-height:1.4;margin-top:6px;color:#2c4a57'>{t}</div></div>" for d,t,c in mk)+"</div>"
 "<div class='card' style='margin-top:26px;background:#e6f4ee;border:none'><div class='t' style='font-size:20px'><b>Socratic and Role-play AI Conversations:</b> core license.</div></div>"
 "<div class='card' style='margin-top:12px;background:#e7eef0;border:none'><div class='t' style='font-size:20px'><b>AI Design Assistant:</b> not tied to the AVA license in the pages we read.</div></div>")
sf=[("Student submits","In Ultra as usual",0),("Eduface receives the work","Via LTI 1.3",0),("Scores each criterion","Explainable breakdown, annotations, flagged uncertainty",1),("Instructor reviews","In the Eduface interface, opened from Blackboard. Blind or AI-visible mode.",0),("Instructor approves","",0),("Grade returns","To the Blackboard gradebook via LTI Grade Services",0)]
def sc2(i,a,b,k):
    return f"<div class='card' style='flex:1;padding:14px;{'background:#002333;border-color:#002333;color:#fff' if k else ''}'><div class='num' style='width:32px;height:32px;font-size:16px;{'background:#fff;color:#002333' if k else ''}'>{i}</div><div class='t' style='font-size:18px;font-weight:700;margin-top:8px'>{a}</div><div style='font-size:15px;line-height:1.4;margin-top:5px;{'color:rgba(255,255,255,.78)' if k else 'color:#2c4a57'}'>{b}</div></div>"
F['58-f4-eduface-beside-ultra']=("How Eduface sits next to Blackboard Ultra, schematic",
 "<h1>How Eduface sits next to Ultra</h1><div class='sub'>Schematic. Nothing reaches the student or the gradebook until the instructor approves.</div>"
 "<div class='row' style='gap:6px;align-items:stretch'>"+"<div class='arrow' style='font-size:20px'>→</div>".join(sc2(i+1,a,b,k) for i,(a,b,k) in enumerate(sf))+"</div>")
F['58-f5-which-ai']=("Decision tree: which AI do you need for this assessment in Blackboard Ultra",
 "<h1>Which AI do you need?</h1><div class='sub'>Start from the pain, not the product. Two of the exits are Blackboard’s own tools.</div>"
 +q("1 · Is the pain building the instrument (rubric, prompt, questions)?")+br("Yes",leaf("<b>Blackboard AI Design Assistant</b>","g"))
 +"<div style='margin-top:12px'>"+q("2 · Is the pain turning your own notes into comments?",1)+"</div>"+br("Yes",leaf("<b>AVA Summarize and Rewrite</b> (needs an AVA license)","g"))
 +"<div style='margin-top:12px'>"+q("3 · Do you need a score or draft feedback on the submission itself?",1)+"</div>"+br("No",leaf("Keep grading by hand with a clear rubric","x"))
 +"<div style='margin:12px 0 0 48px'>"+q("4 · Do several graders, a regulator or an accreditor need consistency and a record?",2)+"</div>"+br("Yes",leaf("<b>A dedicated tool via LTI 1.3, such as Eduface</b>","n"),96)+br("No",leaf("Pilot both on 25 to 40 submissions","a"),96))
F['58-f6-where-minutes-go']=("Example: where the minutes go on one 1,500-word essay",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Where the minutes go on one essay</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Illustrative numbers for a 1,500-word essay, not a measurement.</div>"
 +sbar("By hand in Flexible Grading",[(7,"#cdd9de","read"),(4,"#cdd9de","rate"),(9,"#2c4a57","write comments")],30,"min",20)
 +sbar("With Summarize and Rewrite",[(7,"#cdd9de","read"),(4,"#cdd9de","rate"),(4,"#2c4a57","short notes"),(2,"#2c4a57","accept")],30,"min",17)
 +"<div style='margin-top:18px'><div class='row' style='align-items:center;gap:14px'><div class='s' style='width:230px;color:#002333;font-weight:600;font-size:19px'>Dedicated tool</div><div style='width:420px;height:46px;border:3px dashed #a9bcc4;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#5b7480;font-size:18px'>your numbers: measure them in a pilot</div></div></div>"
 "<div class='card' style='margin-top:24px'><div class='t' style='font-size:20px'>A wording tool can only shrink the writing segment. Reading and rating stay with you, which is the part a scoring tool targets.</div></div>")
for k,(alt,body) in F.items():
    open(os.path.join(OUT,k+'.html'),'w').write(page(body)); open(os.path.join(OUT,k+'.alt'),'w').write(alt)
print(len(F))
