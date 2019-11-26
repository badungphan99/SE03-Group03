from app import db
from sqlalchemy.sql import func

__all__ = ["Forum", "Post"]
class Forum(db.Model):
    __tablename__ = 'forum'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    posts = db.relationship('Post', backref='forum', lazy='dynamic')

    def __init__(self, course_id=-1):
        self.course_id = course_id

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.String(250), unique=True, nullable=False)
    create_date = db.Column(db.DateTime(timezone=True), default=func.now())
    is_active = db.Column(db.Boolean, default=1)

    def __init__(self, forum_id, topic_id, title, content):
        self.forum_id = forum_id
        self.topic_id = topic_id
        self.title = title
        self.content = content



