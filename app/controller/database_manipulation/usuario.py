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


# def __role__():
#     role = DAO.buscar_por_criterio(tables.Role, name='ADMINISTRADOR')
#     if not role:
#         role = tables.Role(name="ADMINISTRADOR")
#         DAO.transacao(role)
#
#     user = DAO.buscar_por_criterio(tables.User, username='admin')
#     role = DAO.buscar_por_criterio(tables.Role, name='ADMINISTRADOR')
#     user_id = int(user.get_id())
#     role_id = int(role.get_id())
#     roles_user = DAO.buscar_por_criterio(RolesUsers, user_id=user_id, role_id=role_id)
#     if not roles_user:
#         roles_user = tables.RolesUsers(user_id=user_id, role_id=role_id)
#         DAO.transacao(roles_user)
