from app import *
from app.controller import *
from flask import render_template, request, flash, redirect, url_for

@app.route('/login.html', endpoint='render_login')
def render_login():
    return render_template('login.html')

@app.route('/login', endpoint='process_login', methods=['POST', 'GET'])
def process_login():
    _username = request.form.get('username')
    _passwd = request.form.get('password')
    
    status = check_login(_username, _passwd)
    if status == True:
        if(current_user.type_id == 2):
            return redirect('block_course.html')
        if(current_user.type_id == 1):
            return redirect('teacher_home')
        # session['username'] = _username
    flash(status)
    return redirect('/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')