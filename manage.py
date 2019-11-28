import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import *
from dotenv import load_dotenv
from app.models import *
from app.routes import *

# load_dotenv(dotenv_path='./env/flask_setting.env')
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@manager.command
def migrate():
    """
    Creates database. Use only in first time
    """
    db.create_all()
    db.session.commit()

@manager.command
def build():
    db.create_all()
    db.session.commit()
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    manager.run()
