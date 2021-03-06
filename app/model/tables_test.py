# from datetime import datetime
#
# from flask_security import RoleMixin, UserMixin
# from sqlalchemy import UniqueConstraint
# from sqlalchemy.orm import backref
#
# from app import db, Util
#
#
# # TODO falta fazer os relacionamentos de algumas tabelas
# class Aluno(db.Model):
#     __tablename__ = 'aluno'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     matricula = db.Column(db.VARCHAR(15), nullable=False, unique=True, default=('A' + Util.__gerar_num_matricula__()))
#     ativado = db.Column(db.BOOLEAN, default=True)
#     # plano_id = db.Column(db.VARCHAR(36), db.ForeignKey('plano.id', name='FK_aluno_plano'))
#     pessoa_id = db.Column(db.VARCHAR(36), db.ForeignKey('pessoa.id', name='FK_aluno_pessoa'), nullable=False)
#
#     def __init__(self):
#         self.id = Util.__generate_id__()
#         self.matricula = 'A' + Util.__gerar_num_matricula__()
#
#     # Relacionamento
#     # many to one
#     # plano = db.relationship("Plano", backref='alunos', lazy='dynamic')
#
#
# # todo falta relacionar com linha_ficha
# class Aparelho(db.Model):
#     __tablename__ = 'aparelho'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     fabricante = db.Column(db.VARCHAR(20), nullable=False)
#     modelo = db.Column(db.VARCHAR(20), nullable=False)
#
#     def __init__(self, fabricante, modelo):
#         self.id = Util.__generate_id__()
#         self.fabricante = fabricante
#         self.modelo = modelo
#
#     @property
#     def dict_class(self):
#         dicionario = [{'Fabricante': self.fabricante}, {'Modelo': self.modelo}]
#         return dicionario
#
#     # @staticmethod
#     # @property
#     @classmethod
#     def dict_att(cls):
#         return [{'Fabricante', 'Modelo'}]
#
#
# # todo falta relacionar com aluno e funcionario(avaliador)
# class AvaliacaoFisica(db.Model):
#     __tablename__ = 'avaliacaofisica'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     avaliador_id = db.Column(db.INTEGER, nullable=False)
#     data_avaliacao = db.Column(db.DATE, nullable=False)
#     abdominal = db.Column(db.INTEGER, nullable=True)
#     flexoes_braco = db.Column(db.INTEGER, nullable=True)
#     altura = db.Column(db.DECIMAL(precision=3, scale=2), nullable=False)
#     peso = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     busto = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     braco_esquerdo = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     braco_direito = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     abdomen = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     cintura = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     quadril = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     culote = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     coxa_esquerda = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     coxa_direita = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     panturrilha_esquerda = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     panturrilha_direita = db.Column(db.DECIMAL(precision=4, scale=2), nullable=False)
#     aluno_id = db.Column(db.INTEGER, nullable=False)
#
#     def __init__(self, data, abdominal, flexoes, altura, peso, busto, bc_esq, bc_dir, abdomen, cintura, quadril, culote,
#                  coxa_esq, coxa_dir, pant_esq, pant_dir):
#         self.id = Util.__generate_id__()
#         self.data_avaliacao = data
#         self.abdominal = abdominal
#         self.flexoes_braco = flexoes
#         self.altura = altura
#         self.peso = peso
#         self.busto = busto
#         self.braco_esquerdo = bc_esq
#         self.braco_direito = bc_dir
#         self.abdomen = abdomen
#         self.cintura = cintura
#         self.quadril = quadril
#         self.culote = culote
#         self.coxa_esquerda = coxa_esq
#         self.coxa_direita = coxa_dir
#         self.panturrilha_esquerda = pant_esq
#         self.panturrilha_direita = pant_dir
#
#
# class Cargo(db.Model):
#     __tablename__ = 'cargo'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     nome = db.Column(db.VARCHAR(20), nullable=False)
#
#     def __init__(self, nome):
#         self.id = Util.__generate_id__()
#         self.nome = nome
#
#
# class Endereco(db.Model):
#     __tablename__ = 'endereco'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     rua = db.Column(db.VARCHAR(80), nullable=False)
#     numero = db.Column(db.VARCHAR(5), nullable=False)
#     cep = db.Column(db.VARCHAR(10), nullable=False)
#     complemento = db.Column(db.TEXT, nullable=True, default=None)
#     cidade = db.Column(db.VARCHAR(30), nullable=False)
#     bairro = db.Column(db.VARCHAR(20), nullable=False)
#
#     # RELATIONSHIP
#     # One to one
#     # unidade = db.relationship('Unidade', uselist=False, back_populates='endereco')
#     # One to many
#
#     def __init__(self, rua, numero, cep, complemento, cidade, bairro):
#         self.id = Util.__generate_id__()
#         self.rua = rua
#         self.numero = numero
#         self.cep = cep
#         self.complemento = complemento
#         self.cidade = cidade
#         self.bairro = bairro
#
#     def __repr__(self):
#         return '%s, %s %s - %s' % (self.rua, self.numero, self.bairro, self.cidade)
#
#
# # todo falta relacionar com aluno e linha_ficha
# class Ficha(db.Model):
#     __tablename__ = 'ficha'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     data_elaboracao = db.Column(db.DATE, nullable=False)
#     aluno_id = db.Column(db.INTEGER, nullable=False)
#
#     def __init__(self, data):
#         self.id = Util.__generate_id__()
#         self.data_elaboracao = data
#
#
# class Funcionario(db.Model):
#     __tablename__ = 'funcionario'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     registro = db.Column(db.VARCHAR(10), nullable=False, unique=True)
#     ativado = db.Column(db.BOOLEAN, default=True)
#     cargo_id = db.Column(db.VARCHAR(36), db.ForeignKey('cargo.id', name='FK_funcionario_cargo'), nullable=False)
#     pessoa_id = db.Column(db.VARCHAR(36), db.ForeignKey('pessoa.id', name='FK_funcionario_pessoa'), nullable=False)
#
#     def __init__(self, registro):
#         self.id = Util.__generate_id__()
#         self.registro = registro
#
#     # RELATIONSHIP
#     # One to one
#     cargo = db.relationship('Cargo',
#                             backref=backref('funcionario', uselist=False, lazy='joined', cascade='save-update'))
#     # one to many
#     modalidades = db.relationship('Modalidade', backref='funcionario', lazy='dynamic')
#
#
# # todo falta relacionar com aparelho e ficha
# class LinhaFicha(db.Model):
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     ciclo1 = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     ciclo2 = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     ciclo3 = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     ciclo4 = db.Column(db.DECIMAL(precision=5, scale=2), nullable=False)
#     aparelho_id = db.Column(db.VARCHAR(36), db.ForeignKey('aparelho.id'), nullable=False)
#     ficha_id = db.Column(db.VARCHAR(36), db.ForeignKey('ficha.id'), nullable=False)
#
#     def __init__(self):
#         self.id = Util.__generate_id__()
#
#
# class Modalidade(db.Model):
#     __tablename__ = 'modalidade'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     categoria = db.Column(db.VARCHAR(100), nullable=False)
#     nivel = db.Column(db.VARCHAR(20), nullable=True)
#     categoria_pai_id = db.Column(db.VARCHAR(36), db.ForeignKey('modalidade.id', name='FK_modalidade_categoria'),
#                                  nullable=True)
#     unidade_id = db.Column(db.VARCHAR(36), db.ForeignKey('unidade.id', name='FK_modalidade_unidade'), nullable=False)
#     professor_id = db.Column(db.VARCHAR(36), db.ForeignKey('funcionario.id', name='FK_modalidade_professor'),
#                              nullable=True)
#
#     def __init__(self, categoria, nivel):
#         self.id = Util.__generate_id__()
#         self.categoria = categoria
#         self.nivel = nivel
#
#     # RELATIONSHIP
#     # Self
#     categorias_pai = db.relationship('Modalidade')
#     # One to many
#     turma = db.relationship('Turma', backref='modalidade')
#     # many to one
#     unidade = db.relationship('Unidade', backref='modalidade')
#
#
# # todo falta relacionar com valor e aluno
# class Pagamento(db.Model):
#     __tablename__ = 'pagamento'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     tipo = db.Column(db.Enum('DEBITO', 'CREDITO', 'DINHEIRO'), nullable=False)
#     vencimento_data = db.Column(db.DATETIME, nullable=False)
#     referencia = db.Column(db.DATE, nullable=False)
#     status_pagamento = db.Column(db.Enum('EFETUADO', 'ATRASADO', 'PENDENTE'), nullable=False)
#     aluno_id = db.Column(db.INTEGER, nullable=False)
#     valor_plano_id = db.Column(db.INTEGER, nullable=False)
#
#     def __init__(self, tipo, vencimento_data, referencia, status):
#         self.id = Util.__generate_id__()
#         self.tipo = tipo
#         self.vencimento_data = vencimento_data
#         self.referencia = referencia
#         self.status_pagamento = status
#
#
# class Pessoa(db.Model):
#     __tablename__ = 'pessoa'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     nome = db.Column(db.VARCHAR(120), nullable=False)
#     nome_mae = db.Column(db.VARCHAR(120), nullable=False)
#     documento_tipo = db.Column(db.Enum('RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'), nullable=False)
#     documento_num = db.Column(db.VARCHAR(20), nullable=False)
#     endereco_id = db.Column(db.VARCHAR(36), db.ForeignKey('endereco.id', name='FK_pessoa_endereco'), nullable=False)
#     telefone = db.Column(db.VARCHAR(15), nullable=True, default=None)
#     usuario_id = db.Column(db.VARCHAR(36), db.ForeignKey('usuario.id', name='FK_pessoa_usuario'), nullable=False)
#
#     def __init__(self, nome, nome_mae, documento_tipo, documento_num, telefone):
#         self.id = Util.__generate_id__()
#         self.nome = nome
#         self.nome_mae = nome_mae
#         self.documento_tipo = documento_tipo
#         self.documento_num = documento_num
#         self.telefone = telefone
#
#     # RELATIONSHIP
#     # One to one
#     funcionario = db.relationship('Funcionario',
#                                   backref=backref("pessoa", uselist=False, lazy='joined', cascade='save-update'))
#     aluno = db.relationship('Aluno', backref=backref("pessoa", uselist=False, lazy='joined', cascade='save-update'))
#     # Many to one
#     endereco = db.relationship('Endereco', backref='pessoas')
#
#
# class Plano(db.Model):
#     __tablename__ = 'plano'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     valor = db.Column(db.DECIMAL(precision=6, scale=2), nullable=False)
#
#     def __init__(self, valor):
#         self.id = Util.__generate_id__()
#         self.valor = valor
#
#
# class Role(db.Model, RoleMixin):
#     __tablename__ = "role"
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     nome = db.Column(db.VARCHAR(80), unique=True)
#     descricao = db.Column(db.VARCHAR(255))
#
#     def __init__(self, name, description):
#         self.id = Util.__generate_id__()
#         self.nome = name
#         self.descricao = description
#
#     def __repr__(self):
#         return '<Role %r: %r>' % (self.id, self.nome)
#
#     def get_id(self):
#         return str(self.id)
#
#
# # todo falta relacionar com turma e modalidade
# class Sala(db.Model):
#     __tablename__ = 'sala'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     numero = db.Column(db.VARCHAR(5), nullable=False)
#
#     def __init__(self, numero):
#         self.id = Util.__generate_id__()
#         self.numero = numero
#
#
# class Turma(db.Model):
#     __tablename__ = 'turma'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     horario = db.Column(db.TIME, nullable=False)
#     modalidade_id = db.Column(db.VARCHAR(36), db.ForeignKey('modalidade.id', name='FK_turma_modalidade'), nullable=True)
#
#     def __init__(self, horario):
#         self.id = Util.__generate_id__()
#         self.horario = horario
#
#
# class Unidade(db.Model):
#     __tablename__ = 'unidade'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     nome = db.Column(db.VARCHAR(120), nullable=False)
#     telefone = db.Column(db.VARCHAR(15), nullable=True, default=None)
#     endereco_id = db.Column(db.VARCHAR(36), db.ForeignKey('endereco.id', name='FK_unidade_endereco'), nullable=False,
#                             unique=True)
#
#     # RELATIONSHIP
#     # One to one
#     endereco = db.relationship('Endereco', backref=backref('unidade', uselist=False, lazy='joined'),
#                                cascade="save-update")
#
#     def __init__(self, nome, telefone):
#         self.id = Util.__generate_id__()
#         self.nome = nome
#         self.telefone = telefone
#
#     @property
#     def dict_class(self):
#         dicionario = [{'Nome': self.nome}, {'Telefone': self.telefone}, {"endereco": self.endereco}]
#         return dicionario
#
#
# class Usuario(db.Model, UserMixin):
#     __tablename__ = "usuario"
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     username = db.Column(db.VARCHAR(80), unique=True, nullable=False)
#     password = db.Column(db.VARCHAR(95), nullable=False)
#     nome = db.Column(db.VARCHAR(200), nullable=False)
#     email = db.Column(db.VARCHAR(120), unique=True, nullable=False)
#     active = db.Column(db.BOOLEAN, default=True)
#     confirmed_at = db.Column(db.DATETIME)
#
#     # RELATIONSHIP
#     # One to one
#     pessoa = db.relationship('Pessoa', backref=backref("usuario", uselist=False, lazy='joined', cascade='save-update'))
#     # many to many
#     roles = db.relationship('Role', secondary='roles_users', backref=backref('usuario', lazy='dynamic'))
#
#     def __init__(self, username, password, nome, email):
#         self.id = Util.__generate_id__()
#         self.username = username
#         self.password = password
#         self.nome = nome
#         self.email = email
#         self.confirmed_at = datetime.now()
#
#     def __repr__(self):
#         return '<User %r: %r, %r>' % (self.id, self.username, self.name)
#
#     @property
#     def dict_class(self):
#         dicionario = [{'Nome': self.name}, {'Usuário': self.username}, {"e-mail": self.email}]
#         return dicionario
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return str(self.id)
#
#
# # Tabelas intermediarias
# class PlanoAluno:
#     __tablename__ = 'plano_aluno'
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     plano_id = db.Column(db.VARCHAR(36), db.ForeignKey('plano.id'))
#     aluno_id = db.Column(db.VARCHAR(36), db.ForeignKey('aluno.id'))
#
#     def __init__(self):
#         self.id = Util.__generate_id__()
#
#
# class RolesUsers(db.Model):
#     __tablename__ = "roles_users"
#
#     id = db.Column(db.VARCHAR(36), primary_key=True, default=Util.__generate_id__())
#     user_id = db.Column(db.VARCHAR(36), db.ForeignKey('user.id'))
#     role_id = db.Column(db.VARCHAR(36), db.ForeignKey('role.id'))
#
#     def __init__(self):
#         self.id = Util.__generate_id__()
#
#     __table_args__ = (
#         UniqueConstraint('user_id', 'role_id', name='unique_role_user'),
#     )
#
#     def __repr__(self):
#         return '<RoleUsers %r: %r, %r>' % (self.id, self.user_id, self.role_id)
