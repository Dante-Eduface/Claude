import os, figs
from figs import page, OUT
F={}
A="<div class='arrow' style='font-size:26px'>→</div>"
def dots(n,hi,cols=20,size=22,gap=6):
    return "<div style='display:grid;grid-template-columns:repeat(%d,%dpx);gap:%dpx'>"%(cols,size,gap)+"".join(f"<div style='width:{size}px;height:{size}px;border-radius:4px;background:{'#b26a00' if i>=n-hi else '#cdd9de'}'></div>" for i in range(n))+"</div>"
F['54-f1-two-rates']=("Turnitin's two published false positive rates, document and sentence level",
 "<h1>Two false positive rates, two questions</h1><div class='sub'>Turnitin publishes one rate for whole documents and one for highlighted sentences.</div>"
 "<div class='row'><div class='card' style='flex:1'><div class='lab'>Document level</div><div style='margin:18px 0'>"+dots(100,1,cols=20,size=20)+"</div><div class='t'><b>About 1 in 100</b> fully human-written documents may be scored above 20%.</div><div class='s' style='margin-top:8px;font-size:17px'>Applies only to documents with more than 20% AI writing detected.</div></div>"
 "<div class='card' style='flex:1'><div class='lab'>Sentence level</div><div style='margin:18px 0'>"+dots(100,4,cols=20,size=20)+"</div><div class='t'><b>About 4 in 100</b> highlighted sentences may be human-written.</div><div class='s' style='margin-top:8px;font-size:17px'>Most sit next to actual AI writing (Turnitin, May 2023).</div></div></div>"
 "<div class='foot'>Source: Turnitin’s own published figures. Not independently verified.</div>")
st=[("Submission","300+ words of prose; .docx, .pdf, .txt or .rtf"),("Filter","Only long-form prose counts; lists, code, bibliographies left out"),("Segments","Overlapping blocks of five to ten sentences"),("Sentence scores","Each sentence scored from 0 (human) to 1 (AI)"),("Document %","Average across segments")]
def sc(i,a,b,last=False):
    sty="background:#002333;border-color:#002333;color:#fff" if last else ""
    return f"<div class='card' style='flex:1;padding:18px;{sty}'><div class='num' style='width:40px;height:40px;font-size:20px;{'background:#fff;color:#002333' if last else ''}'>{i}</div><div class='t' style='font-size:21px;font-weight:700;margin-top:12px'>{a}</div><div style='font-size:17px;line-height:1.4;margin-top:6px;{'color:rgba(255,255,255,.75)' if last else 'color:#2c4a57'}'>{b}</div></div>"
F['54-f2-how-score-is-built']=("How Turnitin builds the AI writing percentage",
 "<h1>How the percentage is built</h1><div class='sub'>An average of sentence predictions over qualifying prose, not a count of highlighted text.</div>"
 "<div class='row' style='gap:10px;align-items:stretch'>"+A.join(sc(i+1,a,b,i==4) for i,(a,b) in enumerate(st))+"</div>")
def chip(v,lbl,dark,br):
    return f"<div style='flex:1;text-align:center'><div class='chip' style='font-size:34px;padding:16px 30px;{'background:#002333;color:#fff' if dark else 'background:#e7eef0;color:#2c4a57'}'>{v}</div><div class='s' style='margin-top:14px;font-size:18px;text-align:left'>{lbl}</div></div>"
F['54-f3-indicator-states']=("The four states of Turnitin's AI writing indicator",
 "<h1>Four indicator states</h1><div class='sub'>Three tell you nothing about authorship. The fourth tells you where to look.</div>"
 "<div class='row' style='align-items:flex-start'>"+chip("38%","<b>Processed.</b> Share of qualifying prose predicted to be AI.",True,"")+chip("*%","<b>Below 20%.</b> Marked with an asterisk: less reliable, more false positives.",False,"")+chip("- -","<b>Not processed.</b> Under 300 words, wrong file type, or submitted before detection existed.",False,"")+chip("!","<b>Error.</b> Processing failed; try again.",False,"")+"</div>"
 "<div class='row' style='margin-top:22px'><div style='flex:1;border-top:4px solid #002333;padding-top:10px' class='lab'>A reason to look, not a conclusion</div><div style='flex:3;border-top:4px solid #a9bcc4;padding-top:10px;color:#5b7480' class='lab'>Not a finding</div></div>")
def hb(lbl,v,col,note):
    return f"<div class='row' style='align-items:center;gap:16px;margin-top:14px'><div class='s' style='width:300px;color:#002333;font-weight:600'>{lbl}</div><div style='width:{max(v,1)/100*460}px;height:40px;border-radius:6px;background:{col}'></div><div class='t' style='font-weight:700'>{note}</div></div>"
F['54-f4-liang-bias']=("Detector false positives on non-native English writers, Liang et al. 2023",
 "<h1>Seven detectors, two groups of human writers</h1><div class='sub'>Liang et al., 2023. All essays were written by people.</div>"
 +hb("US eighth-grade essays (n = 88)",1,"#002333","near-perfect accuracy")+hb("TOEFL essays, non-native writers (n = 91)",61.22,"#b26a00","61.22% average false positive rate")+
 "<div class='row' style='margin-top:28px'>"+"".join(f"<div class='card' style='flex:1'><div style=\"font-family:'League Spartan';font-size:46px;font-weight:700\">{a}</div><div class='s' style='margin-top:6px'>{b}</div></div>" for a,b in [("97.80%","flagged by at least one detector"),("19.78%","flagged by all seven"),("11.77%","after ChatGPT enriched the vocabulary")])+"</div>"
 "<div class='foot'>Turnitin was not among the seven detectors tested. The study shows a mechanism, not a Turnitin error rate.</div>")
