import os
from flask import render_template, request
from app import create_app
app = create_app(os.getenv('FLASK_CONFIG'))

@app.route('/')
#@app.route('/hello')# URL '/' to be handled by main() route handler (or view function)
def main():
    """Say hello"""
    # return render_template('j2_query.html')
    return render_template('bock_login.html')


@app.route('/processmm', methods=['POST'])
def process():
    # return "HELLO"
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  # get(attr) returns None if attr is not present


    # Validate and send response
    if _username:
        print(_username)
        # print(_password)
        return render_template('block_home.html', username=_username)
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


if __name__ == '__main__':
    app.run()