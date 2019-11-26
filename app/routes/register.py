from app import app
from flask import render_template

@app.route('/register.html', endpoint='render_register')
def render_register():
    return render_template('register.html')