from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QSpacerItem, QPushButton, QSizePolicy
from PyQt5 import uic

from widgets import FormRendererWidget
from form import render_form
from apf import read_apf

import sys

APPNAME = "AP Forms"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/form_main_window.ui", self)
        self.setWindowTitle(APPNAME)
        main_layout = self.centralWidget().layout()
        form_renderer = FormRendererWidget(parent=None)
        main_layout.addWidget(form_renderer)
        test_form = read_apf()
        render_form(test_form, form_renderer)
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        form_renderer.add_form_item(spacer)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
