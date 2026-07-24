from dataclasses import dataclass, field
from core import enums
from typing import List, Tuple


@dataclass
class Scenario:
    id: int
    name: str
    tier: Tuple[int, int]
    tags: List[enums.ScenarioTag] = field(default_factory=list)
    data = None

    @property
    def display_name(self) -> str:
        if self.tier[0] == self.tier[1]:
            return f"{self.id:02d}: {self.name} ({self.tier[0]})"
        else:
            return f"{self.id:02d}: {self.name} ({self.tier[0]}-{self.tier[1]})"