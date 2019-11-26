from manage import app
from flask import render_template

@app.route('/')
def render():
    return render_template('block_home.html')

@app.route('/register.html')
def render():
    return render_template('register.html')