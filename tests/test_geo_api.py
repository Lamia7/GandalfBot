"""
Module test to test the geo_api module
mocking : imiter
monkeypatch: remplacer pour imiter
"""
import requests

from app.geo_api import GeoWrapper


def test_get_location_coordinates_success(monkeypatch):  #monkeypatch fixture to replace
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    #class MockResponse(object): #object ?
    class MockResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                'type': 'FeatureCollection', 'query': ['barcelone'],
                'features': [
                    {'id': 'place.8188885146167790', 'type': 'Feature', 'place_type': ['place'], 'relevance': 1,
                     'properties': {'wikidata': 'Q1492'}, 'text_fr': 'Barcelone', 'language_fr': 'fr',
                     'place_name_fr': 'Barcelone, province de Barcelone, Espagne', 'text': 'Barcelone',
                     'language': 'fr', 'place_name': 'Barcelone, province de Barcelone, Espagne',
                     'bbox': [2.052333, 41.317203, 2.229555, 41.467943], 'center': [2.17694, 41.3825],
                     'geometry':
                         {'type': 'Point',
                          'coordinates': [2.17694, 41.3825]},
                     'context': [{'id': 'region.10356397360167790', 'wikidata': 'Q81949', 'short_code': 'ES-B',
                                  'text_fr': 'province de Barcelone', 'language_fr': 'fr',
                                  'text': 'province de Barcelone', 'language': 'fr'},
                                 {'id': 'country.3373497261570100', 'wikidata': 'Q29', 'short_code': 'es',
                                  'text_fr': 'Espagne', 'language_fr': 'fr', 'text': 'Espagne', 'language': 'fr'}]},
                    {'id': 'place.7102865829451400', 'type': 'Feature', 'place_type': ['place'], 'relevance': 1,
                     'properties': {'wikidata': 'Q2025087'}, 'text_fr': 'Barceloneta', 'language_fr': 'fr',
                     'place_name_fr': 'Barceloneta, Barceloneta, Porto Rico', 'text': 'Barceloneta',
                     'language': 'fr', 'place_name': 'Barceloneta, Barceloneta, Porto Rico',
                     'bbox': [-66.5934580068456, 18.389405981119, -66.5211250002571, 18.4935790184711],
                     'center': [-66.5413, 18.4563],
                     'geometry': {'type': 'Point', 'coordinates': [-66.5413, 18.4563]}, 'context': [
                        {'id': 'region.11679311305451400', 'wikidata': 'Q2025087', 'text_fr': 'Barceloneta',
                         'language_fr': 'fr', 'text': 'Barceloneta', 'language': 'fr'},
                        {'id': 'country.16776721557498950', 'wikidata': 'Q1183', 'short_code': 'pr',
                         'text_fr': 'Porto Rico', 'language_fr': 'fr', 'text': 'Porto Rico', 'language': 'fr'}]},
                    {'id': 'region.11679311305451400', 'type': 'Feature', 'place_type': ['region'], 'relevance': 1,
                     'properties': {'wikidata': 'Q2025087'}, 'text_fr': 'Barceloneta', 'language_fr': 'fr',
                     'place_name_fr': 'Barceloneta, Porto Rico', 'text': 'Barceloneta', 'language': 'fr',
                     'place_name': 'Barceloneta, Porto Rico',
                     'bbox': [-66.5934569998696, 18.3894070140351, -66.5211260302365, 18.5857753252961],
                     'center': [-66.53861, 18.45056],
                     'geometry': {'type': 'Point', 'coordinates': [-66.53861, 18.45056]}, 'context': [
                        {'id': 'country.16776721557498950', 'wikidata': 'Q1183', 'short_code': 'pr',
                         'text_fr': 'Porto Rico', 'language_fr': 'fr', 'text': 'Porto Rico', 'language': 'fr'}]},
                    {'id': 'poi.42949696199', 'type': 'Feature', 'place_type': ['poi'], 'relevance': 1,
                     'properties': {'foursquare': '55f06179498e77636e64d09a', 'landmark': True,
                                    'address': 'Kinkerstraat 228',
                                    'category': 'seafood, seafood restaurant, restaurant'},
                     'text_fr': 'Barceloneta',
                     'place_name_fr': 'Barceloneta, Kinkerstraat 228, Amsterdam, Hollande-Septentrionale 1053 EN, Pays-Bas',
                     'text': 'Barceloneta',
                     'place_name': 'Barceloneta, Kinkerstraat 228, Amsterdam, Hollande-Septentrionale 1053 EN, Pays-Bas',
                     'center': [4.865995, 52.365722],
                     'geometry': {'coordinates': [4.865995, 52.365722], 'type': 'Point'}, 'context': [
                        {'id': 'neighborhood.17269576747609360', 'wikidata': 'Q3637742', 'text_fr': 'Bellamybuurt',
                         'language_fr': 'fr', 'text': 'Bellamybuurt', 'language': 'fr'},
                        {'id': 'postcode.13154402476556750', 'text_fr': '1053 EN', 'text': '1053 EN'},
                        {'id': 'locality.17269501081005190', 'wikidata': 'Q1742210', 'text_fr': 'Kinkerbuurt',
                         'language_fr': 'fr', 'text': 'Kinkerbuurt', 'language': 'fr'},
                        {'id': 'place.9718548927723970', 'wikidata': 'Q727', 'text_fr': 'Amsterdam',
                         'language_fr': 'fr', 'text': 'Amsterdam', 'language': 'fr'},
                        {'id': 'region.9930807704279220', 'wikidata': 'Q701', 'short_code': 'NL-NH',
                         'text_fr': 'Hollande-Septentrionale', 'language_fr': 'fr',
                         'text': 'Hollande-Septentrionale', 'language': 'fr'},
                        {'id': 'country.13545879598622050', 'wikidata': 'Q55', 'short_code': 'nl',
                         'text_fr': 'Pays-Bas', 'language_fr': 'fr', 'text': 'Pays-Bas', 'language': 'fr'}]},
                    {'id': 'poi.395137085614', 'type': 'Feature', 'place_type': ['poi'], 'relevance': 1,
                     'properties': {'foursquare': '5acb2371c9a51750091c088f', 'wikidata': 'Q1492', 'landmark': True,
                                    'category': 'park, leisure'}, 'text_fr': 'Barcelone', 'language_fr': 'fr',
                     'place_name_fr': 'Barcelone, Barcelone, province de Barcelone 08002, Espagne',
                     'text': 'Barcelone', 'language': 'fr',
                     'place_name': 'Barcelone, Barcelone, province de Barcelone 08002, Espagne',
                     'center': [2.1765205, 41.381997],
                     'geometry': {'coordinates': [2.1765205, 41.381997], 'type': 'Point'},
                     'context': [{'id': 'postcode.14988663762430790', 'text_fr': '08002', 'text': '08002'},
                                 {'id': 'locality.4948880326656110', 'text_fr': 'el Gòtic', 'text': 'el Gòtic'},
                                 {'id': 'place.8188885146167790', 'wikidata': 'Q1492', 'text_fr': 'Barcelone',
                                  'language_fr': 'fr', 'text': 'Barcelone', 'language': 'fr'},
                                 {'id': 'region.10356397360167790', 'wikidata': 'Q81949', 'short_code': 'ES-B',
                                  'text_fr': 'province de Barcelone', 'language_fr': 'fr',
                                  'text': 'province de Barcelone', 'language': 'fr'},
                                 {'id': 'country.3373497261570100', 'wikidata': 'Q29', 'short_code': 'es',
                                  'text_fr': 'Espagne', 'language_fr': 'fr', 'text': 'Espagne',
                                  'language': 'fr'}]}], }

    def mock_get_coordinates(url):
        return MockResponse()

    # Replacing the requests.get function by mock_get, giving it the url given to requests.get
    monkeypatch.setattr(requests, 'get', mock_get_coordinates)
    # or monkeypatch.setattr('requests.get', mock_get_coordinates)

    request = GeoWrapper("input")
    assert request.longitude, request.latitude == (41.3825, 2.17694)


def test_get_location_coordinates_failure(monkeypatch):
    """GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response has failed
    THEN check the HTTP response"""

    class MockResponse():  # object in param?
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"error": "bad"}

    def mock_get_coordinates(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get_coordinates)

    request = GeoWrapper("input")
    assert (request.longitude, request.latitude) == (None, None)

