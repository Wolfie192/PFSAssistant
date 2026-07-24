from enum import Enum


class Proficiency(Enum):
    UNTRAINED = ("untrained", "Untrained")
    TRAINED = ("trained", "Trained")
    EXPERT = ("expert", "Expert")
    MASTER = ("master", "Master")
    LEGENDARY = ("legendary", "Legendary")

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
    def display_names(cls) -> list[str]:
        return [prof.display_name for prof in cls]