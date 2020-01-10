from app import app
from flask import render_template, make_response, request
from flask import render_template, session, jsonify, request, json
import json
from app.controller import *

@app.route('/block_course.html', endpoint='render_course')
def render_course():
    # print(current_user.id)
    topic, length = learning()
    courses = get_course()
    course = {
        "course" : [
        ]
    }
    lencourses = len(courses)
    for cs in courses:
        tcs = get_techercourse_of_courseID(cs.id)
        tc = ""
        # print (tcs)
        for name in tcs:
            tc = tc + str(name)[2:-3] + ","
        course['course'].append({
            "id" : cs.id,
            "title" : cs.title,
            "topic_id" : cs.topic_id,
            "description" : cs.description,
            "create_date" : cs.create_date,
            "duration" : cs.duration,
            "techer_course" : tc[:-1],
            "link" : "/course/" + str(cs.id)
        })
    return render_template('block_course.html', topic= topic, len=length, course=course, lencourses=lencourses)

@app.route('/block_learncourse.html', endpoint='render_learncourse')
def render_learncourse():
    topic, length = learning()
    courses = get_course()

    return render_template('block_learncourse.html', topic= topic, len=length)

@app.route('/block_topic.html', endpoint='render_topic')
def render_topic():
    topic, length = learning()
    courses = get_course()
    course = {
        "course" : [
        ]
    }
    for cs in courses:
        tc = get_techercourse_of_courseID(cs.id)
        course['course'].append({
            "id" : cs.id,
            "title" : cs.title,
            "topic_id" : cs.topic_id,
            "description" : cs.description,
            "create_date" : cs.create_date,
            "duration" : cs.duration,
            "techer_course" : tc
        })
    return render_template('block_topic.html', topic= topic, len=length, course=course)

@app.route('/Learning/<int:id>', endpoint='render_learning', methods=['GET', 'POST'])
def render_learning(id):
    topic, length = learning()
    courses = get_list_course_by_topic_id(id)
    course = {
        "course" : [
        ]
    }
    lencourses = len(courses)
    for cs in courses:
        tcs = get_techercourse_of_courseID(cs.id)
        tc = ""
        # print (tcs)
        for name in tcs:
            tc = tc + str(name)[2:-3] + ","
        course['course'].append({
            "id" : cs.id,
            "title" : cs.title,
            "topic_id" : cs.topic_id,
            "description" : cs.description,
            "create_date" : cs.create_date,
            "duration" : cs.duration,
            "techer_course" : tc[:-1],
            "link" : "/course/" + str(cs.id)
        })
    varLogin="/login.html"
    varSignUp = "/register.html"
    myCourse = "/block_mycourse.html"
    varLogout = "/logout"
    return render_template('block_topic.html', topic= topic, len=length, course=course, lencourses=lencourses, varLogin=varLogin, varSignUp=varSignUp, myCourse=myCourse, varLogout=varLogout)


@app.route('/course/<string:courseID>', endpoint="testvar", methods=['GET', 'POST'])
def testvar(courseID):
    topic, length = learning()
    course = get_course_by_courseID(courseID)
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
            'link' : "/course/" + str(courseID) + '/lesson=' + str(ls.id)
        })
    course_js = {
        "title" : course.title,
        "description" : course.description
    }

    lenlesson = len(lessons)
    return render_template('block_learncourse.html', topic= topic, len=length, lesson=lesson, lenlesson=lenlesson, course=course_js)

@app.route("/block_mycourse.html")
@login_required
def viewCourse():
    topic, length = learning()
    courses = get_all_student_course_by_user_id(current_user.id)
    
    course = {
        "course" : [
        ]
    }
    for cs in courses:
        tcs = get_techercourse_of_courseID(cs.id)
        tc = ""
        # print (tcs)
        for name in tcs:
            tc = tc + str(name)[2:-3] + ","
        course['course'].append({
            "id" : cs.id,
            "title" : cs.title,
            "topic_id" : cs.topic_id,
            "description" : cs.description,
            "create_date" : cs.create_date,
            "duration" : cs.duration,
            "techer_course" : tc[:-1],
            "link" : "/course/" + str(cs.id)
        })
    return render_template('block_mycourse.html', topic= topic, len=length, course=course, lencourses=len(courses))

@app.route('/course/<string:courseID>/lesson=<string:lessonID>', endpoint="render_lesson", methods=['GET', 'POST'])
def render_lesson(courseID, lessonID):
    topic, length = learning()
    ls = get_lesson_by_ID(lessonID)
    lesson = {
        'title' : ls.title,
        'content' : ls.content 
    }
    print(lesson)
    return render_template("block_course_item.html", topic=topic, len=length, lesson=lesson)