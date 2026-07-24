from dataclasses import dataclass, field
from typing import Dict, List
from core import models


@dataclass
class Character:
    name: str
    level: int
    challenge_points: int
    skills: Dict[str, int] = field(default_factory=dict)
    lore_skills: List[models.LoreSkill] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)