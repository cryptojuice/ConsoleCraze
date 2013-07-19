from nose.tools import *
import os
import app
import unittest
import tempfile


class UsersTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_one():
        return True

if __name__ == '__main__':
    unitest.main()
