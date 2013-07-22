import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['grobins2@gmail.com'])
SECRET_KEY = ')hq2m&o7-@be2-(6-__-6c-n(-5_#z(+nj)h1kfkg7&9dch%e9'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "=*nndg4fm#lvygzkkbcq6j!ll^z=mehp!l0w^g#&6qh8g($e%t"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = "blablabla"
RECAPTCHA_PRIVATE_KEY = "blahblabla"
RECAPTCHA_OPTIONS = {'theme':'white'}
