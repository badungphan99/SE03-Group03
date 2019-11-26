from app import app
from flask import render_template

@app.route('/', endpoint='render_home')
def render_home():
    return render_template('block_home.html')
