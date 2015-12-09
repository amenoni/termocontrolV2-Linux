#!/usr/bin/python
from sendMailbox import sendMailbox

'''
by the way the arduino modes are programed this method actualy cant work becouse
the current mode is going to change the heater status
'''
def heaterControl(heaterOn):
    if heaterOn == True:
        sendMailbox("heater on")
    else:
        sendMailbox("heater off")


def reposeMode():
    sendMailbox("mode repose")


def waitingTempMode(temp):
    sendMailbox("mode waiting_temp " + str(temp))

def prepareUsageMode(temp):
    sendMailbox("mode prepare_usage " + str(temp))
