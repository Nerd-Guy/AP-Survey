import xml.etree.ElementTree as ET
from enum import Enum

class FormMetadata:
    def __init__(self, title: str, author: str, description: str) -> None:
        self.title = title
        self.author = author
        self.description = description

    def __repr__(self) -> str:
        return f"{self.title} ({self.author}): {self.description}"

class FormElementType(Enum):
    entry_field = "entryField"
    multiple_choice = "multipleChoice"

class FormElement:
    def __init__(self, prompt, type_: FormElementType, **kwargs):
        self.prompt = prompt
        self.type = type_
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def display_widget(self):
        ...

class EntryField(FormElement):
    def __init__(self, prompt, type_: FormElementType, **kwargs):
        super().__init__(prompt, type_, **kwargs)

    def display_widget(self):
        ...

class MultipleChoice(FormElement):
    def __init__(self, prompt, type_: FormElementType, **kwargs):
        super().__init__(prompt, type_, **kwargs)

    def display_widget(self):
        ...

class FormData:
    def __init__(self, xml_data: str):
        self.metadata: FormMetadata | None = None
        self.elements: list[FormElement] = []
        self.__parse_xml(xml_data)
    
    def __parse_xml(self, data):
        root = ET.fromstring(data)
        meta = root.find("meta")
        meta_ = {child.tag: child.text for child in meta}
        self.metadata = FormMetadata(**meta_)

        elements = root.find("page")
        for element in elements:
            prompt = element.attrib["prompt"]
            current_element = FormElement(prompt, element.tag)
            if element.tag == FormElementType.multiple_choice.value:
                choices = []
                for choice in element:
                    choice.append()

            self.elements.append(
                FormElement(prompt, element.tag)
            )