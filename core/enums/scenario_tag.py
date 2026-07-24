from enum import Enum


class ScenarioTag(Enum):
    EXCLUSIVE = ("exclusive", "Exclusive")
    GLYPH = ("glyph", "Glyph")
    METAPLOT = ("metaplot", "Metaplot")
    ENVOYS_ALLIANCE = ("envoys_alliance", "Envoy's Alliance")
    GRAND_ARCHIVE = ("grand_archive", "Grand Archive")
    HORIZON_HUNTERS = ("horizon_hunters", "Horizon Hunters")
    RADIANT_OATH = ("radiant_oath", "Radiant Oath")
    VERDANT_WHEEL = ("verdant_wheel", "Verdant Wheel")
    VIGILANT_SEAL = ("vigilant_seal", "Vigilant Seal")
    ALL_AGES = ("all_ages", "All Ages")

    def __init__(self, key: str, display_name: str):
        self._key = key
        self._display_name = display_name

    @property
    def key(self) -> str:
        return self._key

    @property
    def display_name(self) -> str:
        return self._display_name