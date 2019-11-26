import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import *
from dotenv import load_dotenv
from app.models import *
from app.routes import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)