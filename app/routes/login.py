from app import *
from app.controller import *
from flask import render_template, request, flash, redirect, make_response
import json

@app.route('/login.html', endpoint='render_login')
def render_login():
    return render_template('login.html')

@app.route('/login', endpoint='process_login', methods=['POST'])
def process_login():
    _username = request.form.get('username')
    _passwd = request.form.get('password')
    status = check_login(_username, _passwd)
    print(status)
    if status == True:
        res = make_response(json.dumps("Dang nhap thanh cong"))
        res.status_code = 200
        return res
    else:
        res = make_response(json.dumps("Nhap sai username hoac password"))
        res.status_code = 200
        return res

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/block_home.html')