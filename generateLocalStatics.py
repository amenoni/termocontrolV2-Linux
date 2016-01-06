from __future__ import division
from data.usageLog import usageLog
from data.statistics import localStatistics,localStatisticsWeekdays
import session_manager
import config

session = session_manager.getSession()

usagesCount = session.query(usageLog).filter(usageLog.type == 0).count()

if usagesCount >= config.minUsagesForStatics:
    try:
        session.query(localStatistics).delete()
        session.query(localStatisticsWeekdays).delete()
        session.commit()
    except:
        session.rollback()
        print ('error deleting current statics from db')

    #Generate the local statistics
    for hour in range(0,24):
        hourCount = session.query(usageLog).filter(usageLog.hour == hour).count()
        probability = float(hourCount / usagesCount)
        local_statistics = localStatistics(hour,probability)
        session.add(local_statistics)

    try:
        session.commit()
    except ValueError:
        print("there was a problem saving the local probability's %s" % ValueError)

    #Generate the local statistics for the weekdays
    for day in range(0,7):
        dayUsagesCount = session.query(usageLog).filter(usageLog.type == 0, usageLog.weekday == day).count()
        for hour in range(0,24):
            hourCount = session.query(usageLog).filter(usageLog.hour == hour,usageLog.weekday == day).count()
            probability = float(hourCount / dayUsagesCount)
            local_statistics_weekday = localStatisticsWeekdays(day,hour,probability)
            session.add(local_statistics_weekday)

    try:
        session.commit()
    except ValueError:
        print("there was a problem saving the local probability's %s" % ValueError)

else:
    print("There's no enough uses to generate the statistics, use count= %s" % usagesCount)
    ''' Uncomment to generate test usageLog data
    for i in range(0,30):
        us = usageLog(0,0)
        us.generatRandomTimeValues()
        session.add(us)
    session.commit()'''