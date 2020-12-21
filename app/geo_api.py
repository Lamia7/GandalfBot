"""
Module to get data from the Mapbox API
"""
import requests

from configuration.config import GEO_API_URL, GEO_TOKEN


class GeoWrapper:
    """Represents the Mapbox API"""

    def __init__(self, input):
        self.latitude = None
        self.longitude = None
        self.get_coordinates(input)

    def get_coordinates(self, input):
        """Gets the coordinates from Mapbox API and sets
        latitude & longitude according to input"""
        result = requests.get(
            f"{GEO_API_URL}{input}.json?access_token={GEO_TOKEN}&language=fr")

        if result.status_code == 200:
            json_result = result.json()  # convert2json

            if len(json_result['features']) > 0:

                # choose lat & long from result and store them into variables
                self.longitude = \
                    json_result['features'][0]['geometry']['coordinates'][1]
                self.latitude = \
                    json_result['features'][0]['geometry']['coordinates'][0]
                # print(f"Pour {input}, la longitude est {self.longitude} "
                # f"et la latitude est {self.latitude}")

        # else:
            # print(f"Geo API error occured: {result.status_code}")
