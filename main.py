from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

from form_hub import SurveyHub
from widgets import TitleWidget

import sys

APPNAME = "AP Forms"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APPNAME)
        self.title = TitleWidget(self, "", "", "")
        self.title.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
