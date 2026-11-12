const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch(); const dir=process.argv[2];
 const names=['part1','part2','part3','part4','part5','all'];
 const out={part1:'槐荫胡同十七号_1부_春',part2:'槐荫胡同十七号_2부_夏',part3:'槐荫胡同十七号_3부_秋',part4:'槐荫胡同十七号_4부_冬',part5:'槐荫胡同十七号_5부_新春',all:'槐荫胡同十七号_전48화'};
 for(const n of names){
  const p=await b.newPage();
  await p.goto('file://'+dir+'/'+n+'.html',{waitUntil:'networkidle',timeout:120000});
  await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:dir+'/'+out[n]+'.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,
   headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#888"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
   margin:{top:'16mm',bottom:'18mm',left:'15mm',right:'15mm'}});
  await p.close(); console.log('done',n);
 }
 await b.close();
})();
