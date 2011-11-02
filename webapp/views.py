# -*- coding: utf-8 -*-
# refs: http://flask.pocoo.org/docs/quickstart/#redirects-and-errors

import os
from flask import render_template, request, abort, Response
from server import app
from ipdb import set_trace


def pprint(value):
    """Pretty print for the specified value
    http://docs.python.org/library/pprint.html
    """
    import pprint
    return pprint.pprint(value)
    

@app.route('/')
def index():
    """Handles index requests
    """
    response = {
        "title" : u"Welcome"
    }
    return render_template('index.html', **response)
    
    
@app.route('/json')
def json_view():
    headers = request.headers
    # get form vars
    if request.method == 'POST':
        form = request.form
    else:
        form = request.args
    set_trace()
    return Response('{"error" : 0 }', mimetype='application/json')