#!./venv/bin/python3

import os
import subprocess

import sys
from flask_script import Command, Option

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, 'src'))


# Originally from https://gist.github.com/menghan/9a632bbb0acb445f4f3a
class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def get_options(self):
        from gunicorn.config import make_settings

        settings = make_settings()
        options = []

        for setting, klass in settings.items():
            if klass.cli:
                if klass.const is not None:
                    options.append(Option(*klass.cli, const=klass.const, action=klass.action))
                else:
                    options.append(Option(*klass.cli, action=klass.action))

        return options

    def run(self, *args, **kwargs):
        run_args = sys.argv[2:]
        # !!!!! Change your app here !!!!!
        run_args.append('--reload')
        run_args.extend(['-k', 'flask_sockets.worker'])
        run_args.append('app:app')
        subprocess.Popen([os.path.join(os.path.dirname(sys.executable), 'gunicorn')] + run_args).wait()


# !!!!! Change your app here !!!!!
from app import manager

#Não excluir
from app.controller.database_manipulation import usuario

manager.add_command('runserver', GunicornServer())

if __name__ == '__main__':
    manager.run()
