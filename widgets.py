from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class TitleWidget(QWidget):
    def __init__(self, parent, title: str, description: str, author: str):
        super(TitleWidget, self).__init__(parent)
        uic.loadUi("ui/title_widget.ui", self)
        self.title_label.setText(title)
        self.description_label.setText(description)


class EntryWidget(QWidget):
    def __init__(self, parent, prompt: str):
        super(EntryWidget, self).__init__(parent)
        uic.loadUi("ui/entry_widget.ui", self)
        self.prompt_label.setText(prompt)
