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

### Checklist
- [x] Initialize flask app
- [ ] Create templates folder for templates organization
- [ ] Create index.html template
- [ ] Create base.html in template folder
- [ ] Add bot presentation with picture and title 
- [ ] Add input text field for the questions 
- [ ] Add input button to send questions 
- [ ] Add footer with name and github link
- [ ] Create static folder for style organisation
- [ ] Add style for elements on index template
- [ ] Add style link to base.html
- [ ] Create partials folder for forms
- [ ] Add _form.html to partials folder