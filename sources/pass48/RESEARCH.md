# Pass 48 — coronary gap-fill (Mon 2026-11-02, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest categories: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run and recall CSVs not touched (weekly Wednesday routine only).
Remaining Imaging and Atherectomy/IVL blanks are almost all N/A by device type (pressure-wire french/sheath/MHz/pullback, IVUS wire/physiology, OCT MHz, solid-state pullback, IVL/atherectomy NP/RBP/burr/french). Blanks stay blank.

## Angles tried (new vs passes 44-47 unless noted)
1. **CrossFAST CFM60 (required recheck; ships Nov 2026).** AccessGUDID "CFM60" → "SEARCH RESULTS FOR: CFM60 (0 result)". "CrossFAST" and "Vantis" → 2 results, CFM55 only (raw/agudid_*.html). Vantis WP media API: newest upload 2026-01-05, so no CFM60 sheet (raw/vantis_media.json). The WP pages/posts API returned 202 (bot check). Not bypassed.
   - A web-search summary claimed CFM60 "ID 0.056 in". None of the cited pages (BioSpace/PRNewswire 2026-10-13 release, Innolitics K262817 page) states that figure; they say only "larger lumen", "shorter distal tip", "6F guide", "0.014 in wire". Not used. CFM55 values not copied.
2. **openFDA 510(k) window 2026-10-15 onward**: 34 decisions, cut still 2026-10-18/19 (meta last_updated 2026-10-19). Nothing new in scope. K260168 (Skycade) summary PDF still 404 (watch item for the Wednesday routine).
3. **New: openFDA 510(k) device-name/applicant sweep for rows with open blanks** (raw/k_names.txt): TriReme/Chocolate, Ringer, Pantera, NC Quantum, Cougar, ROTAPRO, Launcher, Vista Brite Tip. Previously unread summaries were fetched (raw/pdf/, text in docs/):
   - Launcher K022764 (7F), K023402 (8F), K030779 (5F), K103386 (hub material, scanned), K132673 (5F/6F): no inner diameter in mm (no dimensional tables).
   - Vista Brite Tip K021593 (6F 0.070" in title, inches only), K972978, K982632, K992673 (scanned; device-description prose only, read by page image): no ID in mm. Launcher / Vista inner_diameter_mm stay blank (inches are not converted).
4. **New: Abbott K252512 (Armada 14 NC PTA, 2026-02)** lists NC TREK NEO (K220634) and NC TREK OTW (K180040) as reference devices. Both are siblings, not NC TREK RX, and no figures are tabulated (tip entry / crossing tested, no values). NC TREK RX NP/tip/crossing stay blank.
5. **New: openFDA UDI device_sizes for Shockwave QMG catalogs** (raw/udi_shockwave_QMG.json, raw/udi_sizes.txt). "Introducer Sheath Compatibility 6 French" exists only on the original Shockwave C2 (C2IVL*, not a guide row). C2+ (C2PIVL*), C2 Aero (C2AIVL*) and C2 Aero Fly (C2AFIVL*) records have no sheath or tip field. Their "Guidewire Compatibility 5/6 French" is the guide size already in the rows. Nothing to apply. Not used as a sibling value.
   - Data-quality note: GUDID Aero Fly "Balloon Proximal OD 0.044–0.047 Millimeter" is a unit error (inches). Informational only.
   - ROTAPRO GUDID: "Guidewire Diameter" field carries the burr size. No sheath value.
6. **Chocolate XD tip profile**: web search again found only the LA brochure MC-005667 (crossing only, defined balloon-to-tip) and K153682 (no tip number). No change.
7. **SION blue PLUS / Cougar tip load**: K243733 predicate table (SION blue, sibling) has no tip-load figure. For Cougar, the only figure is a reseller listing (Cougar LS 0.7 g; third-party, and LS is a sibling). Not used.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45/47: Shockwave C2+ tip/french/sheath; ROTAPRO/Diamondback/ELCA N/A fields; Diamondback tip (Abbott eIFU gated); Dragonfly OpStar MHz/pullback/wire; Navvus MHz/pullback; pressure-wire N/A fields; Launcher/Vista ID mm; SION blue PLUS/Cougar tip load; AngioJet lumen; BioFreedom max expansion; NC TREK RX NP/tip; Pantera Pro / NC Quantum Apex / DES crossing; CFM60 dims (unpublished; AccessGUDID still 0).

## New-row candidates
None.
