# Pass 39 weekly recall refresh: re-query openFDA device/recall, exact catalog/GTIN word-boundary match (recalls.py rule).
import json,csv,re,urllib.request,urllib.parse,time,os,sys
os.chdir('/workspace/coronary-specs'); OUT='sources/pass39/raw/'
rows=list(csv.DictReader(open('coronary-specs-verified.csv'))); cats=json.load(open('raw/catalogs.json'))
REN={'Diamondback 360 Precision':'Diamondback 360 Coronary OAS','AngioSculpt Evo RX':'AngioSculpt RX PTCA'}
UDIF={'BioFreedom':'BioFreedom','INDIGO CAT RX':'CAT_RX','Ringer Perfusion Balloon Catheter':'Ringer_PTCA'}
def get_all(q):
    out=[];skip=0
    while True:
        u='https://api.fda.gov/device/recall.json?search='+urllib.parse.quote(q)+'&limit=1000&skip=%d'%skip
        for t in range(3):
            try: d=json.load(urllib.request.urlopen(u,timeout=90));break
            except urllib.error.HTTPError as e:
                if e.code==404: return out
                time.sleep(2); d=None
            except Exception: time.sleep(2); d=None
        if not d: print('FAIL',q,file=sys.stderr); return out
        out+=d['results'];skip+=1000
        if skip>=d['meta']['results']['total']: return out
        time.sleep(.3)
pool={};qlog={}
def add(q):
    r=get_all(q);qlog[q]=len(r)
    for x in r: pool[x['product_res_number']+'|'+x.get('res_event_number','')]=x
    time.sleep(.25)
PCS=sorted({p.strip() for r in rows for p in r['product_code'].split(',') if p.strip()})
MO=len(sys.argv)>1 and sys.argv[1]=='match'
if MO: pool={x['product_res_number']+'|'+x.get('res_event_number',''):x for x in json.load(__import__('gzip').open(OUT+'recall_pool.json.gz','rt'))}
else:
  for pc in PCS: add('product_code:%s'%pc)
ids={}
for r in rows:
    m=r['model']; rc={re.sub(r'\s*\(.*?\)','',c).strip() for c in r['catalog_numbers'].split(';') if c.strip()}
    rc|=set(re.findall(r'GTIN (\d{14})',r['catalog_numbers']))
    s=set(x for x in rc if x and not x.startswith('GTIN'))
    key=REN.get(m,m)
    for t in cats.get(key,[]):
        if (t[0] in rc) or (t[1] in rc) or not rc or len(r['catalog_numbers'])>=3990: s|={x for x in t if x}  # build_master truncates catalog_numbers at 4000 chars (Launcher, Vista Brite Tip): use full GUDID set
    if m in UDIF and os.path.exists('raw/udi/%s.json'%UDIF[m]):
        for u in json.load(open('raw/udi/%s.json'%UDIF[m])):
            if (u.get('catalog_number') in rc) or (u.get('version_or_model_number') in rc):
                s|={i['id'] for i in u.get('identifiers',[])}
    ids[m]=s
    base=re.sub(r'^(NES|Vein360|Innovative Health) Reprocessed ','',m).split(' RX')[0]
    if MO: continue
    add('product_description:"%s"'%base)
    for sub in sorted(set(re.findall(r'\b([PKH]\d{6})\b',r['fda_submission']))):
        add(('pma_numbers:%s' if sub[0] in 'PH' else 'k_numbers:%s')%sub)
if not MO:
    json.dump(list(pool.values()),__import__('gzip').open(OUT+'recall_pool.json.gz','wt'))
    json.dump(qlog,open(OUT+'recall_queries.json','w'),indent=0)
json.dump({k:sorted(v) for k,v in ids.items()},open(OUT+'row_ids.json','w'))
out=[];short={}
for r in rows:
    m=r['model'];I=ids[m];L={i for i in I if len(i)>=5}
    for x in pool.values():
        txt=(x.get('code_info','') or '')+' '+(x.get('product_description','') or '')
        mt=sorted(i for i in L if i in txt and re.search(r'(?<![A-Za-z0-9])'+re.escape(i)+r'(?![A-Za-z0-9])',txt))
        sh=sorted(i for i in I-L if re.search(r'(?<![A-Za-z0-9-])'+re.escape(i)+r'(?![A-Za-z0-9-])',txt))
        if sh: short.setdefault(m,[]).append((x['product_res_number'],sh,x.get('product_description','')[:120]))
        if mt:
            out.append({'manufacturer':r['manufacturer'],'model':m,'category':r['category'],'recall_number':x.get('product_res_number',''),'event':x.get('res_event_number',''),
              'recalling_firm':x.get('recalling_firm',''),'status':x.get('recall_status',''),'date':x.get('event_date_initiated',''),'reason':(x.get('reason_for_recall','') or '')[:300],
              'matched_catalogs':'; '.join(mt[:20])+(' …' if len(mt)>20 else ''),'n_matched':len(mt),'source':'openFDA device recall API https://api.fda.gov/device/recall.json?search=product_res_number:"%s"'%x.get('product_res_number',''),
              '_class':x.get('openfda',{}).get('device_class',''),'_posted':x.get('event_date_posted',''),'_term':x.get('event_date_terminated','')})
json.dump(out,open(OUT+'recomputed_matches.json','w'),indent=0); json.dump(short,open(OUT+'short_id_hits.json','w'),indent=0)
print('pool',len(pool),'matches',len(out))
