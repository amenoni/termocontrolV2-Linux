from data.templog import tempLog
import config
import session_manager
import requests



session = session_manager.getSession()


def sendTempLogs():

    unsincronized_logs = session.query(tempLog).filter(tempLog.synchronized == False)

    url = "%s/templogs/?format=json" % config.apiURL
    headers = {'Content-Type': 'application/json'}

    for log in unsincronized_logs:
        data = '{"temp": "%s", "timestamp_UTC":"%s"}' %(log.temp, log.timestamp_UTC)
        try:
            r = requests.post(url,headers=headers, data=data)
            log.synchronized = True
            session.add(log)
        except:
            print("ERROR")


    session.commit()