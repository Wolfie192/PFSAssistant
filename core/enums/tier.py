from enum import Enum


class Tier(Enum):
    LOW = ("low", "Low")
    HIGH = ("high", "High")

    def __init__(self, key: str, display_name: str):
        self._key = key
        self._display_name = display_name

    @property
    def key(self) -> str:
        return self._key

    @property
    def display_name(self) -> str:
        return self._display_name