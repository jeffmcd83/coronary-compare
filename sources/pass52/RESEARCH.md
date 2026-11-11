# Pass 52: weekly recall and new-model refresh (Wed 2026-11-11, ~8:57–9:20 AM ET). No-op for data.

Result: **no new recalls, no new models, no spec changes.** Recalls stay at 110 (19 rows). Fill unchanged 90.9% (921/1013; 76 rows).

## openFDA data cut dates (meta.last_updated, queried 2026-11-11 ~8:57 ET)
- device/recall: **2026-11-07** (59,705 records; pass 49: 2026-10-31 / 59,659)
- device/enforcement: **2026-11-04** (40,481; pass 49: 2026-10-28)
- device/510k and device/pma: **2026-11-02** (pass 49/51: 2026-10-26)
- device/udi: **2026-11-02** (5,182,695; pass 49: 2026-10-01)
- AccessGUDID daily deltas parsed: 2026-11-09, 2026-11-10 (11-07, 11-08, 11-11 not published/404; weekend/not yet). Pass 51 covered 11-04..11-06. Files off-repo in /workspace/gudid_delta/p52/.

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass52/raw/recall_pool.json.gz`: pool 2,058 recall products (identical key set and recall_status to pass 49: 0 new, 0 gone, 0 status changes); 110 matches, 3 dropped. coronary-recalls.csv and raw/recall_dropped.json remained byte-identical to the pre-pass52 backups.
- All recall products posted 2026-10-31…11-11 (44; `raw/recalls_posted_since1031_all.json`) reviewed: Cardinal Health Presource kits (BD Alaris sets), Edwards Commander M delivery system Z-0287 (structural/TAVI), GE Senographe, Baxter operating tables, Henry Schein sutures, Shimadzu Trinias angiography system Z-0347 (cath-lab x-ray, not a guide row), AVID packs, Cochlear, restor3d, Corin, Remel, Luminex, Intelerad. **None is a coronary interventional device in the guide.**
- Direxion microcatheter Z-0223…0263-2027 (peripheral): still not a guide row, not added.
- FDA Recalls & Early Alerts page: curl fetched; no coronary/catheter/stent/guidewire/balloon/atherectomy/Impella keyword hits (page may be JS-rendered, so treat as weak evidence); openFDA posts above show no coronary item.

## 2. Enforcement endpoint
- Reports with report_date ≥ 2026-10-29 (31; `raw/enforcement_since_1029.json`) mapped and run through `recalls.py match` → **0 matches** (script crashed on empty result as documented; CSV and raw/recall_dropped.json restored, verified byte-identical to backups). Keyword scan: Medtronic OmniaSecure lead (CRM), Abiomed Impella controllers Z-0208…0210 (not coronary guide rows). None relevant.

## 3. New models / submissions
- `sources/pass52/newmodels.py` (window 2026-09-01→; `raw/newmodels_openfda.json`): nothing new vs pass 49 (same P900056 S226/S228/S229, K262917, K260708, etc.).
- All 510(k) (95) and PMA (66) decisions 2026-10-26→11-11 (`raw/all_decisions_1026_1111.json`). Cardiovascular items:
  - K263596 Medtronic DLP Coronary Ostial Cannulae (DWF, SE 2026-10-29, special 510(k)): CPB cardioplegia delivery cannula for surgery ("conditions requiring CPB procedures up to 6 hours... delivery of cardioplegia solutions directly to the coronary arteries"); labeling-only change. Surgical, not a coronary interventional device; not a candidate. https://www.accessdata.fda.gov/cdrh_docs/pdf26/K263596.pdf
  - K263076 AngioDynamics AngioVac F1885 (venous), K262839 Cleerly ISCHEMIA (CT software), K261886 Catheter Precision VIVO (EP), K262864 Expanse FLOWRUNNER (neuro aspiration), PMA supplements for CRM, VADs, Edwards SAPIEN/EVOQUE/INSPIRIS/PERIMOUNT, Abbott Navitor, Amplatzer Paraclose (P260019, structural), Perclose ProStyle, Abre, CELT. No coronary interventional model; no reprocessed coronary 510(k).
- GUDID deltas (`raw/gudid_delta_hits.json`, 5 hits): Mindray ultrasound (ITX), Euroimmun reagent (brand-regex false positive), Piraeus Medical "35 Helix Guidewire" 100590 (K260751, MOF/DQX; 0.035" 180 cm peripheral). No new or updated DI for any guide row.

## 4. Watch items
- CrossFAST CFM60 (K262817): AccessGUDID "CFM60" → 0 results; openFDA UDI (cut 11-02) → CFM55 only. Dims unpublished; CFM55 not copied.
- IMDS NHanceIT (K260559): AccessGUDID 0 results.
- Skycade K260168: closed in pass 50 (peripheral only).
- Direxion: not in guide.
- Pass 51 pending suggestions (Euphora K261759, Navvus II K233904, balloon candidates) untouched, waiting for Jeff.

## 5. Files
Backups: *.pre-pass52 (recalls, supplier rollup, specs, provenance, app/build.py, raw/recall_dropped). values.csv header-only; conflicts.json empty. coronary-recalls-by-supplier.csv unchanged (recalls identical).
