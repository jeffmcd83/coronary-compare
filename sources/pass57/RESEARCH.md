# Pass 57 — coronary gap-fill (Mon 2026-11-23, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run; recall CSVs untouched (weekly Wednesday routine only). Structural heart not touched.

## Feed cuts (checked 2026-11-23 ~8:50 AM ET)
openFDA meta.last_updated: 510(k) 2026-11-09, PMA 2026-11-09, UDI 2026-11-02 (recall 2026-11-19, not used). No cut newer than pass 55/56, and the 11-02..11-09 decision window was already swept in pass 55.
AccessGUDID daily deltas: 2026-11-19 and 2026-11-20 newly published and parsed (11-21, 11-22, 11-23 → 404, not yet posted). Files off-repo in /workspace/gudid_delta/p57/. Script: gudid_delta.py (pass-56 script, paths updated).

## Angles tried
1. **AccessGUDID deltas 11-19 / 11-20** (raw/gudid_delta_hits.json, 121 hits on guide product codes/brand regexes): no new or updated DI for any guide row (0 catalog/DI matches against coronary-specs-verified.csv).
   - Boston Scientific original SYNERGY (P150003, H7493926xxxxx, 60 DIs) updated to Not in Commercial Distribution — not a guide row (guide has SYNERGY XD and SYNERGY MEGATRON only; no catalog overlap). No action.
   - Sonorous NV "BosCATH Support Catheter" (K254046, QJP/DQY, SE 2026-04-21, 6 new DIs SON-105/115/125-00x): GUDID description = "neuro and peripheral vasculature" → out of scope, not a candidate.
   - Wallaby "p17XR Microcatheter" (K254071, KRA/QJP/DQY, SE 2026-08-18, 4 new DIs): neurovascular → out of scope.
   - Others: Abbott/St. Jude EnSite mapping (DQK, EP), GE Vivid ultrasound — not coronary guide devices.
2. **CrossFAST CFM60** — AccessGUDID devices/search.json "CFM60" → 0 (raw/agudid_CFM60.json); "CrossFAST" → CFM55 only (2 records); openFDA UDI "CFM60" → no match. Vantis WP media API (WebFetch; curl gets sgcaptcha, not bypassed): newest upload still 2026-01-05 (favicon). Dims stay blank; CFM55 not copied.
3. **NHanceIT** — AccessGUDID 0 (raw/agudid_NHanceIT.json); openFDA UDI no match.
4. **Shockwave WP media API** (raw/sw_media_since1119.json): 0 uploads since 2026-11-19 (only one since 11-01: C2 Aero animation thumbnail jpg, 11-06, already seen).
5. **Shockwave C2+ tip_profile** — web search surfaced a NEW lead: Turin CTO Chip 2025 "Factoids" booklet (https://turinctochip.com/wp-content/uploads/2025/05/TCC25_Factoids-booklet.pdf, p.32; text extract raw/tcc25.txt) table "Shockwave C2+ … Tip Profile 0.023 in, Max crossing 0.044–0.047 in, 5F, 138 cm". Third-party Italian conference compilation (page footer carries a Boston Scientific IC code, not a Shockwave doc); not OEM, not US, not FDA → **not used**. US C2+ tech sheet SPL 66116 Rev E and US product page still give no tip profile. Mentioned to Jeff as a lead (not recommended).
6. **Diamondback 360 Precision tip_profile** — search again returns only OUS procardia.pl IFU/catalog (Classic crown sibling C-2DB-CL125-135, "leading edge profile .016 in"), Baystate copy of an older US sell sheet (DBEC-125 Classic, no tip), OUS brochure MAT-2202900. Sibling/OUS → not used.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45–56: IVUS/OCT physiology_indices N/A; pressure-wire MHz/pullback N/A; Navvus II MHz/pullback N/A; OpStar MHz (OCT N/A) and pullback (Jeff decision); Eagle Eye pullback (solid-state); ROTAPRO/Diamondback/ELCA rbp N/A. FDA cfPMN web search not retried (gated pass 51).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions
- New (FYI, not recommended): Shockwave C2+ tip profile 0.023 in appears only in a third-party OUS conference booklet (TCC25 p.32); leaving blank.
- Still open: Euphora K261759 (recommended); Navvus II K233904/dPR (not recommended); OpStar pullback_speed from OPTIS system manual (not recommended); balloon new-row candidates from pass 51 (Firefighter NC Pro/Pro, Sprinter Legend RX/NC Sprinter, Sapphire ULTRA/NC ULTRA/NC 24, Ryurei, FLASH Flex); PendraCare Climber/Primum row (pass 54).
