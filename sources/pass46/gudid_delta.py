# Parse AccessGUDID daily delta XMLs (2026-10-21..2026-10-27) for coronary product codes / guide brands.
import glob,json,re,csv,sys,os
import xml.etree.ElementTree as ET
os.chdir('/workspace/coronary-specs'); sys.path.insert(0,'.')
from fam import F
NS='{http://www.fda.gov/cdrh/gudid}'
rows=list(csv.DictReader(open('coronary-specs-verified.csv')))
PCS={p.strip() for r in rows for p in r['product_code'].split(',') if p.strip()}|{'NIQ','MAF','NIV','DYG','OOB','LOX','NWX','DQY','DQO','DQX','MCX','LPC','QMG','ITX','OBJ','OWQ','PNY'}
BR=[(k,re.compile(v[1])) for k,v in F.items()]
out=[]
for f in sorted(glob.glob('/workspace/gudid_delta/p46/*/*.xml')):
    for ev,el in ET.iterparse(f):
        if el.tag!=NS+'device': continue
        g=lambda t:(el.findtext(NS+t) or '')
        pcs=[p.findtext(NS+'productCode') for p in el.iter(NS+'fdaProductCode')]
        brand=g('brandName')
        fams=[k for k,rx in BR if rx.search(brand)]
        if set(pcs)&PCS or fams:
            ids=[(i.findtext(NS+'deviceId'),i.findtext(NS+'deviceIdType')) for i in el.iter(NS+'identifier')]
            subs=[s.findtext(NS+'submissionNumber') for s in el.iter(NS+'premarketSubmission')]
            out.append({'file':os.path.basename(f),'status':g('publicVersionStatus'),'ver':g('publicVersionNumber'),'vdate':g('publicVersionDate'),'pub':g('devicePublishDate'),
              'dist':g('deviceCommDistributionStatus'),'dist_end':g('deviceCommDistributionEndDate'),'di':[i for i,t in ids if t=='Primary'],'brand':brand,'version':g('versionModelNumber'),
              'catalog':g('catalogNumber'),'company':g('companyName'),'desc':g('deviceDescription')[:200],'pcs':pcs,'subs':subs,'fams':fams})
        el.clear()
json.dump(out,open('sources/pass46/raw/gudid_delta_hits.json','w'),indent=0)
print(len(out))
