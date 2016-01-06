from sqlalchemy import Column,Integer
import session_manager

Base = session_manager.getBase()

class localStatistics(Base):
    __tablename__ = 'localStatistics'
    hour = Column(Integer,nullable=False,primary_key=True)
    probability = Column(Integer,nullable=False)

class localStatisticsWeekdays(Base):
    __tablename__ = 'localStatisticsWeeksdays'
    day = Column(Integer,nullable=False,primary_key=True)
    hour = Column(Integer,nullable=False,primary_key=True)
    probability = Column(Integer,nullable=False)