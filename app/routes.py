"""
Module that contains routes
- routes: different URLs implemented by the app
- view function : functions that will handle app routes
- they are mapped to 1 or several URL routes so that Flask knows what to execute when a URL is requested
"""
from app import app


@app.route('/')  # view function with route URL
@app.route('/index')  # view function with 'index' as route URL
def index():
    return "Hello, welcome to GandalfBot!"