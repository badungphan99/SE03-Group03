from app import app
from app.controller import *
from app.models import *
from flask import render_template, request, flash, redirect

@app.route('/teacher_home', endpoint='teacher_home')
def teacher_home():
    courses = get_all_teacher_course_by_user_id(current_user.id)
    course = {
        "course": [
        ]
    }
    for cs in courses:
        tcs = get_techercourse_of_courseID(cs.id)
        tc = ""
        # print (tcs)
        for name in tcs:
            tc = tc + str(name)[2:-3] + ","
        course['course'].append({
            "id": cs.id,
            "title": cs.title,
            "topic_id": cs.topic_id,
            "description": cs.description,
            "create_date": cs.create_date,
            "duration": cs.duration,
            "techer_course": tc[:-1],
            "link": "/course/" + str(cs.id)
        })
    return render_template('teacher-home.html', course=course, lencourses=len(courses))

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
    insert_teacher_course(current_user.id, _name_course, _des, _duration, _topic)
    return redirect('/teacher_home')