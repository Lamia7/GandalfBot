"""
Module test pour la récupération des données de l'API mapbox
- créer une classe geo_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import GEO_API_URL, TOKEN


class GeoWrapper:

    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_coordinates(self, query):

        # get result from request to mapbox api
        result = requests.get(f"{GEO_API_URL}{query}.json?access_token={TOKEN}&language=fr")

        # convert to Json
        json_result = result.json()
        print(json_result)

        # choose latitude & longitude from result and store them into variables
        self.longitude = json_result['features'][0]['geometry']['coordinates'][1]
        self.latitude = json_result['features'][0]['geometry']['coordinates'][0]
        print(f"Pour {query} la longitude est {self.longitude} et la latitude est {self.latitude}")

        return self.longitude, self.latitude

# testing with paris as query
#geo = GeoWrapper()
#print(geo.get_coordinates("reims"))
