const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch(); const dir=process.argv[2], out=process.argv[3];
 const map={part1:'向阳里驿站_1부_冬',part2:'向阳里驿站_2부_春',part3:'向阳里驿站_3부_夏',part4:'向阳里驿站_4부_秋',all:'向阳里驿站_전60화'};
 for(const n of Object.keys(map)){
  const p=await b.newPage();
  await p.goto('file://'+dir+'/'+n+'.html',{waitUntil:'networkidle',timeout:300000});
  await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:out+'/'+map[n]+'.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,timeout:0,
   headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#888"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
   margin:{top:'16mm',bottom:'18mm',left:'15mm',right:'15mm'}});
  await p.close(); console.log('done',n);
 }
 await b.close();
})();
