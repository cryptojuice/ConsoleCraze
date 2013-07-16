from app.users import constants as USER
from app.database import Base

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

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)