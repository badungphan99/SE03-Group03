import os
from app import app
from app.controller import *
from flask import render_template, request, flash, redirect, send_file
from werkzeug.utils import secure_filename
import urllib.request
from dotenv import load_dotenv

from datetime import datetime

load_dotenv(dotenv_path='./env/data_upload.env')
COURSE_DOCUMENT = os.getenv('COURSE_DOCUMENT')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = COURSE_DOCUMENT
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/download_lesson/<string:lesson>', methods=['GET', 'POST'])
def download(lesson):
    filename = "../" + UPLOAD_FOLDER + "/" + '07.01.2020.17.42.31.094714.bai3.txt'
    print (filename)
    # download = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_file(filename, attachment_filename='bai3.txt', as_attachment=True)