from sqlalchemy import Column,Integer, DateTime, Boolean
import datetime
import session_manager

Base = session_manager.getBase()

class tempLog(Base):
    __tablename__ = 'tempLog'
    timestamp = Column(DateTime(), primary_key=True)
    temp = Column(Integer, nullable=False)
    synchronized = Column(Boolean,nullable=False, default=False)

    def __init__(self,temp):
        self.timestamp = datetime.datetime.now()
        self.temp = temp
        self.synchronized = False