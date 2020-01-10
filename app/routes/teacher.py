from app import app
from app.controller import *
from flask import render_template, request, flash, redirect

@app.route('/teacher_home', endpoint='teacher_home')
def teacher_home():
    return render_template('teacher-home.html')

@app.route('/add_course', endpoint='add_course')
def add_course():
    return render_template('teacher_addcourse.html')