import json,urllib.request,urllib.parse,time,os
os.chdir('/workspace/coronary-specs')
OUT='sources/pass58/raw/'

def get_all(ep,q):
    out=[];skip=0; meta={}
    while True:
        u=f'https://api.fda.gov/device/{ep}.json?search='+urllib.parse.quote(q,safe=':[]+')+'&limit=1000&skip=%d'%skip
        try:
            d=json.load(urllib.request.urlopen(u,timeout=90))
        except urllib.error.HTTPError as e:
            if e.code==404:
                return out, {'empty':True}
            print('ERR',e.code,u); return out, {'error':e.code,'url':u}
        out+=d['results'];skip+=1000
        meta=d.get('meta',{})
        if skip>=d['meta']['results']['total']:
            return out, meta
        time.sleep(.3)

# Recalls posted since last weekly review window (pass 55 reviewed through 2026-11-18; cut was 11-14)
rec, meta = get_all('recall', 'event_date_posted:[20261114+TO+20261125]')
json.dump(rec, open(OUT+'recalls_posted_since1114_all.json','w'))
print('recalls posted 11-14..11-25:', len(rec), 'meta.last_updated', meta.get('last_updated'))

# Also the tighter new-only window after pass 55's last reviewed posted date
rec2, meta2 = get_all('recall', 'event_date_posted:[20261119+TO+20261125]')
json.dump(rec2, open(OUT+'recalls_posted_since1119.json','w'))
print('recalls posted 11-19..11-25:', len(rec2), 'meta.last_updated', meta2.get('last_updated'))

# Enforcement report_date since after pass-55 window (pass 55 used >=2026-11-05, all were 11-11)
enf, emeta = get_all('enforcement', 'report_date:[20261112+TO+20261125]')
json.dump(enf, open(OUT+'enforcement_since_1112.json','w'))
print('enforcement report_date>=2026-11-12:', len(enf), 'meta.last_updated', emeta.get('last_updated'))
if enf:
    print(' sample keys', sorted(enf[0].keys())[:40])
    dates={}
    for x in enf:
        dates[x.get('report_date','?')]=dates.get(x.get('report_date','?'),0)+1
    print(' report_date counts', dates)

# All 510(k) and PMA decisions since previous cut (2026-11-09, swept in pass 55)
k, kmeta = get_all('510k', 'decision_date:[20261109+TO+20261125]')
p, pmeta = get_all('pma', 'decision_date:[20261109+TO+20261125]')
json.dump({'510k':k,'pma':p,'k_meta':{'last_updated':kmeta.get('last_updated')}, 'p_meta':{'last_updated':pmeta.get('last_updated')}},
          open(OUT+'all_decisions_1109_1125.json','w'))
print('510k decisions 11-09..11-25:', len(k), 'pma:', len(p), 'k_cut', kmeta.get('last_updated'), 'p_cut', pmeta.get('last_updated'))
