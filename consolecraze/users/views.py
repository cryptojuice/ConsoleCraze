from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for
from flask.ext.login import LoginManager, current_user, login_required, \
        logout_user

from werkzeug import check_password_hash, generate_password_hash

from consolecraze.users.forms import RegisterForm, LoginForm
from consolecraze.users.models import User
from consolecraze.users.decorators import requires_login
from consolecraze import login_manager

from consolecraze.database import db_session

mod = Blueprint('users', __name__, url_prefix='/users')

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@mod.route('/profile/')
@login_required
def profile():
    return render_template("users/profile.html", user=g.user)

@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('frontend.index'))
        error = 'Incorrect e-mail or password'
    return render_template("users/login.html", form=form, error=error)

@mod.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('frontend.index'))


@mod.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Registration form
    """
    form = RegisterForm(request.form)
    if  request.method == "POST" and form.validate():

        user = User(name=form.name.data, email=form.email.data, \
            password=generate_password_hash(form.password.data))

        db_session.add(user)
        db_session.commit()

        session['user_id'] = user.id

        flash('Thanks for registering')

        return redirect(url_for('frontend.index'))
    return render_template("users/register.html", form=form)
