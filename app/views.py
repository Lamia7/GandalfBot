"""
Module that contains routes
- routes: different URLs implemented by the app
- view function : functions that will handle app routes
- they are mapped to 1 or several URL routes so that Flask knows what to execute when a URL is requested
"""
from flask import render_template, jsonify, request

from app import app
from utils import change_to_upper


@app.route('/')  # view function with route URL
@app.route('/index')  # view function with 'index' as route URL
def index():
    # render_template change some elements ... param: variables
    return render_template('index.html', title='Accueil', message='coucou')


@app.route('/result', methods=["POST"])  # route will be accessed by POST method
def result():
    """Method result called when user submit his input that help us to retrieve data from JS to Python
    result view recieves an HTTP request and sends an HTTP response"""
    #user_input = request.form["user_input"]

    # object request allows me to access to data
    user_input = request.get_data('user_input').decode()  # decode unicode
    print(user_input)
    response = change_to_upper(user_input)  # treatment on data with function (making user input uppercase)
    return jsonify(response)  # jsonify is making json and puts it into an http response
    # return render_template('index.html', )


"""
Jinja2 remplace les {{ ... }} blocs par les valeurs correspondantes, 
données par les arguments fournis dans l'appel render_template()

jsonify fabrique du JSON et le met à l'intérieur d'une rep HTTP
json.dumps fabrique du JSON tout court

{{}}  : afficher qqchose
{% %} : utiliser du python
{# #} : intégrer un commentaire

garder fonctions de views très courtes (8 lignes maxi):
je récup l'info, je la traite en appelant fonction de traitement, je la renvoie
fonction de traitement ds un autre fichier: utils.py

"""
