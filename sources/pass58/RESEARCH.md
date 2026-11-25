# Pass 58: weekly recall and new-model refresh (Wed 2026-11-25, ~8:50–9:05 AM ET). No recall or spec-CSV changes; one new coronary model candidate (not added).

Result: **no new recalls, no spec values applied.** Recalls stay at 110 (19 rows). Fill unchanged 90.9% (921/1013; 76 rows). One new US-cleared coronary interventional model found and **not added** (Jeff decision): RAYWATT FASTER OCT Imaging System (RV201) / Chouette Imaging Catheter (CH-01–CH-04), K260445. Also logged: AGENT 40 mm length PMA approval (existing row; catalogs not yet in GUDID); IMDS InfuseIt K263017 pending 510(k) summary.

## openFDA data cut dates (meta.last_updated, queried 2026-11-25 ~8:52 ET)
- device/recall: **2026-11-21** (59,705 records; pass 55: 2026-11-14 / 59,705)
- device/enforcement: **2026-11-18** (40,625; pass 55: 2026-11-11 / 40,535)
- device/510k and device/pma: **2026-11-16** (pass 55: 2026-11-09)
- device/udi: **2026-11-02** (5,182,695; unchanged since pass 52)
- AccessGUDID daily deltas parsed: 2026-11-23, 2026-11-24 (11-21 and 11-22 = weekend/404; 11-25 not yet published). Pass 57 covered 11-19, 11-20. Files off-repo in /workspace/gudid_delta/p58/.

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass58/raw/recall_pool.json.gz`: pool 2,058 recall products (identical key set and recall_status to pass 55: 0 new, 0 gone, 0 status changes); 110 matches, 3 dropped. coronary-recalls.csv and raw/recall_dropped.json remained byte-identical to the pre-pass58 backups.
- Query event_date_posted 2026-11-14 to 2026-11-25 and 2026-11-19 to 2026-11-25 both returned 0 (raw/recalls_posted_since1114_all.json, raw/recalls_posted_since1119.json). No recall products initiated or posted on or after 2026-11-14 in the live pool.
- Direxion microcatheter (peripheral): still not a guide row, not added.
- FDA Medical Device Recalls and Early Alerts page (https://www.fda.gov/medical-devices/medical-device-safety/medical-device-recalls): listed items include Boston Scientific Imager II angiographic catheters (Class I, initiated 2026-08-24 — diagnostic angio catheter, not a guide row), Edwards transcatheter mitral delivery system (structural), Abiomed Impella controllers, Cardinal Health Presource / BD Alaris kits (already reviewed in passes 52/55), Siemens ARTIS movement-control corrections (cath-lab x-ray, not a guide row), and others. None is a coronary interventional device in the guide.

## 2. Enforcement endpoint
- Reports with report_date on or after 2026-11-12 (88, all report_date 2026-11-18; raw/enforcement_since_1112.json) mapped and run through `recalls.py match` → **0 matches** (script crashed on empty result as documented; CSV was truncated to 0 bytes and restored from pre-pass58 backup, verified byte-identical, as was raw/recall_dropped.json). Keyword scan: Siemens ACUSON Origin ICE (EP/structural ultrasound), Siemens ARTIS icono/pheno (cath-lab x-ray), Medtronic SmartSync programmer (CRM), Cardinal Health Presource/Alaris kits, TransMedics OCS Liver, Baxter/IMRIS tables, 3B Medical Luna BPAP (Class I). None is a coronary-guide device.

## 3. New models / submissions
- `sources/pass58/newmodels.py` (window 2026-09-01 onward; raw/newmodels_openfda.json) vs pass 55, plus all 510(k) (64) and PMA (30) decisions 2026-11-09 to 11-25 (raw/all_decisions_1109_1125.json). New vs pass 55:
  - **K260445 RAYWATT, Inc. FASTER OCT Imaging System (RV201); Chouette Imaging Catheter (CH-01, CH-02, CH-03, CH-04)** (primary NQQ, subsequent **DQO**, SE 2026-11-11, traditional, review panel Cardiovascular). Not caught by newmodels.py (primary code NQQ is outside the guide product-code set; found in the all-decisions sweep). FDA 510(k) database names the exact models and DQO (same code as Dragonfly OpStar). 510(k) summary PDF not yet posted (https://www.accessdata.fda.gov/cdrh_docs/pdf26/K260445.pdf returned 404). Company and investor communications (Raywatt LinkedIn 2026-11-12; SBI Investment 2026-11-17; Hankyung 2026-11-16) describe US clearance for imaging of coronary arteries in patients who are candidates for transluminal intervention; press also cites 400 fps / saline flush / 1.7–2.6 Fr catheters / 2.0–3.5 mm vessels — press/OEM marketing only, not used as guide values. **New-row candidate for Imaging & physiology. Not added (Jeff decision).** No GUDID DIs yet (UDI cut still 2026-11-02; not in 11-23/11-24 deltas).
  - **P230035/S008** Boston Scientific AGENT Paclitaxel-Coated Balloon Catheter Matrix Expansion (40 mm Balloon Length), APPR 2026-11-13, Normal 180-Day Track, OOB. ao_statement: "approval for 40 mm balloon length AGENT Paclitaxel-Coated Balloon Catheter and a shelf-life extension." Existing DCB row currently lists lengths 12, 15, 20, 30 mm. **Not applied**: no 40 mm catalogs/DIs in GUDID yet. Recommend adding 40 mm to lengths_mm (and SKUs) once GUDID lists the new catalogs. Japan already launched a 40 mm size (Boston Scientific Japan 2026-04-01) — OUS, not used.
  - **P900056/S230** ROTAPRO 30-Day Notice, OK 2026-11-15: "a change in supplier and supplier manufacturing location for the ROTAPRO Advancer piston component." Existing row; not a new model or size.
  - **K263017** IMDS Operation B.V. InfuseIt (DQY / 870.1250, SE 2026-11-13). Same applicant as the NHanceIT guide row. 510(k) summary PDF not yet posted; indications, dimensions, and whether it is coronary vs peripheral-only are unverified. Possible microcatheter new-row candidate — hold until the summary (or GUDID) names the indication. Not added.
  - Reprocessed 510(k)s in this window are out of scope: Innovative Health Reprocessed Carto Octaray (K260574, NLG, EP mapping); Stryker Cranial Guidance 4.1 (K262404), cprPRO (K261579), VariAx 2 Ulna Shortening (K262903); Medline UNITE IMX Fibula Nail (K261773).
- Other cardiovascular decisions reviewed and excluded: Medtronic/BSC CRM 30-day notices, EluPro BioEnvelope K263742 (CRM), Perclose-class and TAVI-adjacent supplements, carotid CGuard Prime P240029/S005, Esprit BTK, iliac Absolute Pro, etc. No other coronary interventional model; no reprocessed coronary 510(k).
- GUDID deltas (raw/gudid_delta_hits.json, 12 hits): **one existing guide-row DI appeared** — Vantis Vascular CrossFAST Integrated Microcatheter Advanced Delivery System, version CFM60, primary DI 00860007727924, package 10860007727921 (qty 5), DQY, K262817, In Commercial Distribution, publicVersionDate 2026-11-24, status New (raw/gudid_00860007727924.json). deviceDescription = "6F, Catheter with Rapid Exchange Length". **deviceSizes is empty** (dimensions still unpublished). Catalog number in GUDID is null (row already lists CFM60). GTIN not added this pass (no other spec change). Other hits: QISDA/Esaote and Philips InnoSight ultrasound, GE Vivid/Voluson, GE monitor SW, B. Braun CSL Behring set, Boston Scientific OPAL HDx (DQK, EP). No other guide-row catalog/DI/version match.
- Note: AccessGUDID /api/v3/devices/search.json now returns 404; the working search URL is https://accessgudid.nlm.nih.gov/devices/search.json?query=...

## 4. Watch items
- CrossFAST CFM60 (K262817): **now in AccessGUDID** (see above). Sizes/ID/length still unpublished; existing guide fields stay as-is. openFDA UDI still 0 (cut 2026-11-02). CFM55 not copied.
- IMDS NHanceIT (K260559): AccessGUDID 0 results; openFDA UDI 0.
- Skycade K260168: closed in pass 50 (peripheral only).
- Direxion: not in guide.
- Pending suggestions (Euphora K261759, Navvus II K233904, balloon candidates, PendraCare Climber/Primum K250972, OpStar pullback_speed, C2+ tip FYI) untouched, waiting for Jeff. Climber/Primum still listed in GUDID (6F curves, unchanged this week).

## 5. Files
Backups: *.pre-pass58 (recalls, supplier rollup, specs, provenance, app/build.py, raw/recall_dropped). values.csv header-only; conflicts.json empty. coronary-recalls-by-supplier.csv unchanged (recalls identical).
