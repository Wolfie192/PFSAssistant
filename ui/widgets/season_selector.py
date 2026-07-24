from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox, QApplication


class SeasonSelectionComboBox(QComboBox):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setPlaceholderText("Choose a season")
        self.addItems([s.display_name for s in CampaignRegistry().get_seasons()])


if __name__ == "__main__":
    app = QApplication()
    window = SeasonSelectionComboBox()
    window.show()
    app.exec()