class MyString:
    def __init__(self, value=""):
        self._value = value

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
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Split based on '.', '!', and '?' followed by a space or end of string
        sentences = re.split(r'[.!?](?:\s|$)', self._value)
        # Filter out empty strings from the split result
        sentences = list(filter(lambda x: x.strip() != '', sentences))
        return len(sentences)