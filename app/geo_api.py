"""
Module test pour la récupération des données de l'API mapbox
- créer une classe geo_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import GEO_API_URL, TOKEN


class GeoWrapper:
    """ajouter user input dans l'init
    et ds ma méth jv setter lat et long sans return
    dès que j'init GeoWrapper, il va me renvoyer directement long et lat"""

    def __init__(self, input):
        self.latitude = None
        self.longitude = None
        self.get_coordinates(input)

    def get_coordinates(self, input):

        # get result from request to mapbox api
        result = requests.get(f"{GEO_API_URL}{input}.json?access_token={TOKEN}&language=fr")

        # convert to Json
        json_result = result.json()
        print(json_result)

        # choose latitude & longitude from result and store them into variables
        self.longitude = json_result['features'][0]['geometry']['coordinates'][1]
        self.latitude = json_result['features'][0]['geometry']['coordinates'][0]
        print(f"Pour {input} la longitude est {self.longitude} et la latitude est {self.latitude}")

        #return self.longitude, self.latitude

# testing with paris as query
#geo = GeoWrapper()
#print(geo.get_coordinates("reims"))
