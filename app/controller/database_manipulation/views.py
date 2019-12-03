from flask import flash, redirect, url_for, render_template
from flask_login import login_required
from werkzeug.security import generate_password_hash

from app import db
from app.controller.database_manipulation import DAO
from app.model.forms import RegistrationForm, EquipamentoForm, UnidadeForm, EnderecoForm
from app.model.tables import User, Aparelho, Endereco, Unidade
from . import database_manipulation


@database_manipulation.route('/cg/cadastro/usuario/novo/', methods=['GET', 'POST'])
@login_required
def cadastrar_usuario():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data.upper()
        username = form.username.data.lower()
        email = form.email.data.lower()
        password = generate_password_hash(form.password.data)
        user = User(username, password, name, email)
        DAO.transacao(user)
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('auth.login'))
    return render_template('cadastro_usuario.html', form=form)


@login_required
@database_manipulation.route('/cg/usuario/visualizar/', methods=['GET', 'POST'])
def visualizar_usuario():
    table = User.query.all()
    return render_template('visualizar.html', table=table)


@login_required
@database_manipulation.route('/cg/cadastrar/<objeto>/', methods=['GET', 'POST'])
def cadastro(objeto):
    if objeto == 'usuario':
        return redirect(url_for('database_manipulation.cadastrar_usuario'))
    elif objeto == 'equipamento':
        return redirect(url_for('database_manipulation.cadastrar_equipamento'))
    elif objeto == 'unidade':
        return redirect(url_for('database_manipulation.cadastrar_unidade'))
    return render_template('cadastro.html', objeto=objeto)


@login_required
@database_manipulation.route('/cg/cadastrar/equipamento/novo/', methods=['GET', 'POST'])
def cadastrar_equipamento():
    form = EquipamentoForm()
    if form.validate_on_submit():
        fabricante = form.fabricante.data.upper()
        modelo = form.modelo.data.upper()
        aparelho = Aparelho(fabricante, modelo)
        DAO.transacao(aparelho)
        flash('Equipamento cadastrado com sucesso!')
        # return redirect(url_for('home.index'))
    return render_template('cadastro_equipamento.html', form=form)


@login_required
@database_manipulation.route('/cg/cadastrar/unidade/novo/', methods=['GET', 'POST'])
def cadastrar_unidade():
    uform = UnidadeForm(prefix='u')
    eform = EnderecoForm(prefix='e')
    if eform.validate_on_submit():
        rua = eform.rua.data.upper()
        numero = eform.numero.data.upper()
        cep = eform.cep.data.upper()
        complemento = eform.complemento.data.upper()
        cidade = eform.cidade.data.upper()
        bairro = eform.bairro.data.upper()

        nome = uform.nome.data.upper()
        telefone = uform.telefone.data.upper()

        endereco = Endereco(rua, numero, cep, complemento, cidade, bairro)

        unidade = Unidade(nome, telefone)
        unidade.endereco = endereco

        DAO.transacao(unidade)
        flash('Unidade cadastrada com sucesso!')

    return render_template('cadastro_unidade.html', eform=eform, uform=uform)
