from app import app
from flask import render_template

@app.route('/', endpoint='render_root')
def render_root():
    return render_template('block_home.html')

@app.route('/block_home.html', endpoint='render_home')
def render_home():
    return render_template('block_home.html')
