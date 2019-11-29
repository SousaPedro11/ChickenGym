from app import db


def transacao(objeto):
    db.session.add(objeto)
    db.session.commit()
    db.session.close()


def buscar_por_criterio(table, **filtros):
    return table.query.filter_by(**filtros).first()


def busca_join_composto_com_criterio(table1, table2, table3, *filtro):
    return table1.query.join(table2).join(table3).filter(*filtro).add_entity(table2).add_entity(table3).all()
