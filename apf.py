import pickle

import form as f


def write_apf(form_):
    with open("test.apf", "wb") as fs:
        pickle.dump(form_, fs)


def read_apf():
    with open("test.apf", "rb") as fs:
        return pickle.load(fs)


form = f.FormData()
form.metadata = f.FormMetadata("Form", "", "This is a test form!")
form.elements = [
    f.LineEntry("What is your name?"),
    f.MultipleChoice("What year do you graduate?", ["2023", "2024", "2025", "2026"]),
    f.MultipleChoice("What is the chemical formula for Water?", ["HO", "H2O", "OH", "O2H"])
]
write_apf(form)
