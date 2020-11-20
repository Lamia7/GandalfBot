"""
Module test pour la récupération des données de l'API wikimedia
- créer une classe wiki_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import WIKI_API_URL


class Wikiwrapper:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_wiki_info(self):

        payload = {"action": "query",
                   "format": "json",
                   "ggscoord": f"{self.longitude}|{self.latitude}",
                   "generator": "geosearch",
                   "prop": "extracts|info",
                   "explaintext": True,  # convert HTML to plain text
                   "exsentences": 3,  # how sentences to return
                   "inprop": "url",  # get url (added info to prop for this)
                   }
        # variable contains request result
        result = requests.get(WIKI_API_URL, payload)

        # if request works
        if result.status_code == 200:
            # mettre en json
            json_result = result.json()

            # ds dico query, le dico pages
            pages = json_result['query']['pages']  # access to pages from result json
            pages = (list(pages.values()))  # convert values of pages into list of dict

            title = pages[0]['title']  # get title's value from first dict
            description = pages[0]['extract']  # get extract's value
            url = pages[0]['fullurl']  # get wikipedia link

            #return title, description, url
            # Return a json
            wiki_details = {
                "title": title,
                "description": description,
                "url": url
            }
            print(wiki_details)

            return wiki_details

        else:
            #print(f"Une erreur s'est produite: {result.status_code}")
            # error is a tuple with 3 elements, like result
            #err = (f"Une erreur s'est produite.", "Plus d'informations:", f"{result.status_code}")

            # Return a json
            return {
                "ERREUR :": result.status_code
            }


#test
#wikiwrapper = Wikiwrapper(48.85658, 2.35183)
#print(wikiwrapper.get_wiki_info())


"""
            # Return a json
            wiki_details = {
                "title": title,
                "description": description,
                "url": url
            }
            print(wiki_details)

            return wiki_details


print(f"TITRE: {wikiwrapper.get_wiki_info()[0]}\n"
      f"DESCRIPTION: {wikiwrapper.get_wiki_info()[1]}\n"
      f"URL: {wikiwrapper.get_wiki_info()[2]}")"""

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

#result = requests.get("https://fr.wikipedia.org/w/api.php?action=query&format=json&ggscoord=48.85658|2.35183&generator=geosearch&prop=extracts|info&explaintext&exsentences=3&inprop=url&titles=paris")
"""