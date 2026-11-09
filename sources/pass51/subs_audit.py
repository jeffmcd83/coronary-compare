# Pass 51 angle: 510(k) submission-completeness audit — openFDA 510(k) decisions 2024-01-01..cut for coronary product codes whose device_name matches a guide row model but whose K-number is not in that row's fda_submission.
import json,csv,re,urllib.request,time
rows=list(csv.DictReader(open('/workspace/coronary-specs/coronary-specs-verified.csv')))
out=[];allr=[]
for pc in ['LOX','DQY','DQX','MCX','QMG','DQO','OBJ','ITX','OWQ','DXO','LPC','NWX','QEF','QAN','DRG','DQK','OBI']:
  skip=0
  while True:
    u=f"https://api.fda.gov/device/510k.json?search=product_code:{pc}+AND+decision_date:[20240101+TO+20261231]&limit=1000&skip={skip}"
    try: d=json.load(urllib.request.urlopen(u))
    except Exception as e: break
    R=d['results'];allr+=R;skip+=len(R)
    if skip>=d['meta']['results']['total'] or not R: break
    time.sleep(0.3)
json.dump(allr,open('raw/k510_2024on_codes.json','w'))
def norm(s): return re.sub(r'[^a-z0-9 ]','',re.sub(r'[™®]','',s.lower()))
seen=set()
for r in allr:
  dn=norm(r['device_name'])
  for row in rows:
    m=norm(row['model']).replace(' coronary laser atherectomy','').replace(' ptca balloon catheter','').replace(' balloon catheter','')
    if len(m)<4: continue
    if re.search(r'\b'+re.escape(m)+r'\b',dn) and r['k_number'] not in row['fda_submission']:
      k=(r['k_number'],row['model'])
      if k in seen: continue
      seen.add(k);out.append(dict(k=r['k_number'],date=r['decision_date'],applicant=r['applicant'],device=r['device_name'],pc=r['product_code'],row=row['model'],row_subs=row['fda_submission'][:60]))
json.dump(out,open('raw/subs_audit.json','w'),indent=1)
print(len(allr),'decisions scanned')
for o in out: print(o['k'],o['date'],o['pc'],'|',o['applicant'][:30],'|',o['device'][:70],'=> row',o['row'],'|',o['row_subs'])
