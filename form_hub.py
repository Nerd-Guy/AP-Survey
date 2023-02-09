from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize

class FormHub(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        font = QtGui.QFont()
        font.setPointSize(20)
        layout = QtWidgets.QVBoxLayout()
        survey_hub_label = QtWidgets.QLabel(self, text="Survey Hub")
        survey_hub_label.setStyleSheet("background-color: black")
        survey_hub_label.setFixedSize(QSize(500, 500))
        survey_hub_label.setFont(font)
        layout.addWidget(survey_hub_label)
