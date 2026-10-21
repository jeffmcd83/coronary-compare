import json,urllib.request,urllib.parse,time,csv,re,os
os.chdir('/workspace/coronary-specs');OUT='sources/pass43/raw/'
def get_all(ep,q):
    out=[];skip=0
    while True:
        u=f'https://api.fda.gov/device/{ep}.json?search='+urllib.parse.quote(q,safe=':[]+')+'&limit=1000&skip=%d'%skip
        try: d=json.load(urllib.request.urlopen(u,timeout=90))
        except urllib.error.HTTPError as e:
            if e.code==404: return out
            print('ERR',e.code,u);return out
        out+=d['results'];skip+=1000
        if skip>=d['meta']['results']['total']: return out
        time.sleep(.3)
rows=list(csv.DictReader(open('coronary-specs-verified.csv')))
PMAS=sorted({s for r in rows for s in re.findall(r'\b([PH]\d{6})\b',r['fda_submission'])})
PCS=sorted({p.strip() for r in rows for p in r['product_code'].split(',') if p.strip()}|{'PNY','DQX','DQY','LOX','NIQ','MAF','NWX','OOB','MCX','LPC','QMG','NIV','DYG'})
D='[20260901+TO+20261231]'
res={'pmas':PMAS,'pcs':PCS,'pma_supp':{},'pma_pc':{},'k_pc':{},'k_reproc':{}}
for p in PMAS:
    res['pma_supp'][p]=get_all('pma',f'pma_number:{p}+AND+decision_date:{D}');time.sleep(.3)
for pc in PCS:
    res['pma_pc'][pc]=get_all('pma',f'product_code:{pc}+AND+decision_date:{D}');time.sleep(.3)
    res['k_pc'][pc]=get_all('510k',f'product_code:{pc}+AND+decision_date:{D}');time.sleep(.3)
for a in ['Innovative','Stryker','Sustainability','"North East Scientific"','NES','Vein360','SterilMed','ReNewal','Medline','reprocess*']:
    res['k_reproc'][a]=get_all('510k',f'applicant:{a}+AND+decision_date:{D}');time.sleep(.3)
res['k_reproc']['devname_reprocessed']=get_all('510k',f'device_name:reprocessed+AND+decision_date:{D}')
json.dump(res,open(OUT+'newmodels_openfda.json','w'),indent=0)
for k in ['pma_supp','pma_pc','k_pc','k_reproc']:
    print(k,{a:len(b) for a,b in res[k].items() if b})
