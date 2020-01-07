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

@app.route('/upload.html', endpoint='render_upload')
def render_upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			now = datetime.now()
			dt_string = now.strftime("%d.%m.%Y.%H.%M.%S.%f")
			#untested
			insert_file_to_db(filename, UPLOAD_FOLDER + "/" + dt_string + "." + filename, "", "")

			file.save(os.path.join(app.config['UPLOAD_FOLDER'], dt_string + "." + filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)
