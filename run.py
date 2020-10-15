import os

from dotenv import load_dotenv

from app import manager

# Não excluir
from app.controller.database_manipulation import usuario

# manager.add_command('runserver', GunicornServer())
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


if __name__ == '__main__':
    manager.run()
