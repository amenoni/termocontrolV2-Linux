#!/usr/bin/python
from sendMailbox import sendMailbox
from data.hwConfig import hwConfig
import session_manager



def reposeMode():
    sendMailbox("mode repose")


def waitingTempMode(temp):
    sendMailbox("mode waiting_temp " + str(int(temp)))

def prepareUsageMode(temp):
    sendMailbox("mode prepare_usage " + str(int(temp)))

def updateTemp():
    sendMailbox("updateTemp")

def writeHWconfig():
    session = session_manager.getSession()
    globalVariables = session.query(hwConfig).all()
    for var in globalVariables:
        sendMailbox("config %s %s" % (var.variable,var.value))