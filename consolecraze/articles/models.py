from consolecraze.database import Base

from sqlalchemy import Column, Integer, String, SmallInteger

class Article(Base):
    __tablename__ = "articles_article"
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    summary = Column(String(140))
    url = Column(String(200))
    thumbnail_url = Column(String(200))
    user_id = Column(Integer)
    upvoted_by = Column(Integer)
    downvoted_by = Column(Integer)

    def __init__(self, title=None, summary=None, url=None,
            user_id=None, thumbnail_url=None):
        self.title = title
        self.summary = summary
        self.url = url
        self.user_id = user_id
        self.thumbnail_url = thumbnail_url

    def __repr__(self):
        return "Article %s" % (self.title)
