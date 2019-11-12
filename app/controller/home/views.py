from flask import url_for, render_template
from flask_login import login_required
from werkzeug.utils import redirect

from . import home


@home.route('/')
def index():
    return redirect(url_for('auth.login'))


@home.route('/cg/')
@home.route('/cg/index/')
def cg():
    return redirect(url_for('auth.login'))


@home.route('/cg/home/')
@login_required
def home():
    return render_template('home.html')
