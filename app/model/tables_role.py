from datetime import datetime

from flask_security import RoleMixin, SQLAlchemyUserDatastore, Security
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import backref

from app import db, app


# Define models
class RolesUsers(db.Model):
    __tablename__ = "roles_users"

    id = db.Column(db.INTEGER, primary_key=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    role_id = db.Column(db.INTEGER, db.ForeignKey('role.id'))

    __table_args__ = (
        UniqueConstraint('user_id', 'role_id', name='unique_role_user'),
    )


class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    # @property
    def get_id(self):
        return str(self.id)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True, nullable=False)
    username = db.Column(db.VARCHAR(80), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(95), nullable=False)
    name = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    active = db.Column(db.BOOLEAN, default=True)
    confirmed_at = db.Column(db.DATETIME)

    roles = db.relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.confirmed_at = datetime.now()

    def __repr__(self):
        return '<User %r, %r>' % (self.username, self.name)

    @property
    def dict_class(self):
        dicionario = [{'Nome': self.name}, {'Usuário': self.username}, {"e-mail": self.email}]
        return dicionario

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # @property
    def get_id(self):
        return str(self.id)


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
