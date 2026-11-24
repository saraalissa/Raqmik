import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'
def font(n,s): return ImageFont.truetype(F+n,s)
src=np.array(Image.open('win/feed_nocircle.png').convert('RGB'))
r,g,b=[src[...,i].astype(int) for i in range(3)]
red=((r>150)&(r-np.maximum(g,b)>70)).astype(np.uint8)
H,W=red.shape
BLK=1055
hm=cv2.dilate(red,np.ones((9,9),np.uint8))
src=src.copy()
for y in range(916,990):
    for x in range(500,590):
        if hm[y,x] and not (y<918):
            src[y,x]=src[y,x-80]
r,g,b=[src[...,i].astype(int) for i in range(3)]
red=((r>150)&(r-np.maximum(g,b)>70)).astype(np.uint8)
# remove the old arrow (below the circle) and old note
m=np.zeros_like(red); m[936:1262,200:890]=red[936:1262,200:890]; m[919:936,490:590]=red[919:936,490:590]
m=cv2.dilate(m,np.ones((7,7),np.uint8))
clean=cv2.cvtColor(cv2.inpaint(cv2.cvtColor(src,cv2.COLOR_RGB2BGR),m*255,9,cv2.INPAINT_TELEA),cv2.COLOR_BGR2RGB)
out=Image.fromarray(clean).convert('RGBA')
# handwriting words as RGBA from original
alpha=np.clip((r-np.maximum(g,b)-35)*4,0,255).astype(np.uint8)
L=Image.fromarray(src).convert('RGBA'); L.putalpha(Image.fromarray(alpha))
def word(x0,x1):
    w=L.crop((x0,1166,x1,1264)); a_=w.split()[3].point(lambda v:0 if v<70 else v); w.putalpha(a_); return w.crop(w.getbbox())
from PIL import ImageFilter
import math
cf=ImageFont.truetype('Caveat.ttf',84); cf.set_variation_by_name('Bold')
RED=(214,32,38,255)
txt='no hunting for the number.'
tl=Image.new('RGBA',out.size,(0,0,0,0)); td=ImageDraw.Draw(tl)
tw=td.textlength(txt,font=cf); TX=(1080-tw)/2+20; TY=4
# soft white glow behind the words so they pop on any background
glow=Image.new('RGBA',out.size,(0,0,0,0)); gd=ImageDraw.Draw(glow)
gd.text((TX,TY),txt,font=cf,fill=(255,255,255,230),stroke_width=10,stroke_fill=(255,255,255,230))
glow=glow.filter(ImageFilter.GaussianBlur(6))
out.alpha_composite(glow)
td.text((TX,TY),txt,font=cf,fill=RED)
out.alpha_composite(tl)
# --- new hand-drawn circle around the dose text (clear of the letters)
import math as _m
_cx,_cy,_a,_b,_rot=604,866,262,58,_m.radians(-4)
_pts=[]
for i in range(0,381):
    t=_m.radians(-200+i)          # a bit more than one turn, like a hand-drawn loop
    rr=1+0.025*_m.sin(t*3)+ (0.04 if i>350 else 0)
    x=_a*rr*_m.cos(t); y=_b*rr*_m.sin(t)
    _pts.append((_cx+x*_m.cos(_rot)-y*_m.sin(_rot), _cy+x*_m.sin(_rot)+y*_m.cos(_rot)))
_d=ImageDraw.Draw(out)
_d.line(_pts,fill=(214,32,38,255),width=7,joint='curve')
d=ImageDraw.Draw(out)
# arrow: from the end of the note, sweeping down the right side (outside the jar) into the circle
P=[(TX+tw-30,TY+100),(1060,330),(1040,850),(900,848)]
pts=[]
for i in range(81):
    t=i/80
    x=(1-t)**3*P[0][0]+3*(1-t)**2*t*P[1][0]+3*(1-t)*t*t*P[2][0]+t**3*P[3][0]
    y=(1-t)**3*P[0][1]+3*(1-t)**2*t*P[1][1]+3*(1-t)*t*t*P[2][1]+t**3*P[3][1]
    pts.append((x,y))
