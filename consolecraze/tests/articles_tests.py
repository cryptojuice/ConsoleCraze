import unittest
from nose.tools import *

from consolecraze import app
from consolecraze.database import db_session, init_db, drop_all
from consolecraze.articles.models import Article

from werkzeug import generate_password_hash

class ArticlesTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        db_session.flush()
        drop_all()
