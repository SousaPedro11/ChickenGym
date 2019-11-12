from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash

from app.controller.default import is_safe_url
from app.model.forms import LoginForm
from app.model.tables import User
from . import auth


@auth.route('/cg/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = LoginForm()
    if form.validate_on_submit():
        if '@' in form.username.data:
            user = User.query.filter_by(email=form.username.data.lower()).first()
        else:
            user = User.query.filter_by(username=form.username.data.lower()).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash("Sessão Iniciada")
                next_url = request.args.get('next')
                if not is_safe_url(next_url):
                    return abort(400)
                return redirect(next_url or url_for("home.home"))
            else:
                flash("Senha Inválida")
    return render_template('login.html', form=form)


@auth.route("/cg/logout/")
@login_required
def logout():
    logout_user()
    flash("Sessão Finalizada")
    return redirect(url_for("home.cg"))
