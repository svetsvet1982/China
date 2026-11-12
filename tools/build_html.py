import glob,re,sys,markdown,html
SP=sys.argv[1]
files=sorted(glob.glob('/home/user/China/대화문/第*.md'), key=lambda f:int(re.search(r'第(\d+)集',f).group(1)))
parts=[(1,10,"1부 春 (봄)","HSK 3~4급 · 2026년 3~5월"),(11,20,"2부 夏 (여름)","HSK 4~5급 · 2026년 6~8월"),(21,30,"3부 秋 (가을)","HSK 5~6급 · 2026년 9~11월"),(31,40,"4부 冬 (겨울)","HSK 6~7급 · 2026.12~2027.2"),(41,48,"5부 新春 (이듬해 봄)","HSK 7~9급 · 2027년 2~4월")]
CSS="""
@page{size:A4}
body{font-family:'Noto Serif CJK SC',serif;font-size:10.5pt;line-height:1.75;color:#1d1d1d}
h1{font-family:'Noto Sans CJK SC',sans-serif;font-size:19pt;color:#7a1f1f;border-bottom:2px solid #7a1f1f;padding-bottom:4px;margin-top:0}
h2{font-family:'Noto Sans CJK SC',sans-serif;font-size:13pt;color:#7a1f1f;margin-top:18px}
h3{font-family:'Noto Sans CJK SC',sans-serif;font-size:11pt;background:#f3ece4;padding:3px 8px;border-left:4px solid #7a1f1f}
.ep{page-break-before:always}
p{margin:4px 0}
ul{margin:4px 0 8px 18px;padding:0;font-size:9.5pt}
table{border-collapse:collapse;width:100%;font-size:8.8pt;margin:6px 0;page-break-inside:auto}
th,td{border:1px solid #bbb;padding:3px 5px;vertical-align:top}
th{background:#7a1f1f;color:#fff}
tr{page-break-inside:avoid}
hr{border:none;border-top:1px dashed #aaa;margin:12px 0}
.cover{text-align:center;padding-top:70mm}
.cover h1{border:none;font-size:30pt}
.cover p{font-family:'Noto Sans CJK SC';font-size:12pt;color:#555}
.part{page-break-before:always;text-align:center;padding-top:90mm}
.part h1{border:none;font-size:26pt}
.toc{page-break-before:always}
.toc li{list-style:none;font-size:10pt}
"""
def ep_html(f):
    t=open(f).read()
    return '<section class="ep">'+markdown.markdown(t,extensions=['tables'])+'</section>'
def build(sel,name,title,sub):
    out=['<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>']
    out.append(f'<div class="cover"><h1>《槐荫胡同十七号》</h1><p>표준중국어 연속 대화문</p><p>{html.escape(title)}</p><p>{html.escape(sub)}</p></div>')
    out.append('<div class="toc"><h1>목차</h1><ul>')
    for a,b,pt,ps in parts:
        lst=[f for f in files if a<=int(re.search(r'第(\d+)集',f).group(1))<=b and f in sel]
        if not lst: continue
        out.append(f'<li><b>{pt}</b> · {ps}</li>')
        for f in lst: out.append('<li>&nbsp;&nbsp;'+html.escape(open(f).readline().lstrip('# ').strip())+'</li>')
    out.append('</ul></div>')
    for a,b,pt,ps in parts:
        lst=[f for f in files if a<=int(re.search(r'第(\d+)集',f).group(1))<=b and f in sel]
        if not lst: continue
        if len(sel)>10: out.append(f'<div class="part"><h1>{pt}</h1><p>{ps}</p></div>')
        out+= [ep_html(f) for f in lst]
    out.append('</body></html>')
    open(f'{SP}/{name}.html','w').write('\n'.join(out))
build(files,'all','전 48화 (5부)','2026년 3월 ~ 2027년 4월')
for i,(a,b,pt,ps) in enumerate(parts,1):
    build([f for f in files if a<=int(re.search(r'第(\d+)集',f).group(1))<=b],f'part{i}',pt,ps)
print('ok')
