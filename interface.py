#!/usr/bin/python
from sendMailbox import sendMailbox


def reposeMode():
    sendMailbox("mode repose")


def waitingTempMode(temp):
    sendMailbox("mode waiting_temp " + str(int(temp)))

def prepareUsageMode(temp):
    sendMailbox("mode prepare_usage " + str(int(temp)))

def updateTemp():
    sendMailbox("updateTemp")