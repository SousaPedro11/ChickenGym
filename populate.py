import inspect

from app.model.tables import Aparelho

# def get_class( kls ):
#     parts = kls.split('.')
#     module = ".".join(parts[:-1])
#     m = __import__( module )
#     for comp in parts[1:]:
#         m = getattr(m, comp)
#     print(m)
#
#
# user = User("pp", "123", "Pedro", 'email@email')
#
# for _ in range(1):
#     get_class('app.model.tables.User')

fie = inspect.getmembers(Aparelho, lambda a: not (inspect.isroutine(a)))
lista = [a for a in fie if
         not ((a[0].startswith('__') and a[0].endswith('__')) or a[0].startswith('_'))]
print(lista)
