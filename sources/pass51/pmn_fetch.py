# Pass 51: FDA 510(k) database (accessdata cfpmn) by product code, decisions 2026-10-20..11-09 (newer than openFDA 510k cut 2026-10-26). Headless Chrome (public page; JS wait page only).
import sys,re,time
from playwright.sync_api import sync_playwright
PCS=sys.argv[1:] or ['DQY','DQX','LOX','MCX','QMG','NIQ','PNY','OBJ','DQO','DYB','LIT','QAN','QBZ','QEF','MAF','NWX','ITX','OOB']
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page()
  for pc in PCS:
    u=f"https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?start_search=1&productcode={pc}&decisiondatefrom=10%2F20%2F2026&decisiondateto=11%2F09%2F2026&pagenum=100"
    pg.goto(u,timeout=90000)
    for i in range(20):
      h=pg.content()
      if 'being processed' not in h and 'Object Moved' not in h: break
      time.sleep(5)
    open(f'raw/pmn_{pc}.html','w').write(h)
    t=re.sub('<[^>]+>',' ',h)
    print(pc,len(h),sorted(set(re.findall(r'K2\d{5}',h))), 'No records' if re.search('No records|no records',t) else '')
