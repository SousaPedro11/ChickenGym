import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aluno:aluno01@localhost:3306/chickengym?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///storage.db')
# SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(16))
THREADED = True
