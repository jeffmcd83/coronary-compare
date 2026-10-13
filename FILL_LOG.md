# FILL_LOG
## Pass 01 (2026-10-12)
- Seeded 65 device families across 12 approved categories (no embolic protection).
- Sizes, catalog numbers, FDA submission numbers, product codes: GUDID via openFDA UDI API (raw/udi/*.json). Values are only from records whose brand matches the exact family (regex in fam.py); no sibling copying.
- Name/classification-derived: balloon_type, compliance (NC prefix), atherectomy mechanism, imaging modality.
- Recalls: openFDA device recall API, matched only when an exact catalog/model number from that family's GUDID records appears in code_info/product_description → 92 recall rows.
- IFU-only specs (drug/dose, polymer, strut, crossing profile, RBP, tip load, ID/OD, frequency, pullback…) intentionally BLANK — not yet extracted from OEM IFUs. Next pass.
- Excluded wrong-brand GUDID hits: Cougar (Medos neuro), Wolverine (Kenmark), Mamba (Richard Wolf), GRAFTMASTER (Smith & Nephew ortho → left blank).
## Conflicts
- None overwritten. Families with mixed generations in GUDID (e.g., Launcher spans many 510(k)s; Integrity GUDID entries show P030009) recorded as-is.
