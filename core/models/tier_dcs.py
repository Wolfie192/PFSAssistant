from dataclasses import dataclass, field
from typing import Dict, Union

from core.enums import Tier


@dataclass
class TierDcs:
    dcs: Dict[Tier, int] = field(default_factory=dict)

    def get_dc(self, tier: Union[Tier, str]) -> int:
        """
        Retrieves the DC for a given Tier enum or string key.
        """
        if isinstance(tier, str):
            tier = Tier(tier)

        dc = self.dcs.get(tier)

        if dc is None:
            raise KeyError(f"DC not defined for tier: {tier.display_name}")
        return dc