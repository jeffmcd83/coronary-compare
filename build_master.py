import json,re,csv,collections,urllib.parse
from fam import F,CAT
def num(v):
    try: return float(v)
    except: return None
def rng(vals,unit):
    v=sorted({x for x in vals if x is not None})
    if not v: return ''
    f=lambda x:('%g'%x)
    return (f(v[0]) if len(v)==1 else f'{f(v[0])}–{f(v[-1])}')+f' {unit}'+('' if len(v)<2 else f' ({len(v)} sizes)')
def lst(vals,unit):
    v=sorted({x for x in vals if x is not None}); return ', '.join('%g'%x for x in v)+(' '+unit if v else '')
rows=[];prov={};devs={}
MMX=re.compile(r'(\d+(?:\.\d+)?)\s*(?:mm)?\s*[xX×]\s*(\d+(?:\.\d+)?)\s*(?:mm)?')
for fam,(fn,brx,inc,exc) in F.items():
    R=[r for r in json.load(open(f'raw/udi/{fn}.json')) if re.search(brx,r.get('brand_name',''))]
    CO={'Cougar':'MEDTRONIC','Wolverine Cutting Balloon':'BOSTON','Mamba':'BOSTON','GRAFTMASTER RX':'ABBOTT VASCULAR'}
    if fam in CO: R=[r for r in R if CO[fam] in r.get('company_name','').upper()]
    if inc: R=[r for r in R if re.search(inc,(r.get('device_description') or '')+' '+r.get('brand_name','')+' '+json.dumps(r.get('device_sizes')))]
    if exc: R=[r for r in R if not re.search(exc,(r.get('device_description') or '')+' '+r.get('brand_name',''))]
    cat=CAT[fam]; reproc=fam.startswith(('NES ','Vein360'))
    S=collections.defaultdict(list); cats=set(); dis=[]; subs=set(); pc=set(); comp=collections.Counter()
    for r in R:
        cats.add(r.get('catalog_number') or r.get('version_or_model_number') or '')
        di=[i['id'] for i in r.get('identifiers',[]) if i.get('type')=='Primary']; dis+=di
        comp[r.get('company_name','')]+=1
        for p in r.get('premarket_submissions') or []: subs.add(p['submission_number'])
        for p in r.get('product_codes') or []: pc.add(p['code'])
        for s in r.get('device_sizes') or []:
            t=s['type'];u=s.get('unit') or '';v=num(s.get('value'))
            if t=='Device Size Text, specify':
                m=MMX.search(s.get('text') or s.get('value') or '')
                if m and cat in('DES','BMS','Covered stent','DCB','Balloon'): S['dia'].append(float(m.group(1)));S['len'].append(float(m.group(2)))
                continue
            if v is None: continue
            if t in('Stent Diameter','Balloon Diameter') or (t=='Outer Diameter' and u=='Millimeter' and cat in('DES','BMS','Balloon')): S['dia'].append(v)
            elif t in('Stent Length','Balloon Length') or (t=='Length' and u=='Millimeter' and cat in('DES','BMS','Balloon','Covered stent')): S['len'].append(v)
            elif t=='Catheter Gauge': S['fr'].append(v)
            elif t in('Length','Catheter Length','Catheter Working Length','Shaft Length','Guidewire Length') and u=='Centimeter': S['lcm'].append(v)
            elif t in('Outer Diameter','Guidewire Diameter') and u=='Inch' and cat in('Guidewire','Imaging & physiology') and t=='Outer Diameter' or (t=='Guidewire Diameter' and cat=='Guidewire'): S['wire'].append(v)
            elif t=='Guidewire Diameter': S['gw'].append(v if u=='Inch' else round(v/25.4,3))
            elif t=='Introducer Sheath Compatibility': S['sheath'].append(v)
            elif t=='Atherectomy Rotating Component Diameter': S['burr'].append(v)
            elif t=='Lumen/Inner Diameter' and u=='Millimeter': S['id'].append(v)
            elif t=='Balloon Nominal (Inflation) Pressure': S['nom'].append(v)
        if cat in('DES','BMS','Balloon','DCB','Covered stent') and not S['dia']:
            m=MMX.search(r.get('device_description') or '')
            if m and float(m.group(1))<6: S['_ddia'].append(float(m.group(1)));S['_dlen'].append(float(m.group(2)))
    if not R: subs=set()
    man=comp.most_common(1)[0][0] if comp else ''
    q='https://api.fda.gov/device/udi.json?search='+urllib.parse.quote(f'brand_name:"{R[0]["brand_name"]}"') if R else ''
    gsrc=f'GUDID (FDA AccessGUDID via openFDA UDI) — {len(R)} device identifiers, brand "{R[0]["brand_name"] if R else ""}"; record-level device_sizes; {q}'
    if R and R[0].get('_source'):  # pass13: records pulled from AccessGUDID v3 API (not yet in openFDA UDI)
        gsrc=f'GUDID (AccessGUDID v3 device lookup API; not yet in openFDA UDI) — {len(R)} device identifiers, brand "{R[0]["brand_name"]}"; record-level device_sizes; https://accessgudid.nlm.nih.gov/devices/search?query='+urllib.parse.quote_plus('"'+R[0]['brand_name']+'"')
    def ap(s):
        return f'https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm?id={s}' if s.startswith(('P','H')) else f'https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID={s}'
    o={'category':cat,'manufacturer':man,'model':fam,'reprocessed':'Yes (third-party 510(k))' if reproc else 'No',
       'n_skus':str(len(R)) if R else '','catalog_numbers':'; '.join(sorted(c for c in cats if c))[:4000],
       'fda_submission':', '.join(sorted(subs)),'product_code':', '.join(sorted(pc)),
       'diameters_mm':lst(S['dia'] or S['_ddia'],'mm'),'lengths_mm':lst(S['len'] or S['_dlen'],'mm'),
       'french_sizes':lst(S['fr'],'Fr'),'length_cm':lst(S['lcm'],'cm'),'wire_diameter_in':lst(S['wire'],'in'),
       'guidewire_compat_in':lst(S['gw'],'in'),'sheath_compat_fr':lst(S['sheath'],'Fr'),'burr_sizes_mm':lst(S['burr'],'mm'),
       'inner_diameter_mm':lst(S['id'],'mm'),'nominal_pressure_atm':lst(S['nom'],'atm')}
    p={}
    for k in o:
        if k in('category','model','reprocessed') or not o[k]: continue
        if k=='fda_submission': p[k]='FDA premarket database via GUDID premarket_submissions; '+' ; '.join(ap(s) for s in sorted(subs)[:3])
        elif k in('diameters_mm','lengths_mm') and not (S['dia'] or S['len']): p[k]=gsrc.replace('record-level device_sizes','parsed from GUDID device_description "D x L" text')
        else: p[k]=gsrc
    rows.append(o);prov[fam]=p;devs[fam]=R
