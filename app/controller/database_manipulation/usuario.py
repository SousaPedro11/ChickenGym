from werkzeug.security import generate_password_hash

from app import tables, db


def __admin__():
    r = tables.User.query.filter_by(username='admin').first()
    passwd = generate_password_hash("admin")
    if not r:
        i = tables.User("admin", passwd, "ADMINISTRADOR", "admin@admin.com")
        db.session.add(i)
        db.session.commit()
        db.session.close()
    else:
        r.password = passwd
        db.session.commit()
        db.session.close()
