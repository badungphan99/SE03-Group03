from app.models import *
from app import db

def get_topic():
    topic = Topic.query.all()
    return topic

def get_list_course_by_topic_id(topic_id):
    # topic = db.session.query(Topic).filter(Topic.topic_name.like(username)).first()
    courses = db.session.query(Course).filter(Course.topic_id.like(topic_id)).all()
    return courses