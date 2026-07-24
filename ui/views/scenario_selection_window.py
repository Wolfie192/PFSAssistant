from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.widgets import SeasonScenarioCombinedSelector, TitleBlock


class ScenarioSelectionView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.layout = QVBoxLayout()

        self.title_widget = TitleBlock()
        self.scenario_selector_combo = SeasonScenarioCombinedSelector(self.controller)

        self.layout.addWidget(self.title_widget)
        self.layout.addSpacing(60)
        self.layout.addWidget(self.scenario_selector_combo)
        self.layout.addStretch()

        self.setLayout(self.layout)