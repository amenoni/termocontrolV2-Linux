from crontab import CronTab
import session_manager
import os,sys, inspect
from data.hwConfig import hwConfig
from interface import writeHWconfig

cron = CronTab(user=True)
pythonPath = sys.executable
files_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#create the crontab jobs
cron.remove_all() # remove all current cron jobs
generateStatisticsJob = cron.new('%s %s/generateLocalStatics.py' % (pythonPath,files_dir))
generateStatisticsJob.hour.on(0)

checkSystemJob = cron.new('%s %s/systemCheck.py' % (pythonPath,files_dir))
checkSystemJob.minute.every(1)
cron.write()

#create the database and the tables
session_manager.createTables()

#Create arduino side global values variables
session = session_manager.getSession()
session.query(hwConfig).delete()

PERCENTAGE_TEMP_FOR_READY = hwConfig("PERCENTAGE_TEMP_FOR_READY",0.9)
tempValidTimeSec = hwConfig("tempValidTimeSec",30)
InUseSensingTempTimeSec = hwConfig("InUseSensingTempTimeSec",60)
MaxTempDropForUseDetectedPercent = hwConfig("MaxTempDropForUseDetectedPercent",-5)
MaxTempUpForDetectUseFinishedPercent = hwConfig("MaxTempUpForDetectUseFinishedPercent",5)


session.add(PERCENTAGE_TEMP_FOR_READY)
session.add(tempValidTimeSec)
session.add(InUseSensingTempTimeSec)
session.add(MaxTempDropForUseDetectedPercent)
session.add(MaxTempUpForDetectUseFinishedPercent)
session.commit()
writeHWconfig()
