import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'
def font(n,s): return ImageFont.truetype(F+n,s)
src=np.array(Image.open('win/feed.jpg').convert('RGB'))
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
d=ImageDraw.Draw(out)
# arrow: from the end of the note, sweeping down the right side (outside the jar) into the circle
P=[(TX+tw-30,TY+100),(1060,330),(1025,874),(856,874)]
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
# black block (style B)
d.rectangle((0,BLK,W,H),fill=(10,10,10,255))
def ctext(y,t,f,fill,sp=0):
    w=sum(d.textlength(c,font=f) for c in t)+sp*(len(t)-1); x=(W-w)/2
    for c in t: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
ctext(BLK+18,'BLACK FRIDAY',font('InterDisplay-ExtraBold.otf',44),(255,255,255),sp=14)
ctext(BLK+66,'3 FOR 2',font('InterDisplay-Black.otf',150),(255,214,72))
ctext(BLK+240,'BUY 2, GET 1 FREE  ·  ENDS MONDAY',font('InterDisplay-Bold.otf',30),(255,255,255),sp=3)
out.convert('RGB').save('/home/user/Raqmik/meva/ads/2026-11-24-bf-overlays/winner-feed-B-3for2-note.jpg',quality=95)
