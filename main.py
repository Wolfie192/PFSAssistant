from PySide6.QtWidgets import QApplication
from ui import MainWindow
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PFS Assistant")
    parser.add_argument("--dev", action="store_true", help="Enable developer mode to access un-implemented scenarios.")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = MainWindow(sys.argv)
    window.show()
    app.exec()