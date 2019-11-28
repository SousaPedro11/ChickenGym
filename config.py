import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://iec_desenv:iec_desenv@localhost:3306/chickengym?charset=utf8mb4'
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://iec_desenv:iec_desenv@localhost:3306/chickengym?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'Miguel@12345'
