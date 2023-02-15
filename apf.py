import pickle

import form as f

def write_apf(form_):
    with open("test.apf", "wb") as fs:
        pickle.dump(form_, fs)

def read_apf():
    with open("test.apf", "rb") as fs:
        return pickle.load(fs)


form = f.FormData()
form.metadata = f.FormMetadata("Test Form", "Developer", "This is a test form!")
form.elements = [f.EntryField("What is your name?")]
