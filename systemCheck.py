from datetime import datetime, timedelta
import session_manager
import interface
import config
import  memcache_manager
from data import statistics

'''
MemCache values
CurrentStatus   - PreparingUsage
                - WaitingTemp
                - Repose
                - NoData <- when there's no statistics info

WaitingTemp  - Value
'''

session = session_manager.getSession()
mc = memcache_manager.getMemCache()

def getProbabilityForHour(hour,weekday):
    generalProb = session.query(statistics.localStatistics).get(hour)
    weekdayProb = session.query(statistics.localStatisticsWeekdays).get((weekday,hour))

    if(generalProb >= weekdayProb):
        currentHourProb = generalProb
    else:
        currentHourProb = weekdayProb

    return currentHourProb


currentTime = datetime.now()


if session.query(statistics.localStatistics).count() > 0:
    currentProb = 0

    if currentTime.minute > 60 - config.bufferTimeToNextHourUse:
        nextHour = currentTime + timedelta(hours=1)
        nextHour = nextHour.hour
        currentProb = getProbabilityForHour(nextHour,currentTime.weekday())
    else: # use the current hour probabilitys
        currentProb = getProbabilityForHour(currentTime.hour,currentTime.weekday())


    if currentProb.probability >= 70:
        interface.prepareUsageMode(config.maxTemp)  # TODO change this value to the target max temp
        mc.set('CurrentStatus','PreparingUsage')
    else:
        interface.waitingTempMode(config.maxTemp * currentProb.probability)
        mc.set('CurrentStatus','WaitingTemp')
        mc.set('WaitingTemp',config.maxTemp * currentProb.probability)


else:#if there's no statistics
    interface.prepareUsageMode(config.maxTemp)  # TODO change this value to the target max temp
    mc.set('CurrentStatus','NoData')


interface.updateTemp() # ask the arduino to retrive the current temp value for logging proposes