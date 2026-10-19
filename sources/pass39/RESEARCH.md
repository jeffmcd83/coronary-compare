# Pass 39: weekly recall and new-model refresh (2026-10-19, first weekly run)

## openFDA data cut dates (meta.last_updated, queried 2026-10-19 ~08:25 ET)
- device/recall: **2026-10-15** (59,494 records)
- device/510k: **2026-10-05**; device/pma: **2026-10-05** (unchanged since passes 31–38)
- device/udi: **2026-10-01** (unchanged). AccessGUDID daily delta files from 2026-09-28 to 2026-10-16 were also parsed (see below).
- FDA cfPMN web search, for decisions after the openFDA cut: it returned the "request is being processed" bot-challenge page (HTTP 400). It was not bypassed.

## 1. Recalls
Script: `sources/pass39/recall_refresh.py` (run once live; `match` mode re-matches offline from `raw/recall_pool.json.gz`). Diff: `sources/pass39/diff.py`.
- Query pool (2,016 unique recall products):
  - (a) every recall in each of the guide's 25 product codes (from the rows' GUDID product codes: DQK DQO DQX DQY DRG DSK DXO DYG ITX KRA LOX LPC MAF MCX NIQ NIV NWX OBI OBJ OOB OWQ QEW QEX QEZ QMG; skip-paged, limit 1000);
  - (b) `product_description:"<row base name>"` for every row;
  - (c) `pma_numbers:` / `k_numbers:` for every submission number in each row. The numbers are extracted with a regex, which fixes recalls.py's broken split for annotated fda_submission values such as Orsiro Mission, MULTI-LINK 8 and Integrity.
- Row IDs, written to `raw/row_ids.json`:
  - the row's own catalog_numbers;
  - plus every GUDID tuple (catalog, version/model, DIs) in raw/catalogs.json whose catalog or model is in the row;
  - for the renamed rows, catalogs.json is read under the pre-rename keys ("Diamondback 360 Coronary OAS", "AngioSculpt RX PTCA");
  - Launcher and Vista Brite Tip use the full GUDID set, because build_master truncates catalog_numbers at 4,000 characters;
  - BioFreedom, INDIGO CAT RX and Ringer DIs come from raw/udi.
- Match rule: as in recalls.py, an exact ID of 5 or more characters with a word-boundary match in code_info or product_description. No sibling or family matching.
- Result: 110 matches against 92 in the pre-run CSV. All 92 existing rows were re-found, with no status or field changes. The 18 extra are listed below.

### Added to coronary-recalls.csv (17). All are historical; none is a newly initiated recall.
| Row | Recall | Event | Firm | Initiated | Status / class | Matched | Reason |
|---|---|---|---|---|---|---|---|
| Launcher | Z-0930-06, Z-0931-06, Z-0932-06, Z-0936-06, Z-0982-06, Z-0983-06, Z-0984-06, Z-0985-06, Z-0987-06, Z-0989-06, Z-0991-06, Z-0993-06, Z-0995-06 | 35236 | Medtronic, Inc. | 2006-04-05 | Terminated / II | LA5IMAA, LA5JL40A, LA5JR40A, LA5SR50A, LA83DRCSH, LA8EBU40SHA, LA8EBU45SHA, LA8EBU50SHA, LA8SR30SH, LA8SR35SH, LA8SR40SH, LA8SR50SH, LA8SR60SH | Potential for non-sterility due to loss of package integrity. These are more products from the same event as the 52 Launcher 2006 rows already listed; the earlier limit=100 query cut them off. |
| Vista Brite Tip | Z-0588-05 | 29574 | Cordis Corporation | 2004-05-05 | Terminated / II | 4038553S | Labeled as Straight Catheter, but the package contains Contralateral Guide catheters. The catalog is a VISTA BRITE TIP IG introducer guide (flag in conflicts.json). |
| HI-TORQUE PILOT | Z-0259-2020 | 83001 | **AnewMed Corporation** (third party) | 2019-05-23 | **Open, Classified** / II | 1010483-HJ | The contract sterilizer did not have adequate packaging data to support the 2-year shelf life (flag). |
| Diamondback 360 Precision | Z-1095-2014 | 67445 | Cardiovascular Systems, Inc. | 2014-01-27 | Terminated / III | 70058-02; DBEC-125 | The OAD contained a peripheral saline line that was not part of the approved coronary system. |
| ELCA Coronary Laser Atherectomy | Z-0662-2017 | 75617 | Spectranetics Corporation | 2016-10-31 | Terminated / III | 110-004; 114-009; 117-016; 120-009 | Possibly compromised integrity of the outer sterile packaging. |

openFDA links: `https://api.fda.gov/device/recall.json?search=product_res_number:"<recall>"`

### Found but NOT added (pending Jeff; details in conflicts.json)
- **Diamondback Z-2122-2017** (CSI SIP-3000 pump, Part 7-10014, 2017-04-14, Terminated, class III): matches only on model number SIP-3000, the same basis as Z-3021-2018.
- **Twin-Pass Z-0053-2017** (Model 5200) and **Z-0055-2017** (Model 5230), both 2016-09-16, Terminated, class II, excess material at the tip; **Z-1712-2009** (REF 5200, 2009-07-02, Terminated, class II, PTFE beading). The catalogs are exact in-row 4-digit numbers, and recalls.py's 5-character minimum excludes them.
- **GuideLiner V3 Z-0259-2020** (catalog 5573 in the AnewMed list): ambiguous, because V2 and V3 share 557x catalog numbers.

