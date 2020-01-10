from app import app
from app.controller import *
from flask import render_template, request, flash, redirect

@app.route('/teacher_home', endpoint='teacher_home')
def teacher_home():
    return render_template('teacher-home.html')

@app.route('/add_course', endpoint='add_course')
def add_course():
    topic, len = learning()
    print(topic)
    return render_template('teacher_addcourse.html', topic=topic, len=len)

@app.route('/insert_course', endpoint='insert_course', methods=["POST"])
def insert_course():
    _name_course = request.form.get('DisplayName')
    _topic = request.form.get('topicvalue')
    _des = request.form.get('descourse')
    _duration = request.form.get('thoiluong')
    course = Course(_name_course, _des, _duration)

    topic = db.session.query.(Topic).filter(Topic.id == topicId).first()
    if topic:
        topic.coursers.append(course)
    print(course.title)
    print(course.description)
    print(course.duration)
    db.session.add(course)
    db.session.commit()
    return render_template('teacher_addcourse_listitem.html')