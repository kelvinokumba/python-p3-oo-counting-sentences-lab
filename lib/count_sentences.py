#!/usr/bin/env python3

import re

class MyString:
    def __init__(self):
        self.value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            raise ValueError("Value must be a string")
        self._value = val

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value using punctuation characters as separators
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings from the list
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

