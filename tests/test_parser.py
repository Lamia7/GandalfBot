"""
Module to test parser
"""

from app.parser import Parser

question_1 = "Bonjour Gandalf, comment ça va? Peux tu me dire où se trouve Paris ?"
question_2 = "Bonsoir Gandalf, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Aragorn."


def test_parser_gets_key_words_question_1():
    parser = Parser(question_1)
    assert parser.parsed_input == "bonjour ca trouve paris"


def test_parser_gets_key_words_question_2():
    parser = Parser(question_2)
    assert parser.parsed_input == "bonsoir espere passe belle semaine est-ce indiquer adresse tour eiffel avance salutations aragorn"

