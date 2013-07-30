from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from consolecraze.database import Base

class Vote(Base):

    """Defines Votes tables for database"""

    __tablename__ = "votes"
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    upvoted = Column(Boolean)
    downvoted = Column(Boolean)

    def __init__(self, article_id, user_id, upvoted = False, downvoted = False):

        self.article_id = article_id
        self.user_id = user_id
        self.upvoted = upvotes
        self.downvoted = downvotes

    def __repr__(self):
        return "user_id(%s) voted on article_id(%s)" % (self.user_id,
                self.article_id)
