from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox


class SeasonSelectionComboBox(QComboBox):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setPlaceholderText("Choose a season")

        seasons = CampaignRegistry().get_seasons()

        for season in seasons:
            self.addItem(season.display_name, userData=season)