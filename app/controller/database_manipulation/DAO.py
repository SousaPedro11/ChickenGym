from app import db


def transacao(objeto):
    db.session.add(objeto)
    db.session.commit()
    db.session.close()


def buscar_por_criterio(table, **filtros):
    return table.query.filter_by(**filtros).first()


def buscar_por_criterio_bool(table, *filtros):
    return table.query.filter(*filtros).first()


def busca_join_composto_com_criterio(table1, table2, table3, *filtro):
    return table1.query.join(table2).join(table3).filter(*filtro).add_entity(table2).add_entity(table3).all()


def buscar_todos(table, *order_by):
    return table.query.order_by(*order_by).all()


def buscar_todos_por_criterio(table, **filtros):
    return table.query.filter_by(**filtros).all()


def deletar(objeto):
    db.session.delete(objeto)
    db.session.commit()
    db.session.close()
