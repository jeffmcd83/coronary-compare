# Pass 02: curated values from FDA SSED / 510(k) summaries / OEM pages. Exact model only. Executed inside build_master.py.
import csv as _csv
SS='https://www.accessdata.fda.gov/cdrh_docs/'
def U(d):
    y=int(d[1:3]); return SS+(f'pdf{y}/' if y>=10 else (f'pdf{y}/' if d[0]!='H' or y else 'pdf/'))+d+('B' if d[0] in 'PH' else '')+'.pdf'
URL={'P160043':SS+'pdf16/P160043B.pdf','P130030':SS+'pdf13/P130030B.pdf','P190020':SS+'pdf19/P190020B.pdf','H170004':SS+'pdf17/H170004B.pdf','P230035':SS+'pdf23/P230035B.pdf',
'K062877':SS+'pdf6/K062877.pdf','K063695':SS+'pdf6/K063695.pdf','K101116':SS+'pdf10/K101116.pdf','K113335':SS+'pdf11/K113335.pdf','K152447':SS+'pdf15/K152447.pdf','K161126':SS+'pdf16/K161126.pdf',
'K160583':SS+'pdf16/K160583.pdf','K163314':SS+'pdf16/K163314.pdf','K172090':SS+'pdf17/K172090.pdf','K190401':SS+'pdf19/K190401.pdf','K190473':SS+'pdf19/K190473.pdf','K192599':SS+'pdf19/K192599.pdf',
'K192886':SS+'pdf19/K192886.pdf','K193279':SS+'pdf19/K193279.pdf','K210655':SS+'pdf21/K210655.pdf','K212211':SS+'pdf21/K212211.pdf','K213593':SS+'pdf21/K213593.pdf','K223026':SS+'pdf22/K223026.pdf',
'K232584':SS+'pdf23/K232584.pdf','K230411':SS+'pdf23/K230411.pdf','K180558':SS+'pdf18/K180558.pdf','K220683':SS+'pdf22/K220683.pdf',
'MDT-OF':'https://www.medtronic.com/en-us/healthcare-professionals/products/cardiovascular/coronary-stents/onyx-frontier-drug-eluting-stent.html'}
def src(doc,pg,what): return f'{what} — {doc} p.{pg}; {URL[doc]}'
SSED=lambda d,p:src(d,p,f'FDA SSED {d}')
K=lambda d,p:src(d,p,f'FDA 510(k) summary {d}')
MO=lambda:src('MDT-OF','web','Medtronic Onyx Frontier HCP product page (Ordering information / Product details)')
PMA_DB='https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm?id='
NEW=[ # new rows: (category, manufacturer, model, submission)
 ('DES','Biosensors International','BioFreedom','P190020'),
 ('Thrombectomy','Penumbra','INDIGO CAT RX','K220683'),
 ('Imaging & physiology','Innovative Health','Innovative Health Reprocessed Eagle Eye Platinum RX','K210655'),
 ('Imaging & physiology','Innovative Health','Innovative Health Reprocessed Eagle Eye Platinum ST RX','K210655'),
]
V=[
('Resolute Onyx','drug','Zotarolimus',SSED('P160043',2)),('Resolute Onyx','drug_dose','~1.6 µg/mm²; max 317 µg (4.0×38 mm)',SSED('P160043',2)),
('Resolute Onyx','polymer','BioLinx (Parylene C primer)',SSED('P160043',3)),('Resolute Onyx','platform_alloy','Cobalt alloy shell (ASTM F562) + platinum-iridium core; single wire',SSED('P160043',2)),
('Resolute Onyx','nominal_pressure_atm','12 atm',SSED('P160043',3)),('Resolute Onyx','rbp_atm','18 atm (2.25–4.0 mm); 16 atm (4.5–5.0 mm RX)',SSED('P160043',3)),
('Resolute Onyx','guide_compat','≥5 Fr (min ID 1.42 mm / 0.056 in)',SSED('P160043',3)),
('Onyx Frontier','drug','Zotarolimus',MO()),('Onyx Frontier','drug_dose','51–317 µg nominal by size',MO()),('Onyx Frontier','polymer','BioLinx',MO()),
('Onyx Frontier','platform_alloy','Cobalt alloy shell + platinum-iridium core; single wire',MO()),('Onyx Frontier','max_expansion_mm','3.50 (2.0–2.5); 4.00 (2.75–3.0); 5.00 (3.5–4.0); 6.00 (4.5–5.0)',MO()),
('REBEL','platform_alloy','Platinum chromium (PtCr)',SSED('P130030',2)),('REBEL','strut_thickness_um','81 (2.25–3.50 mm); 86 (4.00–4.50 mm)',SSED('P130030',2)),
('REBEL','nominal_pressure_atm','11 atm',SSED('P130030',2)),('REBEL','rbp_atm','18 atm',SSED('P130030',2)),('REBEL','delivery_length_cm','144 cm',SSED('P130030',2)),
('BioFreedom','drug','Biolimus A9 (BA9)',SSED('P190020',2)),('BioFreedom','polymer','Polymer-free (abluminal BA9 on micro-structured surface)',SSED('P190020',2)),
('BioFreedom','strut_thickness_um','119 (6-crown, 2.25–3.0 mm); 114 (9-crown, 3.5–4.0 mm)',SSED('P190020',2)),('BioFreedom','platform_alloy','316L stainless steel',SSED('P190020',2)),
('BioFreedom','diameters_mm','2.25, 2.5, 2.75, 3, 3.5, 4 mm',SSED('P190020',2)),('BioFreedom','lengths_mm','8, 11, 14, 18, 24, 28 mm',SSED('P190020',2)),
('BioFreedom','nominal_pressure_atm','7 atm',SSED('P190020',2)),('BioFreedom','rbp_atm','16 atm (6-crown); 14 atm (9-crown)',SSED('P190020',2)),
('BioFreedom','delivery_length_cm','142 cm',SSED('P190020',2)),('BioFreedom','guide_compat','≥6 Fr (min ID 0.070 in / 1.78 mm)',SSED('P190020',2)),
('PK Papyrus','covering_material','Electrospun siloxane-based polyurethane (abluminal)',SSED('H170004',2)),('PK Papyrus','platform_alloy','L605 cobalt chromium, proBIO a-SiC:H coated',SSED('H170004',2)),
('PK Papyrus','diameters_mm','2.5, 3, 3.5, 4, 4.5, 5 mm',SSED('H170004',2)),('PK Papyrus','lengths_mm','15, 20, 26 mm',SSED('H170004',2)),
('PK Papyrus','delivery_length_cm','140 cm',SSED('H170004',2)),('PK Papyrus','guide_compat','Guide ID ≥0.056 in (1.42 mm); 0.014 in wire',SSED('H170004',3)),
('AGENT','drug','Paclitaxel',SSED('P230035',2)),('AGENT','coating_excipient','Acetyl tributyl citrate (ATBC), 20% of coating by weight',SSED('P230035',4)),
('Twin-Pass','inner_diameter_in','Dual lumen: OTW ≤0.018 in wire; RX ≤0.014 in wire (Twin-Pass .023")',K('K062877',2)),('Twin-Pass','marker_bands','1 distal radiopaque marker band',K('K062877',2)),
('Runthrough NS','core_material','Ni/Ti + stainless steel joined core',K('K063695',1)),('Runthrough NS','coating','Silicone and/or hydrophilic (by product code)',K('K063695',1)),
('HI-TORQUE PILOT','coating','Hydrophilic over polyurethane-covered distal section',K('K101116',1)),
('Heartrail III','inner_diameter_in','',None),
('Caravel','tip_od_fr','Distal OD 0.62 mm; proximal 0.85 mm (nominal)',K('K152447',5)),
('Corsair Pro','shaft_od_fr','Nominal OD 0.93 mm',K('K161126',5)),('Corsair Pro','marker_bands','No marker (per comparison table)',K('K161126',6)),
('Refinity ST','pullback_speed','Imaging core travel up to 15 cm (telescoping section)',K('K160583',5)),
('Guidezilla II','marker_bands','',None),
('GuideLiner V3','length_cm','150 cm working length (125 cm SS pushrod)',K('K172090',4)),
('Mamba','inner_diameter_in','Accepts ≤0.014 in guidewires',K('K190401',5)),
('Navvus II','physiology_indices','FFR, resting Pd/Pa',K('K190473',5)),('Navvus II','wire_diameter_in','Rides over 0.014 in wire; max profile 2.7 F (0.036 in) at sensor',K('K190473',4)),
('Gaia Next','core_material','Stainless steel',K('K192599',5)),('Gaia Next','coating','Hydrophilic, distal 40 cm',K('K192599',5)),
('OmniWire','coating','Hydrophilic distal 39 cm; proximal 146 cm coating',K('K192886',4)),
('COMET II','physiology_indices','FFR',K('K193279',5)),('PressureWire X','physiology_indices','FFR',K('K180558',6)),
('Turnpike','guidewire_compat_in','0.014 in',K('K212211',5)),
('OptiCross HD','frequency_mhz','60 MHz',K('K213593',6)),('OptiCross HD','pullback_speed','Imaging core travel 15 cm (telescoping section)',K('K213593',5)),
('Dragonfly OpStar','modality','OCT (near-infrared, rotating fiber-optic core)',K('K230411',4)),
('NES Reprocessed Eagle Eye Platinum RX','french_sizes','3.5 Fr',K('K223026',6)),('NES Reprocessed Eagle Eye Platinum RX','sheath_compat_fr','5 Fr',K('K223026',6)),('NES Reprocessed Eagle Eye Platinum RX','guidewire_compat_in','0.014 in',K('K223026',6)),
('Vein360 Reprocessed Eagle Eye Platinum RX','french_sizes','3.5 Fr',K('K232584',7)),('Vein360 Reprocessed Eagle Eye Platinum RX','sheath_compat_fr','5 Fr',K('K232584',7)),('Vein360 Reprocessed Eagle Eye Platinum RX','length_cm','150 cm',K('K232584',7)),('Vein360 Reprocessed Eagle Eye Platinum RX','guidewire_compat_in','0.014 in',K('K232584',7)),
('Innovative Health Reprocessed Eagle Eye Platinum RX','french_sizes','3.5 Fr',K('K210655',6)),('Innovative Health Reprocessed Eagle Eye Platinum RX','guidewire_compat_in','0.014 in',K('K210655',6)),('Innovative Health Reprocessed Eagle Eye Platinum RX','length_cm','150 cm',K('K210655',6)),('Innovative Health Reprocessed Eagle Eye Platinum RX','catalog_numbers','85900P (OEM item reprocessed)',K('K210655',6)),
('INDIGO CAT RX','mechanism','Aspiration (Penumbra pump)',K('K220683',4)),
]
SUB={'XIENCE Skypoint':('P110019','FDA PMA DB: P110019 supplements (e.g., S113 2021-05-13) trade name "XIENCE Skypoint"; '+PMA_DB+'P110019'),
'XIENCE Sierra':('P110019','FDA PMA DB: P110019 supplements (e.g., S096 2018-03-05) incl. "Sierra"; '+PMA_DB+'P110019'),
'Orsiro Mission':('P170030','FDA PMA DB: P170030 S036/S046 "Orsiro Mission"; '+PMA_DB+'P170030'),
'MULTI-LINK 8':('P020047','FDA PMA DB: P020047 "MULTI-LINK 8 and MULTI-LINK 8 LL"; '+PMA_DB+'P020047'),
'PK Papyrus':('H170004','FDA HDE H170004 SSPB p.1; '+SS+'pdf17/H170004B.pdf'),
'Diamondback 360 Coronary OAS':('P130005','FDA SSED P130005 p.1; '+SS+'pdf13/P130005B.pdf'),
'Shockwave C2 Aero':(None,None),
'GuideLiner V3':('K172090','FDA 510(k) K172090 "GuideLiner V3 Catheter"; '+SS+'pdf17/K172090.pdf'),
'Heartrail III':('K113335','FDA 510(k) K113335 "HEARTRAIL III GUIDING CATHETER"; '+SS+'pdf11/K113335.pdf'),
'Gaia Next':('K192599','FDA 510(k) K192599 "ASAHI Gaia Next"; '+SS+'pdf19/K192599.pdf'),
'HI-TORQUE PILOT':('K101116','FDA 510(k) K101116 "HI-TORQUE PILOT 50 and 150"; '+SS+'pdf10/K101116.pdf'),
'Runthrough NS':('K063695','FDA 510(k) K063695 "RUNTHROUGH NS"; '+SS+'pdf6/K063695.pdf'),
'SION black':('K173277','FDA 510(k) K173277 "ASAHI SION black"; https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K173277'),
'Guidezilla II':('K163314','FDA 510(k) K163314 "Guidezilla II"; '+SS+'pdf16/K163314.pdf'),
'Mamba':('K190401','FDA 510(k) K190401 "MAMBA and MAMBA Flex"; '+SS+'pdf19/K190401.pdf'),
'Corsair Pro':('K161126','FDA 510(k) K161126 "ASAHI Corsair Pro"; '+SS+'pdf16/K161126.pdf'),
'Caravel':('K152447','FDA 510(k) K152447 "ASAHI Caravel"; '+SS+'pdf15/K152447.pdf'),
'OptiCross HD':('K213593','FDA 510(k) K213593 "OptiCross HD"; '+SS+'pdf21/K213593.pdf'),
'Dragonfly OpStar':('K230411','FDA 510(k) K230411 "Dragonfly OpStar Imaging Catheter"; '+SS+'pdf23/K230411.pdf'),
'COMET II':('K193279','FDA 510(k) K193279 "Comet II Pressure Guidewire"; '+SS+'pdf19/K193279.pdf'),
'ROTAPRO':('K220962','FDA 510(k) K220962 "ROTAPRO" (also P900056 per GUDID); '+SS+'pdf22/K220962.pdf'),
'BioFreedom':('P190020',SSED('P190020',1)),'INDIGO CAT RX':('K220683',K('K220683',1)),
'Innovative Health Reprocessed Eagle Eye Platinum RX':('K210655',K('K210655',1)),
'Telescope':('K252390','FDA 510(k) DB K183353 (2019) and K252390 (2025) "Telescope Guide Extension Catheter"; '+SS+'pdf18/K183353.pdf')}
CONF=[]
byname={r['model']:r for r in rows}
for c,m,mo,s in NEW:
    if mo not in byname:
        o={'category':c,'manufacturer':m,'model':mo,'reprocessed':'Yes (third-party 510(k))' if 'Reprocessed' in mo else 'No'};rows.append(o);byname[mo]=o;prov[mo]={}
