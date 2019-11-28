from app import db


def transacao(objeto):
    db.session.add(objeto)
    db.session.commit()
    db.session.close()


def buscar_por_criterio(table, **kwargs):
    return table.query.filter_by(**kwargs).first()
