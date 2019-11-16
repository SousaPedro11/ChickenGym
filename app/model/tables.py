from app import db


# TODO falta fazer os relacionamentos

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

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

    def get_id(self):
        return str(self.id)


class Unidade(db.Model):
    __tablename__ = 'unidade'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(120), nullable=False)
    endereco_id = db.Column(db.SMALLINT, nullable=False)


class Endereco(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    rua = db.Column(db.VARCHAR(80), nullable=False)
    numero = db.Column(db.VARCHAR(5), nullable=False)
    cep = db.Column(db.VARCHAR(10), nullable=False)
    complemento = db.Column(db.TEXT, nullable=True)
    cidade = db.Column(db.VARCHAR(30), nullable=False)
    bairro = db.Column(db.VARCHAR(20), nullable=False)
    telefone = db.Column(db.VARCHAR(15), nullable=True)


class Modalidade(db.Model):
    __tablename__ = 'modalidade'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    categoria = db.Column(db.VARCHAR(100), nullable=False)
    nivel = db.Column(db.VARCHAR(20), nullable=True)
    categoria_pai_id = db.Column(db.SMALLINT, nullable=True)
    unidade_id = db.Column(db.SMALLINT, nullable=False)
    professor_id = db.Column(db.VARCHAR(10), nullable=True)


class Turma(db.Model):
    __tablename__ = 'turma'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    horario = db.Column(db.TIME, nullable=False)
    modalidade_id = db.Column(db.SMALLINT, nullable=True)


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(120), nullable=False)
    nome_mae = db.Column(db.VARCHAR(120), nullable=False)
    documento_tipo = db.Column(db.Enum('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'), nullable=False)
    documento_num = db.Column(db.VARCHAR(20), nullable=False)
    endereco_id = db.Column(db.SMALLINT, nullable=False)


class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    registro = db.Column(db.VARCHAR(10), nullable=False, unique=True)
    ativado = db.Column(db.BOOLEAN, default=True)
    cargo_id = db.Column(db.SMALLINT, nullable=False)


class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    matricula = db.Column(db.VARCHAR(10), nullable=False, unique=True)
    ativado = db.Column(db.BOOLEAN, default=True)
    plano_id = db.Column(db.SMALLINT, nullable=False)


class Pagamento(db.Model):
    __tablename__ = 'pagamento'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    tipo = db.Column(db.Enum('DEBITO', 'CREDITO', 'DINHEIRO'), nullable=False)
    vencimento_data = db.Column(db.DATETIME, nullable=False)
    referencia = db.Column(db.DATE, nullable=False)
    status_pagamento = db.Column(db.Enum('EFETUADO', 'ATRASADO', 'PENDENTE'))
    aluno_id = db.Column(db.SMALLINT, nullable=False)
    valor_plano_id = db.Column(db.SMALLINT, nullable=False)


class Cargo(db.Model):
    __tablename__ = 'cargo'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    nome = db.Column(db.VARCHAR(20), nullable=False)


# TODO falta completar
class AvaliacaoFisica(db.Model):
    __tablename__ = 'avaliacao_fisica'

    id = db.Column(db.SMALLINT, nullable=False, autoincrement=True, primary_key=True)
    avaliador = db.Column(db.SMALLINT, nullable=False)
    data_avaliacao = db.Column(db.DATE, nullable=False)
    abdominal = db.Column(db.SMALLINT, nullable=True)
    flexoes_braco = db.Column(db.SMALLINT, nullable=True)
    altura = db.Column(db.DECIMAL(precision=3, scale=2), nullable=False)
