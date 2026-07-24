from PySide6.QtWidgets import QApplication, QWidget

from ui.main_window import MainWindow


class App(QApplication):
    def __init__(self, dev_mode: bool = False):
        super().__init__()
        self.dev_mode = dev_mode

        self.main_window = MainWindow(self)

    def switch_widget(self, widget: QWidget):
        self.main_window.setCentralWidget(widget)



if __name__ == "__main__":
    app = App(dev_mode=True)
    app.exec()