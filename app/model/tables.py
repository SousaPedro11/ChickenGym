from app import db


# TODO falta fazer os relacionamentos

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True, nullable=False)
    username = db.Column(db.VARCHAR(80), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(95), nullable=False)
    name = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True, nullable=False)

    # RELATIONSHIP
    # One to one
    pessoa = db.relationship('Pessoa', uselist=False, back_populates='usuario')

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

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

    @property
    def get_id(self):
        return str(self.id)


class Endereco(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    rua = db.Column(db.VARCHAR(80), nullable=False)
    numero = db.Column(db.VARCHAR(5), nullable=False)
    cep = db.Column(db.VARCHAR(10), nullable=False)
    complemento = db.Column(db.TEXT, nullable=True)
    cidade = db.Column(db.VARCHAR(30), nullable=False)
    bairro = db.Column(db.VARCHAR(20), nullable=False)
    telefone = db.Column(db.VARCHAR(15), nullable=True)

    # RELATIONSHIP
    # One to one
    unidade = db.relationship('Unidade', uselist=False, back_populates='endereco')
    # One to many
    pessoas = db.relationship('Pessoa', back_populates='endereco')


class Unidade(db.Model):
    __tablename__ = 'unidade'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(120), nullable=False)
    endereco_id = db.Column(db.INTEGER, db.ForeignKey('endereco.id', name='FK_unidade_endereco'), nullable=False,
                            unique=True)

    # RELATIONSHIP
    # One to one
    endereco = db.relationship('Endereco', back_populates='unidade')
    # Many to one
    modalidades = db.relationship('Modalidade', back_populates='unidade')


class Modalidade(db.Model):
    __tablename__ = 'modalidade'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    categoria = db.Column(db.VARCHAR(100), nullable=False)
    nivel = db.Column(db.VARCHAR(20), nullable=True)
    categoria_pai_id = db.Column(db.INTEGER, db.ForeignKey('modalidade.id', name='FK_modalidade_categoria'),
                                 nullable=True)
    unidade_id = db.Column(db.INTEGER, db.ForeignKey('unidade.id', name='FK_modalidade_unidade'), nullable=False)
    professor_id = db.Column(db.INTEGER, db.ForeignKey('funcionario.id', name='FK_modalidade_professor'),
                             nullable=True)

    # RELATIONSHIP
    # Self
    categorias_pai = db.relationship('Modalidade')
    # One to many
    unidade = db.relationship('Unidade', back_populates='modalidades')
    professor = db.relationship('Funcionario', back_populates='modalidades')
    # Many to one
    turmas = db.relationship('Turma', back_populates='modalidade')


class Turma(db.Model):
    __tablename__ = 'turma'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    horario = db.Column(db.TIME, nullable=False)
    modalidade_id = db.Column(db.INTEGER, db.ForeignKey('modalidade.id', name='FK_turma_modalidade'), nullable=True)

    # RELATIONSHIP
    # One to many
    modalidade = db.relationship('Modalidade', back_populates='turmas')


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(120), nullable=False)
    nome_mae = db.Column(db.VARCHAR(120), nullable=False)
    documento_tipo = db.Column(db.Enum('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'), nullable=False)
    documento_num = db.Column(db.VARCHAR(20), nullable=False)
    endereco_id = db.Column(db.INTEGER, db.ForeignKey('endereco.id', name='FK_pessoa_endereco'), nullable=False)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id', name='FK_pessoa_user'), nullable=False)

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


class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    matricula = db.Column(db.VARCHAR(10), nullable=False, unique=True)
    ativado = db.Column(db.BOOLEAN, default=True)
    plano_id = db.Column(db.INTEGER, nullable=False)
    pessoa_id = db.Column(db.INTEGER, nullable=False)


class Pagamento(db.Model):
    __tablename__ = 'pagamento'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    tipo = db.Column(db.Enum('DEBITO', 'CREDITO', 'DINHEIRO'), nullable=False)
    vencimento_data = db.Column(db.DATETIME, nullable=False)
    referencia = db.Column(db.DATE, nullable=False)
    status_pagamento = db.Column(db.Enum('EFETUADO', 'ATRASADO', 'PENDENTE'))
    aluno_id = db.Column(db.INTEGER, nullable=False)
    valor_plano_id = db.Column(db.INTEGER, nullable=False)


class Cargo(db.Model):
    __tablename__ = 'cargo'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(20), nullable=False)

    # RELATIONSHIP
    # One to one
    funcionario = db.relationship('Funcionario', uselist=False, back_populates='cargo')


class AvaliacaoFisica(db.Model):
    __tablename__ = 'avaliacaofisica'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    avaliador = db.Column(db.INTEGER, nullable=False)
    data_avaliacao = db.Column(db.DATE, nullable=False)
    abdominal = db.Column(db.INTEGER, nullable=True)
    flexoes_braco = db.Column(db.INTEGER, nullable=True)
    altura = db.Column(db.DECIMAL(precision=3, scale=2), nullable=False)
    peso = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
    busto = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
    braco_esquerdo = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    braco_direito = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    abdomen = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
    cintura = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
    quadril = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
    culote = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    coxa_esquerda = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    coxa_direita = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    panturrilha_esquerda = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    panturrilha_direita = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
    aluno_id = db.Column(db.INTEGER, nullable=False)


class Plano(db.Model):
    __tablename__ = 'plano'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    valor = db.Column(db.DECIMAL(precision=6, scale=2), nullable=False)


class Sala(db.Model):
    __tablename__ = 'sala'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    numero = db.Column(db.VARCHAR(5), nullable=False)


class Ficha(db.Model):
    __tablename__ = 'ficha'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    data_elaboracao = db.Column(db.DATE, nullable=False)
    aluno_id = db.Column(db.INTEGER, nullable=False)


class Aparelho(db.Model):
    __tablename__ = 'aparelho'

    id = db.Column(db.INTEGER, nullable=False, autoincrement=True, primary_key=True)
    fabricante = db.Column(db.VARCHAR(20), nullable=False)
    modelo = db.Column(db.VARCHAR(20), nullable=False)


# TABELAS INTERMEDIARIAS
linha_ficha = db.Table('linha_ficha',
                       db.Column('id', db.INTEGER, nullable=False, autoincrement=True, primary_key=True),
                       db.Column('ciclo1', db.DECIMAL(precision=5, scale=2)),
                       db.Column('ciclo2', db.DECIMAL(precision=5, scale=2)),
                       db.Column('ciclo3', db.DECIMAL(precision=5, scale=2)),
                       db.Column('ciclo4', db.DECIMAL(precision=5, scale=2)),
                       db.Column('aparelho_id', db.INTEGER, db.ForeignKey('aparelho.id')),
                       db.Column('ficha_id', db.INTEGER, db.ForeignKey('ficha.id'))
                       )