for mo,(s,why) in SUB.items():
    r=byname.get(mo)
    if not r or not s: continue
    if r.get('fda_submission') and s not in r['fda_submission']: CONF.append((mo,'fda_submission',r['fda_submission'],s,why)); r['fda_submission']=r['fda_submission']+', '+s; prov[mo]['fda_submission']=prov[mo].get('fda_submission','')+' | '+why
    elif not r.get('fda_submission'): r['fda_submission']=s;prov[mo]['fda_submission']=why
for mo,f,v,w in V:
    if not v: continue
    r=byname[mo]
    if r.get(f) and r[f]!=v: CONF.append((mo,f,r[f],v,w));continue
    r[f]=v;prov[mo][f]=w
r=byname['Innovative Health Reprocessed Eagle Eye Platinum RX'];r['modality']='IVUS (solid-state)';prov[r['model']]['modality']=K('K210655',5)
import json as _j
_j.dump([{'pass':2,'model':a,'field':b,'existing':c,'candidate':d,'source':e} for a,b,c,d,e in CONF],open('sources/pass02/conflicts.json','w'),indent=1)
_j.dump([{'pass':2,'table':'spec','model':a,'field':b,'new':c,'source':d} for a,b,c,d in V if c]+[{'pass':2,'table':'spec','model':a,'field':'fda_submission','new':s,'source':w} for a,(s,w) in SUB.items() if s],open('sources/pass02/applied.json','w'),indent=1)
_j.dump(prov,open('provenance.json','w'))
print('pass02 conflicts',len(CONF))
for x in CONF: print('  ',x[:4])
