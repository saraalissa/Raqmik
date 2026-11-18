const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:1440},deviceScaleFactor:1.5});
await p.goto('file://'+__dirname+'/ben3.html');await p.waitForTimeout(500);await p.locator('#s').screenshot({path:'cn-benefits-light.png'});
await p.setViewportSize({width:1440,height:1440});await b.close();})();
