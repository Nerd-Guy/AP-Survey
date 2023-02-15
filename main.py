from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QSpacerItem, QPushButton
from PyQt5 import uic

from widgets import TitleWidget, EntryWidget

import sys

APPNAME = "AP Forms"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/form_main_window.ui", self)
        scroll_area_vlayout = self.scroll_area_contents.layout()
        tw = TitleWidget(self, "test form", "this is a test form", "unknown")
        ew = EntryWidget(self, "What is your name?")
        scroll_area_vlayout.addWidget(tw)
        scroll_area_vlayout.addWidget(ew)
        submit_btn = QPushButton(self, text="Submit")
        scroll_area_vlayout.addWidget(submit_btn)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
