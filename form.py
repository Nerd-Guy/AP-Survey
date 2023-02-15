import pickle


class Text(str):
    ...


class Image:
    ...


class FormElement:
    ...


class EntryField(FormElement):
    def __init__(self, prompt: str):
        super().__init__()
        self.prompt = prompt

class FormMetadata:
    def __init__(self, title=None, author=None, description=None) -> None:
        self.title = title
        self.author = author
        self.description = description

    def __repr__(self) -> str:
        return f"{self.title} ({self.author}): {self.description}"


class FormData:
    def __init__(self):
        self.metadata: FormMetadata | None = None
        self.elements: list[FormElement] = []


def main():
    with open("test.apf", "rb") as fs:
        test: FormData = pickle.load(fs)
        print(test.metadata)


if __name__ == "__main__":
    main()
