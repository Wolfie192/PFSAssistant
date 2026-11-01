import unittest

from core.engine import PFSGameEngine
from core.enums import Tier
from core.models import Character, Scenario


class PFSGameEngineTierTests(unittest.TestCase):
    def make_engine(self, levels):
        engine = PFSGameEngine()
        engine.scenario = Scenario(id=1, name="Test", tier=(1, 4))
        engine.roster = {
            str(index): Character(name=str(index), level=level, challenge_points=0)
            for index, level in enumerate(levels)
        }
        return engine

    def test_no_scenario_defaults_to_low_tier(self):
        self.assertIs(PFSGameEngine().tier, Tier.LOW)

    def test_party_at_fifteen_challenge_points_is_low_tier(self):
        # Levels 1, 2, 3, and 4 contribute 2, 3, 4, and 6 points.
        engine = self.make_engine([1, 2, 3, 4])

        self.assertIs(engine.tier, Tier.LOW)

    def test_party_of_four_at_sixteen_points_is_high_tier(self):
        # Two level-4 and two level-1 characters contribute 16 points.
        engine = self.make_engine([4, 4, 1, 1])

        self.assertIs(engine.tier, Tier.HIGH)

    def test_party_larger_than_four_needs_nineteen_points_for_high_tier(self):
        at_sixteen = self.make_engine([4, 3, 1, 1, 1])
        at_nineteen = self.make_engine([4, 4, 2, 1, 1])

        self.assertIs(at_sixteen.tier, Tier.LOW)
        self.assertIs(at_nineteen.tier, Tier.HIGH)


if __name__ == "__main__":
    unittest.main()
