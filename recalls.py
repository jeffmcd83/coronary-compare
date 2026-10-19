# Recall matcher (pass 40). Usage: python3 recalls.py [match|live] [pool.json.gz]
#   match (default): re-match offline from the stored openFDA pool (latest sources/pass*/raw/recall_pool.json.gz)
#   live: re-query openFDA (pass-39 query set: product codes + base name + PMA/510(k) numbers) and store a new pool.
# Match rules (Jeff-approved, pass 40):
#  1. IDs = row catalog numbers + GTINs, plus GUDID tuples (catalog, model, DIs) whose catalog/model is in the row.
#  2. IDs >= 5 chars: exact word-boundary match in code_info or product_description (unchanged rule).
#  3. Short IDs (3-4 chars, must contain a digit): exact match ONLY when the recall's product_description names the
#     row's base model name AND the ID appears in an explicitly labelled list (Model/Models/REF/Catalog (No./Number)/
#     Cat. No./Part No./Product Number) in code_info or the first sentence of product_description.
#     Generic narrative mentions (e.g. "The Twin-Pass catheter (Models 5200 and 5230) ...") do not count.
#  4. A recall must match at least one ID that is a row catalog number, GTIN or DI. Matches only on a GUDID
#     version/model number (e.g. Diamondback DBEC-125, SIP-3000) are dropped.
#  5. EXCL: recalls Jeff has ruled not attributable to a row.
import json,csv,re,urllib.request,urllib.parse,time,os,sys,gzip,glob
os.chdir('/workspace/coronary-specs')
EXCL={('GuideLiner V3','Z-0259-2020'):'pass 40: AnewMed multi-product list names catalog 5573, shared by GuideLiner V2 and V3; not attributable to one model',
      ('GuideLiner V3','Z-1655-2012'):'pass 40: GuideLiner V2 recall (catalog 5571 shared with V3)'}
REN={'Diamondback 360 Precision':'Diamondback 360 Coronary OAS','AngioSculpt Evo RX':'AngioSculpt RX PTCA'}
UDIF={'BioFreedom':'BioFreedom','INDIGO CAT RX':'CAT_RX','Ringer Perfusion Balloon Catheter':'Ringer_PTCA'}
LIVE=len(sys.argv)>1 and sys.argv[1]=='live'
POOLF=sys.argv[2] if len(sys.argv)>2 else sorted(glob.glob('sources/pass*/raw/recall_pool.json.gz'),key=lambda p:int(re.search(r'pass(\d+)',p).group(1)))[-1]
rows=list(csv.DictReader(open('coronary-specs-verified.csv'))); cats=json.load(open('raw/catalogs.json'))
def get_all(q):
    out=[];skip=0
    while True:
        u='https://api.fda.gov/device/recall.json?search='+urllib.parse.quote(q)+'&limit=1000&skip=%d'%skip;d=None
        for t in range(3):
            try: d=json.load(urllib.request.urlopen(u,timeout=90));break
            except urllib.error.HTTPError as e:
                if e.code==404: return out
                time.sleep(2)
            except Exception: time.sleep(2)
        if not d: print('FAIL',q,file=sys.stderr); return out
        out+=d['results'];skip+=1000
        if skip>=d['meta']['results']['total']: return out
        time.sleep(.3)
base=lambda m:re.sub(r'^(NES|Vein360|Innovative Health) Reprocessed ','',m).split(' RX')[0]
pool={}
if LIVE:
    def add(q):
        for x in get_all(q): pool[x['product_res_number']+'|'+x.get('res_event_number','')]=x
        time.sleep(.25)
    for pc in sorted({p.strip() for r in rows for p in r['product_code'].split(',') if p.strip()}): add('product_code:%s'%pc)
    for r in rows:
        add('product_description:"%s"'%base(r['model']))
        for sub in sorted(set(re.findall(r'\b([PKH]\d{6})\b',r['fda_submission']))): add(('pma_numbers:%s' if sub[0] in 'PH' else 'k_numbers:%s')%sub)
    POOLF=sys.argv[2] if len(sys.argv)>2 else 'raw/recall_pool.json.gz'
    json.dump(list(pool.values()),gzip.open(POOLF,'wt'))
