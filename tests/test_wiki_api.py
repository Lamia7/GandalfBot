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
                "continue": {
                    "excontinue": 1,
                    "continue": "||info"
                },
                "warnings": {
                    "extracts": {
                        "*": "\"exlimit\" was too large for a whole article extracts request, lowered to 1."
                    }
                },
                "query": {
                    "pages": {
                        "5211": {
                            "pageid": 5211,
                            "ns": 0,
                            "title": "Barcelone",
                            "index": -1,
                            "extract": "Barcelone [baʁsəlɔn] (en catalan : Barcelona [bərsəˈɫonə] ; en espagnol : Barcelona [baɾθeˈlona] ) est la capitale administrative et économique de la Catalogne, de la province de Barcelone, de la comarque du Barcelonès ainsi que de son aire et de sa région métropolitaines, en Espagne.\nBarcelone est la deuxième ville d'Espagne au regard de la population, de l'économie et des activités, la onzième ville la plus peuplée de l'Union européenne et la sixième en incluant sa banlieue : en 2018, 4,84 millions de personnes vivent dans l'agglomération barcelonaise. La majeure partie des municipalités adjacentes sont en outre rassemblées dans l'Aire métropolitaine de Barcelone.",
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-12-04T15:27:26Z",
                            "lastrevid": 177266993,
                            "length": 126214,
                            "fullurl": "https://fr.wikipedia.org/wiki/Barcelone",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Barcelone&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Barcelone"
                        },
                        "771897": {
                            "pageid": 771897,
                            "ns": 0,
                            "title": "Quartier gothique",
                            "index": 0,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-30T05:15:49Z",
                            "lastrevid": 166609677,
                            "length": 1799,
                            "fullurl": "https://fr.wikipedia.org/wiki/Quartier_gothique",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Quartier_gothique&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Quartier_gothique"
                        },
                        "1002545": {
                            "pageid": 1002545,
                            "ns": 0,
                            "title": "Cités et Gouvernements locaux unis",
                            "index": 1,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-21T12:53:55Z",
                            "lastrevid": 175119274,
                            "length": 12553,
                            "fullurl": "https://fr.wikipedia.org/wiki/Cit%C3%A9s_et_Gouvernements_locaux_unis",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Cit%C3%A9s_et_Gouvernements_locaux_unis&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Cit%C3%A9s_et_Gouvernements_locaux_unis"
                        },
                        "4082734": {
                            "pageid": 4082734,
                            "ns": 0,
                            "title": "Palais de la généralité de Catalogne",
                            "index": 2,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-12-04T09:54:43Z",
                            "lastrevid": 176243758,
                            "length": 4332,
                            "fullurl": "https://fr.wikipedia.org/wiki/Palais_de_la_g%C3%A9n%C3%A9ralit%C3%A9_de_Catalogne",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Palais_de_la_g%C3%A9n%C3%A9ralit%C3%A9_de_Catalogne&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Palais_de_la_g%C3%A9n%C3%A9ralit%C3%A9_de_Catalogne"
                        },
                        "4999522": {
                            "pageid": 4999522,
                            "ns": 0,
                            "title": "Place Sant Jaume",
                            "index": 3,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-10T03:20:25Z",
                            "lastrevid": 173863027,
                            "length": 2229,
                            "fullurl": "https://fr.wikipedia.org/wiki/Place_Sant_Jaume",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Place_Sant_Jaume&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Place_Sant_Jaume"
                        },
                        "5001673": {
                            "pageid": 5001673,
                            "ns": 0,
                            "title": "Femme (Miró)",
                            "index": 4,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-26T23:45:14Z",
                            "lastrevid": 156701811,
                            "length": 1246,
                            "fullurl": "https://fr.wikipedia.org/wiki/Femme_(Mir%C3%B3)",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Femme_(Mir%C3%B3)&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Femme_(Mir%C3%B3)"
                        },
                        "5086768": {
                            "pageid": 5086768,
                            "ns": 0,
                            "title": "Mairie de Barcelone",
                            "index": 5,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-21T13:24:54Z",
                            "lastrevid": 169661802,
                            "length": 6758,
                            "fullurl": "https://fr.wikipedia.org/wiki/Mairie_de_Barcelone",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Mairie_de_Barcelone&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Mairie_de_Barcelone"
                        },
                        "7234024": {
                            "pageid": 7234024,
                            "ns": 0,
                            "title": "Temple d'Auguste (Barcelone)",
                            "index": 6,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-30T05:25:28Z",
                            "lastrevid": 136954587,
                            "length": 3034,
                            "fullurl": "https://fr.wikipedia.org/wiki/Temple_d%27Auguste_(Barcelone)",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Temple_d%27Auguste_(Barcelone)&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Temple_d%27Auguste_(Barcelone)"
                        },
                        "11657084": {
                            "pageid": 11657084,
                            "ns": 0,
                            "title": "Archives municipales de Barcelone",
                            "index": 7,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-21T14:20:00Z",
                            "lastrevid": 148869286,
                            "length": 5330,
                            "fullurl": "https://fr.wikipedia.org/wiki/Archives_municipales_de_Barcelone",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Archives_municipales_de_Barcelone&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Archives_municipales_de_Barcelone"
                        },
                        "13065113": {
                            "pageid": 13065113,
                            "ns": 0,
                            "title": "Semaine du livre en catalan (Barcelone)",
                            "index": 8,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-11-21T14:32:16Z",
                            "lastrevid": 169418421,
                            "length": 3168,
                            "fullurl": "https://fr.wikipedia.org/wiki/Semaine_du_livre_en_catalan_(Barcelone)",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Semaine_du_livre_en_catalan_(Barcelone)&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Semaine_du_livre_en_catalan_(Barcelone)"
                        }
                    }
                }
            }

    longitude = 41.3825
    latitude = 2.17694

    WIKI_API_URL = "https://fr.wikipedia.org/w/api.php?"

    payload = {"action": "query",
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

    monkeypatch.setattr(requests, 'get', mock_get_wiki_info)

    request = Wikiwrapper()
    result = request.get_wiki_info_by_long_lat(longitude, latitude)
    expected_result = {
        'title': 'Barcelone',
        'description': "Barcelone [baʁsəlɔn] (en catalan : Barcelona [bərsəˈɫonə] ; en espagnol : Barcelona [baɾθeˈlona] ) est la capitale administrative et économique de la Catalogne, de la province de Barcelone, de la comarque du Barcelonès ainsi que de son aire et de sa région métropolitaines, en Espagne.\n"
                                             "Barcelone est la deuxième ville d'Espagne au regard de la population, de l'économie et des activités, la onzième ville la plus peuplée de l'Union européenne et la sixième en incluant sa banlieue : en 2018, 4,84 millions de personnes vivent dans l'agglomération barcelonaise. "
                                             "La majeure partie des municipalités adjacentes sont en outre rassemblées dans l'Aire métropolitaine de Barcelone.",
        'url': 'https://fr.wikipedia.org/wiki/Barcelone'}

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

    payload = {"action": "query",
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

    monkeypatch.setattr(requests, 'get', mock_get_wiki_info)

    request = Wikiwrapper()
    result = request.get_wiki_info_by_long_lat(longitude, latitude)

    assert result == None