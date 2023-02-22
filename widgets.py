from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QRadioButton


class TitleWidget(QWidget):
    def __init__(self, parent, title: str, description: str, author: str):
        super(TitleWidget, self).__init__(parent)
        uic.loadUi("ui/title_widget.ui", self)
        self.title_label.setText(title)
        self.description_label.setText(description)


class TextEntryWidget(QWidget):
    def __init__(self, parent, prompt: str):
        super(TextEntryWidget, self).__init__(parent)
        uic.loadUi("ui/entry_widget.ui", self)
        self.prompt_label.setText(prompt)


class LineEntryWidget(QWidget):
    def __init__(self, parent, prompt: str):
        super(LineEntryWidget, self).__init__(parent)
        uic.loadUi("ui/line_entry_widget.ui", self)
        self.prompt_label.setText(prompt)


class MultipleChoiceWidget(QWidget):
    def __init__(self, parent, prompt: str, options: list[str]):
        super(MultipleChoiceWidget, self).__init__(parent)
        uic.loadUi("ui/multiple_choice_widget.ui", self)
        self.prompt_label.setText(prompt)
        # Create a radio button for every option
        for option in options:
            radio_button = QRadioButton(parent=parent, text=option)
            self.layout().addWidget(radio_button)


class FormRendererWidget(QWidget):
    """The parent of all form element widgets."""

    def __init__(self, parent):
        super(FormRendererWidget, self).__init__(parent)
        uic.loadUi("ui/form_viewer_widget.ui", self)
        self.vlayout = self.scroll_area_contents.layout()

    def add_form_widget(self, widget: QWidget):
        self.vlayout.addWidget(widget)

    def add_form_item(self, item):
        self.vlayout.addItem(item)
