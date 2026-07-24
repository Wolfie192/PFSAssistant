from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from ui.widgets.scenario_selector import ScenarioSelectionComboBox
from ui.widgets.season_selector import SeasonSelectionComboBox


class SeasonScenarioCombinedSelector(QWidget):
    def __init__(self, parent=None, include_dev: bool = False):
        super().__init__(parent)
        self.include_dev = include_dev

        self.season_selector = SeasonSelectionComboBox()
        self.scenario_selector = ScenarioSelectionComboBox(include_dev=include_dev)

        self.season_selector.currentIndexChanged.connect(self.season_updated)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.season_selector)
        self.layout.addWidget(self.scenario_selector)

        self.setLayout(self.layout)

    def season_updated(self, index: int):
        season_arg = None if index < 0 else index

        self.scenario_selector.season_changed(season=season_arg, include_dev=self.include_dev)


if __name__ == "__main__":
    app = QApplication()
    window = SeasonScenarioCombinedSelector(include_dev=True)
    window.show()
    app.exec()