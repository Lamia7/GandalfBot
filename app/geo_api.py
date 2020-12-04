"""
Module pour la récupération des données de l'API mapbox
- créer une classe geo_wrapper
- mettre les variables globales dans fichier de config
"""
import os
import requests

from config import GEO_API_URL # importer
#from config import GEO_API_URL, TOKEN

#TOKEN = os.environ.get("GEOLOC_TOKEN")

class GeoWrapper:
    """ajouter user input dans l'init
    et ds ma méth jv setter lat et long sans return
    dès que j'init GeoWrapper, il va me renvoyer directement long et lat"""

    def __init__(self, input):
        self.latitude = None
        self.longitude = None
        self.get_coordinates(input)

    def get_coordinates(self, input):

        TOKEN = "pk.eyJ1IjoibGFtaWE3IiwiYSI6ImNraTM2dHp0aTc3YXMzNWw2Mmg0cXNibmcifQ.pvEc-B7aSOxM194G65MwfA"
        # get result from request to mapbox api
        result = requests.get(f"{GEO_API_URL}{input}.json?access_token={TOKEN}&language=fr")

        if result.status_code == 200:
            # convert to Json
            json_result = result.json()

            # choose latitude & longitude from result and store them into variables
            self.longitude = json_result['features'][0]['geometry']['coordinates'][1]
            self.latitude = json_result['features'][0]['geometry']['coordinates'][0]
            #print(f"Pour {input} la longitude est {self.longitude} et la latitude est {self.latitude}")

        else:
            print(f"Geo API error occured: {result.status_code}")
            #return result.raise_for_status()
