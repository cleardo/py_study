# coding=utf-8

import time
import sched


schedule = sched.scheduler(time.time, time.sleep)

print "begin:", time.time()

schedule.enter(2, 0)

print "end:", time.time()
