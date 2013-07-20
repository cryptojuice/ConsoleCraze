import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.test'

import unittest
from nose.tools import *

from consolecraze import app
from consolecraze.database import db_session, init_db, drop_all

from werkzeug import generate_password_hash, check_password_hash


class UsersTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        db_session.flush()
        drop_all()


    def login(self, username, password):
        return self.app.post('/users/login/', data=dict(
            username=username,
            password=generate_password_hash(password)), follow_redirects=True)

    def logout(self):
        return self.app.get('/users/logout/', follow_redirects=True)

    def test_login(self):
        rv = self.login('iznasty@gmail.com', 'temppassword')
        print(rv.data)
