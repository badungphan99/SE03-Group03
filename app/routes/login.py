from manage import app
from flask import render_template

@app.route('/login.html')
def render():
    return render_template('login.html')