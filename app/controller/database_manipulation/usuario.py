from werkzeug.security import generate_password_hash

from app import tables
from app.controller.database_manipulation import DAO


def __admin__():
    user = DAO.buscar_por_criterio(tables.User, username='admin')
    passwd = generate_password_hash("admin")

    if not user:
        user = tables.User("admin", passwd, "ADMINISTRADOR", "admin@admin.com")
        DAO.transacao(user)
    else:
        user.password = passwd
        DAO.transacao(user)


def __role__():
    role = DAO.buscar_por_criterio(tables.Role, name='ADMINISTRADOR')
    if not role:
        role = tables.Role(name="ADMINISTRADOR")
        DAO.transacao(role)

    user = DAO.buscar_por_criterio(tables.User, username='admin')

    # join = DAO.busca_join_composto_com_criterio(
    #     tables.RolesUsers,
    #     tables.User,
    #     tables.Role,
    #     tables.User.username == 'admin',
    #     tables.Role.name == "ADMINISTRADOR")
    #
    # print(join)
    if not user.roles:
        user.roles.append(role)
        DAO.transacao(user)
