from app.models import *
from app import *
from sqlalchemy import and_

def check_login(_username, _password):
    user1 = db.session.query(User).filter(and_(User.username.like(_username), User.password.like(_password))).first()
    if user1:
        login_user(user1)
        return True
    else:
        return "Sai username hoac password"