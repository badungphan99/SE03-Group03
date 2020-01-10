from app.models import *
from app import db

def insert_teacher_course(user_id,_name_course, _des, _duration, _topic):
    print(user_id)
    print(_topic)
    print(_name_course)
    course1 = Course(_name_course, _des, _duration)
    topic = db.session.query(Topic).filter(Topic.id == _topic).first()
    print(topic.topic_name)
    user = db.session.query(User).filter(User.id == user_id).first()
    # # print(topic)
    # # print()

    teachCourse = TeacherCourse()
    teachCourse.course = course1
    user.courses.append(teachCourse)
    db.session.add(course1)
    db.session.commit()

    topic.coursers.append(course1)
    db.session.commit()






