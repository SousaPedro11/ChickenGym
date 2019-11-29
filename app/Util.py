from uuid import uuid4


def __generate_id__():
    codigo = uuid4()
    return str(codigo)


# print(len(__generate_id__()))
