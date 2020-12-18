"""
Module that represents the parser that will analyze the user_input by:
making it in lower case, removing accents,
punctuation and stop words from user_input
"""
from unidecode import unidecode

from configuration.config import PUNCTUATION, STOP_WORDS


class Parser:
    """Represents the parser"""

    def __init__(self, user_input):
        self.user_input = user_input
        self.delete_accents()
        self.make_lower_case()
        self.delete_punctuation()
        self.separate_words()
        self.get_key_words()
        self.parsed_input = self.user_input

    def delete_accents(self):
        """Removes accents from user_input"""
        self.user_input = unidecode(self.user_input)

    def make_lower_case(self):
        """Makes user_input in lower case"""
        self.user_input = self.user_input.lower()

    def delete_punctuation(self):
        """Removes punctuation from user input"""
        for char in self.user_input:
            if char in PUNCTUATION:
                self.user_input = self.user_input.replace(char, " ")

    def separate_words(self):
        """Separate user_input string into a list of words"""
        self.user_input = self.user_input.split()

    def get_key_words(self):
        """Gets only key words that are not in stop words
        and join them in a string"""
        key_words = \
            [word for word in self.user_input if word not in STOP_WORDS]
        self.user_input = ' '.join(key_words)
