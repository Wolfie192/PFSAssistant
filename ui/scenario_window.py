from PySide6.QtWidgets import QWidget


class ScenarioWindow(QWidget):
    def __init__(self, engine, dev_mode: bool = False):
        super().__init__()
        self.dev_mode = dev_mode
        self.engine = engine

        self.setWindowTitle(self.engine.scenario.display_name)