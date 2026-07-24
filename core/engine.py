from typing import Dict, Optional
from core import models


class PFSGameEngine:
    def __init__(self):
        self.roster: Dict[str, models.Character] = {}
        self.current_scenario: Optional[models.Scenario] = None

    def add_character(self, character: models.Character):
        self.roster[character.name] = character

    def set_active_scenario(self, scenario: models.Scenario):
        self.current_scenario = scenario