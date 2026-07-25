from PySide6.QtWidgets import QWidget


class RunScenarioView(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode
        self.engine = parent.engine