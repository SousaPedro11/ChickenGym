from flask import Blueprint

database_manipulation = Blueprint('database_manipulation', __name__)

from . import views
