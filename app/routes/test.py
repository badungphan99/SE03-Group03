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
                "name":"ủeuqgoqwufq",
                "link":"login.html"
            }
        ]
    }
    return jsonify(a)

@app.route('/testajaxxx/<int:id>', endpoint='render_testxxx', methods=['GET', 'POST'])
def render_testxxx(id):
    id = 1
    return render_template("login.html")
