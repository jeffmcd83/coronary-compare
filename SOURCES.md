# SOURCES
- GUDID / openFDA UDI: https://api.fda.gov/device/udi.json (per-family query URL stored per cell in provenance.json)
- AccessGUDID v3 API (pass 13, for devices not yet mirrored in openFDA UDI, e.g. SELUTION SLR): https://accessgudid.nlm.nih.gov/api/v3/devices/lookup.json?di=<DI> — raw pulls in raw/udi/SELUTION_SLR.json (openFDA-shaped) + raw/gudid_v3/
- FDA PMA DB: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm ; 510(k) DB: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm
- openFDA device recall: https://api.fda.gov/device/recall.json
- Reprocessor 510(k)s (coronary IVUS): K223026 NES Reprocessed Eagle Eye Platinum RX (2023-02-03); K210655 Innovative Health Reprocessed Eagle Eye Platinum RX (2022-05-25); K232584 Vein360 Reprocessed Visions PV.014P RX + Eagle Eye Platinum RX (2023-10-24); K043453 Sterilmed reprocessed IVUS imaging catheter (2005, generic).
