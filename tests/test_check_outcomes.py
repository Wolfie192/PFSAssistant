import unittest

from core.enums import CheckOutcomes


class CheckOutcomesTests(unittest.TestCase):
    def test_degree_boundaries(self):
        cases = (
            (10, CheckOutcomes.CRIT_SUCCESS),
            (0, CheckOutcomes.SUCCESS),
            (-9, CheckOutcomes.FAILURE),
            (-10, CheckOutcomes.CRIT_FAILURE),
        )

        for difference, expected in cases:
            with self.subTest(difference=difference):
                self.assertIs(CheckOutcomes.from_diff(difference), expected)

    def test_natural_twenty_improves_degree_by_one(self):
        self.assertIs(
            CheckOutcomes.from_diff(0, nat_20=True),
            CheckOutcomes.CRIT_SUCCESS,
        )

    def test_natural_one_worsens_degree_by_one(self):
        self.assertIs(
            CheckOutcomes.from_diff(0, nat_1=True),
            CheckOutcomes.FAILURE,
        )

    def test_natural_adjustments_stop_at_degree_limits(self):
        self.assertIs(
            CheckOutcomes.from_diff(20, nat_20=True),
            CheckOutcomes.CRIT_SUCCESS,
        )
        self.assertIs(
            CheckOutcomes.from_diff(-20, nat_1=True),
            CheckOutcomes.CRIT_FAILURE,
        )


if __name__ == "__main__":
    unittest.main()
