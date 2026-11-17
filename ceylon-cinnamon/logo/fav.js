const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/fav.html');await p.locator('#f').screenshot({path:'cinnora-favicon.png',omitBackground:true});await b.close();})();
