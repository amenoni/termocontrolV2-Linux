#!/usr/bin/python
import sys
from data.usagelog import usageLog
import session_manager


usageType = sys.argv[1]

usage = usageLog(type=usageType)
session = session_manager.getSession()
session.add(usage)
session.commit()

