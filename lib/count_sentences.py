#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        return isinstance(self.value, str) and self.value.endswith(".")

    def is_question(self):
        return isinstance(self.value, str) and self.value.endswith("?")

    def is_exclamation(self):
        return isinstance(self.value, str) and self.value.endswith("!")

    def count_sentences(self):
        if not isinstance(self.value, str):
            return 0
        import re
        # Split on . ! ? followed by space or end of string, ignore empty
        sentences = re.split(r'[.!?](?:\s|$)', self.value)
        return len([s for s in sentences if s.strip()])
