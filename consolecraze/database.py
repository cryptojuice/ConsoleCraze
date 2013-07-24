import os
from consolecraze import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],\
        convert_unicode=True, echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False,\
#    autoflush=False,
#    bind=engine))
Session = sessionmaker(bind=engine)
db_session = Session()

Base = declarative_base()
#Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

def drop_all():
    Base.metadata.drop_all(bind=engine)
