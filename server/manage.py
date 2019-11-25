import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db
from dotenv import load_dotenv
from server.app.models import user, quiz, forum, course

load_dotenv(dotenv_path='./env/flask_setting.env')
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def recreate_db():
    """
    Recreates a local database. Not use this on production
    """
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()