json.dump(prov,open('provenance.json','w'),indent=0)
json.dump({k:[(r.get('catalog_number'),r.get('version_or_model_number'))+tuple(i['id'] for i in r.get('identifiers',[])) for r in v] for k,v in devs.items()},open('raw/catalogs.json','w'))
SPEC={'DES':['drug','drug_dose','polymer','strut_thickness_um','platform_alloy','crossing_profile_in','max_expansion_mm','nominal_pressure_atm','rbp_atm','delivery_length_cm','guide_compat'],
'BMS':['platform_alloy','strut_thickness_um','crossing_profile_in','nominal_pressure_atm','rbp_atm','delivery_length_cm'],'Covered stent':['covering_material','platform_alloy','crossing_profile_in','delivery_length_cm','guide_compat'],
'DCB':['drug','coating_excipient','drug_dose'],'Balloon':['balloon_type','compliance','nominal_pressure_atm','rbp_atm','crossing_profile_in','tip_profile_in','shaft_length_cm'],
'Guide catheter':['curves','inner_diameter_in','side_holes'],'Guidewire':['tip_load_gf','core_material','coating','wire_use'],
'Microcatheter':['tip_od_fr','shaft_od_fr','inner_diameter_in','marker_bands'],'Guide extension':['inner_diameter_in','outer_diameter_in','guide_compat_fr'],
'Atherectomy & IVL':['mechanism','pulses_or_runs','rbp_atm','crossing_profile_in','tip_profile_in','guide_compat'],'Imaging & physiology':['modality','frequency_mhz','pullback_speed','physiology_indices'],
'Thrombectomy':['mechanism','aspiration_lumen_in']}
allspec=[];[allspec.append(x) for v in SPEC.values() for x in v if x not in allspec]
# conservative name-derived values
for o in rows:
    m=o['model'];p=prov[o['model']]
    def setv(k,v,why): o[k]=v;p[k]=why
    if o['category']=='Balloon':
        if 'Wolverine' in m: setv('balloon_type','Cutting','Brand name / GUDID product code')
        elif 'AngioSculpt' in m: setv('balloon_type','Scoring','Brand name / GUDID brand "AngioSculpt PTCA RX Scoring Balloon Catheter"')
        else: setv('balloon_type','PTCA dilatation','GUDID product code LOX (PTCA catheter)' if 'LOX' in o['product_code'] else 'Brand name')
        if m.startswith('NC '): setv('compliance','Non-compliant','Brand name prefix "NC" (manufacturer designation)')
    if o['category']=='Atherectomy & IVL':
        mech={'ROTAPRO':'Rotational','Diamondback':'Orbital','ELCA':'Excimer laser','Shockwave':'Intravascular lithotripsy'}
        for k,v in mech.items():
            if k in m: setv('mechanism',v,'FDA product code / device classification name for '+o['product_code'])
    if o['category']=='Imaging & physiology':
        mod='IVUS (solid-state)' if 'Eagle' in m else 'IVUS (rotational)' if m in('Refinity ST','OptiCross HD') else 'OCT' if 'Dragonfly' in m else 'Pressure wire' if m in('OmniWire','PressureWire X','COMET II') else 'Pressure microcatheter' if 'Navvus' in m else ''
        if mod: setv('modality',mod,'GUDID brand name / FDA product code '+o['product_code'])
