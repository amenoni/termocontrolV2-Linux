from sqlalchemy import Column,Integer, DateTime, Boolean
import datetime
import session_manager
import radar

Base = session_manager.getBase()



class usageLog(Base):
    USAGE_STARTED = 0
    USAGE_FINISHED = 1

    __tablename__ = 'usageLog'
    timestamp_UTC = Column(DateTime(), primary_key=True)
    hour = Column(Integer,nullable=False)
    weekday = Column(Integer,nullable=False)
    type = Column(Integer,nullable=False)
    synchronized = Column(Boolean,nullable=False, default=False)

    def __init__(self,type,synchronized):
        self.timestamp_UTC = datetime.datetime.now()
        self.hour = self.timestamp_UTC.hour
        self.weekday = self.timestamp_UTC.weekday()
        self.type = type
        self.synchronized = synchronized


    def generatRandomTimeValues(self): #use it only to generate testing usageLog data
        self.timestamp_UTC = radar.random_date(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7))
        self.hour = self.timestamp_UTC.hour
        self.weekday = self.timestamp_UTC.weekday()