from dataclasses import dataclass, field
from typing import List

from core.models import Skill


@dataclass
class Character:
    name: str
    level: int
    challenge_points: int
    skills: List[Skill] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)