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
