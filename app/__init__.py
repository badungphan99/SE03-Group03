import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

app = Flask(__name__)

from app.routes import *

config_name = config

if not isinstance(config, str):
    config_name = os.getenv('FLASK_CONFIG', 'default')

app.config.from_object(config[config_name])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'openschool_secretkey'
config[config_name].init_app(app)

db.init_app(app)