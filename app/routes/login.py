from app import app
from flask import render_template

@app.route('/login.html', endpoint='render_login')
def render_login():
    return render_template('login.html')