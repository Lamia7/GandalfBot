"""
Module test pour la récupération des données de l'API mapbox
- créer une classe geo_wrapper
- mettre les variables globales dans fichier de config
"""

import requests

from config import GEO_API_URL, TOKEN


class GeoWrapper:

    def __init__(self, query):

        # get result from request to mapbox api
        result = requests.get(f"{GEO_API_URL}{query}.json?access_token={TOKEN}&language=fr")

        # convert to Json
        json_result = result.json()
        # choose latitude & longitude from result
        lat_lng = json_result['features'][0]['geometry']['coordinates']

        #print(json_result)
        print(lat_lng)

        # store result into variables
        latitude = json_result['features'][0]['geometry']['coordinates'][0]
        longitude = json_result['features'][0]['geometry']['coordinates'][1]
        print(f"Pour {query} la latitude est {latitude} et la longitude est {longitude}")


# testing with paris as query
geo = GeoWrapper("paris")

