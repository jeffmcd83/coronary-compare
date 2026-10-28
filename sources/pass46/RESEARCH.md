# Pass 46: weekly recall and new-model refresh (Wed 2026-10-28, ~08:50–09:20 AM ET). No-op for data.

Result: **no new recalls, no new models, no spec changes.** Recalls stay at 110 (19 rows; 4 Open, 106 Terminated). Fill unchanged 90.9% (921/1013; 76 rows).

## openFDA data cut dates (meta.last_updated, queried 2026-10-28 ~08:52 ET)
- device/recall: **2026-10-24** (59,618 records; pass 43 saw 2026-10-19 / 59,536)
- device/enforcement: **2026-10-21** (40,358; pass 43 saw 2026-10-14 / 40,300)
- device/510k and device/pma: **2026-10-19** (latest decisions 2026-10-18 / 2026-10-16; pass 43 saw 2026-10-12)
- device/udi: 2026-10-01 (unchanged). AccessGUDID daily deltas 2026-10-21, 10-22, 10-23 (weekly zip 20261019_20261023), 10-26, 10-27 parsed (pass 43 covered to 10-20). Files kept off-repo in /workspace/gudid_delta/p46/.

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass46/raw/recall_pool.json.gz` (pass-40 rules, unchanged): pool 2,058 recall products (pass 43: 2,016; +42 new keys, 0 gone, 0 recall_status changes). 110 matches, 3 dropped (the Jeff-ruled Diamondback model-number-only Z-1290-2015, Z-3021-2018, Z-2122-2017; raw/recall_dropped.json unchanged).
- coronary-recalls.csv regenerated **byte-identical** to coronary-recalls.pre-pass46.csv; coronary-recalls-by-supplier.csv regenerated, byte-identical (110).
- The 42 new pool records (all posted 2026-10-22):
  - 41 × Boston Scientific Cork **Direxion Torqueable Microcatheter** (Z-0223-2027 … Z-0263-2027, event 99906, initiated 2026-09-16, Class II, Open/Classified, KRA, K163701; reason: insufficient UV curing of hydrophilic coating + raised ridges on nitinol sleeves). Direxion is a peripheral microcatheter and **not a guide row**; no catalog/GTIN/DI/510(k) match to any row (Material Numbers M0011952xx–M0011959xx). Pulled in by the KRA product-code query (Finecross row code). Not added.
  - 1 × restor3d MTP implant Z-0264-2027 (orthopedic, KWD) — unrelated.
- FDA "Medical Device Recalls and Early Alerts" page (checked 2026-10-28): no coronary item. New since pass 43: B. Braun Streamline bloodline (10/27), Cardinal Health Presource/BD Alaris packs (10/20), Nova StatStrip (10/20), Philips Lumify (10/19). Edwards mitral alert (10/15) = structural, out of scope.

## 2. Enforcement endpoint (device/enforcement)
- All reports with report_date ≥ 2026-10-01 (245: 10-07 ×136, 10-14 ×51, 10-21 ×58; `raw/enforcement_since_1001.json`) run through the recalls.py matcher (`python3 recalls.py match /tmp/enf46.json.gz`; CSV + raw/recall_dropped.json restored afterwards, verified byte-identical). Output `raw/enforcement_matches.csv`: 2 matches, both **rejected** — Medline kits Z-0180-2027 / Z-0184-2027 (CONMED AirSeal ports) hitting the word "ADVANCE" (Export Advance), the known collision pattern from pass 43.
- Keyword scan (coronary/PTCA/stent/wire/balloon/IVUS/major coronary firms): only Philips MR/CT, IntraSight Plus console Z-3276-2026 (seen pass 43, not a guide row), Stryker reprocessed EP catheter, Medtronic Pipeline/insulin/Grafton, BSC pancreatic stent pusher. None coronary.

## 3. New models / submissions
- `sources/pass46/newmodels.py` (pass-43 script, window 2026-09-01→; `raw/newmodels_openfda.json`). Compared with pass 43, the new items are:
  - **P160043/S096** (Resolute Onyx, 2026-10-16): 30-Day Notice, process change (point of finished-device test sample collection). No new trade name/model; no spec impact.
  - **K260168** Skycade Med Corp "Small Diameter Core Wire" (CMAN-000-00 / CMAN-000-14), DQX, Traditional, SE 2026-10-16. 510(k) summary PDF not yet posted (accessdata pdf26/K260168.pdf returns the HTML placeholder); cfPMN record gives no indication. **Coronary use not verifiable → not added**; watch item.
  - **K262904** Penumbra INDIGO Aspiration System, QEW, SE 2026-10-15; cfPMN cites NCT05003843 (BOLT-DVT, deep-vein thrombosis). Venous/peripheral indication, not a coronary model (INDIGO CAT RX row K220683 unaffected). Not added.
- All 510(k) decisions 2026-10-10→10-18 (52) and PMA decisions 2026-10-10→10-16 (50) (`raw/all_decisions_1010_1019.json`): besides the above, no coronary device. Cardiovascular-panel items are Kossel Giranel guiding sheath (DYB, K262674), Route 92 neuro reperfusion (NRY), monitors, peripheral stents (Abre, S.M.A.R.T., EverFlex, Protégé, Visi-Pro 30-day notices), CRM/BIOexpress, Vivasure PerQseal closure (P250015), Abbott Volt PFA. JenaValve P250024/S005 = structural (out of scope).
- Reprocessed coronary 510(k)s: none (reprocessor applicant hits = the same 3 Stryker non-coronary items as pass 43).
- GUDID deltas (`raw/gudid_delta_hits.json`, 15 hits): no new or updated DI for any guide row; no new coronary device. Hits: Teleflex Arrow arterial kit (DQX), BSC ACUITY 7060 (DQY; LV-lead delivery, CRM), Accurate Medical SeQure (DQO, not-in-distribution update), Inquis Aventus thrombectomy (QEZ/KRA; venous/PE), GE/Masimo/CardioSense monitoring.
- Previously flagged candidates: IMDS NHanceIT (K260559) and Vantis CrossFAST CFM60 (K262817) are rows since pass 40; status unchanged (neither in the GUDID deltas; CFM60 dims still unpublished).

## 4. Files
- Backups: coronary-recalls.pre-pass46.csv, coronary-recalls-by-supplier.pre-pass46.csv, coronary-specs-verified.pre-pass46.csv, provenance.pre-pass46.json (spec/provenance untouched), app/build.pre-pass46.py (publish.sh pass-label bump only).
- values.csv header-only; conflicts.json empty.
