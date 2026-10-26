# Pass 45 — coronary gap-fill (Mon 2026-10-26, scheduled ~9:05 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest categories: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run and recall CSVs not touched (weekly Wednesday routine only).

## Angles tried
1. openFDA 510(k) sweep by product code since 2026-09-01: DQY, DQO, ITX, OBJ, DQX, DXO, MCX, QMG, LOX, LPC, OBI, OWQ, DRG, NIQ, DQK, KRA, PNO, MGB, DQE (raw/k_*.json, `curl -g`).
   - Data cut is still 2026-10-12, the same as pass 43/44.
   - Only coronary-relevant hit: K262817 (CrossFAST), already in the guide.
   - Other hits are out of scope (non-coronary): CIVCO K260114, Siemens ACUNAV K261696, Rapid Medical K253146, Filmecc K261281 (.035 wires), Centerline K263016, Abbott EnSite K261729, SmartWise K254051, TriSalus K253509, OrbusNeich JADE SCORE PTA K261778 (peripheral).
2. Shockwave US /ifu/ page compared against pass 44 (raw/shockwave_ifu_page.html).
   - Only new upload: PN-81501 Rev B, E8 Large peripheral IFU (out of scope).
   - The 825Dx manual link has been removed.
3. Shockwave C2+ / C2 Aero / C2 Aero Fly US product pages re-crawled (raw/sw_*.html). Embedded images saved to docs/.
   - Image contents: marker-spacing graphic, treatment-time chart, Aero Fly feature diagram.
   - No C2+ tip/french/sheath number. Aero/Aero Fly tip 0.022 in already applied (pass 44).
4. CrossFAST CFM60: AccessGUDID still returns 0 results (raw/agudid_CFM60.html); CrossFAST shows only CFM55 (2 records).
   - Web search: only the 2026-10-13 press release (ships Nov 2026, "larger lumen … shorter distal tip", no numbers) and K262817 summary.
   - The CFM55 sell sheet MKT003 Rev B.0 is a sibling and was not used.
   - Vantis site returns an sgcaptcha challenge to curl (raw/vantis_home.html). Not bypassed. WP media API search for CFM60 returned [].
5. Dragonfly OpStar pullback: re-read the K221257 / K253101 / K210458 / K253459 / K230411 tables.
   - The OPTIS system shows image length/collection time and system pullback speeds only (system-level; already judged not a catheter value in pass 32). Not applied.
6. Orsiro Mission tip/lesion entry: two sources checked (docs/irc_orsiro_mission_brochure_2026-04.pdf).
   - Teleflex US IRC brochure MC-011204 Rev 0 (03/2026): no lesion-entry/crossing figure.
   - go.teleflex.com spec sheet (Nov 2025) lists "Lesion entry profile 0.017"", but it carries OUS catalog numbers 4191xx (US = 4539xx). OUS → not used.
7. Ringer: the US IRC procedural guide gives "Distal Shaft 0.027"". That is distal shaft OD, not tip profile, and is already in provenance. Not applied.
   - Chocolate XD: the brochure defines crossing as balloon→tip max, with no separate tip number (as before).

## Skipped (exhausted / N/A / sibling / OUS / gated)
- Shockwave C2+ tip/french/sheath.
- ROTAPRO sheath/NP/RBP and Diamondback/ELCA burr/french/NP/RBP: N/A or exhausted.
- Dragonfly OpStar MHz/wire.
- Navvus MHz/pullback.
- Pressure-wire physiology N/A fields.
- Launcher/Vista ID mm.
- SION blue PLUS/Cougar tip load.
- AngioJet lumen.
- BioFreedom max expansion.
- NC TREK RX NP/tip.
- Pantera Pro / NC Quantum Apex crossing.
- CFM60 length/ID/OD (unpublished).

## New-row candidates
None.