F['54-f5-false-positive-math']=("Example: false positives at a 1% rate across 10,000 papers",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>One term at a multi-campus college</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>10,000 human-written papers checked. Each square is 100 papers.</div>"
 "<div class='row' style='align-items:center;gap:40px'><div>"+dots(100,1,cols=10,size=44,gap=8)+"<div class='s' style='margin-top:14px'><span style='color:#b26a00;font-weight:700'>■</span> about 100 human-written papers flagged above 20%</div></div>"
 "<div style='flex:1'>"+"".join(f"<div class='card' style='margin-bottom:14px'><div class='lab' style='font-size:15px'>{a}</div><div style=\"font-family:'League Spartan';font-size:44px;font-weight:700;margin-top:4px\">{b}</div></div>" for a,b in [("Per term","about 100"),("Per year, three intakes","about 300"),("Per instructor, 400 papers a year","about 4")])+"</div></div>"
 "<div class='foot'>All numbers EXAMPLE, at Turnitin’s stated 1% document-level rate. Real rates for your students may be higher.</div>")
def sbar(lbl,tot,t,f,note):
    W=1000
    return f"<div style='margin-top:22px'><div class='row' style='justify-content:space-between'><div class='t' style='font-weight:700'>{lbl}</div><div class='t' style='font-weight:700;color:#8a5200'>{note}</div></div><div class='row' style='gap:0;margin-top:10px'><div style='width:{t/940*W}px;height:48px;background:#002333;border-radius:6px 0 0 6px;color:#fff;font-size:18px;display:flex;align-items:center;padding-left:14px'>{t} AI-written</div><div style='width:{f/940*W}px;height:48px;background:#b26a00;border-radius:0 6px 6px 0'></div><div class='s' style='margin-left:12px;align-self:center;font-size:18px'>{f} human-written · {tot} flags</div></div></div>"
F['54-f6-how-many-flags-wrong']=("Example: share of AI flags that are wrong when misuse is common or rare",
 "<div class='row' style='justify-content:space-between;align-items:center'><h1>Of every flag, how many are wrong?</h1><span class='ex'>EXAMPLE</span></div><div class='sub'>Same detector, same 1% rate, 10,000 papers. Only the share of students misusing AI changes.</div>"
 +sbar("Misuse common (10% of papers)",940,850,90,"about 1 in 10 flags wrong")+sbar("Misuse rare (2% of papers)",268,170,98,"about 1 in 3 flags wrong")+
 "<div class='foot'>All numbers EXAMPLE. The 85% catch rate is an assumption.</div>")
st2=[("Check the rules","Was AI allowed, at what level?",False),("Read the indicator","Number, asterisk, grey, error",True),("Read the paper","Compare with the student’s earlier work",False),("Gather evidence","Drafts, version history, citation trail",False),("Talk to the student","Open questions about their own paper",False),("Decide and record","On the evidence; the score is a footnote",False)]
def sc2(i,a,b,score):
    tag="<div class='chip warn' style='font-size:14px;padding:4px 10px;margin-top:10px'>score used here</div>" if score else ""
    return f"<div class='card' style='flex:1;padding:16px'><div class='num' style='width:38px;height:38px;font-size:18px'>{i}</div><div class='t' style='font-size:20px;font-weight:700;margin-top:10px'>{a}</div><div style='font-size:16px;line-height:1.4;margin-top:6px;color:#2c4a57'>{b}</div>{tag}</div>"
F['54-f7-score-to-decision']=("Six steps from a Turnitin AI score to a decision",
 "<h1>From a score to a decision</h1><div class='sub'>The score enters at step 2 and leaves at step 3. Every later step runs on evidence you can show the student.</div>"
 "<div class='row' style='gap:8px;align-items:stretch'>"+"<div class='arrow' style='font-size:22px'>→</div>".join(sc2(i+1,a,b,s) for i,(a,b,s) in enumerate(st2))+"</div>")
rungs=[("Cannot explain or defend the paper’s own argument in an oral check","#002333","#fff"),("Citations that do not exist or do not say what the paper claims","#2c4a57","#fff"),("No drafts or version history for a long paper","#5b7480","#fff"),("Style differs from earlier work","#cdd9de","#002333"),("AI score alone (Turnitin: not a sole basis)","#e7eef0","#5b7480")]
F['54-f8-evidence-ladder']=("Evidence ladder for suspected AI misuse, weakest to strongest",
 "<h1>From weakest to strongest evidence</h1><div class='sub'>Every rung is a judgement. None is proof on its own.</div>"
 "<div class='row' style='align-items:stretch;gap:24px'><div style='flex:1'>"+"".join(f"<div class='row' style='margin-top:10px;gap:14px;align-items:center'><div class='lab' style='width:30px;color:#5b7480'>{5-i}</div><div style='flex:1;border-radius:10px;padding:18px 22px;background:{bg};color:{c};font-size:21px;font-weight:600;margin-left:{i*0}px'>{t}</div></div>" for i,(t,bg,c) in enumerate(rungs))+"</div>"
 "<div style='width:230px;display:flex;flex-direction:column'><div style='height:242px;border:3px solid #002333;border-left:none;border-radius:0 12px 12px 0;margin-top:10px;display:flex;align-items:center;padding-left:18px'><div class='t' style='font-size:20px;font-weight:700'>Combine two or more before you refer a case</div></div></div></div>")
for k,(alt,body) in F.items():
    open(os.path.join(OUT,k+'.html'),'w').write(page(body)); open(os.path.join(OUT,k+'.alt'),'w').write(alt)
print(len(F))
