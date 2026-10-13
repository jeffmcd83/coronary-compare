# FILL_LOG
## Pass 01 (2026-10-12)
- Seeded 65 device families across 12 approved categories (no embolic protection).
- Sizes, catalog numbers, FDA submission numbers, product codes: GUDID via openFDA UDI API (raw/udi/*.json). Values are only from records whose brand matches the exact family (regex in fam.py); no sibling copying.
- Name/classification-derived: balloon_type, compliance (NC prefix), atherectomy mechanism, imaging modality.
- Recalls: openFDA device recall API, matched only when an exact catalog/model number from that family's GUDID records appears in code_info/product_description → 92 recall rows.
- IFU-only specs (drug/dose, polymer, strut, crossing profile, RBP, tip load, ID/OD, frequency, pullback…) intentionally BLANK — not yet extracted from OEM IFUs. Next pass.
- Excluded wrong-brand GUDID hits: Cougar (Medos neuro), Wolverine (Kenmark), Mamba (Richard Wolf), GRAFTMASTER (Smith & Nephew ortho → left blank).
## Conflicts
- None overwritten. Families with mixed generations in GUDID (e.g., Launcher spans many 510(k)s; Integrity GUDID entries show P030009) recorded as-is.
## Pass 02 (2026-10-12)
- Sources: FDA SSEDs (P160043, P130030, P190020, H170004, P230035 …) and 510(k) summaries (28 PDFs) saved in sources/pass02/{ssed,k}; Medtronic Onyx Frontier HCP page.
- ~70 curated cells with doc + page + URL (sources/pass02/applied.json). Exact-model only: SSEDs for original approvals (XIENCE V P070015, SYNERGY P150003, Orsiro P170030, Shockwave C2 P200039, Driver P030009, ML Vision P020047) NOT applied to later iterations (Skypoint/Sierra, SYNERGY XD/MEGATRON, Orsiro Mission, C2+/Aero, Integrity, ML8).
- Submission numbers filled: XIENCE Skypoint/Sierra P110019, Orsiro Mission P170030, ML8 P020047, PK Papyrus H170004, Diamondback P130005, GuideLiner V3 K172090, Heartrail III K113335, Gaia Next K192599, PILOT K101116, Runthrough K063695, SION black K173277, Guidezilla II K163314, Mamba K190401, Corsair Pro K161126, Caravel K152447, OptiCross HD K213593, Dragonfly OpStar K230411, COMET II K193279, Telescope +K252390.
- New rows: BioFreedom (P190020; not in GUDID), Penumbra INDIGO CAT RX (K220683), Innovative Health Reprocessed Eagle Eye Platinum RX (K210655). GRAFTMASTER fixed (Abbott "Graftmaster" GUDID, 15 DIs).
- Recall matcher now also matches GUDID DIs/GTINs: +XIENCE Sierra (1), +Diamondback (2) → 95 rows. Telescope: no openFDA recall record exists (earlier 14 hits were unrelated endoscopy telescopes).
- Conflicts logged (sources/pass02/conflicts.json): ROTAPRO GUDID P900056 vs 510(k) K220962 (both kept); Dragonfly modality kept "OCT".
- Not US/FDA-found: Ringer, Terumo AltaView, Asahi Hyperion guides; Mach 1 (only 2001 510(k)).

## Pass 03 — fill 61.8%
Skypoint/Sierra IFUs, SYNERGY XD US DFU, MEGATRON spec sheet, Orsiro Mission brochure (45 values). Backup: coronary-specs-verified.pre-pass03.csv. Tag preview-pass03.
## Pass 04 — fill 63.4% (new DES/atherectomy fields added)
Shockwave C2+ IFU/tech sheet, C2 Aero page, AGENT IFU (2 µg/mm²), Asahi catalog tip loads, Caravel/Corsair Pro ODs (2 conflicts logged). Tag preview-pass04.
## Pass 05 — fill 65.4%
GuideLiner V3 IFU IDs, Guidezilla II, Wolverine NP/RBP, Telescope, Heartrail, Vista Brite (curves corrected in pass 06: removed "EBU-type"). Tag preview-pass05.
## Pass 06 — fill 66.0%
Eagle Eye Platinum RX IFU (18.6 MHz; conflicts w/ 20 MHz nominal), Refinity ST IFU 42.1 MHz + brochure pullback (conflict logged, 510(k) value kept), Diamondback 360 IFU P130005 p.8 (1.25 mm, 6 Fr/0.066 in), ROTAPRO Console Guide p.11 (burrs, guide IDs, rpm). Tag preview-pass06.
## Pass 08 — fill 71.0% (Balloon 56→81, DES 81→85) — /preview/ only, tag preview-pass08
45 values. TREK/MINI TREK US page (NP 8/RBP 14, 145 cm; profiles TREK only — measured on 3.00 mm, not copied to MINI TREK), NC TREK NEO US page, Emerge IFU 51340525-01A p.3/p.8 + US page, NC Emerge US page, Euphora US brochure p.2, NC Euphora tech sheet, NC Quantum Apex IFU 51427546-01B p.3/5/7, Onyx Frontier SSED P160043/S058 p.3–4 (strut 81/91 µm also to Resolute Onyx — same SSED table). No new conflicts. Skipped NC TREK RX (US page 404; only third-party PDFs). Backup: coronary-specs-verified.pre-pass08.csv.
## Pass 09 — fill 74.5% (7:13 AM routine run; published + tagged preview-pass09, stalled before FILL_LOG)
32 values (QC'd 10:59 AM: all have doc+page+URL). 510(k) numbers for TREK family/Emerge/NC Emerge; NC Emerge IFU 51348153-01A (NP 12; RBP 20/18; 143 cm); NC Quantum Apex lengths; Wolverine sizes; AngioSculpt RX NP/RBP/137 cm; SYNERGY XD guide compat + post-dilation limits; XIENCE Sierra dilatation limits; Resolute Onyx 140 cm + MSID; Orsiro Mission sizes; BioFreedom dose; Integrity BMS; Export Advance; Launcher IDs/curves; Telescope 150 cm. Backup: coronary-specs-verified.pre-pass09.csv.
## Pass 09b — fill 75.3% (Thrombectomy 55→72) — /preview/ only, tag preview-pass09b
AngioJet Spiroflex (BSC IC reference guide IC-274802-AA p.1–2: 4 F, 135 cm, rheolytic), AngioJet AVX (BSC US page: 6 F, 50 cm), INDIGO CAT RX (Penumbra US page: 5.3 F, 140 cm). Not filled: DES crossing profiles (no exact-model OEM number; Orsiro SSED P170030 is the original Orsiro, not Mission), NC TREK RX (only third-party PDFs), Dragonfly OpStar frequency/pullback (only Dragonfly Duo/OPTIS data = siblings). Flag: AngioJet AVX is AV-access only (not coronary) — review whether it belongs. Backup: coronary-specs-verified.pre-pass09b.csv.
## Pass 10 — remove AngioJet AVX (Jeff-approved 2026-10-13)
Excluded via EXCLUDE in build_master.py: AngioJet AVX is labeled for AV-access grafts/fistulae only (BSC US AngioJet page), not coronary. Its source values remain in sources/pass09/values.csv but are not applied. Backup: coronary-specs-verified.pre-pass10.csv. Tag preview-pass10; released to root as v1.3.
## Pass 11 — fill 75.5→81.5% (1:13 PM routine run; weakest-category focus) — /preview/ only, tag preview-pass11
54 values applied; 0 new conflicts (sources/pass11/conflicts.json empty). Backup: coronary-specs-verified.pre-pass11.csv. passes_apply.py glob extended to `pass0[3-9]*` + `pass1*`.
Category deltas: Microcatheter 68→94; Covered stent 71→92; Guide extension 82→98; Guidewire 78→91; BMS 69→85; Atherectomy & IVL 53→60; Imaging 59.5→60.1 (still ~60%).
Highlights: Turnpike tip/shaft ODs (Teleflex brochure); Finecross all 4 + french (K082519 + Terumo brochure); Mamba tip/shaft/markers/length (BSC US + K190401); Twin-Pass tip/shaft (Teleflex brochure); Caravel/Corsair Pro IDs (Asahi US pages); GRAFTMASTER RX covering/alloy/crossing/143 cm/guide (Abbott US page); MULTI-LINK 8 alloy/strut/crossing/NP/RBP/143 cm (Abbott ML8 brochure); Telescope ID/OD (Medtronic in-lab poster); TrapLiner ID/OD/guide/150 cm (Teleflex brochure); BMW Universal II all 4 (Abbott workhorse page); PILOT tip_load/core/use (Abbott specialty); Runthrough tip_load + use (Terumo Europe); Cougar core/coating/use (Medtronic guidewire brochure); SION black core stainless (K173277); ELCA guide_compat + tip OD + fluence/Hz (Philips brochure); Shockwave C2+ RBP 10 / C2 Aero RBP 8 (US IFUs); Eagle Eye Platinum ST RX frequency 18.6 MHz (Philips ST IFU acoustic table).
Skipped (no exact-model OEM / N/A / sibling risk): Turnpike ID + markers; Caravel markers; Integrity strut/crossing/delivery; REBEL/PK Papyrus/DES crossing; Dragonfly OpStar freq/pullback; Asahi SION blue/Confianza/Fielder XT cores (sibling SSEDs); ROTAPRO/Diamondback pulses/rbp; physiology on IVUS/OCT; thrombectomy aspiration_lumen; NC TREK RX (third-party only).
