# garden_advice.py
# Simple gardening advice tool keyed by month. Meant as a starter script.

# TODO: 1) Refactor the script into reusable functions (e.g., get_advice_for_month, get_advice_for_season).
# TODO: 2) Add proper documentation (module docstring, type hints) and logging.
# TODO: 3) Replace hardcoded advice with a separate JSON/YAML data file or a small database.
# TODO: 4) Add unit tests for important functions.

import datetime

# Hardcoded advice by month (1-based month index)
ADVICE_BY_MONTH = {
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


def get_current_month() -> int:
    """Return the current month as an integer (1-12)."""
    return datetime.date.today().month


def advice_for_month(month: int) -> str:
    """Return gardening advice for the provided month.

    If the month is out of range, returns a helpful error message.
    """
    return ADVICE_BY_MONTH.get(month, "No advice available for this month.")


if __name__ == "__main__":
    month = get_current_month()
    print(f"Month: {month} - Advice: {advice_for_month(month)}")
