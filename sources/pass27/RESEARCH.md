# Pass 27 research notes (2026-10-17, 1:13 PM ET scheduled run)

Imaging & physiology + Atherectomy & IVL first, then other exact-model blanks. New angle this pass: a fresh openFDA GUDID pull (2026-10-17) of record-level device_sizes + commercial-distribution status for every row, plus openFDA PMA supplements decided 2025-01 → 2026-10 for every PMA in the guide. **1 value applied** (blank cell). Fill 889 → 890/992 (89.7%).

## Applied
- **Diamondback 360 Precision — sheath_compat_fr = "6 Fr introducer sheath (all DBEC-125 / DBEC-125M / DBEC-150 DIs)"** — GUDID device_sizes "Intro Sheath 6 Fr" on all 10 coronary OAD DIs in the row (7-10060-01/-02/-09/-10, 7-10098-01, 70058-02/-12/-13 = DBEC-125; 7-10000-01 = DBEC-125M; 70058-03 = DBEC-150). docs/udi_diamondback_openfda_20261017.json. The build's GUDID parser missed it because the labeler stores it as free text ("Device Size Text, specify"). IFU P130005c Table 1 p.2 gives the minimum guide catheter (6 F, ID ≥ 0.066 in) — already in guide_compat; no conflict.

## Found, NOT applied — logged in conflicts.json (existing values not overwritten; Jeff to decide)
- **Orsiro Mission 4.5 / 5.0 mm sizes are US-approved** — PMA P170030/S058 (2026-06-11: "addition of 4.5 and 5.0 mm diameter stents to the Orsiro Mission product matrix"), S064 (2026-07-23, 24-month shelf life for "Orsiro Mission larger diameter stents Ø 4.5 5.0 mm"); GUDID 14 new DIs 473694–473707 (published 2026-06-30; 4.5 and 5.0 mm × 9–30 mm). Teleflex US IRC page (https://irc.teleflex.com/orsiro-mission/, Federal-law caution; docs/teleflex_irc_orsiro-mission_excerpt.md): indication RVD 2.25–5.0 mm; strut 89 µm for 4.5–5.0; NP 11 atm for 4.5–5.0; 6 F guide (min ID 0.070 in) for 4.5–5.0. Row values for diameters_mm, lengths_mm qualifier, strut_thickness_um, nominal_pressure_atm and guide_compat come from the 2022 US brochure 463589 Rev B and stop at 4.0 mm. Candidate updates are in conflicts.json. Still no crossing profile on the Teleflex US page.
- **Orsiro Mission SKU over-match (Fielder XT-class issue)** — fam.py brand regex `Orsiro` also matches 52 GUDID DIs of brand "Orsiro" (original Orsiro, catalog 401729…404677, published 2019-02-26), all "Not in Commercial Distribution", end date 2024-09-09. Exact Orsiro Mission = 66 DIs (453925–453978 + 473694–473707, matching the Teleflex US ordering table). Row currently shows n_skus 118. The fix is regex `^Orsiro Mission$`. It changes existing values, so it needs Jeff's OK.
- **Diamondback GUDID "Max OD"** varies by catalog: 0.0495 in (7-10060-01/-09/-10, 7-10098-01), 0.052 in (7-10060-02, DBEC-125M), 0.057 in (70058-02/-12/-13), 0.061 in (DBEC-150). The IFU gives a single value, 1.34 mm (0.053 in). The IFU value is kept. Log only.
- **Diamondback GUDID "Guidewire size OD 0.012 in"** — the row says "OD not stated in IFU". Log only.

## Evidence for open Jeff items (GUDID pulled 2026-10-17)
- **Integrity (P030009 withdrawn 2026-04-02):** all 78 "Integrity" DIs are Not in Commercial Distribution (39 ended 2026-04-01, 39 ended 2024-05-20). Resolute Integrity DES DIs also ended 2026-04-13. docs/udi_integrity_openfda_20261017.json.
- **MULTI-LINK 8:** all 6 DIs are Not in Commercial Distribution, end date 2018-07-21. docs/udi_ml8_openfda_20261017.json.
- **XIENCE Sierra:** all 56 DIs are still "In Commercial Distribution", but each carries a scheduled distribution end date of 2028-03-28. PMA P110019/S142 (2026-07-31) still names XIENCE Sierra. docs/udi_sierra_openfda_20261017.json, P110019_S142_openfda.json.
- **DBEC-150 (70058-03):** still "In Commercial Distribution" in GUDID (published 2014-09-15), even though Abbott's 2026-08 US catalog lists DBEC-125 only.
- **Synsiro Pro:** P170030/S055 (2025-08-19) approved "an additional trade name, Synsiro Pro" for the Orsiro Mission PMA device. No GUDID brand "Synsiro" was found (openFDA 404). Possible alias/new-row candidate. Not added.

## Checked — no fill
- Dragonfly OpStar: AccessGUDID DI 05415067031129 still has no device sizes (public version 2023-08-14). openFDA 510(k) shows nothing newer than K230411. The Abbott US overview page (MAT-2115908 v3.0) has no dimensions. No publicly indexed eIFU PDF was found, and nothing was bypassed. The recall-record values stay held for Jeff.
- Shockwave US IFU library (re-listed 2026-10-17): newest US coronary docs are PN-77417 Rev C (Aero Fly, 2026-10, already checked in pass 21–24), PN-73663 Rev B, PN-64192 Rev D. New 2026-09 Aero Fly IFUs are OUS (HLE/EDC) — rejected. P200039 S020/S021/S025 are manufacturing 30-day notices.
- PMA supplements 2025–2026 for all guide PMAs: only process/packaging changes, apart from the Orsiro items above and Diamondback P130005/S048 (2026-01-14, IEC 60601 warnings added to the eIFU).
- Integrity P030009/S039 (2010 approval): no FDA labeling/SSED PDF posted (accessdata 404). delivery_length stays blank.
- XIENCE Sierra US eIFU EL2139094-EN Rev. A (indexed direct PDF; already the source for pass 03/09): no strut thickness or crossing profile.
- NC TREK RX: only third-party IFU copies are indexed (imimg.com, rejected). No indexed Abbott eIFU PDF.
- Launcher ID mm: Medtronic US spec sheets give inches only (not converted). Medtronic blocks curl.
- SION blue PLUS tip load: still no OEM value.
- GUDID device_sizes scan of the other blank rows (NC TREK, NC Quantum Apex, AngioSculpt, Turnpike, Launcher, Vista Brite, AngioJet, Cougar, SION blue PLUS, SYNERGY XD, Onyx Frontier, Resolute Onyx, REBEL, NC Euphora, XIENCE Sierra) found no new fields for the blank cells.
- N/A by device type (unchanged): pressure-wire french/sheath/guidewire/MHz/pullback; IVUS/OCT wire_diameter + physiology_indices; solid-state pullback; Navvus II MHz/pullback; ROTAPRO/ELCA/Shockwave french/sheath/NP/RBP/burr.
