from app import app
from flask import render_template

@app.route('/block_coursera.html', endpoint='render_course')
@login_required
def render_course():
    return render_template('block_coursera.html')