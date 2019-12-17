from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from app.controller.database_manipulation import DAO
from app.model.forms import RegistrationForm, EquipamentoForm, UnidadeForm, EnderecoForm, CargoForm, SalaForm, \
    ModalidadeForm, TurmaForm, PessoaForm, FuncionarioForm
from app.model.tables import Usuario, Aparelho, Endereco, Unidade, Pessoa, Sala, Modalidade, Turma, Aluno, Funcionario, \
    Cargo, Role, RolesUsers
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
    elif objeto == 'sala':
        tabela = DAO.buscar_todos(Sala, Sala.numero)
    elif objeto == 'modalidade':
        tabela = DAO.buscar_todos(Modalidade, Modalidade.categoria)
    elif objeto == 'turma':
        tabela = DAO.buscar_todos(Turma, Turma.horario)
    elif objeto == 'aluno':
        tabela = DAO.buscar_todos(Aluno, Aluno.matricula)
    elif objeto == 'funcionario':
        tabela = DAO.buscar_todos(Funcionario, Funcionario.registro)
    elif objeto == 'cargo':
        tabela = DAO.buscar_todos(Cargo, Cargo.nome)

    if not (len(tabela) > 0):
        if objeto == 'usuario':
            tabela2 = Usuario('', '', '', '')
        elif objeto == 'aparelho':
            tabela2 = Aparelho('', '')
        elif objeto == 'unidade':
            tabela2 = Unidade('', '')
        elif objeto == 'endereco':
            tabela2 = Endereco('', '', '', '', '', '')
        elif objeto == 'sala':
            tabela2 = Sala('')
        elif objeto == 'modalidade':
            tabela2 = Modalidade('', '')
        elif objeto == 'turma':
            tabela2 = Turma('')
        elif objeto == 'aluno':
            tabela2 = Aluno()
        elif objeto == 'funcionario':
            tabela2 = Funcionario()
        elif objeto == 'cargo':
            tabela2 = Cargo('')

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
@database_manipulation.route('/cg/cadastrar/cargo/novo/', methods=['GET', 'POST'])
def cadastrar_cargo():
    form = CargoForm()
    if form.validate_on_submit():
        nome = form.nome.data.upper()

        cargo_lista = DAO.buscar_por_criterio(Cargo, nome=nome)
        if cargo_lista:
            flash('Cargo não cadastrado!')
            flash('Cargo já existe!')
        else:
            cargo = Cargo(nome)
            DAO.transacao(cargo)
            flash('Cargo cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='cargo'))
    return render_template('cadastro_cargo.html', form=form)


@login_required
@database_manipulation.route('/cg/cadastrar/sala/novo/', methods=['GET', 'POST'])
def cadastrar_sala():
    form = SalaForm()

    if form.validate_on_submit():
        numero = form.numero.data.upper()
        sala_lista = DAO.buscar_por_criterio(Sala, numero=numero)
        if sala_lista:
            flash('Sala não cadastrado!')
            flash('Sala já existe!')
        else:
            sala = Sala(numero)
            DAO.transacao(sala)
            flash('Sala cadastrado com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='sala'))
    return render_template('cadastro_sala.html', form=form)


@login_required
@database_manipulation.route('/cg/cadastrar/modalidade/novo/', methods=['GET', 'POST'])
def cadastrar_modalidade():
    form = ModalidadeForm()

    if form.validate_on_submit():
        categoria = form.categoria.data.upper()
        nivel = form.nivel.data.upper()

        modalidade_lista = DAO.buscar_por_criterio(Modalidade, categoria=categoria, nivel=nivel)
        if modalidade_lista:
            flash('Modalidade não cadastrada!')
            flash('Modalidade já existe!')
        else:
            modalidade = Modalidade(categoria, nivel)
            DAO.transacao(modalidade)
            flash('Modalidade cadastrada com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='modalidade'))
    return render_template('cadastro_modalidade.html', form=form)


@login_required
@database_manipulation.route('/cg/cadastrar/turma/novo/', methods=['GET', 'POST'])
def cadastrar_turma():
    form = TurmaForm()

    if form.validate_on_submit():
        horario = form.horario.data

        turma_lista = DAO.buscar_por_criterio(Turma, horario=horario)
        if turma_lista:
            flash('Turma não cadastrada!')
            flash('Turma já existe!')
        else:
            turma = Turma(horario)
            DAO.transacao(turma)
            flash('Turma cadastrada com sucesso!')
        return redirect(url_for('database_manipulation.cadastro', objeto='turma'))
    return render_template('cadastro_turma.html', form=form)


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
@database_manipulation.route('/cg/cadastrar/aluno/novo/', methods=['GET', 'POST'])
def cadastrar_aluno():
    pform = PessoaForm(prefix='p')
    eform = EnderecoForm(prefix='e')
    uform = RegistrationForm()
    if uform.validate_on_submit():
        # Dados de usuário
        name = uform.name.data.upper()
        usename = uform.username.data.upper()
        email = uform.email.data.upper()
        password = generate_password_hash(uform.password.data)

        usuario = Usuario(usename, password, name, email)

        # Endereco
        rua = eform.rua.data.upper()
        numero = eform.numero.data.upper()
        cep = eform.cep.data.upper()
        complemento = eform.complemento.data.upper()
        cidade = eform.cidade.data.upper()
        bairro = eform.bairro.data.upper()

        endereco = Endereco(rua, numero, cep, complemento, cidade, bairro)

        # Dados Pessoais
        nome = name
        nome_mae = pform.nome_mae.data.upper()
        documento_tipo = pform.documento_tipo.data.upper()
        documento_num = pform.documento_num.data.upper()
        telefone = pform.telefone.data.upper()

        pessoa = Pessoa(nome, nome_mae, documento_tipo, documento_num, telefone)

        pessoa.endereco = endereco
        pessoa.usuario_id = usuario.id

        query_endereco = DAO.buscar_por_criterio(Endereco, rua=rua, numero=numero, cidade=cidade, bairro=bairro)
        if query_endereco:
            endereco = query_endereco

        query_pessoa = DAO.buscar_por_criterio(Pessoa, nome=nome, nome_mae=nome_mae, documento_num=documento_num)
        if query_pessoa:
            pessoa = query_pessoa
            pessoa.endereco = endereco
            usuario.pessoa = pessoa

        role = DAO.buscar_por_criterio(Role, name='ALUNO')
        role_users = RolesUsers()
        role_users.user_id = usuario.id
        role_users.role_id = role.id

        aluno = Aluno()
        query_aluno = DAO.buscar_por_criterio(Aluno, pessoa_id=pessoa.id)
        if query_aluno:
            aluno = query_aluno

        aluno.pessoa_id = pessoa.id

        DAO.transacao(usuario)
        DAO.transacao(pessoa)
        DAO.transacao(aluno)
        DAO.transacao(role_users)
        return redirect(url_for('database_manipulation.cadastro', objeto='aluno'))

    return render_template('cadastro_aluno.html', eform=eform, uform=uform, pform=pform)


@login_required
@database_manipulation.route('/cg/cadastrar/funcionario/novo/', methods=['GET', 'POST'])
def cadastrar_funcionario():
    pform = PessoaForm(prefix='p')
    eform = EnderecoForm(prefix='e')
    uform = RegistrationForm(prefix='u')
    listacargo = [(i.id, i.nome) for i in DAO.buscar_todos(Cargo, Cargo.nome)]

    if uform.validate_on_submit():
        # Dados de usuário
        name = uform.name.data.upper()
        usename = uform.username.data.upper()
        email = uform.email.data.upper()
        password = generate_password_hash(uform.password.data)

        usuario = Usuario(usename, password, name, email)

        # Endereco
        rua = eform.rua.data.upper()
        numero = eform.numero.data.upper()
        cep = eform.cep.data.upper()
        complemento = eform.complemento.data.upper()
        cidade = eform.cidade.data.upper()
        bairro = eform.bairro.data.upper()

        endereco = Endereco(rua, numero, cep, complemento, cidade, bairro)

        # Dados Pessoais
        nome = name
        nome_mae = pform.nome_mae.data.upper()
        documento_tipo = pform.documento_tipo.data.upper()
        documento_num = pform.documento_num.data.upper()
        telefone = pform.telefone.data.upper()

        pessoa = Pessoa(nome, nome_mae, documento_tipo, documento_num, telefone)

        pessoa.endereco = endereco
        pessoa.usuario_id = usuario.id

        query_endereco = DAO.buscar_por_criterio(Endereco, rua=rua, numero=numero, cidade=cidade, bairro=bairro)
        if query_endereco:
            endereco = query_endereco

        query_pessoa = DAO.buscar_por_criterio(Pessoa, nome=nome, nome_mae=nome_mae, documento_num=documento_num)
        if query_pessoa:
            pessoa = query_pessoa
            pessoa.endereco = endereco
            pessoa.usuario_id = usuario.id

        role = DAO.buscar_por_criterio(Role, name='ALUNO')
        role_users = RolesUsers()
        role_users.user_id = usuario.id
        role_users.role_id = role.id

        select = request.form.get('comp_select')
        cargo = DAO.buscar_por_criterio(Cargo, id=select)
        print(cargo)
        funcionario = Funcionario()
        query_funcionario = DAO.buscar_por_criterio(Funcionario, pessoa_id=pessoa.id)
        if query_funcionario:
            funcionario = query_funcionario
        funcionario.pessoa_id = pessoa.id
        funcionario.cargo = cargo

        DAO.transacao(usuario)
        DAO.transacao(pessoa)
        DAO.transacao(funcionario)
        DAO.transacao(role_users)
        return redirect(url_for('database_manipulation.cadastro', objeto='funcionario'))

    return render_template('cadastro_funcionario.html', eform=eform, uform=uform, pform=pform, listacargo=listacargo)
