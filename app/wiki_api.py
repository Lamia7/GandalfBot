"""
Module to get data from the Wikimedia API
"""

import requests

from configuration.config import WIKI_API_URL


class Wikiwrapper:
    """Represents the Wikimedia API"""

    def get_wiki_info_by_long_lat(self, longitude, latitude):
        """Gets the title, description and url info from Wiki API
        according to the given coordinates"""
        payload = {"action": "query",
                   "format": "json",
                   "ggscoord": f"{longitude}|{latitude}",
                   "generator": "geosearch",
                   "prop": "extracts|info",
                   "explaintext": True,  # convert HTML to plain text
                   "exsentences": 3,  # how many sentences to return
                   "inprop": "url",  # get url (added info to prop for this)
                   }

        # variable contains request result
        result = requests.get(WIKI_API_URL, payload)

        # if request works
        if result.status_code == 200:
            json_result = result.json()  # jsonify the results
            if 'query' in json_result:
                pages = json_result['query']['pages']  # access to pages
                pages = (list(pages.values()))

                # Get the infos needed
                title = pages[0]['title']  # get title's value from first dict
                description = pages[0]['extract']  # get extract's value
                url = pages[0]['fullurl']  # get wikipedia link

                # Return a json
                wiki_details = {
                    "title": title,
                    "description": description,
                    "url": url
                }

                return wiki_details
