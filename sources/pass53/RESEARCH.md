# Pass 53 — coronary gap-fill (Thu 2026-11-12, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run; recall CSVs untouched (weekly Wednesday routine only). Structural heart not touched.

## Feed cuts (2026-11-12)
openFDA 510(k)/PMA/UDI 2026-11-02 (unchanged since pass 52), recall 2026-11-07 (not used). AccessGUDID daily deltas: newest posted file is still 2026-11-10 (parsed in pass 52); 11-11 / 11-12 not yet published → nothing new to parse.

## Angles tried
1. **CrossFAST CFM60** — AccessGUDID es_export "CFM60" → 0 hits (raw/agudid_CFM60.csv); "CrossFAST" → CFM55 only (raw/agudid_CrossFAST.csv). Dims stay blank; CFM55 not copied.
2. **openFDA 510(k) decisions 2026-10-20..cut (150)** filtered to coronary/imaging product codes (raw/k510_new.json): K261648 Evident Vascular Guidance System (IYO) — summary (docs/K261648.txt) = peripheral imaging catheters only; reference devices OptiCross 18 Peripheral (not a guide row); no OptiCross HD / Eagle Eye / OpStar figures. K262093 Rivanna Accuro XV (not coronary). K260686 Zylox PanFlex (peripheral; ruled out before).
3. **Dragonfly OpStar pullback_speed** — Abbott OPTIS Integrated Next Imaging System Operation & Maintenance Manual (model 1014933, released 2021-03-01; "System Specifications → Imaging Specifications", manual p.44; third-party mirror https://www.easymanua.ls/abbott/optis-1014933/manual) states "Pullback Speed Settings: 18.0 mm/sec, 36.0 mm/sec" (pullback range 54 / 75 mm) for the system, used with "Dragonfly OPTIS or Dragonfly OpStar" catheters. **Not applied**: it is a console/system figure shared with the sibling catheter (pass-32 precedent: OPTIS system figures not used for the catheter row) and the copy is a non-OEM mirror. → Decision for Jeff.
4. **Diamondback 360 tip_profile / french** — US IFU 92-10023-02 (rskmedical mirror) and P130005c: crown/OAD OD/guide only (already in row). Procardia catalog "leading edge profile .016 in" = OUS distributor catalog for the pre-Precision device → not used.
5. **Shockwave C2+ tip / sheath** — US product page + 2025-01 US tech sheet + GUDID: crossing range / 5F guide only (already in row). PN-72626 Rev B is OUS IFU (not used).

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45–51: IVUS/OCT wire_diameter + physiology_indices N/A; pressure-wire french/sheath/guidewire/MHz/pullback N/A; Navvus II MHz/pullback N/A; OpStar MHz (OCT N/A); Eagle Eye pullback (solid-state); ROTAPRO/Diamondback/ELCA/Shockwave NP/RBP/burr/sheath N/A or unpublished; NC TREK RX NP/tip/crossing; Chocolate/Ringer tip; Pantera/Quantum/Euphora/Evo crossing; SION blue PLUS/Cougar tip_load; Launcher/Vista ID mm; BioFreedom max_expansion; DES crossing (OUS only); AngioJet Spiroflex lumen; CFM60 dims (unpublished). FDA cfPMN web search not retried (gated in pass 51; openFDA cut unchanged).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions
- NEW: Dragonfly OpStar pullback_speed — fill "18 or 36 mm/s (OPTIS system setting; 54/75 mm pullback)" from the Abbott OPTIS Integrated Next O&M manual? Not recommended without an Abbott-hosted copy; it is a system spec, not a catheter spec.
- Still open from pass 51: Euphora K261759 (recommended); Navvus II K233904/dPR (not recommended); balloon new-row candidates (Firefighter NC Pro/Pro, Sprinter Legend RX/NC Sprinter, Sapphire ULTRA/NC ULTRA/NC 24, Ryurei, FLASH Flex).
