const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1240,height:1754}});
for(const i of [1,2,3,4]){await p.goto('file://'+__dirname+'/pagina-'+i+'.html');await p.waitForTimeout(300);await p.screenshot({path:__dirname+'/pagina-'+i+'.png'});}
await b.close();})();
