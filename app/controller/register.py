from app.models import *
from app import db

def check_user_name(username):
    user = db.session.query(User).filter(User.username.like(username)).first()
    if(user):
        return 1
    else:
        return 0

def insert_new_user(type_user, username, passwd, fullname, email, birthday = None, highest_degree = None, university = None, major = None):
    type_account = TypeAccount(type_user)
    user = User(username, passwd, fullname, email)
    # type_account.users.append(user)
    db.session.add(user)
    db.session.commit()