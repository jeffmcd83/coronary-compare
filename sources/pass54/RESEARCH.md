# Pass 54 — coronary gap-fill (Mon 2026-11-16, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run; recall CSVs untouched (weekly Wednesday routine only). Structural heart not touched.

## Feed cuts (checked 2026-11-16 ~8:50 AM ET)
openFDA 510(k)/PMA/UDI meta.last_updated still 2026-11-02 (no new decisions to sweep since passes 51–53). Recall cut 2026-11-12 (not used — Wednesday routine).
AccessGUDID daily deltas: 2026-11-12 and 2026-11-13 newly published and parsed (11-11, 11-14, 11-15, 11-16 → 404, not posted). Files off-repo in /workspace/gudid_delta/p54/. Script: gudid_delta.py (pass-52 script, paths updated).

## Angles tried
1. **AccessGUDID deltas 11-12/11-13** (raw/gudid_delta_hits.json, 33 hits on guide product codes/brand regexes): no new or updated DI for any guide row. Hits = ultrasound systems/transducers (ITX/IYO/IYN), ECG software (DQK), Instylla guidewire (DQX, K140485, embolic-delivery context), brand-regex false positive (ALIFAX reagent), and **PendraCare International "Climber Guiding Catheter"** (DQY, K250972, catalog GC-P6EB370N / model EBU3.75, In Commercial Distribution).
   - K250972 (docs/K250972.txt; https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250972.pdf): "Primum Hydrophilic Guiding Catheter", SE 2025-06-29, 5/6/7/8 F; IFU "intended to be used in the coronary or peripheral vascular system"; predicate Convey (K120585, K132197). GUDID lists it under brand "Climber". → US coronary-labelled guiding catheter with no row: **new-row candidate for Jeff** (not added; brand vs 510(k) device name differs, no OEM spec sheet checked).
2. **CrossFAST CFM60** — AccessGUDID search.json "CFM60" → 0 (raw/agudid_CFM60.json); "CrossFAST" → CFM55 only (2 records). openFDA UDI CrossFAST → CFM55 only. Dims stay blank; CFM55 not copied. NHanceIT also still 0 in AccessGUDID.
3. **Dragonfly OpStar pullback_speed** — searched for an exact-model OEM IFU statement: only journal methods sections (JAT 2026, JAHA, J Cardiol TACTICS, JACC Adv, REC Interv Cardiol) stating 18–36 mm/s with OPTIS/OpStar. Literature, not OEM/FDA → not used. Pass-53 decision item unchanged.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45–53 (see pass53/RESEARCH.md). No openFDA 510(k)/PMA sweep (cut unchanged since pass 51–53 sweeps). FDA cfPMN web search not retried (gated pass 51).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions
- NEW: add a PendraCare "Climber" (Primum Hydrophilic, K250972) guiding-catheter row? (US coronary/peripheral label; GUDID In Commercial Distribution).
- Still open: OpStar pullback_speed from OPTIS system manual (not recommended); Euphora K261759 (recommended); Navvus II K233904/dPR (not recommended); balloon new-row candidates from pass 51 (Firefighter NC Pro/Pro, Sprinter Legend RX/NC Sprinter, Sapphire ULTRA/NC ULTRA/NC 24, Ryurei, FLASH Flex).
