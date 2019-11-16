from app.model.tables import User


def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    print(m)


user = User("pp", "123", "Pedro", 'email@email')

for _ in range(1):
    get_class('app.model.tables.User')
