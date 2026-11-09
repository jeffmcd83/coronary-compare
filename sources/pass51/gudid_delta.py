# Parse AccessGUDID daily delta XMLs (2026-11-04..2026-11-06; pass-51 gap-fill angle, captures deviceSizes) for coronary product codes / guide brands.
import glob,json,re,csv,sys,os
import xml.etree.ElementTree as ET
os.chdir('/workspace/coronary-specs'); sys.path.insert(0,'.')
from fam import F
NS='{http://www.fda.gov/cdrh/gudid}'
rows=list(csv.DictReader(open('coronary-specs-verified.csv')))
PCS={p.strip() for r in rows for p in r['product_code'].split(',') if p.strip()}|{'NIQ','MAF','NIV','DYG','OOB','LOX','NWX','DQY','DQO','DQX','MCX','LPC','QMG','ITX','OBJ','OWQ','PNY'}
BR=[(k,re.compile(v[1])) for k,v in F.items()]
out=[]
for f in sorted(glob.glob('/workspace/gudid_delta/p51/*/*.xml')):
    for ev,el in ET.iterparse(f):
        if el.tag!=NS+'device': continue
        g=lambda t:(el.findtext(NS+t) or '')
        pcs=[p.findtext(NS+'productCode') for p in el.iter(NS+'fdaProductCode')]
        brand=g('brandName')
        if re.search('vantis|crossfast|CFM6',brand+g('companyName')+g('versionModelNumber'),re.I): pcs=pcs+['__VANTIS__']
        fams=[k for k,rx in BR if rx.search(brand)]
        if set(pcs)&PCS or fams or '__VANTIS__' in pcs:
            ids=[(i.findtext(NS+'deviceId'),i.findtext(NS+'deviceIdType')) for i in el.iter(NS+'identifier')]
            subs=[s.findtext(NS+'submissionNumber') for s in el.iter(NS+'premarketSubmission')]
            out.append({'file':os.path.basename(f),'status':g('publicVersionStatus'),'ver':g('publicVersionNumber'),'vdate':g('publicVersionDate'),'pub':g('devicePublishDate'),
              'dist':g('deviceCommDistributionStatus'),'dist_end':g('deviceCommDistributionEndDate'),'di':[i for i,t in ids if t=='Primary'],'brand':brand,'version':g('versionModelNumber'),
              'catalog':g('catalogNumber'),'company':g('companyName'),'desc':g('deviceDescription')[:200],'pcs':pcs,'subs':subs,'fams':fams,'sizes':[(z.findtext(NS+'sizeType'),z.findtext(NS+'size/'+NS+'value') if False else ''.join(x.text or '' for x in z.iter() if x.tag in (NS+'value',NS+'unit')),z.findtext(NS+'sizeText')) for z in el.iter(NS+'deviceSize')]})
        el.clear()
json.dump(out,open('sources/pass51/raw/gudid_delta_hits.json','w'),indent=0)
print(len(out))
