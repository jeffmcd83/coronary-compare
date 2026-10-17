# STANDING_DECISIONS
1. Row key = manufacturer + model family; catalog numbers listed per row from GUDID.
2. Exact model or blank; never copy sibling values. 3. Per-cell source (doc + record/page + URL) in provenance.json.
4. Conflicts are logged in FILL_LOG, never overwritten. 5. Each pass backs up masters as *.pre-passNN.csv.
6. Reprocessed devices = own rows, only with a found 510(k) number. 7. No embolic protection. 8. Publish to /preview/ first.

- 2026-10-12: v1.0 (pass06 build) published to ROOT https://jeffmcd83.github.io/coronary-compare/ with Jeff's approval; /preview/ retained. Future passes publish to /preview/ first (publish.sh) unless Jeff says otherwise; promoting to root uses release.sh <tag> only with Jeff's explicit approval.
- 2026-10-12: v1.0.1 (duplicate-picker fix) released to root with Jeff's approval.
- 2026-10-12: v1.1 (Desktop view, preview-pass07 build) released to root with Jeff's approval.
- 2026-10-13: v1.2 (pass08 build) released to root with Jeff's approval.
- 2026-10-13: Exclude devices not labeled for coronary use (e.g., AngioJet AVX, AV-access only). Implemented as EXCLUDE in build_master.py. Approved by Jeff.
- 2026-10-13: v1.3 (pass10 build, AngioJet AVX removed) released to root with Jeff's approval.
- 2026-10-13: UI (preview-pass10b, preview only): reprocessing rows hidden unless a selected device is reprocessed; removed devices leave empty placeholder slots (table never collapses).
- 2026-10-13: v1.4 (preview-pass10b UI: conditional reprocessing rows, placeholder slots) released to root with Jeff's approval.
- 2026-10-13: v1.5 (preview-pass11, fill 81.5%) released to root with Jeff's approval.
- 2026-10-13: Scope expanded (Jeff approved) to "Coronary & Structural Heart": therapy filter Coronary | TAVI | Mitral TEER | Tricuspid TEER | Shared accessories. Same data rules. US-labelled indications only (e.g. PASCAL tricuspid not added — no US label). Preview only until Jeff approves a root release.
- 2026-10-13: v1.6 (preview-passsh02: Coronary & Structural Heart, fill 76.0%) released to root with Jeff's approval.
- 2026-10-13: Coronary only. Structural heart moved to its own bot/guide; data, research and UI code live in /workspace/structural-specs. No therapy filter here; title "Coronary Comparison Guide". Supersedes the 2026-10-13 scope-expansion entry.
- 2026-10-13: v1.7 (preview-pass11c: coronary-only, structural removed, fill 81.5%) released to root with Jeff's approval.
- 2026-10-13: Header 'Guides' menu built from /workspace/guides.json at build time (CRM style); coronary entry set live.
- 2026-10-13: Product selection moved into each column header (manufacturer select + searchable model, CRM-style); separate picker bar removed. Guide renamed "Coronary Products and Accessories" (title, header, meta, guides.json); URL unchanged. Preview only (preview-pass11e).
- 2026-10-13: Columns now match CRM guide: 4 static supplier columns (Abbott [incl. St. Jude], Boston Scientific, Medtronic, Other grouped by maker), per-column model menu filtered by supplier+category with model count, Clear ✕, Quick info (recalls, open recalls, 2 key specs), Family ▸ panel, global 'Search all models'. Preview only (preview-pass11f).
- 2026-10-13: v1.8 (preview-pass11f: CRM-style supplier columns, Guides menu, renamed 'Coronary Products and Accessories') released to root with Jeff's approval.
- 2026-10-13: Shockwave C2 Aero Fly added as its own IVL row (US PMA P200039/S019); released as v1.9 with Jeff's approval.
- 2026-10-14: v1.10 (preview-pass13b: pass 13 + IH reprocessed Eagle Eye Platinum ST RX, fill 85.0%) released to root with Jeff's approval.
- 2026-10-14: Per-category supplier columns (replaces the generic 'Other' column). Config: supplier_columns.json. For each category the main columns appear first in a fixed order. DES and Balloon use Abbott, Medtronic, Boston Scientific, Teleflex (Jeff's rule). Other categories use the top suppliers by US model count in our data. Every further supplier gets its OWN column to the right, scrolling horizontally. Empty main columns stay and show a note. Acquired makers are folded into the parent column: St. Jude, LightLab and CSI into Abbott; Vascular Solutions and Biotronik AG into Teleflex; Volcano/Volcarica, Spectranetics and AngioScore into Philips; MedAlliance into Cordis.
- 2026-10-14: Biotronik → Teleflex. Biotronik's Vascular Intervention business was acquired by Teleflex effective 2025-07-01 (sources: https://www.biotronik.com/en-us/change-ownership-vascular-intervention-business and https://investors.teleflex.com/news/news-details/2025/Teleflex-Completes-Acquisition-of-BIOTRONIKs-Vascular-Intervention-Business/default.aspx). Biotronik coronary rows (Orsiro Mission, PK Papyrus) are shown in the Teleflex column with an "originally Biotronik" quick-info note and source. GUDID/FDA labeler data is unchanged (manufacturer = Biotronik AG).

## 2026-10-15 — SKU-matching corrections (Jeff-approved)
- Fielder XT: brand regex tightened to ^FIELDER XT$ — XT-A (APW14R009S/309S) and XT-R (APW14R005S/305S) are separate brands in GUDID (raw/udi/Fielder_XT.json; https://api.fda.gov/device/udi.json?search=brand_name:FIELDER) and must not be merged. Row SKUs = AGP140002, AGP140302 only.
- Guidezilla II: brand regex tightened to ^Guidezilla™ II$ — original "Guidezilla™" 5-in-6 (H7493924215050, GUDID brand "Guidezilla™") is a different (first-gen) device, removed from the Guidezilla II row (raw/udi/Guidezilla_II.json).

## 2026-10-15 — NC TREK RX kept (Jeff decision)
Jeff confirms NC TREK RX and NC TREK NEO are both still sold in the US → keep the NC TREK RX row alongside NC TREK NEO (do not retire/merge).

## 2026-10-16 — Corsair Pro submissions (Jeff decision)
Corsair Pro fda_submission = "K161126, K171933". K171933 (SE 2018-02-12, DQX) adds the CTO-crossing indication and names ASAHI Corsair Pro Microcatheter; https://www.accessdata.fda.gov/cdrh_docs/pdf17/K171933.pdf (copy: sources/pass22/docs/K171933.pdf).

## 2026-10-16 — Jeff decisions (pass 25)
- XIENCE Skypoint ONLY: crossing profile 0.0390 in (3.0 × 18 mm) accepted from Abbott US HCP page/brochure MAT-2106263 v2.0 (https://www.cardiovascular.abbott/us/en/hcp/products/percutaneous-coronary-intervention/xience-family/about.html). Brochure value — an IFU value replaces it if published. Not applied to Sierra.
- Abbott eIFU: direct PDF links that are publicly indexed may be used; never solve/bypass a captcha or gated search.
- Row "Diamondback 360 Coronary OAS" renamed "Diamondback 360 Precision" (PMA P130005/S036, approved 2023-06-01: 1.25 mm crown design change + name change). Implemented as a display rename in build_master.py (RENAME) so earlier pass keys still apply; former name kept in the fda_submission note; recalls CSV model name updated.

## 2026-10-17 — Jeff decisions (pass 28)
- Orsiro Mission: 4.5/5.0 mm sizes added (PMA P170030/S058, 2026-06-11; GUDID 473694–473707; Teleflex US IRC page: 89 µm, NP 11 atm, 6 F/0.070 in for 4.5–5.0). The 6 logged pass-27 size conflicts are resolved in favour of FDA/GUDID/US-page evidence over the 2022 brochure (sources/pass28/override.csv, applied in build_master.py; old values kept in conflicts_passes.json).
- Orsiro Mission SKU match tightened to ^Orsiro Mission$ (66 current DIs); the 52 discontinued original "Orsiro" GUDID DIs (Not in Commercial Distribution since 2024-09-09) are excluded.
- Synsiro Pro (P170030/S055, 2025-08-19) = alias/note on the Orsiro Mission row; no separate row.
- Integrity and MULTI-LINK 8: rows kept, marked DISCONTINUED in fda_submission (Integrity: PMA P030009 withdrawn 2026-04-02 + 78 GUDID DIs not in distribution; MULTI-LINK 8: 6 GUDID DIs not in distribution since 2018-07-21 — PMA P020047 not withdrawn). XIENCE Sierra unchanged.
- Diamondback 360 Precision keeps DBEC-150.
- Dragonfly OpStar recall-record values: not used. Diamondback GUDID guidewire OD 0.012 in: not applied (stays logged conflict); GUDID Max OD per catalog also stays logged (IFU 0.053 in kept).
