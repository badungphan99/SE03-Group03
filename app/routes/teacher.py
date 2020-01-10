from app import app
from app.controller import *
from app.models import *
from flask import render_template, request, flash, redirect

import os
from app import app
from app.controller import *
from flask import render_template, request, flash, redirect, send_from_directory, send_file
from werkzeug.utils import secure_filename
import urllib.request
from dotenv import load_dotenv

from datetime import datetime

load_dotenv(dotenv_path='./env/data_upload.env')
COURSE_DOCUMENT = os.getenv('COURSE_DOCUMENT')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = COURSE_DOCUMENT
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    print(courseID)
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
            'change' : '/change-lesson/' +str(courseID)+ '/lesson=' + str(ls.id),
            'del' : "/del-lesson/" +str(courseID)+'/'+ str(ls.id)
        })
    # course_js = {
    #     "title" : course.title,
    #     "description" : course.description
    # }
    #
    lenlesson = len(lessons)
    return render_template('teacher_addcourse_listitem.html', lesson=lesson, lenlesson=lenlesson, courseID=courseID)

@app.route("/teacher_add_lession/<string:courseID>", endpoint="render_addlis", methods=['POST', 'GET'])
def render_addlis(courseID):
    if request.method == 'POST':
        namelesson = request.form.get('DisplayName')
        contentlesson = request.form.get('content-lesson')
        create_section(courseID, namelesson, contentlesson)
        ls = get_lesson_by_course_id(courseID)
        if 'file' not in request.files:
            flash('No file part')

        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            now = datetime.now()
            dt_string = now.strftime("%d.%m.%Y.%H.%M.%S.%f")
            
            insert_file_to_db(current_user.id, filename, UPLOAD_FOLDER + "/" + dt_string + "." + filename, ls[len(ls)-1].id)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], dt_string + "." + filename))
        return redirect('/change-course/'+ str(courseID))
    return render_template("teacher_addcourse_item.html", courseID=courseID)

@app.route("/change-lesson/<string:courseID>/lesson=<string:lessonID>", endpoint="render_change_lesson", methods=['POST', 'GET'])
def render_change_lesson(lessonID, courseID):
    ls = get_lesson_by_ID(lessonID)
    if request.method == 'POST':
        print (lessonID)
        namelesson = request.form.get('DisplayName')
        contentlesson = request.form.get('content-lesson')
        update_section(lessonID, namelesson, contentlesson)
        # ls = get_lesson_by_course_id(courseID)
        if 'file' not in request.files:
            flash('No file part')

        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            now = datetime.now()
            dt_string = now.strftime("%d.%m.%Y.%H.%M.%S.%f")
            
            insert_file_to_db(current_user.id, filename, UPLOAD_FOLDER + "/" + dt_string + "." + filename, lessonID)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], dt_string + "." + filename))
        return redirect('/change-course/' + str(courseID))
    lesson = {
        "title" : ls.title,
        "content" : ls.content
    }
    print (ls.content)
    return render_template("teacher_change_lesson.html", lesson=lesson, courseID=courseID, lessonID=lessonID)

@app.route("/del-lesson/<string:courseID>/<string:lessonID>", endpoint="render_del_lesson", methods=['GET', 'POST'])
def render_del_lesson(lessonID, courseID):
    print(lessonID)
    delete_section(lessonID)
    return redirect('/change-course/' + str(courseID))