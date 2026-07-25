from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class TitleBlock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dev_mode = parent.dev_mode

        if self.dev_mode:
            self.title_str = "PFS Assistant (Dev)"
        else:
            self.title_str = "PFS Assistant"
        self.title_label = QLabel(self.title_str)
        self.title_label.setFont(QFont("Arial", 28))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.callline_label = QLabel("A digital assistant for running Pathfinder 2e Society games.")
        self.callline_label.setFont(QFont("Arial", 20))
        self.callline_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.callline_label)
        self.layout.setSpacing(0)

        self.setLayout(self.layout)