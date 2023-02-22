import pickle
from widgets import (
    TitleWidget,
    FormRendererWidget,
    TextEntryWidget,
    LineEntryWidget,
    MultipleChoiceWidget,
)
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QPlainTextEdit


class InvalidFormData(BaseException):
    """Raise when the form data is invalid."""


class FormElement:
    def __init__(self, widget: QWidget) -> None:
        self.ui_attributes = {}
        self.widget = widget

    def add_ui_attribute(self, attr, value):
        setattr(self, attr, value)
        self.ui_attributes[attr] = value

    def on_submit(self):
        """
        Called when the form is submitted.
        Returns the value of the element.
        A value of 'None' indicates that
        the field was empty.
        """
        return None


class LineEntry(FormElement):
    def __init__(self, prompt: str):
        super().__init__(widget=LineEntryWidget)
        self.add_ui_attribute("prompt", prompt)

    def on_submit(self):
        return self.widget_instance.line_edit.text()


class TextEntry(FormElement):
    def __init__(self, prompt: str):
        super().__init__(widget=TextEntryWidget)
        self.add_ui_attribute("prompt", prompt)

    def on_submit(self):
        return self.widget_instance.text_edit.toPlainText()


class MultipleChoice(FormElement):
    def __init__(self, prompt, options: list[str]):
        super().__init__(widget=MultipleChoiceWidget)
        self.add_ui_attribute("prompt", prompt)
        self.add_ui_attribute("options", options)

    def on_submit(self):
        for i, radio_button in enumerate(self.widget_instance.radio_buttons):
            if radio_button.isChecked():
                return i

        return None


class FormMetadata:
    def __init__(self, title=None, author=None, description=None) -> None:
        self.title = title
        self.author = author
        self.description = description

    def __repr__(self) -> str:
        return f"{self.title} ({self.author}): {self.description}"


class Title(FormElement):
    def __init__(self, metadata: FormMetadata) -> None:
        super().__init__(widget=TitleWidget)
        self.add_ui_attribute("title", metadata.title)
        self.add_ui_attribute("author", metadata.author)
        self.add_ui_attribute("description", metadata.description)


class FormData:
    def __init__(self):
        self.metadata: FormMetadata | None = None
        self.elements: list[FormElement] = []


def render_form(form: FormData, form_renderer: FormRendererWidget):
    for i, element in enumerate(form.elements):
        # TODO make sure metadata title is first element
        if i == 0:
            title_widget = TitleWidget(
                None,
                form.metadata.title,
                form.metadata.description,
                form.metadata.author,
            )
            form_renderer.add_form_widget(title_widget)
        # The element must inherit from FormElement.
        # if not isinstance(element, FormElement):
        #    raise InvalidFormData(
        #        f"element '{element}' is not of type '{FormElement.__name__}'"
        #    )

        # Create a new instance of the form element's UI widget
        # and pass all of the attributes needed for the widget to render.
        element_widget: QWidget = element.widget(parent=None, **element.ui_attributes)
        element.widget_instance = element_widget
        form_renderer.add_form_widget(element_widget)

    submit_btn = QPushButton(parent=None, text="Submit Form")
    form_renderer.add_form_widget(submit_btn)
    submit_btn.clicked.connect(lambda: submit_form(form))


def get_element_values(form: FormData) -> dict[FormElement, str | int]:
    element_values: dict[FormElement, str | int] = {}
    for element in form.elements:
        element_values[element] = element.on_submit()

    return element_values


def submit_form(form: FormData):
    element_values = get_element_values(form)
    print(element_values)
    # TODO Submit to server


def main():
    with open("test.apf", "rb") as fs:
        test: FormData = pickle.load(fs)
        render_form(test)


if __name__ == "__main__":
    main()
