# GandalfBot 🤖
[Trello](https://trello.com/b/KUVhH5KI/p7-cr%C3%A9ez-grandpy-bot-le-papy-robot)<br>
Program only available in French for now.

***How to play ?***

Click here to try it and enjoy : 🤖 [Let's play](https://gandalf-bot-oc.herokuapp.com/) 👴

### Context
GandalfBot is a school project to practice the use of Python, Flask, JavaScript and APIs.

Ask him a question about a place and he will look for informations, Wikipedia URL and a map.

### Installation and configuration 💻

**Clone the repository from Github by running this command:**
```git clone https://github.com/Lamia7/GandalfBot```

**Execute with a virtual environment:**

Create a virtual environment: `virtualenv -p python3.7 venv` <br>
Activate the virtual environment: `source venv/bin/activate` <br>
_Install all the libraries through the requirements file: `pip3 install -r requirements.txt` <br>_
Run the application: `flask run` and go to your localhost : `http://127.0.0.1:5000/`

(To deactivate the virtual environment, run this command: `deactivate`)

### How does it work ?
__(HTML)__ : User asks question on input and submit it <br>
__(JS)__  : gets (récupère) this input <br>
__(JS)__ : makes a request to API route to pass it to back-end <br>
__(PYTHON)__ : API gets/retrieves the JS info  <br>
__(PYTHON)__ : API sends the request to Mapbox API <br>
__(PYTHON)__ : API recieves coordinates with response from Mapbox API <br>
__(PYTHON)__ : API sends the request containing coordinates to Wikipedia API <br>
__(PYTHON)__ : Wikipedia API gives the response to my API's request (description and URL)<br>
__(PYTHON)__ : API recieves response from Wikipedia API <br>
__(PYTHON)__ : API sends the response to front: JS <br>
__(JS)__ : sends response to HTML <br>
__(HTML)__ : shows reply

### Features 📋
+ Interactions in AJAX : user sends question by hitting enter or clicking on button and the query is displayed on the screen without refreshing the page.
+ Data retrieved from geolocation API and Media Wiki API.
+ If user refreshes the page, history gets deleted without saving it.
+ Possibility to invent different replies from the Bot, but this is optional.

### Checklist 📝
- [x] Initialize flask app
- [x] Create templates folder for templates organization
- [x] Create index.html template
- [x] Add bot presentation with place for picture and title
- [x] Create base.html in template folder and structure block extends
- [x] Add footer with name and github link
- [x] Create static folder for style organisation
- [x] Add image as bot avatar
- [x] Add form input text field for the questions
- [x] Add input button to send questions
- [x] Add social network icons
- [x] Add style for elements on index template
- [x] Add style link to base.html
- [x] Add route to access with POST method (when question is submitted)
- [x] Get question asked (from front to back-end)
- [x] Add parser to analyze question + tests
- [x] Make request to wikimedia API + tests
- [x] Use parser on user_input
- [x] Retrieve wikimedia API response and send it to front
- [x] Retrieve map with coordinates according to user's question + tests
- [x] Display bot replies to chatbox
- [x] Hide previous response but with scrolling option
- [x] Add spinner before bot replies
- [x] Improve style (input, responsive, font, sizes...)
- [x] Added html page (for error 404)
- [x] Check PEP8 with 'flake8' library and reformat with 'black' library
- [x] Format HTML, CSS and JS files

### Ressources used to create this program 🔧
***BACK***
- Language : Python 3.7
- Framework : Flask
- Testing library : pytest

***FRONT***
- Languages : Javascript, HTML5 & CSS3
- Frameworks : Bootstrap 4, jQuery

***EXTERNAL RESSOURCES***
- [Mapbox API](https://www.mapbox.com/)
- [MediaWiki/Wikipedia API](https://www.mediawiki.org/wiki/MediaWiki)
- Map provider : [Leaflet](https://leafletjs.com/)
- Icons : [Flaticon](https://www.flaticon.com/)

- Web server /  HTTP server : [Gunicorn](https://gunicorn.org/)

And a lot of research ...

### Author 📝
[Lamia EL RALIMI](https://github.com/Lamia7)