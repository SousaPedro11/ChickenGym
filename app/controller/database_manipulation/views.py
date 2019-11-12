from flask import flash, redirect, url_for, render_template
from werkzeug.security import generate_password_hash

from app import db
from app.model.forms import RegistrationForm
from app.model.tables import User
from . import database_manipulation


@database_manipulation.route('/pagina/usuario/cadastro', methods=['GET', 'POST'])
def cadastrar_usuario():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(username, password, name, email)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('auth.login'))
    return render_template('conteudo.html', form=form)
