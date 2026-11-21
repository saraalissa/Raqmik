const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const S='file://'+path.join(__dirname,'src')+'/';const OUT=path.join(__dirname,'out');fs.mkdirSync(OUT,{recursive:true});
const css=`@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&family=Caveat:wght@600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter Tight',Arial,sans-serif;color:#3d0f27;-webkit-font-smoothing:antialiased}
.f{position:relative;width:1080px;height:1350px;overflow:hidden}.hw{font-family:Caveat}
img.cover{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.red{color:#e01b24;text-shadow:0 0 14px rgba(255,255,255,.95),0 0 5px #fff}
.cta{position:absolute;left:50%;transform:translateX(-50%);bottom:56px;background:#3d0f27;color:#fff;font-weight:800;font-size:34px;border-radius:999px;padding:20px 40px;white-space:nowrap}`;
// hand-drawn ellipse + arrow + note
const mark=(cx,cy,rx,ry,ax1,ay1,note,ny)=>`<svg width="1080" height="1350" style="position:absolute;inset:0" viewBox="0 0 1080 1350">
<path d="M ${cx-rx+8} ${cy-6} C ${cx-rx} ${cy-ry-6}, ${cx+rx+10} ${cy-ry-2}, ${cx+rx} ${cy+4} C ${cx+rx-6} ${cy+ry+6}, ${cx-rx-4} ${cy+ry+2}, ${cx-rx+2} ${cy-2} C ${cx-rx+6} ${cy-14}, ${cx-rx+30} ${cy-ry+4}, ${cx-rx+60} ${cy-ry+2}" fill="none" stroke="#e01b24" stroke-width="6" stroke-linecap="round"/>
<path d="M ${ax1} ${ay1} C ${ax1+8} ${ay1-60}, ${cx-4} ${cy+ry+90}, ${cx} ${cy+ry+14}" fill="none" stroke="#e01b24" stroke-width="6" stroke-linecap="round"/>
<path d="M ${cx-22} ${cy+ry+40} L ${cx} ${cy+ry+12} L ${cx+20} ${cy+ry+42}" fill="none" stroke="#e01b24" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="hw red" style="position:absolute;left:0;right:0;top:${ny}px;text-align:center;font-size:84px;line-height:1;transform:rotate(-3deg)">${note}</div>`;
const T={
N1:()=>`<div class="f"><img class="cover" src="${S}bath.png">${mark(478,893,190,50,460,1150,'no squinting at the back.',1160)}</div>`,
N2:()=>`<div class="f"><img class="cover" src="${S}car.png">${mark(580,881,150,42,560,1150,'checked it in two seconds.',1165)}</div>`,
G4:()=>`<div class="f" style="background:#fff">
<div style="position:absolute;left:0;top:0;width:540px;height:1350px;background:#eceae6"></div>
<div style="position:absolute;left:0;width:540px;top:90px;text-align:center;font-size:40px;font-weight:700;color:#8a8580">The usual</div>
<div style="position:absolute;left:540px;width:540px;top:90px;text-align:center;font-size:40px;font-weight:800;color:#8e2a5a">Mëva</div>
<div style="position:absolute;left:130px;top:250px;width:280px;height:400px;border:8px solid #c9c3bb;border-top:none;border-radius:0 0 46px 46px;background:linear-gradient(180deg,transparent 22%,#e4ebef 22%)"></div>
<div style="position:absolute;left:205px;top:420px;width:130px;height:130px;border-radius:50%;background:#f3f0ea;border:6px solid #ddd6cc"></div>
${[[190,380,14],[350,330,10],[300,470,12],[230,300,9],[370,420,8],[260,560,10],[330,600,7]].map(([x,y,r])=>`<div style="position:absolute;left:${x}px;top:${y}px;width:${r*2}px;height:${r*2}px;border-radius:50%;border:3px solid #b9c4cb"></div>`).join('')}
<div class="hw" style="position:absolute;left:0;width:540px;top:680px;text-align:center;font-size:54px;color:#8a8580;transform:rotate(-3deg)">*fizzzz...*</div>
<div style="position:absolute;left:0;width:540px;top:790px;text-align:center;font-size:44px;font-weight:700;color:#6f6a66;line-height:1.25">Drop it in water.<br>Wait for the fizz.</div>
<img src="${S}palm.png" style="position:absolute;left:580px;top:200px;width:460px;height:520px;object-fit:cover;object-position:50% 55%;border-radius:30px">
<div style="position:absolute;left:540px;width:540px;top:790px;text-align:center;font-size:44px;font-weight:800;line-height:1.25">Two berry gummies.<br>Chew. Done.</div>
<div style="position:absolute;left:0;right:0;top:990px;text-align:center;font-size:58px;font-weight:900;letter-spacing:-.03em">No glass. No waiting.<br><span style="color:#8e2a5a">180mg magnesium a day.</span></div>
<div class="cta">Join the No Drama Club. Free →</div></div>`};
const story=f=>`<div class="f" style="width:1080px;height:1920px;background:#3d0f27"><img src="file://${f}" style="position:absolute;left:0;top:285px;width:1080px;height:1350px"><div style="position:absolute;left:0;right:0;top:1690px;text-align:center;color:#ffd84d;font-weight:800;font-size:46px">Join the No Drama Club. Free.</div></div>`;
(async()=>{const b=await chromium.launch();for(const id of Object.keys(T)){const ff=path.join(OUT,`${id}-feed.png`);
for(const [nm,w,h] of [['feed',1080,1350],['story',1080,1920]]){const p=await b.newPage({viewport:{width:w,height:h}});const hf=path.join(__dirname,'tmp.html');
fs.writeFileSync(hf,`<html><head><meta charset="utf-8"><style>${css}</style></head><body style="width:${w}px;height:${h}px">${nm=='feed'?T[id]():story(ff)}</body></html>`);
await p.goto('file://'+hf);await p.waitForTimeout(1500);await p.screenshot({path:path.join(OUT,`${id}-${nm}.png`)});await p.close();}}
await b.close()})();
