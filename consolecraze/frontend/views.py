import json
from flask import Blueprint, request, render_template, flash, g, session, \
        redirect, url_for, current_app, jsonify

from consolecraze import articlesModule

mod = Blueprint('frontend', __name__,)


def get_json_response(view_name, *args, **kwargs):
    view = current_app.view_functions[view_name]
    res = view(*args, **kwargs)
    js =  json.loads(res.data)
    return js

@mod.route("/")
def index():
    #js = get_json_response('articlesModule.articles')
    print(dir(url_for('articlesModule.articles')))
    return "Hello"
