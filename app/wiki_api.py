"""
Module test pour la récupération des données de l'API wikimedia
- créer une classe wiki_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import WIKI_API_URL, PAYLOAD


class Wikiwrapper:

    def __init__(self):
        # variable contains request result
        result = requests.get(WIKI_API_URL, PAYLOAD)
        #result = requests.get("https://fr.wikipedia.org/w/api.php?action=query&format=json&ggscoord=48.85658|2.35183&generator=geosearch&prop=extracts|info&explaintext&exsentences=3&inprop=url&titles=paris")

        # if request works
        if result.status_code == 200:
            # mettre en json
            json_result = result.json()
            # afficher résultat 200
            #print(f"JSON RESULT: {json_result}")

            # ds dico query, le dico pages
            pages = json_result['query']['pages']  # access to pages from result json
            #print(type(pages))  # dict
            pages = (list(pages.values()))  # convert values of pages into list of dict
            #print(pages)
            #print(type(pages))  # list

            # get title's value from first dict
            title = pages[0]['title']
            print(f"TITLE: {title}")

            # get extract's value
            extract = pages[0]['extract']
            #print(type(extract))  # str
            print(f"EXTRACT: {extract}")

            # get wikipedia link
            url = pages[0]['fullurl']
            print(f"URL: {url}")

        else:
            print(f"Une erreur s'est produite: {result.status_code}")


wikiwrap = Wikiwrapper()


"""
API_URL = "https://fr.wikipedia.org/w/api.php?"
PAYLOAD = {"action": "query",
           "format": "json",
           "ggscoord": "48.85658|2.35183",
           "generator": "geosearch",
           "prop": "extracts|info",
           "explaintext": True,  # convert HTML to plain text
           "exsentences": 3,  # how sentences to return
           "inprop": "url",  # get url (added info to prop for this)
           "titles": "barcelone"}
           
           
"ggscoord" = longitude|latitude
"""