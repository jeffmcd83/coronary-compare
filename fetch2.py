import json,urllib.request,urllib.parse,time
Q={"BioFreedom Ultra":'brand_name:BioFreedom',"Ringer PTCA":'brand_name:Ringer AND company_name:Teleflex',
"Diamondback 360 Coronary OAS":'brand_name:Diamondback',"AltaView":'brand_name:(AltaView OR "Alta View")',"CAT RX":'brand_name:"CAT RX" OR device_description:"CAT RX"',
"Mach 1":'brand_name:"MACH 1" AND company_name:Boston',"Hyperion":'brand_name:Hyperion AND company_name:Asahi',"Telescope":'brand_name:Telescope AND company_name:Medtronic',
"NC Emerge":'brand_name:Emerge AND company_name:Boston',"SYNERGY XD":'brand_name:SYNERGY AND company_name:Boston',"Integrity":'brand_name:Integrity AND company_name:Medtronic',
"AGENT":'brand_name:AGENT AND company_name:Boston',"HI-TORQUE PILOT":'brand_name:PILOT AND company_name:Abbott',"Runthrough NS":'brand_name:Runthrough OR device_description:Runthrough',
"Dragonfly OpStar":'brand_name:Dragonfly AND company_name:(Abbott OR LightLab OR St)',"Export Advance":'brand_name:Export AND company_name:Medtronic',
"COMET II":'brand_name:Comet AND company_name:Boston',"Launcher":'brand_name:Launcher AND company_name:Medtronic',"TREK RX":'brand_name:TREK AND company_name:Abbott',
"Finecross":'brand_name:Finecross OR device_description:Finecross',"Caravel":'brand_name:Caravel OR device_description:Caravel'}
for f,q in Q.items():
    out=[];skip=0
    while True:
        u='https://api.fda.gov/device/udi.json?search='+urllib.parse.quote(q)+'&limit=100&skip=%d'%skip
        try: d=json.load(urllib.request.urlopen(u,timeout=60))
        except Exception as e: print(f,'ERR',e);break
        out+=d['results'];skip+=100
        if skip>=d['meta']['results']['total'] or skip>=3000: break
    json.dump(out,open('raw/udi/'+f.replace(' ','_')+'.json','w'));print(f,len(out),sorted({r.get('brand_name','') for r in out})[:12])
