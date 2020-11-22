# GandalfBot 
using Flask

### Installation and configuration

**Clone the repository from Github by running this command:**
```git clone https://github.com/Lamia7/GandalfBot```

**Execute with a virtual environment:**

Create a virtual environment: `virtualenv -p python3.7 venv` <br>
Activate the virtual environment: `source venv/bin/activate` <br>
_Install all the libraries through the requirements file: `pip3 install -r requirements.txt` <br>_
Run the application: `python3 GandalfBot/gandalfbot.py`

(To deactivate the virtual environment, run this command: `deactivate`)

### How does it work ?
__(HTML)__ : User asks question on input and submit it <br>
__(JS)__  : gets (récupère) this input <br>
__(JS)__ : makes a request to API route to pass it to back-end <br>
__(PYTHON)__ : API gets/retrieves the JS info  <br>
__(PYTHON)__ : API sends the request to Wikipedia API <br>
__(PYTHON)__ : Wikipedia API gives the response to my API's request <br>
__(PYTHON)__ : API recieves response from Wikipedia API <br>
__(PYTHON)__ : API sends the response to front: JS <br>
__(JS)__ : sends response to HTML <br>
__(HTML)__ : shows reply

### Fonctionnalités
+ Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
+ Données via l'API de Google Maps et celle de Media Wiki.
+ Si l'utilisateur charge de nouveau la page, tout l'historique est perdu, pas de sauvegarde.
+ Possibilité d'inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation.

### Checklist
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
- [x] Add parser to analyze question 
- [x] Make request to wikimedia API
- [ ] Use parser on user_input
- [x] Retrieve wikimedia API response and send it to front
- [ ] Retrieve map with coordinates according to user's question
- [ ] Create partials folder for forms
- [ ] Add _form.html to partials folder
- [ ] Improve style (input, responsive, font, sizes...)
- [ ] Resize avatar image when smaller screen (responsive)

- [ ] Add image as future button (optional)
- [ ] Use regex optional
