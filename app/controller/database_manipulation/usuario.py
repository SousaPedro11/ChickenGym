from werkzeug.security import generate_password_hash

from app import tables, app, Util
from app.controller.database_manipulation import DAO


def __admin__():
    user = DAO.buscar_por_criterio(tables.User, username='admin')
    passwd = generate_password_hash("admin")

    if not user:
        user = tables.User("admin", passwd, "ADMINISTRADOR", "admin@admin.com")
        DAO.transacao(user)
    elif user.password != passwd:
        user.password = passwd
        DAO.transacao(user)
    # print('Usuario cadastrado')


def __role__():
    roles = ["ADMINISTRADOR", "FUNCIONARIO", "GERENTE", "SECRETARIA", "PROFESSOR", "ALUNO"]

    for role_name in roles:
        _cadastrar_role(role_name)

    user = DAO.buscar_por_criterio(tables.User, username='admin')

    if not user.roles:
        user.roles.append(DAO.buscar_por_criterio(tables.Role, name='ADMINISTRADOR'))
        DAO.transacao(user)
    # print("Role cadastrado")


def _cadastrar_role(nome):
    role = DAO.buscar_por_criterio(tables.Role, name=nome)
    if not role:
        role = tables.Role(name=nome, description='')
        role.id = Util.__generate_id__()
        DAO.transacao(role)


@app.before_first_request
def seed():
    __admin__()
    __role__()
