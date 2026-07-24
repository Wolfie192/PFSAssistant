from PySide6.QtWidgets import QMainWindow
from ui.views import ScenarioSelectionView


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("PFS Assistant")
        self.setCentralWidget(ScenarioSelectionView(self.controller))

        self.show()