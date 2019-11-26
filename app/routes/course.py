from manage import app
from flask import render_template

@app.route('/block_coursera.html')
def render():
    return render_template('block_coursera.html')