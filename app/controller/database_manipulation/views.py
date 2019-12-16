from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from app.controller.database_manipulation import DAO
from app.model.forms import RegistrationForm, EquipamentoForm, UnidadeForm, EnderecoForm
from app.model.tables import Usuario, Aparelho, Endereco, Unidade, Pessoa
from . import database_manipulation


@database_manipulation.route('/cg/cadastrar/usuario/novo/', methods=['GET', 'POST'])
@login_required
def cadastrar_usuario():
    form = RegistrationForm()
    table = Usuario.query.order_by(Usuario.nome, Usuario.username).all()
    if form.validate_on_submit():
        name = form.name.data.upper()
        username = form.username.data.lower()
        email = form.email.data.lower()
        password = generate_password_hash(form.password.data)
        user = Usuario(username, password, name, email)
        DAO.transacao(user)
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='usuario'))
    return render_template('cadastro_usuario.html', form=form, table=table)


@login_required
@database_manipulation.route('/cg/visualizar/<objeto>', methods=['GET', 'POST'])
def visualizar(objeto, tabela=None):
    if objeto == 'usuario':
        tabela = DAO.buscar_todos(Usuario)
    elif objeto == 'aparelho':
        tabela = DAO.buscar_todos(Aparelho)
    elif objeto == 'unidade':
        tabela = DAO.buscar_todos(Unidade)
    return render_template('visualizar.html', objeto=objeto, table=tabela)


@login_required
@database_manipulation.route('/cg/cadastrar/<objeto>/', methods=['GET', 'POST'])
def cadastro(objeto, tabela=None, tabela2=None):
    if objeto == 'usuario':
        tabela = DAO.buscar_todos(Usuario, Usuario.nome, Usuario.username)
    elif objeto == 'aparelho':
        tabela = DAO.buscar_todos(Aparelho, Aparelho.fabricante, Aparelho.modelo)
    elif objeto == 'unidade':
        tabela = DAO.buscar_todos(Unidade, Unidade.nome)
    elif objeto == 'endereco':
        tabela = DAO.buscar_todos(Endereco, Endereco.cidade, Endereco.rua)

    if not (len(tabela) > 0):
        if objeto == 'usuario':
            tabela2 = Usuario('', '', '', '')
        elif objeto == 'aparelho':
            tabela2 = Aparelho('', '')
        elif objeto == 'unidade':
            tabela2 = Unidade('', '')
        elif objeto == 'endereco':
            tabela2 = Endereco('', '', '', '', '', '')

    return render_template('cadastro.html', objeto=objeto, table=tabela, tabela2=tabela2)


@login_required
@database_manipulation.route('/cg/cadastrar/aparelho/novo/', methods=['GET', 'POST'])
def cadastrar_equipamento():
    form = EquipamentoForm()
    if form.validate_on_submit():
        fabricante = form.fabricante.data.upper()
        modelo = form.modelo.data.upper()
        aparelho = Aparelho(fabricante, modelo)
        DAO.transacao(aparelho)
        flash('Equipamento cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='aparelho'))
    return render_template('cadastro_equipamento.html', form=form)


@login_required
@database_manipulation.route('/cg/cadastrar/unidade/novo/', methods=['GET', 'POST'])
def cadastrar_unidade():
    uform = UnidadeForm(prefix='u')
    eform = EnderecoForm(prefix='e')
    tabela = Unidade.query.all()
    if uform.validate_on_submit():
        rua = eform.rua.data.upper()
        numero = eform.numero.data.upper()
        cep = eform.cep.data.upper()
        complemento = eform.complemento.data.upper()
        cidade = eform.cidade.data.upper()
        bairro = eform.bairro.data.upper()

        nome = uform.nome.data.upper()
        telefone = uform.telefone.data.upper()

        unidade = Unidade(nome, telefone)

        endereco = Endereco(rua, numero, cep, complemento, cidade, bairro)
        list_end = DAO.buscar_por_criterio(Endereco, rua=rua, numero=numero, cidade=cidade, bairro=bairro)

        if list_end:
            unid_end = DAO.buscar_por_criterio(Unidade, endereco_id=list_end.id)
            pess_end = DAO.buscar_por_criterio(Unidade, endereco_id=list_end.id)
            if unid_end:
                flash('Unidade não cadastrada!')
                flash('Endereço associado a unidade %s' % unid_end.nome)
            elif pess_end:
                flash('Unidade não cadastrada!')
                flash('Endereço associado a pessoa %s' % pess_end.nome)
            else:
                unidade.endereco = list_end
                DAO.transacao(list_end)
        else:
            unidade.endereco = endereco
            DAO.transacao(unidade)
            flash('Unidade cadastrada com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='unidade'))
    return render_template('cadastro_unidade.html', eform=eform, uform=uform, table=tabela)


@login_required
@database_manipulation.route('/cg/deletar/<objeto>/<id>/', methods=['GET', 'POST'])
def deletar(objeto, id):
    string = objeto.capitalize()
    registro = DAO.buscar_por_criterio(globals()[string], id=id)
    if isinstance(registro, Usuario) and registro == current_user:
        flash('Usuário não pode excluir a própria conta!')
        return redirect(url_for('database_manipulation.cadastro', objeto=objeto))
    elif isinstance(registro, Endereco):
        ue = DAO.buscar_todos_por_criterio(Unidade, endereco_id=id)
        pe = DAO.buscar_todos_por_criterio(Pessoa, endereco_id=id)
        if ue or pe:
            flash('Endereço está associado a outro usuário ou unidade!')
            return redirect(url_for('database_manipulation.cadastro', objeto=objeto))

    if request.method == 'POST':
        DAO.deletar(registro)
        return redirect(url_for('database_manipulation.cadastro', objeto=objeto))
    return render_template('deletar.html', registro=registro, objeto=objeto)


@login_required
@database_manipulation.route('/cg/editar/<objeto>/<id>/', methods=['GET', 'POST'])
def editar(objeto, id):
    string = objeto.capitalize()
    registro = DAO.buscar_por_criterio(globals()[string], id=id)
    hold = hash(frozenset(vars(registro).items()))
    if request.method == 'POST':
        for x in registro.dict_fieldname:
            attr = registro.dict_fieldname[x]
            attr_val = request.form.get(x).upper()
            setattr(registro, attr, attr_val)
        hregistro = hash(frozenset(vars(registro).items()))
        DAO.transacao(registro)
        if hold == hregistro:
            flash('Sem alterações')
        else:
            flash('Alterações efetuadas com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto=objeto))
    return render_template('editar.html', registro=registro, objeto=objeto)


@login_required
@database_manipulation.route('/cg/msform/')
def msform():
    return render_template('msform.html')
