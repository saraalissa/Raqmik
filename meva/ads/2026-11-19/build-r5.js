const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const S='file://'+path.join(__dirname,'src')+'/';const OUT=path.join(__dirname,'r5');
const css=`@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&family=Caveat:wght@600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;font-family:'Inter Tight',Arial,sans-serif;color:#3d0f27;-webkit-font-smoothing:antialiased}
.f{position:relative;width:1080px;height:1350px;overflow:hidden}.hw{font-family:Caveat}
img.cover{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.jar{position:absolute;filter:drop-shadow(0 24px 30px rgba(30,5,18,.35))}
.red{color:#e01b24;text-shadow:0 0 14px rgba(255,255,255,.95),0 0 5px #fff}
.cta{position:absolute;left:50%;transform:translateX(-50%);bottom:56px;background:#3d0f27;color:#fff;font-weight:800;font-size:34px;border-radius:999px;padding:20px 40px;white-space:nowrap}`;
const J=(st)=>`<img class="jar" src="${S}meva-jar-cut.png" style="${st}">`;
const split=(L,Lh,Ri,Rh,bot)=>`<div class="f" style="background:#fff">
<div style="position:absolute;left:0;top:0;width:540px;height:1350px;background:#eceae6"></div>
<div style="position:absolute;left:0;width:540px;top:90px;text-align:center;font-size:40px;font-weight:700;color:#8a8580">The usual</div>
<div style="position:absolute;left:540px;width:540px;top:90px;text-align:center;font-size:40px;font-weight:800;color:#8e2a5a">Mëva</div>
${L}
<div style="position:absolute;left:0;width:540px;top:780px;text-align:center;font-size:44px;font-weight:700;color:#6f6a66;line-height:1.25">${Lh}</div>
${Ri}
<div style="position:absolute;left:540px;width:540px;top:780px;text-align:center;font-size:44px;font-weight:800;line-height:1.25">${Rh}</div>
<div style="position:absolute;left:0;right:0;top:990px;text-align:center;font-size:58px;font-weight:900;letter-spacing:-.03em">${bot}</div>
<div class="cta">Join the No Drama Club. Free →</div></div>`;
const hand=`<img src="${S}g3hand.jpg" style="position:absolute;left:580px;top:200px;width:460px;height:520px;object-fit:cover;object-position:50% 60%;border-radius:30px">`;
const jarR=`<img class="jar" src="${S}meva-jar-cut.png" style="left:640px;top:200px;height:520px">`;
const T={
C1:()=>split(`<div style="position:absolute;left:120px;top:300px;width:300px;height:300px;border-radius:0 0 40px 40px;border:8px solid #c9c3bb;border-top:none;background:linear-gradient(180deg,transparent 35%,#e4ddd2 35%)"></div>
<div style="position:absolute;left:300px;top:200px;width:16px;height:330px;background:#b9b2a8;border-radius:8px;transform:rotate(18deg)"></div>
<div style="position:absolute;left:150px;top:410px;width:240px;height:40px;border-radius:50%;background:radial-gradient(#fff 20%,#d9d2c7 70%);opacity:.9"></div>
<div class="hw" style="position:absolute;left:0;width:540px;top:640px;text-align:center;font-size:52px;color:#8a8580;transform:rotate(-3deg)">*clumps*</div>`,
`Stir the powder.<br>Wait. Forget it.`,hand,`Two berry gummies.<br>Chew. Done.`,`No stirring. No water.<br><span style="color:#8e2a5a">180mg magnesium a day.</span>`),
C2:()=>split(`<div style="position:absolute;left:0;width:540px;top:320px;text-align:center;font-size:118px;font-weight:900;letter-spacing:-.05em;color:#b3aca4">1,000mg</div>
<div style="position:absolute;left:0;width:540px;top:500px;text-align:center;font-size:34px;font-weight:600;color:#8a8580;line-height:1.3">*of the whole compound.<br>Real magnesium? Small print.</div>`,
`The big number<br>isn’t the mineral.`,jarR,`180mg magnesium.<br>On the front.`,`The real number.<br><span style="color:#8e2a5a">Where you can see it.</span>`),
C3:()=>split(`<div style="position:absolute;left:70px;top:280px;width:400px;background:#fff;border-radius:20px;padding:30px;box-shadow:0 10px 24px rgba(0,0,0,.08)">
<div style="font-size:30px;font-weight:800;color:#6f6a66">Ingredients</div>
<div style="font-size:26px;color:#9a948d;line-height:1.5;margin-top:10px">Magnesium blend (oxide, glycinate, malate, taurate, carbonate), proprietary complex, …</div></div>
<div class="hw" style="position:absolute;left:0;width:540px;top:600px;text-align:center;font-size:52px;color:#8a8580;transform:rotate(-3deg)">how much of each?</div>`,
`A blend.<br>One total. No idea.`,jarR,`One form:<br>magnesium citrate.`,`Nothing hidden.<br><span style="color:#8e2a5a">180mg magnesium a day.</span>`),
H6:()=>`<div class="f"><img class="cover" src="${S}r5bag.png">
<div class="hw red" style="position:absolute;left:0;right:0;top:1110px;text-align:center;font-size:80px;line-height:1;transform:rotate(-3deg)">in my bag.<br>dose on the front.</div></div>`,
H7:()=>`<div class="f"><img class="cover" src="${S}r5desk.png">
<div class="hw red" style="position:absolute;left:0;right:0;top:1110px;text-align:center;font-size:80px;line-height:1;transform:rotate(-3deg)">two gummies.<br>between emails.</div></div>`
};
const story=f=>`<div class="f" style="width:1080px;height:1920px;background:#3d0f27"><img src="file://${f}" style="position:absolute;left:0;top:285px;width:1080px;height:1350px"><div style="position:absolute;left:0;right:0;top:1690px;text-align:center;color:#ffd84d;font-weight:800;font-size:46px">Join the No Drama Club. Free.</div></div>`;
(async()=>{const b=await chromium.launch();const ids=process.argv.slice(2).length?process.argv.slice(2):Object.keys(T);
for(const id of ids){const ff=path.join(OUT,`${id}-feed.png`);
for(const [nm,w,h] of [['feed',1080,1350],['story',1080,1920]]){const p=await b.newPage({viewport:{width:w,height:h}});const hf=path.join(__dirname,'tmpr5.html');
fs.writeFileSync(hf,`<html><head><meta charset="utf-8"><style>${css}</style></head><body style="width:${w}px;height:${h}px">${nm=='feed'?T[id]():story(ff)}</body></html>`);
await p.goto('file://'+hf);await p.waitForTimeout(900);await p.screenshot({path:path.join(OUT,`${id}-${nm}.png`)});await p.close();}}
await b.close()})();
