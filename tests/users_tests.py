from nose.tools import *
import os
from consolecraze import app, database
import unittest
import tempfile


class UsersTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        database.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_one(self):
        return True

if __name__ == '__main__':
    unitest.main()
