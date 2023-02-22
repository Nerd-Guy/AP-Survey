import pickle
from widgets import (
    TitleWidget,
    FormRendererWidget,
    TextEntryWidget,
    LineEntryWidget,
    MultipleChoiceWidget,
)
from PyQt5.QtWidgets import QWidget, QPushButton


class InvalidFormData(BaseException):
    """Raise when the form data is invalid."""


class FormElement:
    def __init__(self, widget: QWidget) -> None:
        self.ui_attributes = {}
        self.widget = widget

    def add_ui_attribute(self, attr, value):
        setattr(self, attr, value)
        self.ui_attributes[attr] = value


class LineEntry(FormElement):
    def __init__(self, prompt: str):
        super().__init__(widget=LineEntryWidget)
        self.add_ui_attribute("prompt", prompt)


class TextEntry(FormElement):
    def __init__(self, prompt: str):
        super().__init__(widget=TextEntryWidget)
        self.add_ui_attribute("prompt", prompt)


class MultipleChoice(FormElement):
    def __init__(self, prompt, options: list[str]):
        super().__init__(widget=MultipleChoiceWidget)
        self.add_ui_attribute("prompt", prompt)
        self.add_ui_attribute("options", options)


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
        form_renderer.add_form_widget(element_widget)

    submit_btn = QPushButton(parent=None, text="Submit Form")
    form_renderer.add_form_widget(submit_btn)


def main():
    with open("test.apf", "rb") as fs:
        test: FormData = pickle.load(fs)
        render_form(test)


if __name__ == "__main__":
    main()
