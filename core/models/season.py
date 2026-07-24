from dataclasses import dataclass, field
from typing import List
from core import models


@dataclass
class Season:
    id: int
    name: str
    scenarios: List[models.Scenario] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        if self.name == "Quests":
            return "Quests"
        else:
            return f"Season {self.id:02d}: {self.name}"