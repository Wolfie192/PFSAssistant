from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox


class SeasonSelectionComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode
        self.engine = parent.engine

        self.setPlaceholderText("Choose a season")

        seasons = CampaignRegistry().get_seasons()

        for season in seasons:
            self.addItem(season.display_name, userData=season)