# coding=utf-8

import time
import sched


schedule = sched.scheduler(time.time, time.sleep)

def func(string1, float1):
    print "now is", time.time()

print "begin:", time.time()

schedule.enter(2, 0, func, ("test1", time.time()))
schedule.run()

print "end:", time.time()
