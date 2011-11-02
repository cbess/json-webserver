# http://werkzeug.pocoo.org/docs/serving/#werkzeug.serving.run_simple
import flask
import webapp.settings

app = flask.Flask('webapp')
app.config.from_object('webapp.settings')

import views

def run():
    """Runs the flask server
    """
    # dev or low traffic
    app.run()
    pass