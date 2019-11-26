import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_login import login_user, logout_user, login_required, current_user, UserMixin

db = SQLAlchemy()


app = Flask(__name__)

config_name = config
if not isinstance(config, str):
    config_name = os.getenv('FLASK_CONFIG', 'default')

app.config.from_object(config[config_name])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'openschool_secretkey'
# config[config_name].init_app(app)

from app.routes import *

db.init_app(app)

# manager = Manager(app)
# migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)