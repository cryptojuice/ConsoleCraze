from flask import Blueprint, request, render_template, flash, g, session,\
        redirect, url_for
from flask.ext.login import LoginManager, current_user, login_required, \
        logout_user

from werkzeug import check_password_hash, generate_password_hash

from app.database import db
from app.users.forms import RegisterForm, LoginForm
from app.users.models import User
from app.users.decorators import requires_login
from app import login_manager

mod = Blueprint('users', __name__, url_prefix='/users')

@login_manager.user_loader
def load_user(userid):
    print('load_user called')
    return User.query.get(userid)

@mod.route('/profile/')
@login_required
def home():
    return render_template("users/profile.html", user=g.user)

@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('users.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("users/login.html", form=form)

@mod.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@mod.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Registration form
    """
    form = RegisterForm(request.form)
    if  request.method == "POST" and form.validate():

        user = User(name=form.name.data, email=form.email.data, \
            password=generate_password_hash(form.password.data))

        db.add(user)
        db.commit()

        session['user_id'] = user.id

        flash('Thanks for registering')

        return redirect(url_for('users.home'))
    return render_template("users/register.html", form=form)
