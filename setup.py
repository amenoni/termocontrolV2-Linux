from crontab import CronTab
import session_manager
import os,sys, inspect

cron = CronTab(user=True)
pythonPath = sys.executable
files_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#create the database and the tables
session_manager.createTables()

#create the crontab jobs
cron.remove_all() # remove all current cron jobs
generateStatisticsJob = cron.new('%s %s/generateLocalStatics.py' % (pythonPath,files_dir))
generateStatisticsJob.hour.on(0)

checkSystemJob = cron.new('%s %s/systemCheck.py' % (pythonPath,files_dir))
checkSystemJob.minute.every(5)
cron.write()
