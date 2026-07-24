from enum import Enum
from typing import List


class Skill(Enum):
    ACROBATICS = ("acrobatics", "Acrobatics")
    ARCANA = ("arcana", "Arcana")
    ATHLETICS = ("athletics", "Athletics")
    CRAFTING = ("crafting", "Crafting")
    DECEPTION = ("deception", "Deception")
    DIPLOMACY = ("diplomacy", "Diplomacy")
    INTIMIDATION = ("intimidation", "Intimidation")
    MEDICINE = ("medicine", "Medicine")
    NATURE = ("nature", "Nature")
    OCCULTISM = ("occultism", "Occultism")
    PERFORMANCE = ("performance", "Performance")
    RELIGION = ("religion", "Religion")
    SOCIETY = ("society", "Society")
    STEALTH = ("stealth", "Stealth")
    SURVIVAL = ("survival", "Survival")
    THIEVERY = ("thievery", "Thievery")

    def __init__(self, key: str, display_name: str):
        self._key = key
        self._display_name = display_name

    @property
    def key(self) -> str:
        return self._key

    @property
    def display_name(self) -> str:
        return self._display_name

    @classmethod
    def from_string(cls, value: str):
        normalized = value.strip().lower()
        for skill in cls:
            if skill.key == normalized or skill.display_name.lower() == normalized:
                return skill
        raise ValueError(f"Unknown Skill: {value}")

    @classmethod
    def display_names(cls) -> List[str]:
        return [skill.display_name for skill in cls]