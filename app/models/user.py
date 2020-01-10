from app import db, UserMixin
from sqlalchemy.sql import func

__all__ = ["User", "TypeAccount"]
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date)
    highest_degree = db.Column(db.String(250))
    university = db.Column(db.String(250))
    major = db.Column(db.String(250))
    create_date = db.Column(db.DateTime(timezone=True), default=func.now())
    is_verified = db.Column(db.Boolean, default=0)
    is_active = db.Column(db.Boolean, default=1)

    type_id = db.Column(db.Integer, db.ForeignKey('type_account.id'))
    students = db.relationship('StudentCourse', backref='user', lazy='dynamic')
    file_uploads = db.relationship('FileUpload', backref='user', lazy='dynamic')

    courses = db.relationship('TeacherCourse', back_populates='user')

    studentCourses = db.relationship('StudentCourse', back_populates='user2')

    def __init__(self, username, password, fullname, email, birthday = None, highest_degree = None, university = None, major = None):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.date_of_birth = birthday
        self.highest_degree = highest_degree
        self.university = university
        self.major = major

class TypeAccount(db.Model):
    __tablename__ = 'type_account'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), unique=True)
    users = db.relationship('User', backref='type_account', lazy='dynamic')

    def __init__(self, type_name):
        self.type_name = type_name

