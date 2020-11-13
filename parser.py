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

# testing delete_accents method with unidecode library
test = "voilà l'été !"
test_sans_accent = unidecode(test)
print(test)
print(test_sans_accent)

#testing make_lower_case method
phrase = "Bonjour Lamia"
phrase_lower = phrase.lower()
print(phrase)
print(phrase_lower)


class Parser:

    def __init__(self):
        pass

    def cut_question(self):
        pass

    def analyze_words(self):
        pass

    def delete_stop_words(self):
        pass

    def delete_accents(self, user_input):
        return unidecode(user_input)

    def make_lower_case(self, user_input):
        return user_input.lower()
