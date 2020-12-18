"""
Module test to test the geo_api module
mocking : imiter
monkeypatch: remplacer pour imiter
"""
import requests

from app.geo_api import GeoWrapper


def test_get_location_coordinates_success(
    monkeypatch,
):  # monkeypatch fixture to replace
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                "type": "FeatureCollection",
                "query": ["barcelone"],
                "features": [
                    {
                        "id": "place.8188885146167790",
                        "relevance": 1,
                        "text_fr": "Barcelone",
                        "language_fr": "fr",
                        "place_name_fr":
                            "Barcelone, province de Barcelone, Espagne",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [2.17694, 41.3825],
                        },
                    },
                    {
                        "id": "place.7102865829451400",
                        "relevance": 1,
                        "text_fr": "Barceloneta",
                        "language_fr": "fr",
                        "place_name_fr":
                            "Barceloneta, Barceloneta, Porto Rico",
                        "place_name": "Barceloneta, Barceloneta, Porto Rico",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [-66.5413, 18.4563],
                        },
                    },
                    {
                        "id": "region.11679311305451400",
                        "relevance": 1,
                        "text_fr": "Barceloneta",
                        "language_fr": "fr",
                        "place_name_fr": "Barceloneta, Porto Rico",
                        "text": "Barceloneta",

                        "geometry": {
                            "type": "Point",
                            "coordinates": [-66.53861, 18.45056],
                        },
                    },
                    {
                        "id": "poi.42949696199",
                        "relevance": 1,
                        "text_fr": "Barceloneta",
                        "place_name_fr":
                            "Barceloneta, Kinkerstraat 228, Amsterdam, "
                            "Hollande-Septentrionale 1053 EN, Pays-Bas",
                        "geometry": {
                            "coordinates": [4.865995, 52.365722],
                            "type": "Point",
                        },
                    },
                ],
            }

    def mock_get_coordinates(url):
        return MockResponse()

    # Replace requests.get function by mock_get,
    # give it the url given to requests.get
    monkeypatch.setattr(requests, "get", mock_get_coordinates)
    # or monkeypatch.setattr('requests.get', mock_get_coordinates)

    request = GeoWrapper("input")
    assert request.longitude, request.latitude == (41.3825, 2.17694)


def test_get_location_coordinates_failure(monkeypatch):
    """GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response has failed
    THEN check the HTTP response"""

    class MockResponse:  # object in param?
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"error": "bad"}

    def mock_get_coordinates(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_coordinates)

    request = GeoWrapper("input")
    assert (request.longitude, request.latitude) == (None, None)
