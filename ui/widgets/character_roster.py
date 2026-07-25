from PySide6.QtWidgets import QWidget, QVBoxLayout
from core.models import Character


class CharacterRosterWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode
        self.engine = parent.engine