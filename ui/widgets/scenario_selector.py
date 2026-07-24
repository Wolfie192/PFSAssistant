from core import CampaignRegistry
from PySide6.QtWidgets import QComboBox, QApplication


class ScenarioSelectionComboBox(QComboBox):
    def __init__(self, parent=None, season: int|None = None, include_dev: bool = False):
        super().__init__(parent)
        self.season = season
        self.include_dev = include_dev

        self.season_changed(self.season, self.include_dev)

        if self.season is None:
            self.setEnabled(False)
            self.setPlaceholderText("Choose a scenario")
        else:
            self.setPlaceholderText("Choose a scenario")
            self.addItems([s.display_name for s in CampaignRegistry().get_scenarios_for_season(self.season, self.include_dev)])

    def season_changed(self, season: int|None = None, include_dev: bool = False):
        if self.season != season: self.season = season
        if self.include_dev != include_dev: self.include_dev = include_dev

        self.clear()

        if self.season is None:
            self.setEnabled(False)
            self.setPlaceholderText("Choose a scenario")
        else:
            self.setEnabled(True)
            self.setPlaceholderText("Choose a scenario")
            self.addItems([s.display_name for s in CampaignRegistry().get_scenarios_for_season(self.season, self.include_dev)])


if __name__ == "__main__":
    app = QApplication()
    window = ScenarioSelectionComboBox(season=0, include_dev=True)
    window.show()
    app.exec()