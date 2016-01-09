#!/usr/bin/python
import sys
from data.usageLog import usageLog
import session_manager

"""
The arduino sends this parameters to this command
//linux side usage event constants
const int USAGE_STARTED = 0;
const int USAGE_FINISHED = 1;
"""


usageType = sys.argv[1]

usage = usageLog(usageType,False)
session = session_manager.getSession()
session.add(usage)
session.commit()

