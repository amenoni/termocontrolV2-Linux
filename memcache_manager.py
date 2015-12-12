import memcache

mem =  memcache.Client(['127.0.0.1:11211'], debug=0)

def getMemCache():
    return mem