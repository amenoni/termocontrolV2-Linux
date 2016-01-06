from crontab import CronTab
import session_manager
import sys

cron = CronTab(user=True)
pythonPath = sys.executable

#create the database and the tables
session_manager.createTables()

#create the crontab jobs
generateStatisticsJob = cron.new('%s generateLocalStatics.py' % pythonPath)
generateStatisticsJob.hour.on(0)
cron.write()
