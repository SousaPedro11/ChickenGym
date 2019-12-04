from datetime import datetime

from flask_security import RoleMixin, UserMixin
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import backref

from app import db, Util


# TODO falta fazer os relacionamentos de algumas tabelas
class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    nome = db.Column(db.VARCHAR(80), unique=True)
    descricao = db.Column(db.VARCHAR(255))

    def __init__(self, name, description):
        self.nome = name
        self.descricao = description

    def __repr__(self):
        return '<Role %r: %r>' % (self.id, self.nome)

    def get_id(self):
        return str(self.id)


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    username = db.Column(db.VARCHAR(80), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(95), nullable=False)
    name = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
    active = db.Column(db.BOOLEAN, default=True)
    confirmed_at = db.Column(db.DATETIME)

    # RELATIONSHIP
    # One to one
    pessoa = db.relationship('Pessoa', uselist=False, back_populates='usuario')
    # many to many
    roles = db.relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

    def __init__(self, username, password, name, email):
        self.id = Util.__generate_id__()
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.confirmed_at = datetime.now()

    def __repr__(self):
        return '<User %r: %r, %r>' % (self.id, self.username, self.name)

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

    def get_id(self):
        return str(self.id)


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(120), nullable=False)
    nome_mae = db.Column(db.VARCHAR(120), nullable=False)
    documento_tipo = db.Column(db.Enum('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'), nullable=False)
    documento_num = db.Column(db.VARCHAR(20), nullable=False)
    endereco_id = db.Column(db.INTEGER, db.ForeignKey('endereco.id', name='FK_pessoa_endereco'), nullable=False)
    telefone = db.Column(db.VARCHAR(15), nullable=True, default=None)
    user_id = db.Column(db.VARCHAR(36), db.ForeignKey('user.id', name='FK_pessoa_user'), nullable=False)

    # RELATIONSHIP
    # One to one
    usuario = db.relationship('User', back_populates='pessoa')
    funcionario = db.relationship('Funcionario', uselist=False, back_populates='pessoa')
    # Many to one
    endereco = db.relationship('Endereco', back_populates='pessoas')


class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    registro = db.Column(db.VARCHAR(10), nullable=False, unique=True)
    ativado = db.Column(db.BOOLEAN, default=True)
    cargo_id = db.Column(db.INTEGER, db.ForeignKey('cargo.id', name='FK_funcionario_cargo'), nullable=False)
    pessoa_id = db.Column(db.INTEGER, db.ForeignKey('pessoa.id', name='FK_funcionario_pessoa'), nullable=False)

    # RELATIONSHIP
    # One to one
    cargo = db.relationship('Cargo', back_populates='funcionario')
    pessoa = db.relationship('Pessoa', back_populates='funcionario')
    # Many to one
    modalidades = db.relationship('Modalidade', back_populates='professor')


# TODO falta
class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    matricula = db.Column(db.VARCHAR(10), nullable=False, unique=True)
    ativado = db.Column(db.BOOLEAN, default=True)
    plano_id = db.Column(db.INTEGER, nullable=False)
    pessoa_id = db.Column(db.INTEGER, nullable=False)


# Tabelas intermediarias
class RolesUsers(db.Model):
    __tablename__ = "roles_users"

    id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
    user_id = db.Column(db.VARCHAR(36), db.ForeignKey('user.id'))
    role_id = db.Column(db.VARCHAR(36), db.ForeignKey('role.id'))

    def __init__(self):
        self.id = Util.__generate_id__()

    __table_args__ = (
        UniqueConstraint('user_id', 'role_id', name='unique_role_user'),
    )

    def __repr__(self):
        return '<RoleUsers %r: %r, %r>' % (self.id, self.user_id, self.role_id)
