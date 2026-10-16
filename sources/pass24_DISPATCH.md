# Pass 24 coronary gap-fill — executor brief

Work ONLY in `/workspace/coronary-specs` (jeffmcd83/coronary-compare). Do NOT touch structural-specs.
Repo lock already at `sources/.lock` for pass24 — keep it; clear when done.
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
1. Create sources/pass24/{docs/,values.csv,conflicts.json,RESEARCH.md}. values.csv header: model,field,value,source
2. Backup before mutate: cp coronary-specs-verified.csv coronary-specs-verified.pre-pass24.csv (+ fam/passes_apply/build only if edited)
3. Download evidence into sources/pass24/docs/
4. Write NEW blank fills only; model strings must match verified.csv exactly; QC every source has URL
5. python3 build_master.py; confirm fill formula; conflicts via passes_apply
6. Update FILL_LOG.md Pass 24 section
7. ./publish.sh 24 (preview only). On failure fix/retry. No root release.
8. If zero values: header-only values.csv + RESEARCH.md + FILL_LOG no-op; still ./publish.sh 24 (like pass21)
9. Clear sources/.lock when finished
10. Do NOT message Jeff. Report to parent: values changed yes/no, fill before→after, highlights, skipped/blockers, tag, preview confirmation, Jeff decisions (IH ST RX closed), FILL_LOG summary.

## Success
- Lock released; pass24 artifacts present; preview-pass24 tagged; site_gate/tl.py clean; report complete for parent WakeParent only if values changed.

## Pass 24 updates (2026-10-16 7:15 PM routine run)
- Current state: Pass 23 applied 881→887/992 = **89.4%**; Pass 23 released to root as v1.17 (Jeff-approved). Weakest: Imaging & physiology 74.7% (136/182), Atherectomy & IVL 76.9% (83/108).
- Pass 23 also found: NES Eagle Eye frequency (IFU-100006) — DONE; BioFreedom catalogs/crossing from P190020D — DONE; INDIGO CAT RX lumen — DONE. Don't redo these.
- passes_apply.py glob covers sources/pass2*/ — pass24 is picked up automatically; verify after build_master.py.
- Untracked screenshot PNGs in app/ (live-v1.17-*.png, r117-*.png) must NOT be committed: move them to /workspace/coronary-screens/ before ./publish.sh 24.
- New angles worth trying this pass: Asahi US e-IFU library (https://asahi-inteccusa-medical.com/us-ifu/), Teleflex IRC US IFUs (Ringer, Pantera Pro, Chocolate XD tip/crossing), Philips US eIFU for ELCA / Eagle Eye / Refinity / OmniWire, Shockwave US IFU library, FDA PMA SSED/labeling (Diamondback P130005 supplements, Shockwave P200039 supplements), Penumbra/BSC/Medtronic eIFU portals that are NOT captcha-gated. Never bypass captchas or HCP gates.
