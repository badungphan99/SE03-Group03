from app import db
from sqlalchemy.sql import func

__all__ = ["Course" , "Topic", "TeacherCourse", "Section" , "StudentCourse"]
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    description = db.Column(db.String(250), nullable=False)
    create_date = db.Column(db.DateTime(timezone=True), default=func.now())
    duration = db.Column(db.Integer)
    students = db.relationship('StudentCourse', backref='course', lazy='dynamic')
    sections = db.relationship('Section', backref='course', lazy='dynamic')
    # relationship one to one
    forum = db.relationship('Forum', uselist=False, backref='course')

    users = db.relationship('TeacherCourse', back_populates='course')

    def __init__(self, title, description, topic, duration):
        self.title = title
        self.description = description
        self.duration = duration
        self.topic_id = topic

class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(200), unique=True)
    coursers = db.relationship('Course', backref='topic', lazy='dynamic')

    def __init__(self, topic_name):
        self.topic_name = topic_name


class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    enroll_date = db.Column(db.DateTime(timezone=True), default=func.now())
    finish_date = db.Column(db.DateTime)
    total_grade = db.Column(db.Float)
    studentquizs = db.relationship('StudentQuiz', backref='student_course', lazy='dynamic')

    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id


class TeacherCourse(db.Model):
    __tablename__ = 'teacher_course'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

    user = db.relationship('User', back_populates="courses")
    course = db.relationship('Course', back_populates="users")


class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.String(250), unique=True, nullable=False)
    quizs = db.relationship('Quiz', backref='section', lazy='dynamic')

    def __init__(self, course_id, title, content):
        self.course_id = course_id
        self.title = title
        self.content = content
