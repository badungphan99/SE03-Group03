from app import *
from flask import render_template, session, jsonify, request


@app.route('/test', endpoint='render_test')
@login_required
def render_test():
    return current_user.id

@app.route('/testajaxxx', endpoint='test_ajax', methods=['GET', 'POST'])
def test_ajax():
    _username = request.form.get('username')
    _passwd = request.form.get('password')
    
    return jsonify('message')