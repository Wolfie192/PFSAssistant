from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from ui.widgets.scenario_selector import ScenarioSelectionComboBox
from ui.widgets.season_selector import SeasonSelectionComboBox


class SeasonScenarioCombinedSelector(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.season_selector = SeasonSelectionComboBox(self.controller)
        self.scenario_selector = ScenarioSelectionComboBox(self.controller)

        self.season_selector.currentIndexChanged.connect(self.season_updated)

        self.select_scenario_button = QPushButton("Start Scenario")

        self.select_scenario_button.clicked.connect(self.start_season_button_clicked)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.season_selector)
        self.layout.addWidget(self.scenario_selector)
        self.layout.addWidget(self.select_scenario_button)
        self.layout.setSpacing(10)

        self.setLayout(self.layout)

    def season_updated(self, index: int):
        season_arg = None if index < 0 else index

        self.scenario_selector.season_changed(season=season_arg)


    def start_season_button_clicked(self):
        print("Start Scenario Button Clicked:")
        print(self.season_selector.currentText())
        print(self.scenario_selector.currentText())