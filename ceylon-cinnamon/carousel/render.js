const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch();
  const p = await b.newPage({viewport:{width:1100,height:1100},deviceScaleFactor:2});
  await p.goto('file://'+__dirname+'/slides.html'); await p.waitForTimeout(500);
  for (let i=1;i<=10;i++){ await p.locator('#s'+i).screenshot({path:`cinnora-${String(i).padStart(2,'0')}.png`}); }
  // contact sheet at 1x for review
  await b.close();
})();
