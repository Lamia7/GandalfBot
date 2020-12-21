"""
Module that contains views of the app.
"""
from flask import render_template, request

from app import app
from app.geo_api import GeoWrapper
from app.parser import Parser

from app.wiki_api import Wikiwrapper


@app.route("/")  # view function with route URL
@app.route("/index")  # view function with 'index' as route URL
def index():
    # render_template change some elements ... param: variables
    return render_template("index.html", title="Accueil")


@app.route("/result", methods=["POST"])  # route will be accessed by POSTmethod
def result():
    """Method result called when user submit his input that help us
    to retrieve data from JS to Python
    result view recieves an HTTP request and sends an HTTP response"""

    # object request allows me to access to data
    user_input = request.get_data("user_input").decode()  # decode unicode

    # Get coordinates
    parser = Parser(user_input)
    geowrapper = GeoWrapper(parser.parsed_input)

    # If one coord missing, stop here return error
    if geowrapper.latitude is None or geowrapper.longitude is None:
        return {"content": "Missing coordinates"}

    # If coordinates, get wiki infos
    wikiwrapper = Wikiwrapper()
    wiki_details = wikiwrapper.get_wiki_info_by_long_lat(
        geowrapper.longitude, geowrapper.latitude
    )
    if wiki_details is None:
        return {"content": "No wiki details found"}
    else:
        return {
            "description": wiki_details["description"],
            "url": wiki_details["url"],
            "longitude": geowrapper.longitude,
            "latitude": geowrapper.latitude,
        }


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
