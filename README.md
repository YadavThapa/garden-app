# garden-app

A small, opinionated gardening advice tool that gives tips by month or season.

This repository contains a minimal Python script (`garden_advice.py`) that exposes testable functions and a tiny CLI. Advice is loaded from `advice_data.json` (if present) and falls back to built-in defaults.

Quick start

- Run the CLI for the current month:

```pwsh
cd 'c:\Users\hemja\OneDrive\Desktop\garden-app\remote'
python garden_advice.py
```

- Get advice for April (month 4):

```pwsh
python garden_advice.py 4
```

- Get advice for a season:

```pwsh
python garden_advice.py --season spring
```

Run tests

```pwsh
cd 'c:\Users\hemja\OneDrive\Desktop\garden-app\remote'
python -m unittest discover -v
```

Notes

- If you want to update or localize advice, edit `advice_data.json` or replace it with a localized file.
- The repository includes local issue files under `.github/issues/` and PR notes under `PULL_REQUESTS/` to document the workflow used during development.

Contributing

Contributions are welcome — open an issue or send a pull request with tests.
