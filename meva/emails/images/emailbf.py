from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
F='/usr/share/fonts/opentype/inter/'
def font(n,s): return ImageFont.truetype(F+n,s)
src,out=sys.argv[1],sys.argv[2]
ph=Image.open(src).convert('RGBA'); W,Hp=ph.size
BH=330; H=Hp+BH
im=Image.new('RGBA',(W,H),(20,5,14,255)); im.alpha_composite(ph,(0,0))
# band gradient continuing the plum backdrop
band=Image.new('RGBA',(W,BH))
for y in range(BH):
    t=y/(BH-1); c=(int(40*(1-t)+18*t),int(10*(1-t)+4*t),int(26*(1-t)+12*t))
    ImageDraw.Draw(band).line([(0,y),(W,y)],fill=c+(255,))
im.alpha_composite(band,(0,Hp))
# soft fade between photo and band
fade=Image.new('RGBA',(W,60))
for y in range(60): ImageDraw.Draw(fade).line([(0,y),(W,y)],fill=(40,10,26,int(255*y/59)))
im.alpha_composite(fade,(0,Hp-60))
d=ImageDraw.Draw(im); GOLD=(240,206,128,255)
d.line([(0,Hp),(W,Hp)],fill=GOLD,width=3)
def ctext(y,t,f,fill,sp=0):
    w=sum(d.textlength(c,font=f) for c in t)+sp*(len(t)-1); x=(W-w)/2
    for c in t: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
    return (W-w)/2,w
x,w=ctext(Hp+22,'BLACK FRIDAY',font('InterDisplay-SemiBold.otf',38),GOLD,sp=15)
d.line([(x-140,Hp+45),(x-28,Hp+45)],fill=GOLD,width=2); d.line([(x+w+28,Hp+45),(x+w+140,Hp+45)],fill=GOLD,width=2)
big=font('InterDisplay-Black.otf',150); t='3 FOR 2'; tw=d.textlength(t,font=big)
mask=Image.new('L',(int(tw)+10,190),0); ImageDraw.Draw(mask).text((5,0),t,font=big,fill=255)
grad=Image.new('RGBA',mask.size)
for y in range(mask.size[1]):
    u=y/mask.size[1]; c=(int(255*(1-u)+200*u),int(244*(1-u)+146*u),int(196*(1-u)+52*u))
    ImageDraw.Draw(grad).line([(0,y),(mask.size[0],y)],fill=c+(255,))
grad.putalpha(mask)
shd=Image.new('RGBA',mask.size,(0,0,0,0)); shd.putalpha(mask.filter(ImageFilter.GaussianBlur(7)).point(lambda v:int(v*0.6)))
im.alpha_composite(shd,(int((W-tw)/2)-1,Hp+74)); im.alpha_composite(grad,(int((W-tw)/2)-5,Hp+68))
d=ImageDraw.Draw(im)
fp=font('InterDisplay-ExtraBold.otf',32); t2='Buy 2, get 1 FREE  ·  Free UK delivery  ·  Ends Mon 30 Nov'
w2=d.textlength(t2,font=fp)
d.rounded_rectangle(((W-w2)/2-26,Hp+256,(W+w2)/2+26,Hp+306),radius=25,fill=(244,201,214,255))
d.text(((W-w2)/2,Hp+261),t2,font=fp,fill=(61,15,39))
im.convert('RGB').save(out,quality=94)
print(im.size)
