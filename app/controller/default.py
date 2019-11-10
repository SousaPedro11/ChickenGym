from urllib.parse import urlparse, urljoin

from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

from app import app, lm
from app.model.forms import LoginForm
from app.model.tables import User


@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/cg/')
@app.route('/cg/index/')
def cg():
    return redirect(url_for('login'))
    # return render_template('index.html')


@app.route('/cg/home/')
@login_required
def home():
    return render_template('home.html')


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/cg/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Logged in")
            next_url = request.args.get('next')
            if not is_safe_url(next_url):
                return abort(400)
            return redirect(next_url or url_for("home"))
        else:
            flash("Invalid Login")
    return render_template('login.html', form=form)


@app.route("/cg/logout/")
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for("cg"))


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html')
