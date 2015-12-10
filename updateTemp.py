#!/usr/bin/python
import os
import sys
import memcache
from sqlalchemy import Column,Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class tempLog(Base):
    __tablename__ = 'tempLog'
    timestamp_UTC = Column(DateTime(), default=func.now(), primary_key=True)
    temp = Column(Integer, nullable=False)
    synchronized = Column(Boolean,nullable=False, default=False)

'''
Save the current temp sended by the arduino in a key named "CurrentTemp" in the memcached service
usage: updateTemp.py XX
to get the value mc.get('CurrentTemp')

If the new temp value is diferent of the last sended we log the current temp in de local database
'''

CurrentTemp = sys.argv[1]
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

engine = create_engine('sqlite:///termocontrol.db')
Base.metadata.create_all(engine)

if(CurrentTemp != mc.get('CurrentTemp')):
    #set the new value in the memcache
    mc.set('CurrentTemp', CurrentTemp)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    newLog = tempLog(temp=CurrentTemp)
    session.add(newLog)
    session.commit()