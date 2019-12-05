import inspect

from flask import flash, redirect, url_for, render_template
from flask_login import login_required
from werkzeug.security import generate_password_hash

from app.controller.database_manipulation import DAO
from app.model.forms import RegistrationForm, EquipamentoForm, UnidadeForm, EnderecoForm
from app.model.tables import User, Aparelho, Endereco, Unidade
from . import database_manipulation


@database_manipulation.route('/cg/cadastro/usuario/novo/', methods=['GET', 'POST'])
@login_required
def cadastrar_usuario():
    form = RegistrationForm()
    table = User.query.order_by(User.name, User.username).all()
    if form.validate_on_submit():
        name = form.name.data.upper()
        username = form.username.data.lower()
        email = form.email.data.lower()
        password = generate_password_hash(form.password.data)
        user = User(username, password, name, email)
        DAO.transacao(user)
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastrar_usuario'))
    return render_template('cadastro_usuario.html', form=form, table=table)


@login_required
@database_manipulation.route('/cg/visualizar/<objeto>', methods=['GET', 'POST'])
def visualizar(objeto, tabela=None):
    if objeto == 'usuario':
        tabela = DAO.buscar_todos(User)
    elif objeto == 'equipamento':
        tabela = DAO.buscar_todos(Aparelho)
    elif objeto == 'unidade':
        tabela = DAO.buscar_todos(Unidade)
    return render_template('visualizar.html', objeto=objeto, table=tabela)


@login_required
@database_manipulation.route('/cg/cadastrar/<objeto>/', methods=['GET', 'POST'])
def cadastro(objeto, tabela=None, tabela2=None):
    # if objeto == 'usuario':
    #     # tabela = User.query.all()
    #     return redirect(url_for('database_manipulation.cadastrar_usuario'))
    # elif objeto == 'equipamento':
    #     # tabela = Aparelho.query.all()
    #     return redirect(url_for('database_manipulation.cadastrar_equipamento'))
    # elif objeto == 'unidade':
    #     # tabela = Unidade.query.all()
    #     return redirect(url_for('database_manipulation.cadastrar_unidade'))
    classe = object
    if objeto == 'usuario':
        classe = User
        tabela = DAO.buscar_todos(User)
    elif objeto == 'equipamento':
        classe = Aparelho
        tabela = DAO.buscar_todos(Aparelho)
    elif objeto == 'unidade':
        classe = Unidade
        tabela = DAO.buscar_todos(Unidade)

    if not (len(tabela) > 0):
        if objeto == 'usuario':
            tabela2 = User('', '', '', '')
        elif objeto == 'equipamento':
            tabela2 = Aparelho('', '')
        elif objeto == 'unidade':
            tabela2 = Unidade('', '')

    return render_template('cadastro.html', objeto=objeto, table=tabela, tabela2=tabela2)


@login_required
@database_manipulation.route('/cg/cadastrar/equipamento/novo/', methods=['GET', 'POST'])
def cadastrar_equipamento():
    form = EquipamentoForm()
    tabela = Aparelho.query.all()
    if form.validate_on_submit():
        fabricante = form.fabricante.data.upper()
        modelo = form.modelo.data.upper()
        aparelho = Aparelho(fabricante, modelo)
        DAO.transacao(aparelho)
        flash('Equipamento cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastrar_equipamento'))
    return render_template('cadastro_equipamento.html', form=form, table=tabela)


@login_required
@database_manipulation.route('/cg/cadastrar/unidade/novo/', methods=['GET', 'POST'])
def cadastrar_unidade():
    uform = UnidadeForm(prefix='u')
    eform = EnderecoForm(prefix='e')
    tabela = Unidade.query.all()
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
        return redirect(url_for('database_manipulation.cadastrar_unidade'))

    return render_template('cadastro_unidade.html', eform=eform, uform=uform, table=tabela)