else:
    pool={x['product_res_number']+'|'+x.get('res_event_number',''):x for x in json.load(gzip.open(POOLF,'rt'))}
ids={};strong={}
for r in rows:
    m=r['model']; rc={re.sub(r'\s*\(.*?\)','',c).strip() for c in r['catalog_numbers'].split(';') if c.strip()}
    rc|=set(re.findall(r'GTIN (\d{14})',r['catalog_numbers']))
    s=set(x for x in rc if x and not x.startswith('GTIN')); st=set(s)
    full=not rc or len(r['catalog_numbers'])>=3990  # build_master truncates catalog_numbers at 4000 chars: use full GUDID set
    for t in cats.get(REN.get(m,m),[]):
        if (t[0] in rc) or (t[1] in rc) or full:
            s|={x for x in t if x}; st|={x for x in t[2:] if x}
            if t[0]: st.add(t[0])
            if t[1] and (not t[0] or full): st.add(t[1])  # model no. is the orderable ID when GUDID has no catalog, or for full-set rows
    if m in UDIF and os.path.exists('raw/udi/%s.json'%UDIF[m]):
        for u in json.load(open('raw/udi/%s.json'%UDIF[m])):
            if (u.get('catalog_number') in rc) or (u.get('version_or_model_number') in rc):
                d={i['id'] for i in u.get('identifiers',[])}; s|=d; st|=d
    ids[m]=s; strong[m]=st
LAB=re.compile(r'(?<![A-Za-z0-9])(?:models?|ref|catalog(?:\s+(?:no\.?|number|#))?|cat\.?\s*(?:no\.?|#)|part\s*(?:no\.?|number|#)|product\s+number)(?![A-Za-z])\s*[:#.]?\s*([A-Za-z0-9-]*\d[A-Za-z0-9-]*(?:\s*(?:,|/|&|\band\b)\s*(?:and\s+)?[A-Za-z0-9-]*\d[A-Za-z0-9-]*)*)',re.I)
def labelled(txt): return {t for g in LAB.findall(txt) for t in re.split(r'\s*(?:,|/|&|\band\b)\s*',g) if t}
out=[];dropped=[]
for r in rows:
    m=r['model'];I=ids[m];L={i for i in I if len(i)>=5};S={i for i in I-L if 3<=len(i)<=4 and re.search(r'\d',i)}
    for x in pool.values():
        pd=x.get('product_description','') or ''; ci=x.get('code_info','') or ''; txt=ci+' '+pd
        mt={i for i in L if i in txt and re.search(r'(?<![A-Za-z0-9])'+re.escape(i)+r'(?![A-Za-z0-9])',txt)}
        if S and base(m).lower() in pd.lower():
            mt|=S & labelled(ci+' '+re.split(r'\.\s',pd,maxsplit=1)[0])
        if not mt: continue
        rn=x.get('product_res_number','')
        if not (mt & strong[m]): dropped.append((m,rn,'model-number-only match: '+'; '.join(sorted(mt))));continue
        if (m,rn) in EXCL: dropped.append((m,rn,EXCL[(m,rn)]));continue
        mt=sorted(mt)
        out.append({'manufacturer':r['manufacturer'],'model':m,'category':r['category'],'recall_number':rn,'event':x.get('res_event_number',''),
          'recalling_firm':x.get('recalling_firm',''),'status':x.get('recall_status',''),'date':x.get('event_date_initiated',''),'reason':(x.get('reason_for_recall','') or '')[:300],
          'matched_catalogs':'; '.join(mt[:20])+(' …' if len(mt)>20 else ''),'n_matched':len(mt),'source':'openFDA device recall API https://api.fda.gov/device/recall.json?search=product_res_number:"%s"'%rn})
with open('coronary-recalls.csv','w',newline='') as f:
    w=csv.DictWriter(f,list(out[0].keys()));w.writeheader();w.writerows(out)
json.dump(dropped,open('raw/recall_dropped.json','w'),indent=0)
print('pool',POOLF,len(pool),'matches',len(out),'dropped',len(dropped))
