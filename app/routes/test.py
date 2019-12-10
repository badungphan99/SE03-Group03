from app import *
from flask import render_template, session, jsonify, request, json


@app.route('/test', endpoint='render_test')
@login_required
def render_test():
    return current_user.id

@app.route('/testajaxxx', endpoint='test_ajax', methods=['GET', 'POST'])
def test_ajax():
    a = {
        "topic" : [{
                "name" : "Arts and Humanities",
                "link" : "login.html"
            },
            {
                "name":"xzcdsfdx",
                "link":"login.html"
            }
        ]
    }
    return jsonify(a)