import inspect
from app.model.tables import User
from flask_sqlalchemy import SQLAlchemy


def __popular__(object):
    sig = inspect.signature(object)
    for c in sig.parameters.values():
        print(type(c))


user = User("pp", "123", "Pedro", 'email@email')

for _ in range(1):
    # user = User("pp", "123", "Pedro", 'email@email')
    # print(user)
    __popular__(User)
