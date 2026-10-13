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
