from app import app
from flask import render_template
from flask import render_template, session, jsonify, request, json

from app.controller import *

@app.route('/', endpoint='render_root')
def render_root():
    return render_template('block_home.html')

@app.route('/block_home.html', endpoint='render_home')
def render_home():
    topic, length = learning()
    courses = get_course()

    course = {
        "course" : []
    }
    
    for cs in courses:
        tcs = get_techercourse_of_courseID(cs.id)
        tc = ""
        # print (tcs)
        for name in tcs:
            tc = tc + str(name)[2:-3] + ","
        course['course'].append({
            "id" : cs.id,
            "title" : cs.title,
            "topic_id" : cs.topic_id,
            "description" : cs.description,
            "create_date" : cs.create_date,
            "duration" : cs.duration,
            "techer_course" : tc[:-1],
            "link" : "/course/" + str(cs.id)
        })
    return render_template('block_home.html', topic= topic, len=length, course=course)
