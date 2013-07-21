import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.test'

import unittest
from nose.tools import *

from consolecraze import app
from consolecraze.database import db_session, init_db, drop_all
from consolecraze.users.models import User

from werkzeug import generate_password_hash


class UsersTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        db_session.flush()
        drop_all()


    def login(self, email, password):
        return self.app.post('/users/login/', data=dict(
            email=email,
            password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/users/logout/', follow_redirects=True)

    def test_unauthorized(self):
        rv = self.app.get('/users/profile/')
        assert rv.status_code == 401

    def test_login(self):
        user = User(name='admin', email='admin@consolecraze.net', 
                password=generate_password_hash('temppassword'))
        db_session.add(user)
        db_session.commit()
        rv = self.login('admin@consolecraze.net', 'temppassword')
        assert "Hi" in str(rv.data)
