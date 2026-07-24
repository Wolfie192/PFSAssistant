from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox


class ScenarioSelectionComboBox(QComboBox):
    def __init__(self, controller, season: int|None = None):
        super().__init__()
        self.controller = controller
        self.season = season

        self.season_changed(self.season)

    def season_changed(self, season: int|None = None):
        self.season = season
        include_dev = self.controller.dev_mode

        self.clear()

        if self.season is None:
            self.setEnabled(False)
            self.setPlaceholderText("Choose a scenario")
        else:
            self.setEnabled(True)
            self.setPlaceholderText("Choose a scenario")

            scenarios = CampaignRegistry().get_scenarios_for_season(self.season, include_dev)
            self.addItems([s.display_name for s in scenarios])