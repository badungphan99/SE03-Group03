from app import app
from flask import render_template
from flask import render_template, session, jsonify, request, json

from app.controller import *

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
    return result, len(topics)

@app.route('/', endpoint='render_root')
def render_root():
    return render_template('block_home.html')

@app.route('/block_home.html', endpoint='render_home')
def render_home():
    topic, length = learning()
    
    return render_template('block_home.html', topic= topic, len=length)
