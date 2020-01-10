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
            "link": "/change-course/" + str(cs.id)
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

@app.route('/change-course/<string:courseID>', endpoint="change_course", methods=['GET', 'POST'])
def change_course(courseID):
    # topic, length = learning()
    # course = get_course_by_courseID(courseID)
    lessons = get_lesson_by_course_id(courseID)
    print (lessons)
    lesson = {
        "lesson" : [
        ]
    }
    for ls in lessons :
        lesson['lesson'].append({
            'title' : ls.title,
            'content' : ls.content,
            'change' : "/change-lesson/" + str(courseID) + '/lesson=' + str(ls.id),
            'del' : "/del-lesson/" + str(ls.id)
        })
    # course_js = {
    #     "title" : course.title,
    #     "description" : course.description
    # }
    #
    lenlesson = len(lessons)
    return render_template('teacher_addcourse_listitem.html', lesson=lesson, lenlesson=lenlesson)

@app.route("/teacher_add_lession")
def render_addlis():
    return render_template("teacher_addcourse_item.html")

