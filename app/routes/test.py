from app import *
from flask import render_template, session


@app.route('/test', endpoint='render_test')
@login_required
def render_test():
    return current_user.id
