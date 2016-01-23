from sqlalchemy import Column,Float,String
import session_manager

Base = session_manager.getBase()

class hwConfig(Base):
    __tablename__ = 'hwconfig'
    variable = Column(String(),primary_key=True)
    value = Column(Float(),nullable=False)

    def __init__(self,variableName,value):
        self.variable = variableName
        self.value = value