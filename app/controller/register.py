import os
from flask import render_template, request
from app import create_app
app = create_app(os.getenv('FLASK_CONFIG'))

@app.route('/')
def main():
    return render_template('block_home.html')

@app.route('/register.html')
def render():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    _username = request.form.get('username')
    _passwd = request.form.get('password')
    _email = request.form.get('email')
    _birthday = request.form.get('birthday')
    # _typeaccount = request.form.get('typeaccount')
    print(_username, _passwd, _email, _birthday)



    return False

if __name__ == '__main__':
    app.run()