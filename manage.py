import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import *
from dotenv import load_dotenv
from app.models import *
from app.routes import *

manager = Manager(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@manager.command()
def create_db():
    db.create_all()
    db.session.commit()

@manager.command()
def runapp():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    manager.run()