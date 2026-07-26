from typing import Dict, Optional
from core import models
from core import enums
import random


class PFSGameEngine:
    def __init__(self):
        self.roster: Dict[str, models.Character] = {}
        self.season: Optional[models.Season] = None
        self.scenario: Optional[models.Scenario] = None

    def _check_outcome(self, diff: int, nat_20: bool = False, nat_1: bool = False) -> enums.CheckOutcomes:
        """
        Determines the degree of success based on the difference between the DC and total result.
        Adjusts outcomes one degree of success higher for natural 20 and one lower for natural 1.
        """
        if diff >= 10:
            outcome = enums.CheckOutcomes.CRIT_SUCCESS
        elif diff >= 0:
            outcome = enums.CheckOutcomes.SUCCESS
        elif diff > -10:
            outcome = enums.CheckOutcomes.FAILURE
        else:
            outcome = enums.CheckOutcomes.CRIT_FAILURE

        if nat_20: outcome += 1
        elif nat_1: outcome -= 1

        return outcome


    def skill_check(self, dc: int, total: int, nat_20: bool = False, nat_1: bool = False) -> enums.CheckOutcomes:
        """
        Evaluates a skill check where the total is already calculated such as being rolled and calculated by the player.
        """
        diff = total - dc

        return self._check_outcome(diff, nat_20=nat_20, nat_1=nat_1)


    def secret_skill_check(self, dc: int, mod: int) -> enums.CheckOutcomes:
        """
        Evaluates a skill check where the modifier is provided and total a roll is secretly made.
        """
        roll = random.randint(1, 20)
        nat_20 = (roll == 20)
        nat_1 = (roll == 1)

        diff = (roll + mod) - dc

        return self._check_outcome(diff, nat_20=nat_20, nat_1=nat_1)