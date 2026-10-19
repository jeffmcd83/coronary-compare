import json,csv,collections
new=json.load(open('sources/pass39/raw/recomputed_matches.json'));old=list(csv.DictReader(open('coronary-recalls.csv')))
K=lambda x:(x['model'],x['recall_number'])
N={K(x):x for x in new};O={K(x):x for x in old}
print('old',len(O),'new',len(N))
print('ONLY NEW:');[print(' ',k,v['date'],v['status'],v['_class'],v['matched_catalogs'][:80]) for k,v in N.items() if k not in O]
print('ONLY OLD:');[print(' ',k,O[k]['date'],O[k]['matched_catalogs'][:60]) for k in O if k not in N]
print('STATUS CHANGES:');[print(' ',k,O[k]['status'],'->',N[k]['status']) for k in O if k in N and O[k]['status']!=N[k]['status']]
print('OTHER FIELD CHANGES:');[print(' ',k,f,O[k][f][:70],'->',str(N[k][f])[:70]) for k in O if k in N for f in ('date','reason','matched_catalogs','n_matched','recalling_firm','event','manufacturer','category') if str(O[k][f])!=str(N[k][f])]
