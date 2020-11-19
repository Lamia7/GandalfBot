"""Module that represents the parser that will analyze the question asked by
1) cutting down data (question) in words
2) analyzing words
3) keeping the key words

- normaliser minuscules/majuscules
- éliminer accents
- isoler lieu
- éliminer stop words
"""
from unidecode import unidecode

from config import PUNCTUATION


class Parser:

    def __init__(self):
        pass

    def delete_accents(self, user_input):
        return unidecode(user_input)

    def make_lower_case(self, user_input):
        return user_input.lower()

    def delete_punctuation(self, user_input):
        """Removes punctuation from user input"""

        for char in user_input:
            if char in PUNCTUATION:
                user_input = user_input.replace(char, " ")
        return user_input

    def cut_question(self, user_input):
        """Cutdown user_input into words"""
        return user_input.split()

    def analyze_words(self):
        pass

    def delete_stop_words(self):
        pass


"""
# testing delete_accents method with unidecode library
test = "voilà l'été !"
test_sans_accent = unidecode(test)
print(test)
print(test_sans_accent)

# testing make_lower_case method
phrase = "Bonjour Lamia"
phrase_lower = phrase.lower()
print(phrase)
print(phrase_lower)

# testing delete_punctuation method
phrase = "Bonjour ! Comment ça va ?"
phrase2 = "Bonjour! Comment ça va ?"

phrase_no_punc = delete_punctuation(phrase)
phrase_no_punc2 = delete_punctuation(phrase2)
print(f"Phrase 1: {phrase_no_punc} \n"
      f"Phrase 2: {phrase_no_punc2}")
"""
