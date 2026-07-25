from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox


class ScenarioSelectionComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode
        self.season = None

        self.season_changed(self.season)

    def season_changed(self, season: int|None = None):
        self.season = season

        self.clear()

        if self.season is None:
            self.setEnabled(False)
            self.setPlaceholderText("Choose a scenario")
        else:
            self.setEnabled(True)
            self.setPlaceholderText("Choose a scenario")

            scenarios = CampaignRegistry().get_scenarios_for_season(self.season, self.dev_mode)
            self.addItems([s.display_name for s in scenarios])