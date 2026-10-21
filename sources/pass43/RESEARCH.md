# Pass 43: weekly recall and new-model refresh (Wed 2026-10-21, ~08:52–09:20 AM ET). No-op for data.

Result: **no new recalls, no new models, no spec changes.** Recalls stay at 110 (19 rows; 4 Open, 106 Terminated). Fill unchanged 90.7% (919/1013).

## openFDA data cut dates (meta.last_updated, queried 2026-10-21 ~08:52 ET)
- device/recall: **2026-10-19** (59,536 records; pass 39 saw 2026-10-15 / 59,494)
- device/enforcement: **2026-10-14** (40,300 device enforcement reports, pulled in 5 report-date slices)
- device/510k: **2026-10-12** (latest decision in data 2026-10-11); device/pma: **2026-10-12** (latest decision 2026-10-09). Pass 39 saw 2026-10-05.
- device/udi: **2026-10-01** (unchanged). AccessGUDID daily deltas 2026-10-19 and 2026-10-20 parsed (pass 39 covered to 2026-10-16; no files for 10-17/10-18).
- FDA cfPMN web search: HTTP 302 to bot-challenge, not bypassed (same as pass 39).

## 1. Recalls (device/recall)
- `python3 recalls.py live sources/pass43/raw/recall_pool.json.gz` (pass-40 rules, unchanged): pool 2,016 recall products (same 2,016 keys as pass 39; 0 new, 0 gone; field diffs are openfda-block only). 110 matches, 3 dropped (the Jeff-ruled Diamondback model-number-only Z-1290-2015, Z-3021-2018, Z-2122-2017).
- coronary-recalls.csv regenerated **byte-identical** to coronary-recalls.pre-pass43.csv.
- Pool records initiated ≥2026-09-01 or posted ≥2026-10-01: only Karl Storz HOPKINS Telescope Z-3333-2026 (name hit, not a guide row).
- FDA "Medical Device Recalls and Early Alerts" page (checked 2026-10-21): no coronary item. 10/15 Edwards transcatheter mitral delivery-system alert = structural heart (out of scope). BSC Imager II angiographic catheters (09/25) is not a guide row (seen in pass 39).

## 2. Historical sweep: device/enforcement (new angle)
- Full device enforcement dataset (40,300 reports; full pool kept off-repo at /workspace/openfda_cache/enforcement_pool_pass43.json.gz, 25 MB; the 82 matched records are in `raw/enforcement_matched_records.json.gz`) run through the same recalls.py matcher (`python3 recalls.py match /workspace/openfda_cache/enforcement_pool_pass43.json.gz`; CSV restored afterwards). Output: `raw/enforcement_matches.csv`.
- 82 matches: 42 are recalls already in coronary-recalls.csv; **40 rejected** — all coincidental collisions of a 5–6-digit row catalog (or the word "ADVANCE") with serial/lot/part numbers of unrelated devices from other firms, e.g. Abiomed Impella (Orsiro 4539xx, Pantera Pro 3932xx/3933xx), St Jude Unify/Ellipse ICD serials (HI-TORQUE BALANCE 100966x, Dragonfly 1014651), BSC EMBLEM/INVIVE serials (AngioJet 106553), Philips CT/MR, Hospira/Hamilton/GE/Thoratec (PressureWire 12952), MicroPort/J&J "ADVANCE" (Export Advance). None names a guide model; none added. No missed historical recall found.
- Enforcement since 2026-09-01 (465 reports) keyword scan: Volcano/Philips IntraSight Plus console Z-3276-2026 (REF 797423/797417, 2026-08-06, Class II) — console not in the guide; no catalog match. Others non-coronary.

## 3. New models / submissions
- `sources/pass43/newmodels.py` (pass-39 script, window 2026-09-01→): PMA supplements for the guide's PMAs: P110019/S145, P170030/S066, P200039/S025, P250041 — all already reviewed in pass 39. No new supplements 10-05→10-12 for any guide PMA.
- All PMA decisions 2026-10-01→10-09 (57, `raw/all_decisions_oct.json`): no coronary PMA/supplement besides P110019/S145. P260007 Edwards Autus valve, JenaValve P250024 = structural/surgical (out of scope).
- All 510(k) decisions 2026-10-01→10-11 (86): no coronary device. Catheter hits are neuro (K261649 Excelsior Reach, K253422, K261938 APRO 88; QJP), EP (K262068), urology, CVC. No reprocessed coronary device (reprocessor applicants: Stryker Instruments only, non-coronary).
- GUDID deltas 10-19/10-20 (`raw/gudid_delta_hits.json`, 56 hits): no new DI for any guide row; no new coronary device. QXMedical Boosting Catheter BC52/57/63/72-150 record updates (existing device, not in guide). LivaNova coronary-sinus cannula = brand-regex false hit (Diamondback "Coro"). Rest: ultrasound, infusion, IOPS consoles.
- Known candidates (IMDS NHanceIT K260559, Vantis CrossFAST K262817) were added as rows in pass 40; nothing new.

## 4. Other
- coronary-recalls-by-supplier.csv was stale since pass 40 (109 total; still listed the 2 removed Diamondback recalls, missing Twin-Pass 3). Regenerated from coronary-recalls.csv (110). No site impact (not used by the build).
