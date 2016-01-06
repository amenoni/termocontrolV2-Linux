from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

engine = create_engine(config.DBpath)
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def getBase():
    return Base

def getSession():
    return session

def createTables():
    from data import templog,usageLog,statistics
    Base.metadata.create_all(engine)

