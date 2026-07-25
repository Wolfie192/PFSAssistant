from PySide6.QtWidgets import QMainWindow
from ui.views import MainMenuView



class MainWindow(QMainWindow):
    def __init__(self, argv):
        super().__init__()
        self.dev_mode = False

        if "--dev" in argv:
            self.dev_mode = True

        self.setWindowTitle("PFS Assistant")

        self.main_menu_view = MainMenuView(self)

        self.setCentralWidget(self.main_menu_view)