Title: Refactor into functions and add tests

Branch: issue-1-refactor-functions

Description:
- Extracted reusable functions: `get_advice_for_month`, `get_advice_for_season`, and `load_advice_from_json`.
- Added a minimal CLI and basic unit tests in `tests/test_garden_advice.py`.

Status: MERGED (merged locally into `main` and pushed to remote)

Notes:
- Unit tests use the built-in DEFAULT_ADVICE mapping. Run `python -m unittest` to execute tests.
