# Pass 47 — coronary gap-fill (Thu 2026-10-29, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values. values.csv header-only; conflicts.json empty.
Fill unchanged 90.9% (921/1013; 76 rows). Weakest categories: Imaging & physiology 76.9 (140/182), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run and recall CSVs not touched (weekly Wednesday routine only).

## Angles tried
1. openFDA 510(k) sweep, 20 product codes (DQY DQO ITX OBJ DQX DXO MCX QMG LOX LPC OBI OWQ DRG NIQ DQK KRA PNO MGB DQE QJN), decision_date ≥ 2026-10-01 (raw/k_*.json).
   - Data cut 2026-10-19 (same as pass 46). Hits: K260168 Skycade Small Diameter Core Wire (new-model watch item for the Wednesday routine, not a spec source) and K263016 Centerline IOPS (out of scope). No new predicate tables naming a guide row.
2. CrossFAST CFM60: AccessGUDID search "CFM60" → 0 results; "CrossFAST" → CFM55 only (2 records) (raw/agudid_*.html). openFDA UDI (cut 2026-10-01) → CFM55 only. Still unpublished; CFM55 values not copied.
3. Shockwave US /ifu/ page: byte-identical to pass 45 (no new PDFs).
4. Shockwave WP media API "tech sheet" (2024-11 → 2026-10): newest is the C2 Aero Fly US tech sheet already used in pass 44. Re-read C2+ US tech sheet (Shockwave-C2plus-Tech-Sheet_Digital_US.pdf, 2025-01; docs/): crossing .044–.047 max, 5F, 138 cm, .014 only — no tip profile, no sheath. Nothing new.
5. Web search Onyx Frontier crossing profile: only US page "<1 mm" claim and the OUS mzsr.sk sheet (0.038 in, "Not for distribution in the US", rejected pass 24). No change.
6. Web search Dragonfly OpStar specs: only OUS 1014652 distributor spec sheet (rejected earlier) and Abbott US/INT overview pages (no MHz/pullback numbers). No change.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as pass 45: Shockwave C2+ tip/french/sheath; ROTAPRO/Diamondback/ELCA N/A fields; Dragonfly OpStar MHz/pullback/wire; Navvus MHz/pullback; pressure-wire N/A fields; Launcher/Vista ID mm; SION blue PLUS/Cougar tip load; AngioJet lumen; BioFreedom max expansion; NC TREK RX NP/tip; Pantera Pro / NC Quantum Apex / DES crossing; CFM60 dims (unpublished, ships Nov 2026).

## New-row candidates
None.
