# Pass 31 research notes (2026-10-18, 7:22 AM ET scheduled run)

Imaging & physiology + Atherectomy & IVL first, then other exact-model blanks. New angles this pass: the **Medtronic US Manual Library** (manuals.medtronic.com, en_US — public product-name search, no captcha; the "View Manual" step is only an optional e-mail opt-in; PDFs on medtronic.com fetched with headless Chrome because medtronic.com returns an "Incorrect Browser" page to curl); **Boston Scientific eLabeling** portal (direct indexed PDFs + US portal); **Teleflex IRC wp-content PDFs** (direct, indexed); shockwavemedical.com product pages; openFDA 510(k)/PMA decisions to the openFDA data cut (last_updated 2026-10-05). **1 value applied** (blank cell). Fill 891 → 892/992 (89.9%).

## Applied
- **Integrity (BMS) — delivery_length_cm** = "140 cm (MicroTrac RX and OTW delivery systems effective length)". Source: Medtronic Integrity Coronary Stent System US IFU M728550B001 Rev 1A ("CAUTION: Federal (USA) law…"; US Manual Library, publication date on or before 2013-03-01) §1.0 Device Description, printed p.2 (PDF p.4): "The MicroTrac RX (Figure 2) and the MicroTrac OTW (Figure 3) delivery systems have an effective length of 140cm." https://www.medtronic.com/content/dam/emanuals/cardio/CONTRIB_099717.pdf (docs/mdt_integrity_IFU_M728550B001.pdf). Exact model (row = GUDID brand "Integrity", RX + OTW). Row stays marked DISCONTINUED (Jeff 2026-10-17). Earlier passes had only the Medtronic US catalog (no length) and the sibling Resolute Integrity DES.

## Logged in conflicts.json (not overwritten — Jeff to decide)
1. **Resolute Onyx rbp_atm** size range: current US IFU M055193T001 Rev AF (2024-07-24) Table 1, p.5 (PDF p.6): "Rated burst pressure: 2.0-4.0 mm = 18 ATM, RX only: 4.5-5.0 mm = 16 ATM" vs existing "18 atm (2.25–4.0 mm)" from the 2017 SSED P160043 (pre-dates the 2.0 mm sizes, which the row already lists). Values identical; only the range label differs. Kept out of values.csv on purpose (passes_apply.py would auto-replace the SSED value with an IFU value).

## Corroborated (no change)
- Medtronic Onyx Frontier US IFU M016449C001 Rev E (2024-07-24) Table 1: diameters 2.0–5.0, effective length 140 cm, NP 12, RBP 18 (2.0–4.0)/16 (4.5–5.0), min guide ≥5 Fr (1.42 mm/0.056 in) — all match. No crossing profile number (text only: "lower crossing profile").
- Resolute Onyx US IFU M055193T001 Rev AF: 140 cm, NP 12, ≥5 Fr — match; no crossing profile number.
- NC Euphora US IFU M333846D001 Rev 1A (2014-08-21): no crossing/tip numbers (symbols + directions only).
- Medtronic US guide catheter IFU M047606C001 Rev A (2024-02-27; Launcher): "Inner diameter" appears only as a label symbol — no ID value (Launcher ID mm stays blank; inches not converted).
- Teleflex Pantera Pro US brochure MC-011240 Rev 0 (10/25; irc.teleflex.com/wp-content/uploads/2026/06/…; docs/tflx_Pantera-Pro-Product-Brochure_Digital_2026-06.pdf): 5F/0.056 in, 0.014 in, lesion entry 0.017 in, 140 cm, NP 7/RBP 14 compliance chart, 33 catalogs 393289–393321 — all match; no balloon crossing profile.
- Shockwave C2 Aero product page spec table (tip 0.022 in, crossing 0.044–0.047 in, 6 Fr) — matches existing; C2+ page/tech sheets list crossing only; shockwavemedical.com has no C2 Aero Fly product page (404).

## Checked — no fill
- **Dragonfly OpStar (1014651)**: no publicly indexed direct Abbott eIFU PDF (searches return only the gated eLabeling home page); US overview/ordering pages (MAT-2306101 v1.0) no dims; spec sheet MAT-2104450 v1.0 on a distributor host is "for DISTRIBUTION outside of the U.S. ONLY" and lists catalog 1014652 (not 1014651) — not used (as in earlier passes). FDA recall-record values not re-proposed (Jeff rejected). Nothing bypassed.
- **BSC eLabeling**: US portal returns "online product manuals are not available for your country" (US labeling in-box only). Indexed global NC Quantum Apex IFU 51427546-01B and Vietnam eDFU 92590768-01 A (docs/bsc_*.pdf): no crossing/tip profile. Peripheral ROTAPRO eIFU is a peripheral sibling — not used for coronary ROTAPRO.
- **Turnpike ID**: Teleflex US IFU 110485-rA (2026-04/07 uploads) gives ODs/guide only — same as before.
- **openFDA** (data cut 2026-10-05): 510(k) decisions 2026-09-01 → cut (docs/k510_20260901-20261018_openfda.json) — no clearance for any guide row (only unrelated PTA/peripheral/ICE devices); PMA decisions 2026-10-01 → cut (docs/pma_20261001-20261018_openfda.json) — only P110019/S145 (XIENCE 30-day notice) in coronary scope; no labeling/spec change. Nothing newer than 2026-10-17 is in openFDA yet.
- Cougar: no manual in the Medtronic US Manual Library (product-name search returns none).
- N/A by device type (unchanged): pressure-wire french/sheath/guidewire/MHz/pullback; IVUS/OCT wire_diameter + physiology_indices; solid-state pullback; Navvus II MHz/pullback; ROTAPRO/Diamondback/ELCA/Shockwave NP/RBP/burr/french/sheath.

## Notes
- Innovative Health Reprocessed Eagle Eye Platinum ST RX row still present (closed item; present since pass 13b).
- passes_apply.py glob extended to sources/pass3*/values.csv (backup passes_apply.pre-pass31.py) — otherwise pass 31+ values would be ignored.
