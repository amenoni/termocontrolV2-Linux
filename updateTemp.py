#!/usr/bin/python
import sys
import memcache

#Save the current temp sended by the arduino in a key named "CurrentTemp" in the memcached service
#usage: updateTemp.py XX

CurrentTemp = sys.argv[1]

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set('CurrentTemp', CurrentTemp)
