# Pass 29 research notes (2026-10-17, 7:23 PM ET scheduled run)

Imaging & physiology + Atherectomy & IVL first, then other exact-model blanks. New angles this pass: Philips US IFU library (usa.philips.com/healthcare/support/ifu-library — public, ungated) and Philips documents server eIFUs (documents.philips.com); FDA 510(k) decisions per product code (OBJ/ITX/DQO/DQX/DXO/OBI/OWQ) and per device name through 2026-10-17; PMA decisions 2026-08-01 → 2026-10-17 for every guide PMA and coronary product codes (NIQ/QMG/MCX/LPC/LOX/NWX); Medtronic US NC Euphora tech-spec sheet (fetched with headless browser — public PDF; Medtronic blocks curl); us.myteleflex.com product pages; Cordis NA product page. **1 value applied** (blank cell). Fill 890 → 891/992 (89.8%).

## Applied
- **ELCA Coronary Laser Atherectomy — sheath_compat_fr** = "4 Fr (0.9 mm: 110-001 OTW, 110-003 RX, X-80 110-002 OTW / 110-004 RX); 5 Fr (1.4 mm, 114-009); 6 Fr (1.7 mm 117-016; 1.7 mm E 117-205); 7 Fr (2.0 mm, 120-009) — 120-008 not in US IFU". Source: Philips/Spectranetics US IFU booklets linked from the Philips US IFU library as "US": P020691-A (25AUG21, OTW/RX) p.2 Tables 1.1–1.2 "Sheath Compatibility (Fr)" (docs/elca_otw_rx_us_P020691_A.pdf) and P020690-A (18AUG21, 0.9 mm/X-80) p.2 Tables 1.1–1.2 (docs/elca_x80_p020690-a.pdf). Exact catalog numbers = row catalog list. Previous passes had only the brochure and treated ELCA sheath as N/A. The Canada booklet 7030-0012-A (docs/elca_master-layout_us.pdf, despite the filename) adds 120-008 (2.0 mm E, 0.018 in wire) — Canada, not used.

## Logged in conflicts.json (not overwritten — Jeff to decide)
1. **ELCA guide_compat**: newest Philips IFU D002011088.B (2025-12; en/fr, Rx-only/Federal USA caution; docs/elca_ifu_philips_20260914.pdf) Table 1.1 "Guide catheter (Fr)" = 7 Fr (1.4 mm), 8 Fr (1.7 mm), 8 Fr (2.0 mm) vs. existing brochure D2023060101A value "6/7 Fr (1.4); 7 Fr (1.7); 8 Fr (2.0)". IFU outranks brochure. This revision also drops the sheath-compatibility column and lists only 114-009/117-016/120-009.
2. **ELCA sheath_compat_fr** (info): if Jeff prefers only the newest IFU revision, the 1.4/1.7/2.0 mm part of the pass-29 value could be removed; the US IFU library still links P020691-A/P020690-A as the US booklets.
3. **OptiCross HD fda_submission**: later clearances K230453 (2023-05-18; predicate named in K260816) and K260816 (SE 2026-04-08; OptiCross / 6 / HD / 6 HD incl. Bagless) — row shows K213593 only. K260816 summary (docs/K260816.pdf) confirms 60 MHz HD, 5F/6F, 15 cm telescoping travel (match existing).

## Evidence notes
- GUDID ELCA (docs/udi_elca_openfda_20261017.json, 27 DIs): In Commercial Distribution = 110-004 (0.9 mm X-80 RX), 114-009, 117-016, 120-009; the others (110-001/-002/-003, 117-205, 120-008) Not in Commercial Distribution (2019-02-06 / 2023-09-11). Row n_skus/catalogs unchanged (data-quality flag only).
- PMA decisions 2026-08-01 → 2026-10-17 (docs/pma_supplements_20260901-20261017_openfda.json): only 30-day notices/manufacturing (P110019 S144/S145, P170030 S065/S066, P150003 S113, P160043 S095, P200039 S025, P910001 S126/S127, P170008 S064) + SELUTION P250041 (already in guide). No labeling/spec changes; no new US coronary IVL/atherectomy/imaging PMA.
- 510(k)s through 2026-10-17: no new Dragonfly OpStar (still K192019/K230411), Eagle Eye, Refinity, OmniWire, PressureWire X, COMET II, Diamondback coronary, ROTAPRO or ELCA clearance. New: OptiCross K260816 (above); Navvus II K233904 (2024-07-17, system update — Navvus blanks are N/A).

## Checked — no fill
- Dragonfly OpStar 1014651: only gated Abbott eLabeling, the Abbott US overview/ordering pages (no dims), FDA recall record (rejected by Jeff), China NMPA tender listing (not US) and a distributor page (third-party). Nothing bypassed.
- Philips Eagle Eye Platinum RX eIFU (documents.philips.com, 2026-09-29; docs/eep_rx_philips_20260929.pdf): 3.5F crossing, 2.9F shaft, 150 cm, ≤0.014 in, min guide I.D. 0.056 in, tip 0.019 in, 18.6/17.9 MHz — all match existing; no pullback (solid-state) — N/A fields unchanged.
- AngioSculpt RX PTCA (US IFU library: PN-3264-0001-C insert, PN-3265-0001-C outsert, PN-3072-0001-C, PN-3070-0001-D, PN-3261-0001-C taper tip): no compliance chart, crossing or tip profile.
- NC Euphora: Medtronic US tech-spec sheet UC201704032 IE (©2025; docs/mdt_nc-euphora-tech-spec.pdf) — lesion entry 0.015 in, NP 12, RBP 20, 142 cm, MGCID, compliance table; no crossing profile. Existing values corroborated.
- Turnpike ID: us.myteleflex.com spec table (MC-007701 Rev 1) = ODs/guide only. Pantera Pro: us.myteleflex.com ordering only. Teleflex IRC pages now behind a JS bot-verification interstitial (not bypassed).
- Vista Brite Tip ID mm: Cordis NA product page gives inches in SKU descriptions only (not converted).
- SION blue PLUS / Cougar tip load: no OEM value.
- Diamondback 360 Precision tip_profile: IFU P130005c "Maximum tip diameter" is a symbol-glossary entry only. Shockwave C2+/Aero Fly tip: US IFUs unchanged.
- N/A by device type (unchanged): pressure-wire french/sheath/guidewire/MHz/pullback; IVUS/OCT wire_diameter + physiology_indices; solid-state pullback; Navvus II MHz/pullback; ROTAPRO/Diamondback/ELCA/Shockwave NP/RBP/burr; Shockwave french/sheath; ELCA french_sizes (US IFU labels sheath compatibility, not catheter Fr — not inferred).
