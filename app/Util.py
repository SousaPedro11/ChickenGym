from uuid import uuid4
from datetime import datetime


def __generate_id__():
    codigo = uuid4()
    return str(codigo)


def __gerar_num_matricula__():
    matricula = str(datetime.now()).replace('-', '').replace(':', '').replace(' ', '').replace('.', '')
    return matricula
# print(len(__generate_id__()))


def __equals(obj, other):
    hobj = hash(frozenset(vars(obj).items()))
    hother = hash(frozenset(vars(other).items()))
    print(obj, hobj)
    print(other, hother)
    return hobj == hother
