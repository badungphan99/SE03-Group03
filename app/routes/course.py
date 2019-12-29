from app import app
from flask import render_template, make_response, request
from flask import render_template, session, jsonify, request, json
import json
from app.controller import *

@app.route('/block_course.html', endpoint='render_course')
def render_course():
    topic = get_topic()
    return render_template('block_course.html')

@app.route('/block_learncourse.html', endpoint='render_learncourse')
def render_learncourse():
    topic = get_topic()
    return render_template('block_learncourse.html')

@app.route('/block_topic.html', endpoint='render_topic')
def render_topic():
    topic = get_topic()
    return render_template('block_topic.html')

@app.route('/learning', endpoint='learning', methods=['GET', 'POST'])
def learning():
    topics = get_topic()
    
    result = {
        "topic" : []
    }
    for tp in topics :
        result["topic"].append({
            "name" : tp.topic_name,
            "link" : "/Learning/" + str(tp.id)
        })
    return jsonify(result)

@app.route('/Learning/<int:id>', endpoint='render_learning', methods=['GET', 'POST'])
def render_learning(id):
    courses = get_list_course_by_topic_id(id)
    print ("len courses " , len(courses))
    return render_template("login.html")

@app.route("/testajax.html")
def ajaxtest1():
    return render_template('testajax.html')