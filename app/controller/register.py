from app.models import *
from app import db

def check_user_name(username):
    user = db.session.query(User).filter(User.username.like(username)).first()
    if(user):
        return 1
    else:
        return 0

def check_input_register(username, password, retypepassword, fullname, email):
    
    #check username
    if username == None:
        return "Nhap username"
    for c in username:
        if ord(c) < 97 or ord(c) > 119:
            return "username khong duoc co ky tu dac biet"

    #check pass
    if len(password) < 8 or password == None:
        return "Mat khau phai tren 8 ky tu"
    if password != retypepassword:
        return "Mat khau khac nhau, nhap lai"
    
    #check full name
    if fullname == None:
        return "Nhap ten"
    for c in fullname:
        if ord(c) < 97 or ord(c) > 119:
            return "Ten khong duoc co ky tu dac biet"

    #check email
    cntA = 0
    cntD = 0
    for c in email:
        if c == '@':
            cntA = cntA+1
        if c == '.':
            cntD = cntD+1
    if cntA != 1 and cntD != 1:
        return "Nhap sai email"
    
    return True

def insert_new_user(type_user, username, passwd, fullname, email, birthday = None, highest_degree = None, university = None, major = None):
    type_account = TypeAccount(type_user)
    user = User(username, passwd, fullname, email)
    # type_account.users.append(user)
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    print(check_input_register("asfkjasfw", "asfasfasf", "asfasfasf", "wiofoasdaswfowfw", "ashaksfha@k.jsfhwf"))