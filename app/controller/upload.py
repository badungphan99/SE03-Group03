from app.models import *
from app import *
from sqlalchemy import and_

# def insert_file_location(location):
#     fileLocation = FileLocation(location)
#     db.session.add(fileLocation)
#     db.session.commit()
#
# def insert_file_type(_type):
#     file_type = FileType(_type)
#     db.session.add(file_type)
#     db.session.commit()

def insert_file_to_db(user_id, fileName, pathInServer, section_id):
    user = db.session.query(User).filter(User.id == user_id).first()
    fileUpload = FileUpload(fileName, pathInServer, section_id)
    user.file_uploads.append(fileUpload)

    db.session.add(fileUpload)
    db.session.commit()