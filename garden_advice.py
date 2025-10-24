# Hyperion Dev - Git Workflows garden_advice project.
"""garden_advice.py

Small helper to provide gardening advice by month or season.

This module is intentionally small and focused. Improvements include:
- loading advice from an external JSON data file
- exposing functions that are easy to unit test
- providing a minimal CLI for ad-hoc use

Usage:
    python garden_advice.py            # show advice for current month
    python garden_advice.py 4          # show advice for month 4 (April)
    python garden_advice.py --season spring

"""

from __future__ import annotations

import datetime
import json
import logging
from pathlib import Path
from typing import Dict, Optional

LOG = logging.getLogger(__name__)


# Default hardcoded advice (fallback)
DEFAULT_ADVICE: Dict[int, str] = {
    1: "Protect tender plants from frost; plan spring sowing.",
    2: "Start seeds indoors for spring; prune fruit trees in mild areas.",
    3: "Prepare beds and sow early vegetables; clean up winter debris.",
    4: "Plant potatoes and hardy annuals; mulch beds.",
    5: "Plant out tender annuals; watch for late frosts.",
    6: "Water regularly; deadhead flowers to encourage blooms.",
    7: "Harvest summer crops; shade young plants from extreme heat.",
    8: "Continue harvesting; sow autumn crops and cover soil.",
    9: "Plant spring bulbs; divide perennials and clear dying foliage.",
    10: "Reduce feeding; plant trees and shrubs; tidy beds for winter.",
    11: "Protect containers and tender plants; clear fallen leaves.",
    12: "Plan for next year; check tools and store seeds.",
}


def load_advice_from_json(path: Optional[Path] = None) -> Dict[int, str]:
    """Load month->advice mapping from a JSON file.

    If the file can't be read, returns the DEFAULT_ADVICE mapping.
    """
    if path is None:
        path = Path(__file__).with_name("advice_data.json")

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # Ensure keys are ints
        return {int(k): str(v) for k, v in data.items()}
    except Exception as exc:  # fallback to defaults
        LOG.debug("Could not load advice JSON (%s): %s", path, exc)
        return DEFAULT_ADVICE


def get_current_month() -> int:
    """Return the current month as an integer (1-12)."""
    return datetime.date.today().month


def get_advice_for_month(month: int, advice_map: Optional[Dict[int, str]] = None) -> str:
    """Return gardening advice for a specific month.

    Args:
        month: 1-12 month number.
        advice_map: optional mapping to use; if None the JSON/default mapping is used.
    """
    if advice_map is None:
        advice_map = load_advice_from_json()
    return advice_map.get(month, "No advice available for this month.")


def get_advice_for_season(season: str, advice_map: Optional[Dict[int, str]] = None) -> str:
    """Return a short seasonal summary aggregated from monthly advice.

    season must be one of: 'spring', 'summer', 'autumn', 'winter'.
    """
    if advice_map is None:
        advice_map = load_advice_from_json()

    season = season.lower()
    if season == "spring":
        months = (3, 4, 5)
    elif season == "summer":
        months = (6, 7, 8)
    elif season in ("autumn", "fall"):
        months = (9, 10, 11)
    elif season == "winter":
        months = (12, 1, 2)
    else:
        return "Unknown season. Use spring/summer/autumn/winter."

    parts = [advice_map.get(m, "") for m in months]
    return " \n---\n ".join([p for p in parts if p])


def _cli_main(argv: Optional[list[str]] = None) -> int:
    """Minimal CLI entrypoint; returns exit code."""
    import argparse

    parser = argparse.ArgumentParser(description="Simple gardening advice by month or season")
    parser.add_argument("month", nargs="?", type=int, help="month number (1-12)")
    parser.add_argument("--season", choices=["spring", "summer", "autumn", "fall", "winter"], help="show advice for a season")
    args = parser.parse_args(argv)

    if args.season:
        print(get_advice_for_season(args.season))
        return 0

    if args.month:
        print(get_advice_for_month(args.month))
        return 0

    # default: show current month
    month = get_current_month()
    print(f"Month: {month} - Advice: {get_advice_for_month(month)}")
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(_cli_main())
