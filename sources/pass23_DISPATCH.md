# Pass 23 coronary gap-fill — executor brief

Work ONLY in `/workspace/coronary-specs` (jeffmcd83/coronary-compare). Do NOT touch structural-specs.
Repo lock already at `sources/.lock` for pass23 — keep it; clear when done.
Live = site root; staging = `/preview/` only. Never run `release.sh`.

## Current state (2026-10-16 afternoon)
- Last values: Pass 20 (87.7→88.8%, 881/992). Pass 21 no-op. Pass 22 Corsair Pro fda_submission only (still 88.8%). Tag preview-pass22, v1.16.
- Fill formula: COMMON without manufacturer (reprocessed, n_skus, fda_submission, product_code, catalog_numbers) + SIZE[cat] from app/build.py + SPEC[cat] from spec_by_cat.json. Current **881/992 = 88.8%**, 74 rows.
- Weakest: Imaging & physiology 74.2% (135/182), Atherectomy & IVL 76.9% (83/108).
- IH reprocessed Eagle Eye Platinum ST RX already added (pass 13b) — CLOSED.

## Rules
- Exact model/catalog only; never copy siblings.
- OEM IFUs > spec sheets/brochures > FDA. IFU wins on conflict.
- Every cell: doc + page/record + URL in values.csv source string.
- Log conflicts; never overwrite unless higher IFU rank (passes_apply.py).
- Leave blank if unverified. Do not invent "N/A" text. US coronary only.

## Already chased — skip unless NEW exact-model OEM/FDA evidence
- Dragonfly OpStar dims/MHz/pullback (Abbott eIFU captcha — do NOT bypass; OUS 1014652 rejected; K230411/K253459 lack dims)
- Pressure wires french/sheath/guidewire/MHz/pullback = N/A
- IVUS solid-state pullback_speed; catheter physiology_indices (OpStar already has physiology)
- NES reprocessed Eagle Eye MHz (absent last check)
- ROTAPRO/Diamondback/ELCA/Shockwave french/sheath/NP/RBP/burr where N/A; C2+/Aero Fly tip_profile (IFUs = folded balloon = crossing)
- SION blue PLUS tip_load — do NOT copy from SION blue
- NC TREK RX — only exact-model NC TREK RX OEM (not NEO); no third-party
- Turnpike ID — IFU OD only; K212211 Shaft ID is Corsair Pro predicate
- Corsair Pro fda_submission already "K161126, K171933" — do not change

## Priority targets
1. Imaging: NEW public OEM/FDA for Dragonfly OpStar US 1014651; NES Eagle Eye frequency; reprocessor IFUs for remaining blanks only if exact-model.
2. Atherectomy & IVL: NEW tip_profile / exact-model in US Shockwave IFUs, Diamondback P130005, ELCA Philips US, ROTAPRO Console Guide (not peripheral).
3. Other fillable: Pantera Pro crossing_profile_in; Ringer/Chocolate XD tip_profile_in; BioFreedom catalogs/n_skus/max_expansion/crossing (reject wrong-brand ECG GUDID); Cougar tip_load_gf; Launcher/Vista inner_diameter_mm; DES/BMS crossing only if exact-iteration IFU/SSED; INDIGO CAT RX / AngioJet Spiroflex lumen if exact-model numeric ID.

## Workflow
1. Create sources/pass23/{docs/,values.csv,conflicts.json,RESEARCH.md}. values.csv header: model,field,value,source
2. Backup before mutate: cp coronary-specs-verified.csv coronary-specs-verified.pre-pass23.csv (+ fam/passes_apply/build only if edited)
3. Download evidence into sources/pass23/docs/
4. Write NEW blank fills only; model strings must match verified.csv exactly; QC every source has URL
5. python3 build_master.py; confirm fill formula; conflicts via passes_apply
6. Update FILL_LOG.md Pass 23 section
7. ./publish.sh 23 (preview only). On failure fix/retry. No root release.
8. If zero values: header-only values.csv + RESEARCH.md + FILL_LOG no-op; still ./publish.sh 23 (like pass21)
9. Clear sources/.lock when finished
10. Do NOT message Jeff. Report to parent: values changed yes/no, fill before→after, highlights, skipped/blockers, tag, preview confirmation, Jeff decisions (IH ST RX closed), FILL_LOG summary.

## Success
- Lock released; pass23 artifacts present; preview-pass23 tagged; site_gate/tl.py clean; report complete for parent WakeParent only if values changed.
