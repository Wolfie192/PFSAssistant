from typing import Dict, Optional
from core import models


class PFSGameEngine:
    def __init__(self):
        self.roster: Dict[str, models.Character] = {}
        self.season: Optional[models.Season] = None
        self.scenario: Optional[models.Scenario] = None