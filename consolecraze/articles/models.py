from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref

from consolecraze.database import Base

class Article(Base):

    """Defines Article tables for database"""

    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    content = Column(String)
    url = Column(String(200))
    image_url = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship('Comment', backref='article') 
    upvoted_by = Column(Integer)
    downvoted_by = Column(Integer)

    def __init__(self, title, content, url,
            user_id, image_url=None):

        # Note eventually add default image_url to import

        self.title = title
        self.content = content
        self.url = url
        self.user_id = user_id
        self.image_url = image_url

    def __repr__(self):
        return "user_id(%s) submitted Article.title(%s)" % (self.user_id, self.title)
