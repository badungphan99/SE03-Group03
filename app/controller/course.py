from app.models import *
from app import db

def get_topic():
    topic = Topic.query.all()
    return topic