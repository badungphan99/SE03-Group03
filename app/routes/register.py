from app import app
from app.controller import *
from flask import render_template, request, flash, redirect

@app.route('/register.html', endpoint='render_register')
def render_register():
    return render_template('register.html')

@app.route('/register', endpoint='register', methods=['POST'])
def register():
    _username = request.form.get('username')
    _passwd = request.form.get('password')
    _retype_passwd = request.form.get('retypepassword')
    _full_name = "dungpb"
    _email = request.form.get('email')
    _birthday = request.form.get('birthday')
    _type_account = 'student'
    _highest_degree = ''
    _university = ''
    _major = ''

    status = check_input_register(_username, _passwd, _retype_passwd, _full_name, _email)

    if(status == True):
        if (check_user_name(_username)):
            flash("username already exist")
            return redirect('/register.html')
        else:
            insert_new_user(_type_account, _username, _passwd, _full_name, _email, _birthday, _highest_degree, _university, _major)
            flash("success")
            return render_template('register.html')
    else:
        flash(status)
        return redirect('/register.html')