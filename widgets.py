from PyQt5 import QtWidgets, uic


class TitleWidget(QtWidgets.QWidget):
    def __init__(self, parent, title: str, description: str, author: str):
        super(TitleWidget, self).__init__(parent)
        uic.loadUi("ui/title_widget.ui", parent)
        self.show()

