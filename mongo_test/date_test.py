# coding=utf-8
from datetime import datetime
from time import time

__author__ = 'donglin'


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(__name__)


from cof.co_time import CoTime


# 获取昨天的日期
time_o = CoTime(time())

dt1 = time_o.get_dt()

logger.info(dt1)

yest_time_o = CoTime(time_o.get_ts() - 86400)

logger.info(yest_time_o)

dt = datetime(yest_time_o.get_year(), yest_time_o.get_month(), yest_time_o.get_day(), 0, 0, 0)

logger.info(dt)

# 查询记录数，写入数据库

# mysql数据库

