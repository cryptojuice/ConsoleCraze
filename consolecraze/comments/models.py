from consolecraze.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship




class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))

    def __init__(self, content, user_id, article_id):
        self.content = content
        self.user_id = user_id
        self.article_id = article_id

    def __repr__(self):
        return "<user_id(%s) submitted Comment('%s') to article_id(%s)>" % \
                (self.user_id, self.content, self.article_id)
