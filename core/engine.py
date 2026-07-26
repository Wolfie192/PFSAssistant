from typing import Dict, Optional

from core.models import Character, Season, Scenario
from core.enums import Tier


class PFSGameEngine:
    def __init__(self):
        self.roster: Dict[str, Character] = {}
        self.season: Optional[Season] = None
        self.scenario: Optional[Scenario] = None

    @property
    def tier(self) -> Tier:
        if self.scenario is None:
            return Tier.LOW

        challenge_points = 0
        tier_min = self.scenario.tier[0]

        for char in self.roster.values():
            if char.level == tier_min:
                challenge_points += 2
            elif char.level == tier_min + 1:
                challenge_points += 3
            elif char.level == tier_min + 2:
                challenge_points += 4
            elif char.level == tier_min + 3:
                challenge_points += 6

        if challenge_points <= 15: return Tier.LOW
        elif challenge_points >= 19: return Tier.HIGH
        elif challenge_points >= 16 and len(self.roster.keys()) <= 4: return Tier.HIGH
        else: return Tier.LOW