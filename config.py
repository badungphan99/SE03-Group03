import os
from dotenv import load_dotenv
from pathlib import Path


class Config:
    APP_NAME = os.environ.get('APP_NAME', 'Online School')

    def init_app(app):
        pass


class DevelopmentConfig(Config):

    load_dotenv(dotenv_path='./env/db_setting.env')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

    DEBUG = True
    # if(DEBUG):
        # MYSQL_USER = 'root'
        # MYSQL_HOST = 'localhost'
        # MYSQL_PASSWORD = 'root'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + str(MYSQL_USER) + ':' + str(MYSQL_PASSWORD) + '@' + str(MYSQL_HOST) + ':' + str(MYSQL_PORT) + '/' + str(MYSQL_DATABASE)

    print(SQLALCHEMY_DATABASE_URI)

    @classmethod
    def init_app(cls, app):
        print('This app is in debug mode')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