exec(open('pass02_apply.py').read())
exec(open('passes_apply.py').read())
# STANDING_DECISIONS 2026-10-13: exclude devices not labeled for coronary use
EXCLUDE={"AngioJet AVX"}  # AV-access grafts/fistulae only (BSC US AngioJet page)
rows=[r for r in rows if r.get("model") not in EXCLUDE]
# STANDING_DECISIONS 2026-10-17 (Jeff): approved overrides (FDA/IFU-tier evidence replaces brochure values; old value logged in conflicts)
import glob as _gg
for _v in [dict(v,_pf=_f.split('/')[1]) for _f in sorted(_gg.glob('sources/pass*/override.csv')) for v in csv.DictReader(open(_f))]:
    _pf=_v.pop('_pf')
    _r=byname[_v['model']];_old=_r.get(_v['field'],'')
    _conf.append({'pass':_pf+'-override',**_v,'existing':_old,'existing_source':prov[_v['model']].get(_v['field'],''),'resolution':'Jeff-approved override'})
    _r[_v['field']]=_v['value'];prov[_v['model']][_v['field']]=_v['source']
json.dump(_conf,open('sources/conflicts_passes.json','w'),indent=1)
# STANDING_DECISIONS 2026-10-16 (Jeff): display rename after all passes applied (keeps earlier pass keys valid)
_S036='FDA PMA P130005/S036 (approved 2023-06-01): "design change to the 1.25mm Coronary Crown Orbital Atherectomy Device, a name change from Diamondback 360 Coronary Orbital Atherectomy System to Diamondback 360 Precision"; https://api.fda.gov/device/pma.json?search=pma_number:P130005+AND+supplement_number:S036'
RENAME={"Diamondback 360 Coronary OAS":("Diamondback 360 Precision","P130005, S036 (2023-06: 1.25 mm crown; formerly \"Diamondback 360 Coronary OAS\")")}
for r in rows:
    if r.get("model") in RENAME:
        old=r["model"];new,sub=RENAME[old];r["model"]=new;prov[new]=prov.pop(old,{})
        r["fda_submission"]=sub;prov[new]["fda_submission"]=prov[new].get("fda_submission","")+" | "+_S036
json.dump(prov,open('provenance.json','w'))
FIELDS=['category','manufacturer','model','reprocessed','n_skus','catalog_numbers','fda_submission','product_code','diameters_mm','lengths_mm','french_sizes','length_cm','wire_diameter_in','guidewire_compat_in','sheath_compat_fr','burr_sizes_mm','inner_diameter_mm']+[x for x in allspec if x!='inner_diameter_mm']
FIELDS=list(dict.fromkeys(FIELDS))
with open('coronary-specs-verified.csv','w',newline='') as f:
    w=csv.DictWriter(f,FIELDS);w.writeheader();[w.writerow({k:r.get(k,'') for k in FIELDS}) for r in rows]
json.dump(SPEC,open('spec_by_cat.json','w'))
for r in rows: r={k:r.get(k,'') for k in FIELDS};print(r['category'][:12],'|',r['model'][:30],'|',r['manufacturer'][:25],r['n_skus'],r['fda_submission'][:30],r['diameters_mm'][:40],r['french_sizes'][:30],r['length_cm'][:30],r['wire_diameter_in'][:20])
