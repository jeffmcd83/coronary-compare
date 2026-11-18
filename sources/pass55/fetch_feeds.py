import json,urllib.request,urllib.parse,time,os
os.chdir('/workspace/coronary-specs')
OUT='sources/pass55/raw/'

def get_all(ep,q):
    out=[];skip=0
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

# 1) Recalls posted since last reviewed window start (pass 52 reviewed through 2026-11-11; cut was 11-07)
rec, meta = get_all('recall', 'event_date_posted:[20261107+TO+20261118]')
json.dump(rec, open(OUT+'recalls_posted_since1107_all.json','w'))
print('recalls posted 11-07..11-18:', len(rec), 'meta.last_updated', meta.get('last_updated'))

# 2) Enforcement report_date since day after pass-52 window start-overlap (pass 52 used >=2026-10-29; use >=2026-11-05)
enf, emeta = get_all('enforcement', 'report_date:[20261105+TO+20261118]')
json.dump(enf, open(OUT+'enforcement_since_1105.json','w'))
print('enforcement report_date>=2026-11-05:', len(enf), 'meta.last_updated', emeta.get('last_updated'))
if enf:
    print(' sample keys', sorted(enf[0].keys()))
    print(' date fields', {k:enf[0].get(k) for k in enf[0] if 'date' in k.lower() or k in ('recall_number','status','event_id','code_info')})

# 3) All 510(k) and PMA decisions since previous cut (2026-11-02)
k, kmeta = get_all('510k', 'decision_date:[20261102+TO+20261118]')
p, pmeta = get_all('pma', 'decision_date:[20261102+TO+20261118]')
json.dump({'510k':k,'pma':p,'k_meta':{kk:kmeta.get(kk) for kk in ('last_updated',) if kmeta}, 'p_meta':{kk:pmeta.get(kk) for kk in ('last_updated',) if pmeta}},
          open(OUT+'all_decisions_1102_1118.json','w'))
print('510k decisions 11-02..11-18:', len(k), 'pma:', len(p))
