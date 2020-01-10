from app.models import *
from app import db

def insert_teacher_course(user_id,_name_course, _des, _duration, _topic):
    course = Course(_name_course, _des, _duration)
    topic = db.session.query(Topic).filter(Topic.id == _topic).first()
    user = db.session.query(User).filter(User.id == user_id).first()

    if topic:
        topic.coursers.append(course)

    if user:
        teachCourse = TeacherCourse()
        teachCourse.course = course
        user.courses.append(teachCourse)

    db.session.add(course)
    db.session.commit()

