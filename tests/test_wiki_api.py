import requests

from app.wiki_api import Wikiwrapper


def test_get_wiki_info_by_long_lat_with_success(monkeypatch):
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
                "query": {
                    "pages": {
                        "5211": {
                            "pageid": 5211,
                            "ns": 0,
                            "title": "Barcelone",
                            "index": -1,
                            "extract": "Barcelone [baʁsəlɔn] (en catalan : "
                                       "Barcelona [bərsəˈɫonə] ;",
                            "fullurl":
                                "https://fr.wikipedia.org/wiki/Barcelone",
                        },
                        "771897": {
                            "pageid": 771897,
                            "ns": 0,
                            "title": "Quartier gothique",
                            "index": 0,
                            "fullurl":
                                "https://fr.wikipedia.org/wiki/"
                                "Quartier_gothique",
                        },
                        "1002545": {
                            "pageid": 1002545,
                            "ns": 0,
                            "title": "Cités et Gouvernements locaux unis",
                            "index": 1,
                            "fullurl":
                                "https://fr.wikipedia.org/wiki/"
                                "Cit%C3%A9s_et_Gouvernements_locaux_unis",
                        },
                        "4082734": {
                            "pageid": 4082734,
                            "ns": 0,
                            "title": "Palais de la généralité de Catalogne",
                            "index": 2,
                            "fullurl":
                                "https://fr.wikipedia.org/wiki/Palais_"
                                "de_la_g%C3%A9n%C3%A9ralit%C3%A9_de_Catalogne",
                        },
                    }
                },
            }

    longitude = 41.3825
    latitude = 2.17694

    WIKI_API_URL = "https://fr.wikipedia.org/w/api.php?"

    payload = {
        "action": "query",
        "format": "json",
        "ggscoord": f"{longitude}|{latitude}",
        "generator": "geosearch",
        "prop": "extracts|info",
        "explaintext": True,
        "exsentences": 3,
        "inprop": "url",
    }

    def mock_get_wiki_info(WIKI_API_URL=WIKI_API_URL, payload=payload):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_wiki_info)

    request = Wikiwrapper()
    result = request.get_wiki_info_by_long_lat(longitude, latitude)
    expected_result = {
        "title": "Barcelone",
        "description": "Barcelone [baʁsəlɔn] (en catalan : "
                       "Barcelona [bərsəˈɫonə] ;",
        "url": "https://fr.wikipedia.org/wiki/Barcelone",
    }

    assert result == expected_result


def test_get_wiki_info_by_long_lat_with_failure(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response has failed
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"error": "bad"}

    longitude = 41.3825
    latitude = 2.17694

    WIKI_API_URL = "https://fr.wikipedia.org/w/api.php?"

    payload = {
        "action": "query",
        "format": "json",
        "ggscoord": f"{longitude}|{latitude}",
        "generator": "geosearch",
        "prop": "extracts|info",
        "explaintext": True,
        "exsentences": 3,
        "inprop": "url",
    }

    def mock_get_wiki_info(WIKI_API_URL=WIKI_API_URL, payload=payload):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_wiki_info)

    request = Wikiwrapper()
    result = request.get_wiki_info_by_long_lat(longitude, latitude)

    assert result is None
