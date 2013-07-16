from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app.db', convert_unicode = True)
db = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine))

Base = declarative_base()
Base.query = db.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)