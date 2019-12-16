import os
import subprocess

import sys
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command, Option
from flask_sqlalchemy import SQLAlchemy

# Originally from https://gist.github.com/menghan/9a632bbb0acb445f4f3a
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def get_options(self):
        from gunicorn.config import make_settings

        settings = make_settings()
        options = []

        for setting, klass in settings.items():
            if klass.cli:
                if klass.const is not None:
                    options.append(Option(*klass.cli, const=klass.const, action=klass.action))
                else:
                    options.append(Option(*klass.cli, action=klass.action))

        return options

    def run(self, *args, **kwargs):
        run_args = sys.argv[2:]
        # !!!!! Change your app here !!!!!
        run_args.append('--reload')
        run_args.extend(['-k', 'flask_sockets.worker'])
        run_args.append('app:app')
        subprocess.Popen([os.path.join(os.path.dirname(sys.executable), 'gunicorn')] + run_args).wait()


# inicializa a aplicacao
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app, session_options={
    'expire_on_commit': False
})

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('gunicorn', GunicornServer())

# admin = Admin(app, name='ChickenGym', template_mode='bootstrap3')

lm = LoginManager()
lm.init_app(app)
lm.login_view = "auth.login"
lm.session_protection = "strong"

from app.controller.auth import auth as auth_blueprint
from app.controller.database_manipulation import database_manipulation as database_manipulation_blueprint
from app.controller.home import home as home_blueprint

# from app.controller.admin import admin_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(database_manipulation_blueprint)
app.register_blueprint(home_blueprint)
# app.register_blueprint(admin_blueprint)

from app.model import tables, forms
from app.controller import default

db.create_all()
