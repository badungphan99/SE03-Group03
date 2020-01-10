from app.models import *
from app import db

def insert_teacher_course(_name_course, _des, _duration, _topic):
    course = Course(_name_course, _des, _duration)
    topic = db.session.query(Topic).filter(Topic.id == _topic).first()
    if topic:
        topic.coursers.append(course)
    db.session.add(course)
    db.session.commit()