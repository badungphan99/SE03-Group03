import os

class Config:
    APP_NAME = os.environ.get('APP_NAME', 'Online School')

    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        print('This app is in debug mode')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}