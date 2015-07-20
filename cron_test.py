# coding=utf-8

import schedule

import time

def job():
    print "working...", time.time()

# 每隔10秒调用job
schedule.every(10).seconds.do(job)

# 每隔10分钟调用job
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
