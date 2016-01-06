from data.usageLog import usageLog
from data.statistics import localStatistics,localStatisticsWeekdays
from sqlalchemy.sql import func
import session_manager
import config

session = session_manager.getSession()

usagesCount = session.query(usageLog).filter(usageLog.type == 0).count()

if usagesCount >= config.minUsagesForStatics:
    try:
        session.query(localStatistics).delete()
        session.commit()
    except:
        session.rollback()
        print ('error deleting current statics from db')





else:
    print("There's no enough uses to generate the statistics, use count= %s" % usagesCount)
    us = usageLog(type=0,synchronized=0)
    session.add(us)
    session.commit()