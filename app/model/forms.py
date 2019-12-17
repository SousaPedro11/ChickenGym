from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email

from app.controller.database_manipulation import DAO
from app.model.tables import Usuario, Unidade, Cargo


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

    def validate_username(self, username):
        if '@' in username.data:
            user = Usuario.query.filter_by(email=username.data.lower()).first()
        else:
            user = Usuario.query.filter_by(username=username.data.lower()).first()
        if user is None:
            flash(ValidationError('Usuário não existe!'))


class RegistrationForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Endereço de e-mail inválido!')])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita a Senha',
        validators=[DataRequired(), EqualTo('password', message='Este campo deve ser igual a senha informada')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = Usuario.query.filter_by(username=username.data.lower()).first()
        if user is not None:
            raise ValidationError('Use outro nome de usuário, por favor!')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data.lower()).first()
        if user is not None:
            raise ValidationError('Use outro email, por favor!')


class RedefinirSenhaForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email cadastrado')
    nova = PasswordField('Nova senha', validators=[DataRequired()])
    repetir_nova = PasswordField('Repita a nova senha',
                                 validators=[DataRequired(),
                                             EqualTo('nova', message='Este campo deve ser igual a senha informada')])
    submit = SubmitField('Atualizar Senha')

    def validate_username(self, username):
        user = Usuario.query.filter_by(username=username.data.lower()).first()
        if user is None:
            raise ValidationError('Usuário não existe!')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data.lower()).first()
        if user is None:
            raise ValidationError('Email não cadastrado!')


class EquipamentoForm(FlaskForm):
    fabricante = StringField('fabricante', validators=[DataRequired()])
    modelo = StringField('modelo', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')


class EnderecoForm(FlaskForm):
    rua = StringField('rua', validators=[DataRequired()])
    numero = StringField('numero', validators=[DataRequired()])
    cep = StringField('cep', validators=[DataRequired()])
    complemento = StringField('complemento')
    cidade = StringField('cidade', validators=[DataRequired()])
    bairro = StringField('bairro', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')


class UnidadeForm(FlaskForm):
    nome = StringField('Nome da Unidade', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_nome(self, nome):
        unidade = Unidade.query.filter_by(nome=nome.data.upper()).first()
        if unidade is not None:
            raise ValidationError('Use outro nome, por favor!')

    def validate_telefone(self, telefone):
        unidade = Unidade.query.filter_by(telefone=telefone.data).first()
        if unidade is not None:
            raise ValidationError('Use outro telefone, por favor!')


class CargoForm(FlaskForm):
    nome = StringField('Nome do Cargo', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_cargo(self, nome):
        cargo = Cargo.query.filter_by(nome=nome.data.upper()).first()
        print(cargo)
        if cargo is not None:
            raise ValidationError('Cargo já existe!')
