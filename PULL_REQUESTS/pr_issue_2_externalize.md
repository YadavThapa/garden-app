Title: Externalize advice data to advice_data.json

Branch: issue-2-externalize-data

Description:
- Added `advice_data.json` which contains the month-to-advice mapping.
- `garden_advice.py` will automatically load this JSON file; if missing, it falls back to internal defaults.

Status: MERGED (merged locally into `main` and pushed to remote)

Notes:
- This makes it easier to update or localize advice without changing code.
