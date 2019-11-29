from app import app
from flask import render_template, make_response, request
import json
from app.controller import *

@app.route('/block_course.html', endpoint='render_course')
def render_course():
    topic = get_topic()
    return render_template('block_course.html')

@app.route("/testajax", methods=['POST'])
def ajaxtest():
    topic = ["Business", "Computer Science", "Data Science", "Information Technology", "Social Sciences"]
    data = request.form
    resp = make_response(json.dumps(data))
    resp.status_code = 200
    return resp

@app.route("/testajax.html")
def ajaxtest1():
    return render_template('testajax.html')