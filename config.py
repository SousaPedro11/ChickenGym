import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aluno:aluno01@localhost:3306/chickengym?charset=utf8mb4'
DATABASE_URI = os.getenv('DATABASE_URI')
if DATABASE_URI is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2' + DATABASE_URI

# SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(16))
THREADED = True
