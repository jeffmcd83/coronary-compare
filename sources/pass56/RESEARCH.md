# Pass 56 — coronary gap-fill (Thu 2026-11-19, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run; recall CSVs untouched (weekly Wednesday routine only). Structural heart not touched.

## Feed cuts (checked 2026-11-19 ~8:50 AM ET)
openFDA meta.last_updated: 510(k) 2026-11-09, PMA 2026-11-09, UDI 2026-11-02 (recall 2026-11-14, not used). No cut newer than 11-09, and the 11-02..11-09 decision window was already swept in pass 55 (sources/pass55/raw/all_decisions_1102_1118.json: 58 510(k) + 31 PMA; only guide-adjacent items K262590 Brosmed Parafleet PTA = peripheral, P250041/S001 SELUTION = postapproval protocol, no figures).
AccessGUDID daily deltas: 2026-11-18 newly published and parsed (11-19 → 404, not yet posted). Files off-repo in /workspace/gudid_delta/p56/. Script: gudid_delta.py (pass-55 script, paths updated).

## Angles tried
1. **AccessGUDID delta 2026-11-18** (raw/gudid_delta_hits.json, 17 hits on guide product codes/brand regexes): no new or updated DI for any guide row.
   - PendraCare International "Climber Guiding Catheter" (DQY, K250972): 5 NEW DIs — 6F JR4 (GC-P6JR400N), JL4 (GC-P6JL400N), EBU3.5 (GC-P6EB350N), XB3.5 (GC-P6XB350N), XB3 (GC-P6XB300N), In Commercial Distribution. Strengthens the pass-54 new-row candidate (now a multi-curve 6F family listed in GUDID); still not added (Jeff decision).
   - Seigla LiquID 061/071 (DQY, K220691; update) = neuro guide extension, already judged out of scope in pass 49.
   - Merit Pursue (DQY, no submission listed) — peripheral/neuro microcatheter, not a guide row.
   - Others: BD/Edwards HemoSphere Vita modules (DQK), AccurKardia ECG software, GE CardioLab/CARESCAPE, GE Parallel Design probe, Cadwell "Sierra II" (brand-regex false positive on XIENCE Sierra).
2. **CrossFAST CFM60** (Vantis said ships Nov 2026) — AccessGUDID search.json "CFM60" → 0 (raw/agudid_CFM60.json); "CrossFAST" → CFM55 only (2 records); openFDA UDI "CFM60" → no match. Vantis WP media API (via WebFetch): newest upload still 2026-01-05 (favicon) — no CFM60 sheet/IFU. Web search: only the 2026-10-13 press release / CI Today / PharmaDeviceNews / LinkedIn ("larger lumen", "shorter distal tip", no numbers). PMC case series (PMC13005390, JSCAI 2026) says a 6F version "with a 0.056-inch inner dimension is expected" — literature written pre-clearance, not OEM/FDA → not used. Dims stay blank; CFM55 not copied.
3. **NHanceIT** — AccessGUDID 0; openFDA UDI no match.
4. **Shockwave WP media API** (raw/sw_media_*.json): uploads since 2026-11-01 = 1 (C2 Aero animation thumbnail jpg). Newest tech sheet/IFU = C2 Aero Fly US (2026-10-19, already used pass 44/47) and E8 peripheral IFU. No C2+ tip profile source.
5. **Diamondback 360 Precision tip_profile** — web search again returns only the OUS Polish distributor IFU/catalog (procardia.pl; Classic crown C-2DB-CL125-135, a sibling, "leading edge profile .016 in" in OUS catalog) and Abbott US pages (6F only). OUS/sibling → not used. Abbott eIFU still not used (gated).

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45–54 (see pass53/RESEARCH.md): IVUS/OCT wire_diameter + physiology_indices N/A; pressure-wire MHz/pullback N/A; Navvus II MHz/pullback N/A; OpStar MHz (OCT N/A) and pullback (Jeff decision); Eagle Eye pullback (solid-state); ROTAPRO/Diamondback/ELCA rbp N/A; etc. FDA cfPMN web search not retried (gated pass 51).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions
- No new items. Pass-54 PendraCare Climber/Primum (K250972) row candidate updated: GUDID now lists 6F JR4/JL4/EBU3.5/EBU3.75/XB3/XB3.5 curves.
- Still open: Euphora K261759 (recommended); Navvus II K233904/dPR (not recommended); OpStar pullback_speed from OPTIS system manual (not recommended); balloon new-row candidates from pass 51 (Firefighter NC Pro/Pro, Sprinter Legend RX/NC Sprinter, Sapphire ULTRA/NC ULTRA/NC 24, Ryurei, FLASH Flex); PendraCare Climber/Primum row.
