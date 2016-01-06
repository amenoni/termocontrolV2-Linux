from sqlalchemy import Column,Integer,Float
import session_manager

Base = session_manager.getBase()

class localStatistics(Base):
    __tablename__ = 'localStatistics'
    hour = Column(Integer,nullable=False,primary_key=True)
    probability = Column(Float,nullable=False)

    def __init__(self,hour,prob):
        self.hour = hour
        self.probability = prob


class localStatisticsWeekdays(Base):
    __tablename__ = 'localStatisticsWeekdays'
    day = Column(Integer,nullable=False,primary_key=True)
    hour = Column(Integer,nullable=False,primary_key=True)
    probability = Column(Float,nullable=False)

    def __init__(self,day,hour,prob):
        self.day = day
        self.hour = hour
        self.probability = prob