### Kept, still pending Jeff
- **Diamondback Z-1290-2015** (DBEC-125) and **Z-3021-2018** (SIP-3000) are KEPT. The pass-38 drop was a recalls.py key mismatch: the renamed row name is not in catalogs.json. These two match only on the GUDID model number of in-row catalogs, not on a catalog number or GTIN.

### Recently initiated recalls in the coronary product codes (07-01 → 10-15 cut)
There are 8, and none involves a guide row:
- MicroVention BOBBY balloon guide (neuro)
- Galt/BSC Enhance transcarotid kit
- Midmark ECG
- GE Carescape
- Karl Storz / Olympus endoscope "Telescope" (name hits only)
- BSC Imager II angiographic catheters (Z-3214-2026, DQO; not a guide row)

The FDA Recalls & Early Alerts page (checked 2026-10-19) shows no coronary item for any guide row. The Edwards SAPIEN M3 / Commander M alert is structural heart, which is out of scope.

## 2. New models / submissions (decisions 2026-08-01 → openFDA cut 2026-10-05)
Script: `sources/pass39/newmodels.py`; raw output: `raw/newmodels_openfda.json`, `raw/pma_history_for_recent.json`.
- **PMA supplements for the guide's 20 PMAs/HDEs: 12 decisions, no new trade name or model.**
  - P110019 S144/S145 are label-printing and packaging changes. Their trade-name lists include XIENCE PRO5/PROS, which have been in P110019 supplements since S085 (2017).
  - P150003 S113: parametric release.
  - P160043 S095: automation.
  - P170030 S065 (PAS protocol) and S066 (coating process).
  - P200039 S025: coating raw material.
  - P230035 S010: coating equipment.
  - P910001 S126 (ELCA inspection) and S127 (laser cable supplier).
  - P250041 (SELUTION SLR original, 2026-09-18): already a row.
  - Outside the guide: Medinol EluNIR P170008/S064 (shelf-life; this US DES has been approved since 2017 and is not in the guide; not new).
- **New original PMAs in NIQ/MAF/NIV/DYG/OOB/NWX/LOX/MCX/LPC/QMG/PNY: none.**
- **510(k) in the guide's codes plus reprocessor applicants** (Innovative Health, Stryker Sustainability, NES, Vein360, SterilMed, Medline ReNewal, device_name "reprocessed"): 21 decisions. Coronary-relevant ones:
  - **K261428**: Medtronic Ireland, *NC Euphora Rapid Exchange Balloon Dilatation Catheter*, LOX, SE 2026-08-14 (Traditional). Predicate NC Euphora K141090; PTFE-based non-hydrophilic material change on the proximal shaft. This is an existing row (same model), not a new model. Adding the K number needs Jeff's OK (conflicts.json). https://www.accessdata.fda.gov/cdrh_docs/pdf26/K261428.pdf
  - **K260559**: IMDS Operation B.V., *NHanceIT* 0.014" OTW guide wire support catheter (coronary and/or peripheral), DQY, SE 2026-08-14 (Traditional); predicate Turnpike LP K191560. **New-model candidate** (microcatheter). https://www.accessdata.fda.gov/cdrh_docs/pdf26/K260559.pdf
  - **K262817**: Vantis Vascular, *CrossFAST Integrated Microcatheter Advanced Delivery System* (coronary and/or peripheral; used with guide catheters to place interventional devices), DQY, SE 2026-09-18 (Special; earlier K242276 CrossFAST CFM55 guide-extension system, 2024-09-30). **New-model candidate** (guide extension / microcatheter). https://www.accessdata.fda.gov/cdrh_docs/pdf26/K262817.pdf
  - Out of scope:
    - peripheral/neuro: K253146 Hyperdrive 35, K261281 CROSSLEAD 035, K262392 APRO 35, K260223 Aristotle Mini (neuro/peripheral; "not intended for use in the coronary vasculature"), K254035 Mayumi (peripheral), Inari/Helo/Vertex QEW;
    - consoles and EP: K253692 BSC AVVIGO+ guidance system (console, not a catheter/wire row), Affera/EnSite/IOPS;
    - other: ultrasound probes, ICE (K261696), infusion catheters.
  - Reprocessed coronary devices: none.

## 3. GUDID
- openFDA UDI is still cut at 2026-10-01, the same data that raw/udi/*.json was pulled from on 2026-10-17, so the fetch_udi.py path finds nothing new.
- AccessGUDID daily deltas 2026-09-28 → 2026-10-16 (3 weekly zips, 14 daily XMLs; `gudid_delta.py` → `raw/gudid_delta_hits.json`, 329 records in coronary codes or matching guide brands):
  - **Existing rows: no new DI.** SELUTION SLR: 32 "New v1" records, all already in the row (from AccessGUDID v3, pass 13). Euphora EUP1506X and Ringer 5882/5884/5886/5888/5890 are record updates, still In Commercial Distribution, catalogs unchanged.
  - Brand-regex false hits (not applied): a "Triology V3" filter (GuideLiner "V3" regex) and a GE "Coro" ECG cable (Diamondback "Coro" regex). build_master applies each regex only to that row's own raw file, so the build is not affected.
  - Other coronary-indicated DIs first published in this window, none of them a new clearance:
    - Merit SureCross support catheter, SC14135/SC1465/SC1490/SC1865: an existing device (K200317, 2020; coronary and peripheral per Merit IFU 402921002), not in the guide.
    - Opsens OptoMonitor consoles (K142598).
    - Zurich Pressure Guidewire System update (K190852; coronary FFR wire, not in the guide).
    - AngioJet AutoElite console.
