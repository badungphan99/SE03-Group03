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

@app.route('/download_lesson/<string:fileID>', methods=['GET', 'POST'])
def download(fileID):
    # filename = "../" + UPLOAD_FOLDER + "/" + '07.01.2020.17.42.31.094714.bai3.txt'
    # print (filename)
    # download = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    file = get_file_by_fileID(fileID)
    path = "../" + file.path_in_server
    print(path)
    return send_file(path, attachment_filename=file.file_name, as_attachment=True)