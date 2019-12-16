from app import manager

# Não excluir
from app.controller.database_manipulation import usuario

# manager.add_command('runserver', GunicornServer())

if __name__ == '__main__':
    manager.run()
