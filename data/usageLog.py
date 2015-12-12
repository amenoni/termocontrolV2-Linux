from sqlalchemy import Column,Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
import session_manager

Base = session_manager.getBase()

USAGE_STARTED = 0
USAGE_FINISHED = 1

class usageLog(Base):
    __tablename__ = 'usageLog'
    timestamp_UTC = Column(DateTime(), default=func.now(), primary_key=True)
    type = Column(Integer,nullable=False)
    synchronized = Column(Boolean,nullable=False, default=False)