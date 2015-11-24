# coding=utf-8
from datetime import datetime
from time import time

__author__ = 'donglin'


"""
获取昨天时间区间

"""

from cof.co_time import CoTime

time_o = CoTime(time())

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(__name__)

logger.info(time_o.t_info)
logger.info(time_o.get_day())

dt = datetime(time_o.get_year(), time_o.get_month(), time_o.get_day(), 0, 0, 0, 0)

logger.info(dt)


