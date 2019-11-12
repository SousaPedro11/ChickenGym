from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email

from app.model.tables import User


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

    def validate_username(self, username):
        if '@' in username.data:
            user = User.query.filter_by(email=username.data).first()
        else:
            user = User.query.filter_by(username=username.data).first()
        if user is None:
            flash(ValidationError('Usuário não existe!'))


class RegistrationForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita a Senha',
        validators=[DataRequired(), EqualTo('password', message='Este campo deve ser igual a senha informada')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Use outro nome de usuário, por favor!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Use outro email, por favor!')


class EquipamentoForm(FlaskForm):
    modelo = StringField('modelo', validators=[DataRequired()])
