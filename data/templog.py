from sqlalchemy import Column,Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
import session_manager

Base = session_manager.getBase()

class tempLog(Base):
    __tablename__ = 'tempLog'
    timestamp_UTC = Column(DateTime(), default=func.now(), primary_key=True)
    temp = Column(Integer, nullable=False)
    synchronized = Column(Boolean,nullable=False, default=False)



