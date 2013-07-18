import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['grobins2@gmail.com'])
SECRET_KEY = 'needsecretkey'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "anothersecretkey"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = "blablabla"
RECAPTCHA_PRIVATE_KEY = "blahblabla"
RECAPTCHA_OPTIONS = {'theme':'white'}
