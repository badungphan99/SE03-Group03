from app import db

__all__ = ["FileUpload", "FileLocation", "FileType"]
class FileUpload(db.Model):
    __tablename__ = 'file_upload'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(250), nullable=False)
    path_in_server = db.Column(db.Text(), nullable=False)
    file_type_id = db.Column(db.Integer,  db.ForeignKey('file_type.id'))
    user_id = db.Column(db.Integer,  db.ForeignKey('user.id'))
    location_id = db.Column(db.Integer,  db.ForeignKey('file_location.id'))
    file_id = db.Column(db.Integer)

    def __init__(self, fileName, pathInServer):
        self.file_name = fileName
        self.path_in_server = pathInServer

class FileLocation(db.Model):
    __tablename__ = 'file_location'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    file_uploads = db.relationship('FileUpload', backref='file_location', lazy='dynamic')

    def __init__(self, location):
        self.location = location

class FileType(db.Model):
    __tablename__ = 'file_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    file_uploads = db.relationship('FileUpload', backref='file_type', lazy='dynamic')

    def __init__(self, type):
        self.type = type