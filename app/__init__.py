import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config as Config

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Config[config_name].init_app(app)

    db.init_app(app)

    return app