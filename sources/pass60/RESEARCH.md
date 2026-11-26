# Pass 60 — coronary gap-fill (Thu 2026-11-26, scheduled ~9:00 AM ET) — research no-op

Result: no new exact-model US OEM/FDA values that the standing rules allow. values.csv header-only; conflicts.json empty.
Fill unchanged 90.1% (925/1027; 77 rows). Weakest: Imaging & physiology 73.5 (144/196), Atherectomy & IVL 80.6 (87/108). Both unchanged.
Recall checks not run; recall CSVs untouched (weekly Wednesday routine only). Structural heart not touched.

## Feed cuts (checked 2026-11-26 ~8:50 AM ET)
openFDA meta.last_updated: 510(k) 2026-11-16, PMA 2026-11-16, UDI 2026-11-02 — unchanged since pass 58 (that 11-09..11-16 window was already swept in pass 58). No new decisions to sweep.
AccessGUDID daily deltas: 2026-11-25 and 2026-11-26 newly published and parsed (pass 58 covered 11-23/11-24). Files off-repo in /workspace/gudid_delta/p60/. Script: gudid_delta.py (pass-57 script, paths updated).

## Angles tried
1. **AccessGUDID deltas 11-25 / 11-26** (raw/gudid_delta_hits.json, 12 hits on guide product codes/brand regexes): no new or updated DI for any guide row. Hits = St. Jude EnSite (DQK, EP), THD Procto software, Ablative Solutions Peregrine infusion catheter (KRA, renal denervation, → Not in Commercial Distribution), BD VAMP (KRA). No action.
2. **RAYWATT K260445** — 510(k) summary still not posted (cdrh_docs/pdf26/K260445.pdf and reviews/K260445.pdf → 404; FDA 510(k) DB page last updated 11/23/2026, no summary link; raw/K260445_pmn.html). AccessGUDID "RAYWATT" / "Chouette" → 0 (raw/agudid_RAYWATT.json, raw/agudid_Chouette.json). Row specs stay blank per the pass-59 standing decision ("specs blank until a 510(k) summary, IFU, or GUDID record lands").
   - NEW lead (not applied — standing decision): RAYWATT's own global product pages name the exact model. https://www.raywatt.com/eng/pd_faster.html (FASTER OCT system: 400 frames/s, 24,000 rpm, A-scan 200 kHz, wavelength 1300 ± 50 nm, Class 1 laser; Rotary Junction pullback: standard 60 mm @ 60 mm/s or 100 mm @ 100 mm/s; high-resolution 60 mm @ 20 mm/s or 100 mm @ 40 mm/s; fast 60 mm @ 120 mm/s) and https://www.raywatt.com/eng/pd_chouette.html (Chouette: profile 2.6 F / 1.7 F, lens-to-tip 16 mm, usable length 1440 mm, no saline priming, pullback length 60/100 mm). Snapshots raw/raywatt_pd_faster.html, raw/raywatt_pd_chouette.html. Not US-labelled docs (no FDA/US reference on the pages; may predate clearance); fields that would fill: modality (OCT — also stated by the FDA classification name "System, Imaging, Optical Coherence Tomography (OCT)" on the K260445 DB record) and pullback_speed. frequency_mhz = N/A for OCT (same as Dragonfly OpStar). → Decision for Jeff.
3. **CrossFAST CFM60** — AccessGUDID DI 00860007727924 (raw/agudid_CFM60_lookup.json): version 1, publicVersionDate 2026-11-24, In Commercial Distribution, description "6F, Catheter with Rapid Exchange Length", deviceSizes null → no new dims (6 F already on the row). K262817 summary PDF has no text layer of dims (re-checked; already mined in pass 39–41). Vantis WP media: newest upload still 2026-01-05. CFM55 not copied.
4. **AGENT 40 mm (P230035/S008)** — AccessGUDID search "Paclitaxel-Coated Balloon Catheter": AGENT™ = the same 28 catalogs already on the row (12/15/20/30 mm); no 40 mm catalog (H74939608 40xx); openFDA UDI cut still 2026-11-02. 40 mm length not applied (no GUDID catalogs).
5. **NHanceIT** — AccessGUDID 0. **IMDS InfuseIt K263017** — summary still 404; AccessGUDID "InfuseIt" only Salter Labs pressure infusors (unrelated).
6. **Shockwave WP media** since 11-19 (raw/sw_media_since1119.json): 1 upload, an OBL reimbursement video thumbnail (11-25) → nothing for C2+ tip_profile.

## Skipped (exhausted / N/A / sibling / OUS / gated)
Same list as passes 45–57: IVUS/OCT physiology_indices N/A; pressure-wire MHz/pullback N/A; Navvus II MHz/pullback N/A; OpStar MHz (OCT N/A) and pullback (Jeff decision); Eagle Eye pullback (solid-state); ROTAPRO/Diamondback/ELCA rbp N/A; Diamondback tip and C2+ tip (OUS/sibling/third-party only). FDA cfPMN web search not retried (gated pass 51).

## Applied
None.

## Conflicts logged
None (conflicts.json = []).

## Jeff decisions
- New: RAYWATT FASTER OCT / Chouette — allow RAYWATT's own product pages (raywatt.com/eng, exact model, not US-specific) to fill modality = OCT and pullback_speed (20/40/60/100/120 mm/s; 60 or 100 mm pullback), ahead of the 510(k) summary? Pass-59 standing decision currently says wait for summary/IFU/GUDID. Recommendation: wait for the 510(k) summary (expected soon); at most allow modality = OCT from the FDA classification name.
- Still open: Euphora K261759 (recommended); Navvus II K233904/dPR (not recommended); OpStar pullback_speed from OPTIS system manual (not recommended); C2+ tip 0.023 in from TCC25 booklet (not recommended); balloon new-row candidates from pass 51; PendraCare Climber/Primum row (pass 54); IMDS InfuseIt K263017 (hold for summary); AGENT 40 mm length (once GUDID catalogs appear).
