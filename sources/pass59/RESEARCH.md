# Pass 59 — add RAYWATT FASTER OCT row (Jeff-approved 2026-11-25)

Jeff approved adding the RAYWATT FASTER OCT Imaging System / Chouette Imaging Catheter row found in the pass-58 weekly new-model sweep. Published to /preview/ only.

## Row added
Imaging & physiology / RAYWATT column (new extra column to the right of the fixed Philips, Boston Scientific, Abbott columns).

- **Model:** RAYWATT FASTER OCT Imaging System (RV201) with Chouette Imaging Catheter CH-01 through CH-04
- **Manufacturer:** RAYWATT, Inc. (FDA 510(k) applicant)
- **FDA 510(k):** K260445, Traditional, Substantially Equivalent, decision date 2026-11-11
- **Product codes:** NQQ (classification / primary), DQO (subsequent)
- **510(k) review panel:** Cardiovascular
- **Catalog / model numbers (from FDA Device Name only):** RV201; CH-01; CH-02; CH-03; CH-04
- **n_skus and all size/spec fields left blank.** 510(k) summary PDF not posted (https://www.accessdata.fda.gov/cdrh_docs/pdf26/K260445.pdf returned HTTP 404 on 2026-11-25). No GUDID DIs. No values copied from Dragonfly OpStar or any other model, including modality (even though the FDA classification name is "System, Imaging, Optical Coherence Tomography (Oct)").

Source for every filled identity/regulatory value: the FDA 510(k) database entry
https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260445
Field extract: sources/pass59/docs/K260445_fda_510k_database.txt
openFDA 510(k) corroboration (cut 2026-11-16; subsequent code DQO is on the database page, not in the openFDA JSON): sources/pass59/docs/K260445_openfda_510k.json

## How it was applied
- New row via pass02_apply.py NEW list (same path as NHanceIT and CrossFAST CFM60 in pass 40).
- Identity/regulatory values via sources/pass59/values.csv (fda_submission, product_code, catalog_numbers).
- supplier_columns.json: added supplier RAYWATT (match RAYWATT, color #155e75). Imaging & physiology fixed columns unchanged; RAYWATT gets its own extra column automatically.

## Not filled / not used
- Device dimensions, frequency, pullback, physiology indices, modality, n_skus: no exact-model IFU, summary, or GUDID sizes.
- Press/OEM marketing figures cited in pass 58 (400 fps, saline flush, 1.7–2.6 Fr, 2.0–3.5 mm vessels) still unused.
- AGENT 40 mm length (P230035/S008) still not applied (catalogs not yet in GUDID).
- No recall refresh in this pass.

## Conflicts
None (sources/pass59/conflicts.json empty; new row, no existing values).

## Fill
90.9% → 90.1% (925/1027; 77 rows). Imaging & physiology 76.9→73.5 (140/182 → 144/196).
