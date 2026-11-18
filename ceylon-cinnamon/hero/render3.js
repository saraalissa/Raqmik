const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:1100},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/benefits.html');await p.waitForTimeout(400);await p.locator('#s').screenshot({path:'cn-benefits.png'});await b.close();})();
