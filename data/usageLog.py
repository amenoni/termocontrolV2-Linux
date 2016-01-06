from sqlalchemy import Column,Integer, DateTime, Boolean
from sqlalchemy.sql import func
import datetime
import session_manager

Base = session_manager.getBase()

USAGE_STARTED = 0
USAGE_FINISHED = 1

class usageLog(Base):
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