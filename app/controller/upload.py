from app.models import *
from app import *
from sqlalchemy import and_

def insert_file_location(location):
    fileLocation = FileLocation(location)
    db.session.add(fileLocation)
    db.session.commit()

def insert_file_type(_type):
    file_type = FileType(_type)
    db.session.add(file_type)
    db.session.commit()

def insert_file_to_db(fileName, pathInServer, fileLocation, file_type):
    fileUpload = FileUpload(fileName, pathInServer)
    file_location = FileLocation(fileLocation)
    file_location.file_uploads.append(fileUpload)
    db.session.add(fileUpload)
    db.session.commit()