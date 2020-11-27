"""Module that represents the parser that will analyze the question asked by
1) cutting down data (question) in words
2) analyzing words
3) keeping the key words

- normaliser minuscules/majuscules
- éliminer accents
- isoler lieu
- éliminer stop words

A FAIRE:
- ajouter docstrings
-
"""
from unidecode import unidecode

from config import PUNCTUATION, STOP_WORDS


class Parser:

    def __init__(self, user_input):
        """Cleans and parses user_input"""
        self.user_input = user_input
        self.delete_accents()
        self.make_lower_case()
        self.delete_punctuation()
        self.cut_question()
        self.get_key_words()
        self.parsed_input = self.user_input

    def delete_accents(self):
        self.user_input = unidecode(self.user_input)

    def make_lower_case(self):
        self.user_input = self.user_input.lower()

    def delete_punctuation(self):
        """Removes punctuation from user input"""
        for char in self.user_input:
            if char in PUNCTUATION:
                self.user_input = self.user_input.replace(char, " ")

    def cut_question(self):
        """Separate user_input string into a list of words"""
        self.user_input = self.user_input.split()

    def get_key_words(self):
        """ """
        key_words = []
        for word in self.user_input:
            if word not in STOP_WORDS:
                key_words.append(word)
        self.user_input = ' '.join(key_words)


""" 
TEST
parser = Parser()
print(parser)
parser.launch_parse_process("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?")
print(f"PARSED_MSG: {parser.parsed_input}")
print(f"GET PLACE: {parser.get_place(parser.parsed_input)}")


question = "Sais tu où se trouve Paris ?"
print(question)
parser = Parser()
#print(f"PARSER: {parser}")

question_no_acc = parser.delete_accents(question)
#print(f"QUESTION_NO_ACC: {question_no_acc}")

question_lower = parser.make_lower_case(question_no_acc)
#print(f"QUESTION_LOWER: {question_lower}")

question_no_punc = parser.delete_punctuation(question_lower)
#print(f"QUESTION_NO_PUNC: {question_no_punc}")

question_words = parser.cut_question(question_no_punc)
#print(f"QUESTION_WORDS_LIST: {question_words}")

final_question = parser.delete_stop_words(question_words)
print(f"FINAL_QUESTION: {final_question}")




ANCIENNES METHODES
-------   
    def delete_accents(self, user_input):
        return unidecode(user_input)

    def make_lower_case(self, user_input):
        return user_input.lower()
    
        def delete_punctuation(self, user_input):
        #Removes punctuation from user input

        for char in user_input:
            if char in PUNCTUATION:
                user_input = user_input.replace(char, " ")
        return user_input

    def cut_question(self, user_input):
        #Cutdown user_input into words
        return user_input.split()

    def delete_stop_words(self, user_input):
        # print(type(user_input))
        #words_list = user_input.split()
        #for word in words_list:
            #if word in STOP_WORDS:
                # print(word)
                #words_list.remove(word)
        #simple_sentence = ' '.join(words_list)
        #return simple_sentence

        for word in user_input:
            if word in STOP_WORDS:
                # print(word)
                user_input.remove(word)
        simple_sentence = ' '.join(user_input)
        return simple_sentence    
        
        """

"""
def delete_stop_words(user_input):
    print(type(user_input))
    for word in user_input:
        if word in STOP_WORDS:
            print(word)
            user_input.remove(word)
    return user_input



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
