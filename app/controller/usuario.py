from app import tables, db


def __admin__():
    r = tables.User.query.filter_by(username='admin').first()
    if not r:
        i = tables.User("admin", "admin", "Administrador", "admin@admin")
        db.session.add(i)
        db.session.commit()
        db.session.close()
