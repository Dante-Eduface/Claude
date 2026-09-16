#!/usr/bin/env python3
"""Eduface Meta ads — final. All-navy, real logo, no buttons, sources on claims.
9 ads, each with 3 dedicated layouts: 1080x1080 (1:1), 1080x1920 (9:16, fills full height), 1200x628 (1.91:1).
Source: Learnosity survey of 502 UK teachers, 2025."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
HERE=os.path.dirname(os.path.abspath(__file__)); A=os.path.join(HERE,"assets"); FD=os.path.join(HERE,"fonts")

NAVY=(0,35,51); NAVY2=(10,52,69); GREEN=(0,224,117); TEAL=(0,103,84); TEAL2=(0,76,76)
WHITE=(255,255,255); LIGHT=(238,243,246); INK=(0,35,51); GREY=(150,170,178); GREYL=(120,140,148); RED=(235,86,86)
SRC="Source: Learnosity survey of 502 UK teachers, 2025"

_F={}
def head(s):
    k=("h",s)
    if k not in _F:
        f=ImageFont.truetype(os.path.join(FD,"LeagueSpartan-Bold.ttf"),s)
        try: f.set_variation_by_axes([700])
        except: pass
        _F[k]=f
    return _F[k]
def body(s,b=False):
    k=("b",s,b)
    if k not in _F: _F[k]=ImageFont.truetype(os.path.join(FD,"Inter-Regular.ttf"),s)
    return _F[k]

LOGO_W=Image.open(os.path.join(A,"logo_white.png")).convert("RGBA")
CRIT=Image.open(os.path.join(A,"product_criteria.png")).convert("RGB")
GRAD=Image.open(os.path.join(A,"product_grading.png")).convert("RGB")

def base(W,H,c=NAVY): img=Image.new("RGBA",(W,H),c+(255,)); return img,ImageDraw.Draw(img)
def lh(f,g=1.12): a,d=f.getmetrics(); return int((a+d)*g)
def bh(items,g=1.12): return sum(lh(f,g) for _,f,_ in items)
def tblock(d,items,x,y,g=1.12):
    cy=y
    for t,f,c in items: d.text((x,cy),t,font=f,fill=c,anchor="la"); cy+=lh(f,g)
    return cy
def stack_h(d,x,items):
    y=0
    for t,f,c,gap in items: b=d.textbbox((x,y),t,font=f); y=b[3]+gap
    return y
def stack_draw(d,x,top,items):
    y=top
    for t,f,c,gap in items: b=d.textbbox((x,y),t,font=f); d.text((x,y),t,font=f,fill=c,anchor="la"); y=b[3]+gap
    return y
def justify(groups,top,bot):
    n=len(groups); tot=sum(h for h,_ in groups); gap=(bot-top-tot)/(n-1) if n>1 else 0
    if gap<0: gap=0
    y=top
    for h,fn in groups: fn(int(round(y))); y+=h+gap
def glow(img,cx,cy,r):
    ov=Image.new("RGBA",img.size,(0,0,0,0)); ImageDraw.Draw(ov).ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(46,))
    img.alpha_composite(ov.filter(ImageFilter.GaussianBlur(130)))
def shadow(img,x,y,w,h,r=30,blur=24,alpha=130,dy=14):
    sh=Image.new("RGBA",img.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([x,y+dy,x+w,y+h+dy],radius=r,fill=(0,0,0,alpha))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
def card(img,x,y,w,h,fill=LIGHT,r=30,sh=True,accent=None):
    if sh: shadow(img,x,y,w,h,r)
    d=ImageDraw.Draw(img); d.rounded_rectangle([x,y,x+w,y+h],radius=r,fill=fill)
    if accent: d.rounded_rectangle([x+r//2,y,x+w-r//2,y+11],radius=5,fill=accent)
    return d
def logo(img,x=64,y=64,h=110):
    bb=LOGO_W.getbbox(); im=LOGO_W.crop(bb); w=int(im.width*h/im.height)
    img.alpha_composite(im.resize((w,h)),(x,y))
def slabel(d,x,y,text,color=GREEN,size=28):
    f=body(size,True); cx=x
    for ch in text.upper(): d.text((cx,y),ch,font=f,fill=color,anchor="la"); cx+=d.textlength(ch,font=f)+3
def gbar(d,W,H): d.rectangle([0,H-8,W,H],fill=GREEN)
def source(d,x,y,txt=SRC,color=GREYL,size=28): d.text((x,y),txt,font=body(size),fill=color,anchor="la")
def wrap(d,text,f,maxw):
    out=[];line=""
    for wd in text.split():
        t=(line+" "+wd).strip()
        if d.textlength(t,font=f)<=maxw: line=t
        else: out.append(line); line=wd
    if line: out.append(line)
    return out
def paste_img(img,pic,x,y,w,r=22,browser=False,accent=False):
    ratio=w/pic.width; h=int(pic.height*ratio); im=pic.resize((w,h))
    bar=46 if browser else 0; ta=11 if accent else 0; ph=h+bar+ta
    panel=Image.new("RGB",(w,ph),WHITE); pd=ImageDraw.Draw(panel)
    if accent: pd.rectangle([0,0,w,ta],fill=GREEN)
    if browser:
        for i,col in enumerate([(255,95,86),(255,189,46),(39,201,63)]): pd.ellipse([22+i*30,ta+bar//2-8,22+i*30+16,ta+bar//2+8],fill=col)
    panel.paste(im,(0,ta+bar)); shadow(img,x,y,w,ph,r=r)
    mask=Image.new("L",(w,ph),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,w,ph],radius=r,fill=255)
    img.alpha_composite(Image.merge("RGBA",(*panel.split(),mask)),(x,y)); return ph
def icon_check(img,x,y,s=46):
    d=ImageDraw.Draw(img); d.rounded_rectangle([x,y,x+s,y+s],radius=12,fill=GREEN)
    d.line([(x+s*0.26,y+s*0.52),(x+s*0.43,y+s*0.69),(x+s*0.76,y+s*0.30)],fill=WHITE,width=5,joint="curve")
def icon_x(img,x,y,s=40):
    d=ImageDraw.Draw(img); p=s*0.22
    d.line([(x+p,y+p),(x+s-p,y+s-p)],fill=RED,width=6); d.line([(x+s-p,y+p),(x+p,y+s-p)],fill=RED,width=6)

def kind(W,H): return "land" if W>H else ("tall" if H>=1.5*W else "sq")
ADS={}

# 1 Number hero
def ad1(W,H):
    k=kind(W,H); img,d=base(W,H); glow(img,W-110,H-150,520 if k=="tall" else (360 if k=="land" else 440))
    if k=="tall":
        logo(img,h=150)
        num=[("8.2",head(440),GREEN,18),("HOURS A WEEK",head(126),WHITE,46),("spent marking, every single week.",body(50),GREY,0)]
        hn=stack_h(d,62,num)
        justify([(40,lambda y: slabel(d,66,y,"The marking problem",GREEN,32)),
                 (hn,lambda y: stack_draw(d,62,y,num)),
                 (38,lambda y: source(d,66,y,size=30))],300,H-90)
    else:
        ly0=46 if k=="land" else 70; lh_=78 if k=="land" else 150; logo(img,x=64,y=ly0,h=lh_)
        label_y=ly0+lh_+(50 if k=="land" else 90)
        slabel(d,66,label_y,"The marking problem",GREEN,22 if k=="land" else 28)
        blk=[("8.2",head(200 if k=="land" else 300),GREEN,12 if k=="land" else 14),
             ("HOURS A WEEK",head(58 if k=="land" else 78),WHITE,30 if k=="land" else 42),
             ("spent marking, every single week.",body(34 if k=="land" else 40),GREY,0)]
        endy=stack_draw(d,62,label_y+(40 if k=="land" else 58),blk)
        source(d,66,endy+(36 if k=="land" else 50),size=24 if k=="land" else 28)
    gbar(d,W,H); return img.convert("RGB")
ADS["1_number-hero"]=ad1

# 2 Value statement
def ad2(W,H):
    k=kind(W,H); img,d=base(W,H)
    if k=="tall":
        logo(img,h=150)
        hf=head(150)
        hd=[("Feedback in",hf,WHITE,8),("minutes,",hf,GREEN,8),("not evenings.",hf,WHITE,0)]
        hh=stack_h(d,62,hd)
        def draw_hd(y): ey=stack_draw(d,62,y,hd); d.rectangle([66,ey+18,560,ey+30],fill=GREEN)
        sub=[("Same depth on every submission.",body(46),GREY),("You approve every comment first.",body(46),GREY)]
        justify([(44,lambda y: slabel(d,66,y,"Why lecturers switch",GREEN,32)),
                 (hh+40,draw_hd),
                 (bh(sub,1.25),lambda y: tblock(d,sub,66,y,1.25))],300,H-90)
    else:
        ly0=46 if k=="land" else 70; lh_=78 if k=="land" else 150; logo(img,x=64,y=ly0,h=lh_)
        label_y=ly0+lh_+(46 if k=="land" else 80)
        slabel(d,66,label_y,"Why lecturers switch",GREEN,22 if k=="land" else 28)
        hf=head(72 if k=="land" else 110); ty=label_y+(48 if k=="land" else 66)
        ey=tblock(d,[("Feedback in",hf,WHITE),("minutes,",hf,GREEN),("not evenings.",hf,WHITE)],62,ty,1.04)
        d.rectangle([66,ey+14,66+(340 if k=="land" else 460),ey+(22 if k=="land" else 26)],fill=GREEN)
        sf=body(30 if k=="land" else 38); sy=ey+(64 if k=="land" else 86)
        d.text((66,sy),"Same depth on every submission.",font=sf,fill=GREY,anchor="la")
        d.text((66,sy+(46 if k=="land" else 58)),"You approve every comment first.",font=sf,fill=GREY,anchor="la")
    gbar(d,W,H); return img.convert("RGB")
ADS["2_statement"]=ad2

# 3 Quote — big card filling the frame in tall
def ad3(W,H):
    k=kind(W,H); img,d=base(W,H)
    if k=="tall":
        logo(img,h=140)
        cx,cy,cw=64,290,952; ch=H-90-cy
        card(img,cx,cy,cw,ch,LIGHT,accent=GREEN); d=ImageDraw.Draw(img)
        d.text((cx+50,cy+50),"“",font=head(260),fill=GREEN,anchor="la")
        q=[("Over half of lecturers",head(76),INK),("have considered leaving",head(76),INK),("over their marking",head(76),INK),("workload.",head(76),TEAL)]
        qy=cy+(ch-bh(q,1.12))//2+40
        tblock(d,q,cx+50,qy,1.12)
        d.text((cx+50,cy+ch-96),"Learnosity survey of 502 UK teachers, 2025",font=body(30),fill=GREYL,anchor="la")
    else:
        logo(img,x=64,y=44 if k=="land" else 64,h=66 if k=="land" else 110)
        if k=="land":
            cx,cy,cw,ch=64,150,W-128,440
            card(img,cx,cy,cw,ch,LIGHT,accent=GREEN); d=ImageDraw.Draw(img)
            d.text((cx+44,cy+26),"“",font=head(150),fill=GREEN,anchor="la")
            tblock(d,[("Over half of lecturers have considered",head(46),INK),("leaving over their marking workload.",head(46),TEAL)],cx+48,cy+170,1.14)
            d.text((cx+48,cy+ch-74),"Learnosity survey of 502 UK teachers, 2025",font=body(26),fill=GREYL,anchor="la")
        else:
            cx,cy,cw,ch=64,300,952,640
            card(img,cx,cy,cw,ch,LIGHT,accent=GREEN); d=ImageDraw.Draw(img)
            d.text((cx+48,cy+34),"“",font=head(190),fill=GREEN,anchor="la")
            tblock(d,[("Over half of lecturers",head(58),INK),("have considered leaving",head(58),INK),("over their marking workload.",head(58),TEAL)],cx+50,cy+225,1.12)
            d.text((cx+50,cy+ch-84),"Learnosity survey of 502 UK teachers, 2025",font=body(27),fill=GREYL,anchor="la")
    gbar(d,W,H); return img.convert("RGB")
ADS["3_quote"]=ad3

# 4 VS comparison
def ad4(W,H):
    k=kind(W,H); img,d=base(W,H)
    edu=["Rubric-grounded feedback in minutes","Same depth on submission 1 and 300","You approve every comment first","Hours back, every cohort, every term"]
    man=["8.2 hours per batch, marking fatigue","Quality drops by paper 30","Generic comments copied across cohort","No time left to teach or research"]
    if k=="tall":
        logo(img,h=130)
        tblock(d,[("Two ways to mark",head(72),WHITE),("a whole cohort.",head(72),WHITE)],64,250,1.04)
        lx,rx,top=64,572,460; itf=body(30); itfb=body(30,True); wrapw=420; ics=46
        slabel(d,lx,top,"With Eduface",GREEN,28); d.rectangle([lx,top+40,lx+440,top+45],fill=GREEN)
        slabel(d,rx,top,"Manual marking",RED,28); d.rectangle([rx,top+40,rx+440,top+45],fill=RED)
        astart=top+110; aend=H-150; sp=(aend-astart)/len(edu)
        def col(items,x,ic,tc,f):
            for i,t in enumerate(items):
                y=int(astart+i*sp)
                if ic=="c": icon_check(img,x,y,ics)
                else: icon_x(img,x,y+2,ics-4)
                for j,l in enumerate(wrap(d,t,f,wrapw)): d.text((x+ics+18,y-2+j*int(f.size*1.25)),l,font=f,fill=tc,anchor="la")
        col(edu,lx,"c",WHITE,itfb); col(man,rx,"x",GREY,itf)
        source(d,64,H-86,"Marking workload: Learnosity, 2025")
    else:
        logo(img,x=64,y=44 if k=="land" else 64,h=64 if k=="land" else 96)
        if k=="land":
            tblock(d,[("Two ways to mark a whole cohort.",head(48),WHITE)],64,150,1.0)
            lx,rx,top=64,624,235; itf=body(24); itfb=body(24,True); wrapw=470; sp=64; ics=38
        else:
            tblock(d,[("Two ways to mark",head(60),WHITE),("a whole cohort.",head(60),WHITE)],64,200,1.04)
            lx,rx,top=64,572,400; itf=body(32); itfb=body(32,True); wrapw=380; sp=96; ics=48
        slabel(d,lx,top,"With Eduface",GREEN,22 if k=="land" else 28); d.rectangle([lx,top+38,lx+(490 if k=="land" else 440),top+43],fill=GREEN)
        slabel(d,rx,top,"Manual marking",RED,22 if k=="land" else 28); d.rectangle([rx,top+38,rx+(490 if k=="land" else 440),top+43],fill=RED)
        lh2=int(itf.size*1.25)
        def col(items,x,ic,tc,f):
            y=top+90
            for t in items:
                ln=wrap(d,t,f,wrapw)
                if ic=="c": icon_check(img,x,y,ics)
                else: icon_x(img,x,y+2,ics-4)
                for j,l in enumerate(ln): d.text((x+ics+18,y-2+j*lh2),l,font=f,fill=tc,anchor="la")
                y+=max(sp,lh2*len(ln)+(40 if k=="land" else 52))
        col(edu,lx,"c",WHITE,itfb); col(man,rx,"x",GREY,itf)
        source(d,64,H-50 if k=="land" else 1090,"Marking workload: Learnosity, 2025",size=22 if k=="land" else 28)
    gbar(d,W,H); return img.convert("RGB")
ADS["4_vs"]=ad4

# 5 Calendar card
def ad5(W,H):
    k=kind(W,H); img,d=base(W,H); days=["Mon","Tue","Wed","Thu","Fri"]
    if k=="tall":
        logo(img,h=140)
        slabel(d,66,300,"A lecturer's week",GREEN,32)
        tblock(d,[("Where the week",head(80),WHITE),("actually goes.",head(80),WHITE)],62,350,1.03)
        cx,cy,cw=64,560,952; ch=H-230-cy
        card(img,cx,cy,cw,ch,LIGHT); d=ImageDraw.Draw(img)
        x0=cx+50; bw=150; gp=22; at=cy+60; bh_=ch-150
        for i,dy in enumerate(days):
            x=x0+i*(bw+gp); d.rounded_rectangle([x,at,x+bw,at+bh_],radius=10,fill=(214,224,229))
            d.text((x+bw//2,at+bh_+24),dy,font=body(28),fill=GREYL,anchor="ma")
        gw=4*(bw+gp)+bw; gh=int(bh_*0.5)
        d.rounded_rectangle([x0,at+bh_-gh,x0+gw,at+bh_],radius=10,fill=GREEN)
        d.text((x0+gw//2,at+bh_-gh//2),"Marking — 8.2 hrs",font=head(48),fill=NAVY,anchor="mm")
        d.text((64,cy+ch+44),"Eduface gives that time back.",font=body(44),fill=WHITE,anchor="la")
        source(d,64,cy+ch+104)
    else:
        logo(img,x=64,y=44 if k=="land" else 64,h=66 if k=="land" else 110)
        if k=="land":
            slabel(d,66,150,"A lecturer's week",GREEN,22)
            tblock(d,[("Where the week",head(52),WHITE),("actually goes.",head(52),WHITE)],62,190,1.04)
            d.text((66,360),"Eduface gives that time back.",font=body(30),fill=WHITE,anchor="la"); source(d,66,415,size=22)
            cx,cy,cw,ch=590,150,W-590-64,420; card(img,cx,cy,cw,ch,LIGHT); d=ImageDraw.Draw(img)
            x0=cx+34; bw=78; gp=14; at=cy+40; bh_=ch-110
        else:
            slabel(d,66,250,"A lecturer's week",GREEN,28)
            tblock(d,[("Where the week",head(66),WHITE),("actually goes.",head(66),WHITE)],62,298,1.03)
            cx,cy,cw,ch=64,500,952,440; card(img,cx,cy,cw,ch,LIGHT); d=ImageDraw.Draw(img)
            x0=cx+50; bw=150; gp=22; at=cy+50; bh_=ch-140
            d.text((64,1000),"Eduface gives that time back.",font=body(40),fill=WHITE,anchor="la"); source(d,64,1055)
        for i,dy in enumerate(days):
            x=x0+i*(bw+gp); d.rounded_rectangle([x,at,x+bw,at+bh_],radius=10,fill=(214,224,229))
            d.text((x+bw//2,at+bh_+22),dy,font=body(22 if k=="land" else 26),fill=GREYL,anchor="ma")
        gw=4*(bw+gp)+bw; gh=int(bh_*0.5)
        d.rounded_rectangle([x0,at+bh_-gh,x0+gw,at+bh_],radius=10,fill=GREEN)
        d.text((x0+gw//2,at+bh_-gh//2),"8.2 hrs" if k=="land" else "Marking — 8.2 hrs",font=head(28 if k=="land" else 44),fill=NAVY,anchor="mm")
    gbar(d,W,H); return img.convert("RGB")
ADS["5_calendar"]=ad5

# 6 Product hero (criteria browser)
def ad6(W,H):
    k=kind(W,H); img,d=base(W,H)
    if k=="tall":
        logo(img,h=140)
        hd=[("Built for how you",head(76),WHITE),("actually grade.",head(76),GREEN)]
        sub=[("Your rubric, criterion by criterion.",body(40),GREY),("Feedback in minutes.",body(40),GREY)]
        w=952; ph=int(CRIT.height*(w/CRIT.width))+57
        justify([(bh(hd,1.04),lambda y: tblock(d,hd,62,y,1.04)),
                 (ph,lambda y: paste_img(img,CRIT,64,y,w,browser=True,accent=True)),
                 (bh(sub,1.3),lambda y: tblock(d,sub,64,y,1.3))],300,H-90)
        slabel(d,66,236,"Inside Eduface",GREEN,32)
    else:
        logo(img,x=64,y=44 if k=="land" else 64,h=66 if k=="land" else 110)
        if k=="land":
            slabel(d,66,150,"Inside Eduface",GREEN,22)
            tblock(d,[("Built for how",head(50),WHITE),("you actually grade.",head(50),GREEN)],62,190,1.04)
            d.text((66,360),"Your rubric, criterion by criterion.",font=body(28),fill=GREY,anchor="la")
            d.text((66,398),"Feedback in minutes.",font=body(28),fill=GREY,anchor="la")
            w=600; ph=int(CRIT.height*(w/CRIT.width))+57; paste_img(img,CRIT,W-w-64,(H-ph)//2,w,browser=True,accent=True)
        else:
            slabel(d,64,250,"Inside Eduface",GREEN,28)
            tblock(d,[("Built for how you",head(62),WHITE),("actually grade.",head(62),GREEN)],62,298,1.03)
            ph=paste_img(img,CRIT,64,470,912,browser=True,accent=True); d=ImageDraw.Draw(img)
            d.text((64,470+ph+38),"Your rubric, criterion by criterion.",font=body(36),fill=GREY,anchor="la")
            d.text((64,470+ph+86),"Feedback in minutes.",font=body(36),fill=GREY,anchor="la")
    gbar(d,W,H); return img.convert("RGB")
ADS["6_product-hero"]=ad6

# 7 Stat cards
def ad7(W,H):
    k=kind(W,H); img,d=base(W,H)
    stats=[("8.2 hrs","spent marking every single week"),("52%","have considered leaving over it"),("87%","take marking work home")]
    if k=="tall":
        logo(img,h=140)
        slabel(d,66,300,"Marking, by the numbers",GREEN,32)
        ct=400; cb=H-130; cw=952; ch=370; sp=(cb-ct-len(stats)*ch)/(len(stats)-1) if len(stats)>1 else 0
        for i,(num,lab) in enumerate(stats):
            y=int(ct+i*(ch+sp)); card(img,64,y,cw,ch,NAVY2,r=28); dd=ImageDraw.Draw(img)
            dd.rounded_rectangle([64,y,84,y+ch],radius=9,fill=GREEN)
            dd.text((124,y+90),num,font=head(120),fill=GREEN,anchor="la")
            for j,l in enumerate(wrap(dd,lab,body(40),760)): dd.text((124,y+250+j*48),l,font=body(40),fill=WHITE,anchor="la")
        source(d,66,cb+24)
    elif k=="land":
        logo(img,x=64,y=44,h=66); slabel(d,66,150,"Marking, by the numbers",GREEN,22)
        cw=(W-128-2*24)//3; ch=300; y=210; x=64
        for num,lab in stats:
            card(img,x,y,cw,ch,NAVY2,r=24); dd=ImageDraw.Draw(img)
            dd.rounded_rectangle([x,y,x+14,y+ch],radius=7,fill=GREEN)
            dd.text((x+44,y+70),num,font=head(72),fill=GREEN,anchor="la")
            for j,l in enumerate(wrap(dd,lab,body(26),cw-80)): dd.text((x+44,y+180+j*36),l,font=body(26),fill=WHITE,anchor="la")
            x+=cw+24
        source(d,66,y+ch+24,size=22)
    else:
        logo(img,x=64,y=64,h=110); slabel(d,64,250,"Marking, by the numbers",GREEN,28)
        y=320; cw=952; ch=200
        for num,lab in stats:
            card(img,64,y,cw,ch,NAVY2,r=26); dd=ImageDraw.Draw(img)
            dd.rounded_rectangle([64,y,82,y+ch],radius=8,fill=GREEN)
            dd.text((118,y+ch//2-6),num,font=head(92),fill=GREEN,anchor="lm")
            for j,l in enumerate(wrap(dd,lab,body(36),440)): dd.text((540,y+ch//2-18+j*44),l,font=body(36),fill=WHITE,anchor="lm")
            y+=ch+28
        d=ImageDraw.Draw(img); source(d,64,y+8)
    gbar(d,W,H); return img.convert("RGB")
ADS["7_stats"]=ad7

# 8 Product detail (grading options)
def ad8(W,H):
    k=kind(W,H); img,d=base(W,H)
    if k=="tall":
        logo(img,h=140)
        hd=[("Points, pass/fail",head(76),WHITE),("or descriptive levels.",head(76),GREEN)]
        sub=[("Every criterion scored,",body(40),GREY),("tied to your rubric.",body(40),GREY)]
        w=952; ph=int(GRAD.height*(w/GRAD.width))+11
        justify([(bh(hd,1.04),lambda y: tblock(d,hd,62,y,1.04)),
                 (ph,lambda y: paste_img(img,GRAD,64,y,w,accent=True)),
                 (bh(sub,1.3),lambda y: tblock(d,sub,64,y,1.3))],300,H-90)
        slabel(d,66,236,"Grade your way",GREEN,32)
    else:
        logo(img,x=64,y=44 if k=="land" else 64,h=66 if k=="land" else 110)
        if k=="land":
            slabel(d,66,150,"Grade your way",GREEN,22)
            tblock(d,[("Points, pass/fail",head(50),WHITE),("or descriptive levels.",head(50),GREEN)],62,190,1.04)
            d.text((66,375),"Every criterion scored,",font=body(28),fill=GREY,anchor="la")
            d.text((66,413),"tied to your rubric.",font=body(28),fill=GREY,anchor="la")
            w=600; ph=int(GRAD.height*(w/GRAD.width))+11; paste_img(img,GRAD,W-w-64,(H-ph)//2,w,accent=True)
        else:
            slabel(d,64,250,"Grade your way",GREEN,28)
            tblock(d,[("Points, pass/fail",head(62),WHITE),("or descriptive levels.",head(62),GREEN)],62,298,1.03)
            ph=paste_img(img,GRAD,64,480,912,accent=True); d=ImageDraw.Draw(img)
            d.text((64,480+ph+42),"Every criterion scored, tied to your rubric.",font=body(36),fill=GREY,anchor="la")
    gbar(d,W,H); return img.convert("RGB")
ADS["8_product-detail"]=ad8

# 9 Closer
def ad9(W,H):
    k=kind(W,H); img,d=base(W,H); glow(img,150,180,520 if k=="tall" else (300 if k=="land" else 400))
    if k=="tall":
        logo(img,h=150)
        hf=head(98)
        lines=[("Marking costs you",hf,WHITE),("8 hours a week.",hf,GREEN),("It doesn't",hf,WHITE),("have to.",hf,WHITE)]
        groups=[(lh(f,1.04),(lambda yy,tt=t,ff=f,cc=c: d.text((62,yy),tt,font=ff,fill=cc,anchor="la"))) for t,f,c in lines]
        groups.append((38,lambda y: source(d,66,y,size=30)))
        justify(groups,320,H-100)
    else:
        ly0=44 if k=="land" else 64; logo(img,x=64,y=ly0,h=66 if k=="land" else 110)
        hf=head(60 if k=="land" else 92); ty=ly0+(70 if k=="land" else 150)+(40 if k=="land" else 90)
        ey=tblock(d,[("Marking costs you",hf,WHITE),("8 hours a week.",hf,GREEN),(" ",head(20 if k=="land" else 34),WHITE),("It doesn't have to.",hf,WHITE)],62,ty,1.06)
        source(d,66,ey+(30 if k=="land" else 46),size=24 if k=="land" else 28)
    gbar(d,W,H); return img.convert("RGB")
ADS["9_closer"]=ad9

# ---- export ----
FORMATS=[(1080,1080,"1x1"),(1080,1920,"9x16"),(1200,628,"1.91x1")]
OUT=os.path.join(HERE,"final"); os.makedirs(OUT,exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith(".png"): os.remove(os.path.join(OUT,f))
for W,H,tag in FORMATS:
    for name,fn in ADS.items(): fn(W,H).save(os.path.join(OUT,f"ad_{name}_{tag}.png"))
for W,H,tag in FORMATS:
    tw=560; th=int(tw*H/W); cols=3; rows=3; pad=26
    sheet=Image.new("RGB",(cols*tw+(cols+1)*pad,rows*th+(rows+1)*pad),(222,227,230))
    for i,(name,fn) in enumerate(ADS.items()):
        r,c=divmod(i,cols); sheet.paste(fn(W,H).resize((tw,th)),(pad+c*(tw+pad),pad+r*(th+pad)))
    sheet.save(os.path.join(HERE,f"_overzicht_{tag}.png"))
print("done:",len(ADS)*len(FORMATS),"PNGs")
