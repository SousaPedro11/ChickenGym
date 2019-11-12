from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
db.drop_all()
db.create_all()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"
lm.session_protection = "strong"

from app.controller.auth import auth as auth_blueprint
from app.controller.database_manipulation import database_manipulation as database_manipulation_blueprint
from app.controller.home import home as home_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(database_manipulation_blueprint)
app.register_blueprint(home_blueprint)

from app.model import tables, forms
from app.controller import default
from app.controller.database_manipulation import usuario

usuario.__admin__()
