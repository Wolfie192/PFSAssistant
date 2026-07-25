from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ui.widgets import TitleBlock, SeasonSelectionComboBox, ScenarioSelectionComboBox


class MainMenuView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode

        self.layout = QVBoxLayout(self)

        self.title_block = TitleBlock(self)

        self.season_selection = SeasonSelectionComboBox(self)
        self.season_selection.currentIndexChanged.connect(self.season_updated)

        self.scenario_selection = ScenarioSelectionComboBox(self)
        self.scenario_selection.currentIndexChanged.connect(self.scenario_updated)

        self.select_scenario_button = QPushButton("Start Scenario")
        self.select_scenario_button.setEnabled(False)

        self.select_scenario_button.clicked.connect(self.start_season_button_clicked)

        self.layout.addWidget(self.title_block)
        self.layout.addSpacing(60)
        self.layout.addWidget(self.season_selection)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.scenario_selection)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.select_scenario_button)
        self.layout.addStretch()

    def season_updated(self, index: int):
        season_arg = None if index < 0 else index

        self.scenario_selection.season_changed(season=season_arg)


    def scenario_updated(self, index: int):
        if index < 0:
            self.select_scenario_button.setEnabled(False)
        else:
            self.select_scenario_button.setEnabled(True)


    def start_season_button_clicked(self):
        print("Start Scenario Button Clicked")
        print(self.season_selection.currentText())
        print(self.scenario_selection.currentText())