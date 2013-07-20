"""
Defines the users schema for database.
Added support methods for flask.ext.login
"""

from consolecraze.users import constants as USER
from consolecraze.database import Base

from sqlalchemy import Column, Integer, String, SmallInteger

class User(Base):
    __tablename__ = 'users_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(20))
    role = Column(SmallInteger, default=USER.USER)
    status = Column(SmallInteger, default=USER.NEW)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def get_status(self):
        return USER.STATUS[self.status]

    def get_role(self):
        return USER.ROLE[self.role]

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id():
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return '<User %r>' % (self.name)
