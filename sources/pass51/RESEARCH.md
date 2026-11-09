# Pass 51 — coronary gap-fill (Mon 2026-11-09, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest categories: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run and recall CSVs not touched (weekly Wednesday routine only).

## Feed cuts (2026-11-09)
openFDA 510(k)/PMA 2026-10-26 (unchanged since pass 50), UDI 2026-10-01, enforcement 2026-10-28, recall 2026-11-05 (not used).

## Angles tried (new vs passes 45–50)
1. **CrossFAST CFM60 (ships Nov 2026).**
   - AccessGUDID "CFM60" → 0 results; "CrossFAST" → 2 results, CFM55 only (raw/agudid_CFM60.html, agudid_CrossFAST.html).
   - openFDA UDI: CrossFAST → 2 DIs (CFM55); version_or_model_number CFM60* → NOT_FOUND (raw/udi_*.json).
   - **New:** AccessGUDID daily delta XMLs 2026-11-04, 11-05, 11-06 (first files after pass 49's 11-03; /workspace/gudid_delta/p51/, off-repo) parsed with sources/pass51/gudid_delta.py (pass-49 script + Vantis/CrossFAST/CFM6 catch + deviceSizes capture). 292 coronary-code/brand hits (12 New): no Vantis/CrossFAST record and no new or updated DI for any guide row (SYNERGY™ original-brand DIs set Not in Commercial Distribution — not a guide row; Stryker Excelsior Reach K261649 = neuro QJP). raw/gudid_delta_hits.json.
   - Vantis home page re-read (no bot wall): "6F CrossFAST Model" news tile + TCT 2026 event only; no spec table, no CFM60 figures. WP media newest still 2026-01-05. Web search: press items (BioSpace/CIT/g-medtech, 10-13/10-14) restate "larger lumen, shorter distal tip" without numbers.
   - length_cm / inner_diameter_in / outer_diameter_in stay blank. CFM55 values not copied.

2. **FDA 510(k) web database (accessdata cfpmn) for decisions after the openFDA cut** — returns a JS "request is being processed" wait page / headless load timed out. Treated as gated; not bypassed.

3. **New: 510(k) submission-completeness audit** (sources/pass51/subs_audit.py; raw/k510_2024on_codes.json, subs_audit.json): openFDA 510(k) decisions 2024-01-01..cut for 17 coronary product codes, device_name matched to guide row names, K-number missing from the row's fda_submission:
   - **K261759 — Euphora Rapid Exchange (RX) Balloon Dilatation Catheter**, Medtronic Ireland, LOX, SE 2026-07-27. Summary (docs/K261759.txt): predicate K143480 (the Euphora row's only listed submission); only change = PTFE non-hydrophilic proximal-shaft material; same model. Same situation as NC Euphora K261428, which Jeff approved adding in pass 40. **Not applied — decision for Jeff** (add "K261759 (2026-07-27: proximal-shaft material change, same model)" to Euphora fda_submission?). URL: https://www.accessdata.fda.gov/cdrh_docs/pdf26/K261759.pdf
   - **K233904 — ACIST RXi System; ACIST Navvus II Catheter**, SE 2024-07-17 (docs/K233904.txt). Adds a non-hyperemic dPR modality to RXi **system software**; summary p.3: "The Navvus Catheter and accessories … are not affected by this submission." By the pass-13 precedent (system/software indices such as RFR not added to wire rows) dPR is not added to Navvus II physiology_indices. **Decision for Jeff** only if he wants K233904 listed on the Navvus II row / dPR shown. URL: https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233904.pdf
   - K261428 matched the Euphora row by name, but it's NC Euphora (already listed there). K243733 matched SION blue but is the SION blue PLUS row (already listed).

4. **New: US PTCA-balloon coverage check** (openFDA 510(k) LOX 2023+, raw/k510_LOX_2023on.json; openFDA UDI by brand). US-labeled coronary balloons in commercial distribution that have no guide row (new-row candidates only, not added):
   - MicroPort Firefighter NC Pro — K223189 (2023-07-21), 59 GUDID DIs In Commercial Distribution. Firefighter Pro — K252116 (2026-04-07), not yet in GUDID.
   - Medtronic Sprinter Legend RX — K251970 (2026-01-17) / K103095; NC Sprinter / Sprinter (P790017) — in GUDID, In Commercial Distribution.
   - OrbusNeich Sapphire ULTRA (K233505) / Sapphire NC ULTRA (K233499) / Sapphire NC 24 (K211807) / Sapphire NC Plus (K162209) — in GUDID.
   - Terumo Ryurei — K252295 (2026-03-27), not in openFDA UDI (cut 10-01).
   - Verge FLASH Flex Aorto-Ostial — K254022 (2026-04-02), in GUDID (ostial post-dilatation system).

5. **Imaging / Ath-IVL 510(k) name sweep 2026-06..cut** (raw/k510_imaging_2026H2.json): Bolt SEISMIQ K260246 (peripheral only; "Not for use in the coronary…"; predicate own K250225 — no Shockwave coronary figures), Shockwave E8 K262201 (peripheral), Topcon/Venocare (not coronary). No Dragonfly OpStar / Eagle Eye / Shockwave C2-family figures. No competitor coronary IVL approval (Abbott SonicForce/TECTONIC: approval expected H1 2027 per TCT 2026 coverage).
   - openFDA PMA QMG: Shockwave P200039 only (25 records); no competitor predicate table.
   - Web search Shockwave C2+ specs: US page/tech sheet give crossing range only (already in guide); tip profile still unpublished.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45/47/48/50: Dragonfly OpStar MHz/pullback (no public ungated figure; eIFU not bypassed); IVUS wire/physiology and pressure-wire french/sheath/MHz/pullback N/A; Diamondback tip/french (eIFU gated); ROTAPRO sheath; Shockwave C2+/Aero/Aero Fly sheath, C2+ tip; NC TREK RX NP/crossing/tip; Chocolate/Ringer tip; Pantera/Quantum/Euphora/Evo crossing; SION blue PLUS/Cougar tip_load; Launcher/Vista ID mm; BioFreedom max_expansion; DES crossing (OUS only); AngioJet Spiroflex lumen; CFM60 dims (unpublished).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions / new-row candidates
- Euphora fda_submission: add K261759? (recommended — mirrors approved NC Euphora K261428).
- Navvus II: list K233904 / dPR? (not recommended — system software only; catheter unchanged).
- New-row candidates (balloons): Firefighter NC Pro (+ Firefighter Pro), Sprinter Legend / NC Sprinter, Sapphire ULTRA / NC ULTRA / NC 24, Ryurei, FLASH Flex.
