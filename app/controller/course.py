from app.models import *
from app import db

def learning():
    topics = get_topic()

    result = {
        "topic" : []
    }
    for tp in topics :
        result["topic"].append({
            "name" : tp.topic_name,
            "link" : "/Learning/" + str(tp.id)
        })
    return result, len(topics)

def get_topic():
    topic = Topic.query.all()
    return topic

def get_course_by_courseID(courseId):
    courses = db.session.query(Course).filter(Course.id == courseId).first()
    return courses

def get_course():
    return Course.query.all()

def get_list_course_by_topic_id(topic_id):
    # topic = db.session.query(Topic).filter(Topic.topic_name.like(username)).first()
    courses = db.session.query(Course).filter(Course.topic_id == topic_id).all()
    return courses

def get_techercourse_of_courseID(courseId):
    userTeacher = db.session.query(User.fullname).join(TeacherCourse).join(Course).filter(Course.id == courseId).all()
    return userTeacher