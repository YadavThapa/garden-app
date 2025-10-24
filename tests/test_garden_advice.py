"""Unit tests for the :mod:`garden_advice` module."""

from pathlib import Path
import sys
import importlib
import unittest

# Ensure repository root is importable for tests. This makes local imports work
# in editors and CI without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Dynamically import the module from the repository root so linters and
# type-checkers are not blocked by local test layout.
_ga = importlib.import_module("garden_advice")
get_advice_for_month = _ga.get_advice_for_month
get_advice_for_season = _ga.get_advice_for_season
DEFAULT_ADVICE = _ga.DEFAULT_ADVICE


class TestGardenAdvice(unittest.TestCase):
    """Tests for the core functions in :mod:`garden_advice`."""

    def test_get_advice_for_month_known(self):
        """Return advice for a known month (January)."""
        advice = get_advice_for_month(1)
        self.assertIn("frost", advice.lower())

    def test_get_advice_for_month_unknown(self):
        """Unknown month numbers return a fallback message."""
        self.assertEqual(
            get_advice_for_month(99), "No advice available for this month."
        )

    def test_get_advice_for_season_spring(self):
        """Seasonal advice returns a non-empty aggregation for spring."""
        advice = get_advice_for_season("spring", advice_map=DEFAULT_ADVICE)
        self.assertTrue(len(advice) > 0)


if __name__ == "__main__":
    unittest.main()
