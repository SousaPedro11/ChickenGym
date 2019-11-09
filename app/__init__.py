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

from app.model import tables, forms
from app.controller import default, usuario

usuario.__admin__()
