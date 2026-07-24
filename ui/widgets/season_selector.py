from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox, QApplication


class SeasonSelectionComboBox(QComboBox):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setPlaceholderText("Choose a season")

        seasons = CampaignRegistry().get_seasons()

        for season in seasons:
            self.addItem(season.display_name, userData=season)


if __name__ == "__main__":
    app = QApplication()
    window = SeasonSelectionComboBox()
    window.show()
    app.exec()