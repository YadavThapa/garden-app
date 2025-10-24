import unittest
from garden_advice import get_advice_for_month, get_advice_for_season, DEFAULT_ADVICE


class TestGardenAdvice(unittest.TestCase):
    def test_get_advice_for_month_known(self):
        # test with a known month
        self.assertIn("frost", get_advice_for_month(1).lower())

    def test_get_advice_for_month_unknown(self):
        self.assertEqual(get_advice_for_month(99), "No advice available for this month.")

    def test_get_advice_for_season_spring(self):
        advice = get_advice_for_season("spring", advice_map=DEFAULT_ADVICE)
        # aggregated seasonal advice should include one of the months' advice
        self.assertTrue(len(advice) > 0)


if __name__ == "__main__":
    unittest.main()
