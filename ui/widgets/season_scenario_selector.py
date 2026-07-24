from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from ui.widgets.scenario_selector import ScenarioSelectionComboBox
from ui.widgets.season_selector import SeasonSelectionComboBox


class SeasonScenarioCombinedSelector(QWidget):
    def __init__(self, parent=None, include_dev: bool = False):
        super().__init__(parent)
        self.include_dev = include_dev

        self.season_selector = SeasonSelectionComboBox()
        self.scenario_selector = ScenarioSelectionComboBox(include_dev=include_dev)

        self.season_selector.currentTextChanged.connect(self.season_updated)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.season_selector)
        self.layout.addWidget(self.scenario_selector)

        self.setLayout(self.layout)

    def season_updated(self, index: int):
        self.scenario_selector.season = index
        self.scenario_selector.season_changed(season=self.season_selector.currentIndex(), include_dev=self.include_dev)


if __name__ == "__main__":
    app = QApplication()
    window = SeasonScenarioCombinedSelector(include_dev=True)
    window.show()
    app.exec()