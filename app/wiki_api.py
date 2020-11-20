"""
Module test pour la récupération des données de l'API wikimedia
- créer une classe wiki_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import WIKI_API_URL, PAYLOAD


class Wikiwrapper:

    def __init__(self):
        # variable contenant la requête, renvoie 200 si ok
        #result = requests.get(WIKI_API_URL, PAYLOAD)  # requests.get(url, params, kwargs)
        result = requests.get("https://fr.wikipedia.org/w/api.php?action=query&format=json&ggscoord=48.85658|2.35183&generator=geosearch&prop=extracts|extlinks&titles=paris&explaintext")

        # mettre en json
        json_result = result.json()
        # afficher résultat 200
        print(json_result)

        # ds dico query, le dico pages
        pages = json_result['query']['pages']  # access to pages from result json
        print(type(pages))  # dict
        pages = (list(pages.values()))  # convert values of pages into list of dict
        print(pages)
        print(type(pages))  # list

        # get title's value from first dict
        title = pages[0]['title']
        print(f"TITLE: {title}")

        # get extract's value
        extract = pages[0]['extract']
        print(type(extract))
        #print(f"EXTRACT: {extract}")
        # limit caract of extract's value
        resume = extract[0:300]
        print(f"RESUME: {resume}")
        print(type(resume))

        # get wikipedia link


wikiwrap = Wikiwrapper()



"""https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&prop=info&srsearch=reims&srprop=snippet
API_URL = "https://fr.wikipedia.org/w/api.php?"
PAYLOAD = {"action": "query",
           "format": "json",
           "list": "search",
           "prop": "info",
           "srprop": "snippet",
           "srsearch": "barcelone"}
           
           
"ggscoord" = longitude|latitude
"""