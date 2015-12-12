#!/usr/bin/python
import sys
from data.templog import tempLog
import session_manager
import memcache_manager

'''
Save the current temp sended by the arduino in a key named "CurrentTemp" in the memcached service
usage: updateTemp.py XX
to get the value mc.get('CurrentTemp')

If the new temp value is diferent of the last sended we log the current temp in de local database
'''

CurrentTemp = sys.argv[1]
mc = memcache_manager.getMemCache()


if(CurrentTemp != mc.get('CurrentTemp')):
    #set the new value in the memcache
    mc.set('CurrentTemp', CurrentTemp)
    session = session_manager.getSession()
    newLog = tempLog(temp=CurrentTemp)
    session.add(newLog)
    session.commit()