from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///termocontrol.db')
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def getBase():
    return Base

def getSession():
    return session

def createTables():
    from data import templog,usagelog
    Base.metadata.create_all(engine)

