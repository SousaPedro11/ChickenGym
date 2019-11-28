from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

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
from app.controller.database_manipulation import usuario

db.create_all()
usuario.__admin__()
