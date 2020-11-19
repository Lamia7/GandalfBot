"""
Module test pour la récupération des données de l'API wikimedia
- créer une classe wiki_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import API_URL, PAYLOAD


class Wikiwrapper:

    def __init__(self):
        # variable contenant la requête, renvoie 200 si ok
        result = requests.get(API_URL, PAYLOAD)  # requests.get(url, params, kwargs)

        # mettre en json
        json_result = result.json()
        # afficher résultat 200
        print(json_result)
        # ds dico query, le dico search
        result_search = json_result['query']
        result_search2 = result_search['search']
        result_search3 = result_search2[0]['snippet']
        print(f"RESULTAT QUERY: {result_search} \n"
              f"RESULTAT SEARCH : {result_search2} \n"
              f"RESULTAT PREMIER SNIPPET : {result_search3} \n")


wikiwrap = Wikiwrapper()

"""https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&prop=info&srsearch=reims&srprop=snippet
API_URL = "https://fr.wikipedia.org/w/api.php?"
PAYLOAD = {"action": "query",
           "format": "json",
           "list": "search",
           "prop": "info",
           "srprop": "snippet",
           "srsearch": "barcelone"}"""