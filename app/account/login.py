import os
from flask import render_template, request
from app import create_app, db
from app.models import User
from sqlalchemy import and_
app = create_app(os.getenv('FLASK_CONFIG'))

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  # get(attr) returns None if attr is not present
    _password = request.form.get('password')

    # Validate and send response
    if _username and _password:
        user1 = db.session.query(User).filter(and_(User.username.like(_username), User.password.like(_password))).first()
        if user1:
            return render_template('block_course.html')
        else:
            return "Not find", 400
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request

if __name__ == '__main__':
    app.run()