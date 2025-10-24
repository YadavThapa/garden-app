# Issue 2 — Enhancement: Replace hardcoded advice with external data

Description

Move the hardcoded `ADVICE_BY_MONTH` dictionary into a JSON data file (`advice_data.json`) and update `garden_advice.py` to load advice at runtime. This will make it easier to update tips and support localization in future.

Acceptance criteria

- `advice_data.json` is added with the month-to-advice mapping.
- `garden_advice.py` loads data from JSON and falls back to built-in advice if the file is missing.
- Add a small script or command-line flag to export the JSON template.

Notes

- This complements Issue #1 by making functions read from data rather than hardcoded values.

Status: CLOSED (merged into `main`)

Merged PR: `issue-2-externalize-data` -> `main`