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

from config import PUNCTUATION, STOP_WORDS
from app.geo_api import GeoWrapper
from app.wiki_api import Wikiwrapper


class Parser:

    def __init__(self):
        self.user_input = None

    def get_place(self, user_input):
        """Find place"""
        #mapbox_api to get coordinates
        geowrapper = GeoWrapper()
        coordinates = geowrapper.get_coordinates(user_input)

        longitude = coordinates[0]
        latitude = coordinates[1]

        #wikiwrapper = Wikiwrapper(48.85658, 2.35183)
        #wikiwrapper = Wikiwrapper(coordinates)
        wikiwrapper = Wikiwrapper(longitude, latitude)
        wiki_details = wikiwrapper.get_wiki_info()
        return wiki_details

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

    def delete_stop_words(self, user_input):
        """
        PROBLEME : ne supprime pas certains STOP words (voir exemple de test)
        :param user_input:
        :return: sentence with key words & without stop words
        """
        # print(type(user_input))
        words_list = user_input.split()
        for word in words_list:
            if word in STOP_WORDS:
                # print(word)
                words_list.remove(word)
        simple_sentence = ' '.join(words_list)
        return simple_sentence



"""
def delete_stop_words(user_input):
    print(type(user_input))
    for word in user_input:
        if word in STOP_WORDS:
            print(word)
            user_input.remove(word)
    return user_input
"""

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
      
# testing delete_stop_words method
phrase_list = ['enfin', 'sais', 'tu', 'ou', 'est', 'paris']
phrase = "Enfin sais tu ou est paris"
new = delete_stop_words(phrase)
print(new)
#problème: me renvoie : E'nfin sais ou paris' AU LIEU DE 'sais paris'
"""
