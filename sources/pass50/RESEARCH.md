# Pass 50 — coronary gap-fill (Thu 2026-11-05, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest categories: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run and recall CSVs not touched (weekly Wednesday routine only).
Remaining Imaging and Atherectomy/IVL blanks are almost all N/A by device type (pressure-wire french/sheath/MHz/pullback, IVUS wire/physiology, OCT MHz, solid-state pullback, IVL/atherectomy NP/RBP/burr/french). Blanks stay blank.

## Angles tried (new vs passes 45/47/48 unless noted)
1. **CrossFAST CFM60 (highest priority; ships Nov 2026).**
   - AccessGUDID "CFM60" → 0 results (raw/agudid_CFM60.html). "CrossFAST" → 2 results, CFM55 only (raw/agudid_CrossFAST.html).
   - openFDA UDI brand_name:CrossFAST → 2 DIs (CFM55 family); brand/id CFM60 → NOT_FOUND (raw/udi_CFM60.json, udi_CrossFAST.json).
   - Vantis WP media API: newest upload still 2026-01-05; no CFM60 sell sheet (raw/vantis_media.json). Home page loads (no CF challenge) but 0 "CFM60" mentions; /crossfast/ → 404.
   - K262817 PDF re-fetched; summary pages 5–6 read as images (docs/K262817_p5.png, p6.png) + Innolitics OCR. States 6F / 0.014" / min 100 cm guide / inner tip +3 cm beyond outer / "limited dimensional refinements" vs CFM55. **No** length_cm, inner_diameter_in, or outer_diameter_in figures. CFM55 values not copied. (docs/K262817_dims_note.md)
   - Press/web claims of an ID figure remain unverified against any OEM/FDA table → not used.

2. **Skycade K260168 watch (research only; not a gap-fill apply).**
   - Summary PDF now posted (HTTP 200; was 404 through pass 49). Saved raw/K260168.pdf + docs/K260168.txt.
   - Indication = **peripheral vasculature only** (Form FDA 3881 + summary §5; anatomical location "Peripheral"). Predicate Nitrex is peripheral+coronary; subject is peripheral-only.
   - Models CMAN-000-00 (0.018") / CMAN-000-14 (0.014"); lengths 40/50/80 cm. **Do not add a coronary guidewire row.** Watch closed for coronary-guide purposes. (docs/K260168_indication.md)

3. **openFDA 510(k)/PMA window since ~2026-10-19.**
   - 510(k): 63 decisions through 2026-11-05 (raw/k510_since_1019.json). Product-code sweeps DQY/DQX/DYB/LIT/NIQ/OBJ/QAN/QBZ/QEF/MCX/QMG: only in-scope hits already ruled out — K260168 (Skycade, peripheral), K260686 Zylox PanFlex (peripheral PTA scoring), K262917 IH reprocessed BRK (not coronary guide). None cite a guide-row model with a dimensional table for an open blank.
   - PMA: 48 decisions (raw/pma_since_1019.json). P900056/S226/S228/S229 ROTAPRO = console/manufacturing; no model/dim change. Structural-heart supplements (PASCAL/EVOQUE/SAPIEN) out of scope.

4. **Shockwave US /ifu/ + WP media recheck.**
   - Coronary US IFUs on the page match prior passes (C2 Aero Fly PN-77417 Rev C already used for tip in pass 44; C2+ PN-64192 Rev D still silent on tip). Newest coronary tech-sheet media still C2-Aero-Fly-Tech-Sheet_US.pdf (2026-10-19). No new C2+/Aero tip or sheath number. Peripheral E8 Large IFU is out of scope. (raw/shockwave_ifu.html, shockwave_media_C2.json, shockwave_techsheets.json)

5. **Imaging & physiology.**
   - Dragonfly OpStar: Abbott US HCP overview/ordering pages public but still no MHz or pullback-speed number; eIFU not bypassed. Spec-sheet hits are OUS/third-party (already rejected). wire_diameter_in / frequency_mhz / pullback_speed stay blank.
   - OptiCross HD / Eagle Eye / Refinity / reprocessed: open blanks are N/A by device type (IVUS wire_diameter_in, physiology_indices; solid-state pullback). No new exact-model US OEM/FDA text stating those figures.

6. **Atherectomy & IVL other blanks.**
   - Diamondback tip/french: Abbott eIFU gated — not bypassed. ROTAPRO sheath_compat_fr: no exact-model US OEM/FDA figure. Shockwave C2+/Aero/Aero Fly sheath / C2+ tip: unpublished (N/A burr/french left blank).

7. **Other fillable blanks with realistic source paths.**
   - NC TREK RX NP/crossing/tip: Abbott US HCP NC TREK URL 404 (catalog is NEO); IndiaMart third-party brochures rejected (same as passes 21/27/44). K220634 predicate table already used for RBP/shaft only (pass 32); NP not in that table.
   - Chocolate XD tip / Ringer tip / Pantera Pro / NC Quantum Apex / NC Euphora / AngioSculpt Evo crossing: no new exact-model US OEM/FDA figure since pass 48.
   - SION blue PLUS / Cougar tip_load: K243733 predicate is SION blue sibling (no tip-load figure for PLUS); Cougar still only third-party LS sibling listings — not used.
   - Launcher / Vista Brite Tip inner_diameter_mm: inches-only still reject (no conversion).
   - BioFreedom max_expansion_mm / DES crossing: OUS-only still reject.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45/47/48, plus CFM60 dims still unpublished (AccessGUDID 0; K262817 summary silent on ID/OD/length). Skycade ruled out (peripheral-only).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## New-row / Jeff decisions
None for gap-fill apply. Informational watch update only: K260168 summary posted → peripheral-only → do not add coronary row. CFM60 dims still pending GUDID/OEM sheet (ships Nov 2026).
