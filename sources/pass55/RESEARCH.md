# Pass 55: weekly recall and new-model refresh (Wed 2026-11-18, ~8:50–9:10 AM ET). No-op for data.

Result: **no new recalls, no new models, no spec changes.** Recalls stay at 110 (19 rows). Fill unchanged 90.9% (921/1013; 76 rows).

## openFDA data cut dates (meta.last_updated, queried 2026-11-18 ~8:51 ET)
- device/recall: **2026-11-14** (59,705 records; pass 52: 2026-11-07 / 59,705)
- device/enforcement: **2026-11-11** (40,535; pass 52: 2026-11-04 / 40,481)
- device/510k and device/pma: **2026-11-09** (pass 52/54: 2026-11-02)
- device/udi: **2026-11-02** (5,182,695; unchanged since pass 52)
- AccessGUDID daily deltas parsed: 2026-11-16, 2026-11-17 (11-14, 11-15, 11-18 not published/404; weekend/not yet). Pass 54 covered 11-12, 11-13. Files off-repo in /workspace/gudid_delta/p55/.

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass55/raw/recall_pool.json.gz`: pool 2,058 recall products (identical key set and recall_status to pass 52: 0 new, 0 gone, 0 status changes); 110 matches, 3 dropped. coronary-recalls.csv and raw/recall_dropped.json remained byte-identical to the pre-pass55 backups.
- Recall products posted 2026-10-31…11-18 (44; `raw/recalls_posted_since1031_all.json`): same 44 as pass 52 (posted 11-02, 11-03, 11-04, 11-05 only). Query `event_date_posted:[2026-11-12+TO+2026-11-18]` returned 0. Firms: Henry Schein sutures, Cardinal Health Presource kits (BD Alaris sets), Baxter operating tables, GE Senographe, AVID packs, Edwards Commander M delivery system Z-0287 (structural/TAVI), Shimadzu Trinias angiography system Z-0347 (cath-lab x-ray, not a guide row), restor3d, Cochlear, Remel, Corin, Intelerad, Luminex. **None is a coronary interventional device in the guide.**
- Direxion microcatheter Z-0223…0263-2027 (peripheral): still not a guide row, not added.
- FDA Medical Device Recalls page (https://www.fda.gov/medical-devices/medical-device-safety/medical-device-recalls): one item dated after 11-11 — 11/17/2026 Cardinal Health Presource packs / BD Alaris infusion sets (same kits already in the 44 posted recalls). No coronary/stent/guidewire/balloon/atherectomy/IVL guide-row item.

## 2. Enforcement endpoint
- Reports with report_date ≥ 2026-11-05 (54, all report_date 2026-11-11; `raw/enforcement_since_1105.json`) mapped and run through `recalls.py match` → **0 matches** (script crashed on empty result as documented; CSV and raw/recall_dropped.json restored, verified byte-identical to backups). Keyword scan: Cardinal Health Presource/Alaris (false “EMERGE” kit-name hits), Edwards Commander M Z-0287 (structural), GE Senographe, Shimadzu Trinias. None relevant.

## 3. New models / submissions
- `sources/pass55/newmodels.py` (window 2026-09-01→; `raw/newmodels_openfda.json`): two new 510(k)s and one new PMA supplement vs pass 52, none a new coronary guide model:
  - P250041/S001 MedAlliance SELUTION SLR 014 PTCA DEB (OOB, APPR 2026-11-06, Normal 180-Day No User Fee): **Postapproval Study Protocol** (SELUTION4ISR continued follow-up through 5 years). Existing guide row; no new trade name, size, or indication. Not a new model.
  - K262171 Merge Hemo RCSV2 v11.3 (DQK, SE 2026-11-05): cath-lab hemodynamic software, not a guide device.
  - K261376 Terumo Progreat Lambda 2.1Fr (KRA / 870.1210 continuous-flush catheter, SE 2026-11-05). Progreat is an IR/peripheral microcatheter family; 510(k) PDF not yet posted. Not a coronary interventional guide candidate.
- All 510(k) (58) and PMA (31) decisions 2026-11-02→11-18 (`raw/all_decisions_1102_1118.json`). Other cardiovascular items reviewed and excluded: Brosmed Parafleet NC PTA balloons K262590 (LIT, peripheral), iCOR Beat K260383 (MWJ, ambulatory ECG), Contego Neuroguard IEP K260600 / P240009/S006 (carotid embolic protection — out of scope), Argon Option ELITE IVC filter K263678, Perclose ProStyle P960043/S139 (30-day notice), EverFlex / Supera / Zilver / Protege peripheral stents, Evolut FX TAVI P130021/S188. No coronary interventional model; no reprocessed coronary 510(k) (Stryker Steri-Shield hoods K262500; other reproc hits predate this window and are EP/GU/surgical).
- GUDID deltas (`raw/gudid_delta_hits.json`, 512 hits, almost all 2026-11-16): no catalog/DI/version match to any guide row (`raw/catalogs.json`, 10,658 IDs). Hits are a large Shanghai Int Medical Instruments update (INT SlideCath/K2/FirstWire/Falcon/FineThrough/Denali/PV3-G; PV3-G is a GuideLiner V3 brand-regex false positive), plus ultrasound systems/transducers (ITX/IYO/IYN), GE monitors, Innovative Health SoundStar eco ICE (OWQ, EP), Boston Scientific OPAL HDx (DQK/DSA, EP). No new or updated DI for any guide row.

## 4. Watch items
- CrossFAST CFM60 (K262817): AccessGUDID "CFM60" → 0 results; "CrossFAST" → CFM55 only (2 records). Dims unpublished; CFM55 not copied.
- IMDS NHanceIT (K260559): AccessGUDID 0 results.
- Skycade K260168: closed in pass 50 (peripheral only).
- Direxion: not in guide.
- Pending suggestions (Euphora K261759, Navvus II K233904, balloon candidates, PendraCare Climber/Primum K250972, OpStar pullback_speed) untouched, waiting for Jeff.

## 5. Files
Backups: *.pre-pass55 (recalls, supplier rollup, specs, provenance, app/build.py, raw/recall_dropped). values.csv header-only; conflicts.json empty. coronary-recalls-by-supplier.csv unchanged (recalls identical).
