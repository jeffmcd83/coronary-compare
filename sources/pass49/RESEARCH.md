# Pass 49: weekly recall and new-model refresh (Wed 2026-11-04, ~08:50–09:30 AM ET). No-op for data.

Result: **no new recalls, no new models, no spec changes.** Recalls stay at 110 (19 rows; 4 Open, Classified, 106 Terminated). Fill unchanged 90.9% (921/1013; 76 rows).

## openFDA data cut dates (meta.last_updated, queried 2026-11-04 ~08:55 ET)
- device/recall: **2026-10-31** (59,659 records; pass 46 saw 2026-10-24 / 59,618)
- device/enforcement: **2026-10-28** (40,450; pass 46 saw 2026-10-21 / 40,358)
- device/510k and device/pma: **2026-10-26** (pass 46 saw 2026-10-19)
- device/udi: 2026-10-01 (unchanged). AccessGUDID deltas 2026-10-28, 10-29, 10-30 (from weekly zip 20261026_20261030), 11-02, 11-03 parsed (pass 46 covered to 10-27). Files kept off-repo in /workspace/gudid_delta/p49/.

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass49/raw/recall_pool.json.gz` (pass-40 rules, unchanged): pool 2,058 recall products (identical key set to pass 46: 0 new, 0 gone, 0 recall_status changes; other diffs are openFDA re-enrichment / whitespace only). 110 matches, 3 dropped (Jeff-ruled Diamondback model-number-only; raw/recall_dropped.json unchanged).
- coronary-recalls.csv regenerated **byte-identical** to coronary-recalls.pre-pass49.csv; coronary-recalls-by-supplier.csv regenerated, byte-identical (110).
- All recall products posted since 2026-10-20 (123; `raw/recalls_posted_since1020.json`) reviewed by hand. New since pass 46 (posted 10-23…10-30): Abiomed Impella controllers Z-0208…0210-2027, Canon Alphenix and Philips Azurion angiography systems Z-0289…0300-2027 (cath-lab x-ray systems, not guide rows), Medtronic OmniaSecure lead / SmartSync (CRM), Philips 712010, Pentax EUS, Tandem, Illumina, Artivion CryoPatch, Smith & Nephew, etc. **None is a coronary interventional device in the guide.**
- BSC **Direxion** microcatheter Z-0223…0263-2027 (peripheral, KRA/K163701): still not a guide row, no catalog/GTIN/DI/510(k) match. Not added.
- FDA "Medical Device Recalls and Early Alerts" page (checked 2026-11-04): no coronary item. New since pass 46: Compact Medical ButterflyBVM (11/03), IL HemosIL AcuStar HIT-IgG (10/30), Medline beds (10/29), B. Braun Streamline update (11/02), Nova StatStrip update (10/30). BSC Imager II angiographic catheter (09/25) is not a guide row.

## 2. Enforcement endpoint (device/enforcement)
- All reports with report_date ≥ 2026-10-22 (92, all 2026-10-28; `raw/enforcement_since_1022.json`) mapped to recall-pool format and run through the recalls.py matcher (`python3 recalls.py match /tmp/enf49.json.gz`): **0 matches** (recalls.py exits on an empty result; CSV + raw/recall_dropped.json restored and verified byte-identical). Keyword scan: Direxion (41, as above), Abbott Amulet LAA occluder Z-0191-2027 (structural, out of scope), Medtronic navigation/MiniMed/InterStim, Philips Lumify/Smart-hopping. None coronary.

## 3. New models / submissions
- `sources/pass49/newmodels.py` (pass-46 script, window 2026-09-01→; `raw/newmodels_openfda.json`). New vs pass 46:
  - **P900056/S226, S228, S229** (ROTAPRO, 2026-10-20/21): console Pneumatic Kit component design change + two 30-day PCBA process notices. No new model/trade name; no spec impact.
  - K254255 Wellysis S-Patch CardioAI, K263380 Rhythm AI STAR Apollo (DQK; ECG/EP), K260708 Vein360 reprocessed LithoVue ureteroscope, K262386 Stryker SafeAir, K262917 Innovative Health reprocessed BRK transseptal needle (NMK; EP/structural). Not coronary.
- All 510(k) decisions since 2026-10-19 (63) and PMA decisions since 2026-10-17 (48) (`raw/all_decisions_1019_1026.json`): cardiovascular items are Zylox PanFlex PTA scoring catheter (K260686, PNO, peripheral), Toro 71 aspiration (NRY, neuro), Aventusoft/Monebo software, and PMA supplements for CRM, VADs, renal denervation, Edwards PASCAL/EVOQUE/SAPIEN/INSPIRIS (structural, out of scope), Liverty TIPS, Embrace embolic. **No new coronary model; no reprocessed coronary 510(k).**
- GUDID deltas (`raw/gudid_delta_hits.json`, 23 hits): no new or updated DI for any guide row. Hits: Parallel Design ITX probes, Stryker AXS Lift / Seigla LiquID (DQY updates; neuro), MEDTECH "(V3)" navigation probes (brand-regex false positive on GuideLiner V3; HAW), Covidien Vital Sync, LifeSignals, Medistim QuickFit TTFM surgical flow probes (ITX), InVera infusion, STAR Artemis, Sonosite MT.

## 4. Watch items
- **K260168** Skycade Med "Small Diameter Core Wire" (CMAN-000-00/-14, DQX, SE 2026-10-16): 510(k) summary PDF still not posted (pdf26/K260168.pdf → 404); cfPMN record (page updated 2026-11-02) shows no summary link or indication. Coronary use still unverified → not added; keep watching.
- **CrossFAST CFM60** (K262817; row since pass 40): AccessGUDID "CFM60" → 0 results; "CrossFAST"/"Vantis" → CFM55 only (raw/agudid_*.html); openFDA UDI (cut 10-01) → CFM55 only. Dims still unpublished; CFM55 values not copied.
- **IMDS NHanceIT** (K260559; row since pass 40): AccessGUDID "NHanceIT" → 0 results; openFDA UDI IMDS → ShapeIT only. No change.
- **Direxion** Z-0223…0263-2027: peripheral, not in guide (now also in the 2026-10-28 enforcement report). No change.

## 5. Files
- Backups: coronary-recalls.pre-pass49.csv, coronary-recalls-by-supplier.pre-pass49.csv, coronary-specs-verified.pre-pass49.csv, provenance.pre-pass49.json (spec/provenance untouched), app/build.pre-pass49.py (publish.sh pass-label bump only).
- values.csv header-only; conflicts.json empty.
