import inspect
import sys

from flask_admin.contrib.sqla import ModelView

from app import db, admin
from app.model import tables

for name, obj in inspect.getmembers(sys.modules[tables.__name__]):
    print(name, obj)
    if inspect.isclass(obj):
        admin.add_view(ModelView(obj, db.session))