# white halo under the arrow for contrast, then red
d.line(pts,fill=(255,255,255,150),width=16,joint='curve')
d.line(pts,fill=RED,width=9,joint='curve')
p2=pts[-1]; ang=math.atan2(p2[1]-pts[-7][1],p2[0]-pts[-7][0])
for da in (2.55,-2.55):
    e=(p2[0]+38*math.cos(ang+da),p2[1]+38*math.sin(ang+da))
    d.line([p2,e],fill=(255,255,255,150),width=16); 
for da in (2.55,-2.55):
    e=(p2[0]+38*math.cos(ang+da),p2[1]+38*math.sin(ang+da))
    d.line([p2,e],fill=RED,width=9)
# plum + gold luxe block
d=ImageDraw.Draw(out)
BLK2=1040
band=Image.new('RGBA',(W,H-BLK2))
for y in range(H-BLK2):
    t=y/(H-BLK2-1); c=(int(46*(1-t)+20*t),int(10*(1-t)+5*t),int(30*(1-t)+14*t))
    ImageDraw.Draw(band).line([(0,y),(W,y)],fill=c+(255,))
out.alpha_composite(band,(0,BLK2)); d=ImageDraw.Draw(out)
GOLD=(240,206,128,255)
d.line([(0,BLK2),(W,BLK2)],fill=GOLD,width=4)
def ctext(y,t,f,fill,sp=0):
    w=sum(d.textlength(c,font=f) for c in t)+sp*(len(t)-1); x=(W-w)/2
    for c in t: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
    return (W-w)/2,w
# BLACK FRIDAY with gold rules either side
fbf=font('InterDisplay-SemiBold.otf',40)
x,w=ctext(BLK2+26,'BLACK FRIDAY',fbf,GOLD,sp=16)
d.line([(x-150,BLK2+50),(x-30,BLK2+50)],fill=GOLD,width=2); d.line([(x+w+30,BLK2+50),(x+w+150,BLK2+50)],fill=GOLD,width=2)
# gold-gradient "3 FOR 2"
big=font('InterDisplay-Black.otf',178); t='3 FOR 2'
tw=d.textlength(t,font=big); th=170
mask=Image.new('L',(int(tw)+10,th+60),0); ImageDraw.Draw(mask).text((5,0),t,font=big,fill=255)
grad=Image.new('RGBA',mask.size)
for y in range(mask.size[1]):
    u=y/mask.size[1]; c=(int(255*(1-u)+200*u),int(244*(1-u)+146*u),int(196*(1-u)+52*u))
    ImageDraw.Draw(grad).line([(0,y),(mask.size[0],y)],fill=c+(255,))
grad.putalpha(mask)
from PIL import ImageFilter as _IF
shd=Image.new('RGBA',mask.size,(0,0,0,0)); shd.putalpha(mask.filter(_IF.GaussianBlur(7)).point(lambda v:int(v*0.6)))
out.alpha_composite(shd,(int((W-tw)/2)-1,BLK2+62))
out.alpha_composite(grad,(int((W-tw)/2)-5,BLK2+56)); d=ImageDraw.Draw(out)
# pink pill
fp=font('InterDisplay-ExtraBold.otf',34); t2='Buy 2, get 1 FREE  ·  Ends Monday'
w2=d.textlength(t2,font=fp)
d.rounded_rectangle(((W-w2)/2-26,BLK2+256,(W+w2)/2+26,BLK2+304),radius=25,fill=(244,201,214,255))
d.text(((W-w2)/2,BLK2+260),t2,font=fp,fill=(61,15,39))
out.convert('RGB').save('/home/user/Raqmik/meva/ads/2026-11-24-bf-overlays/winner-feed-BF-gold.jpg',quality=95)
