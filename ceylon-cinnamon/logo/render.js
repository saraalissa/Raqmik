const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:3});
await p.goto('file://'+__dirname+'/logo.html');await p.waitForTimeout(300);
for (const [id,f] of [['l1','cinnora-logo.png'],['l2','cinnora-logo-light.png'],['l3','cinnora-wordmark.png'],['i1','cinnora-icon.png']]) await p.locator('#'+id).screenshot({path:f,omitBackground:true});
await b.close();})();
