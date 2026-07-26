import random
from dataclasses import dataclass
from typing import Dict, Optional, List

from core.enums import Proficiency, CheckOutcomes, Tier
from core.models import Skill, TierDcs


@dataclass
class SkillCheck:
    skills: List[Skill]
    dcs: Dict[Skill, TierDcs]
    desc: Optional[str] = None
    req_proficiency: Proficiency = Proficiency.UNTRAINED
    is_secret: bool = False

    def outcome(self, skill: Skill, tier: Tier, total: int = 0, mod: int = 0, nat_20: bool = False, nat_1: bool = False) -> CheckOutcomes:
        if skill not in self.dcs:
            raise KeyError(f"Skill '{skill.name}' is not configured for this skill check.")

        tier_dcs = self.dcs[skill]

        dc = tier_dcs.get_dc(tier)

        if self.is_secret:
            roll = random.randint(1, 20)

            nat_20 = (roll == 20)
            nat_1 = (roll == 1)
            total = roll + mod

        diff = total - dc
        return CheckOutcomes.from_diff(diff, nat_20, nat_1)