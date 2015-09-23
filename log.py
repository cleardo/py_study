# coding=utf-8

"""
日志测试程序
"""
__author__ = 'Administrator'

import logging

# 定义文件名，以及执行的级别
logging.basicConfig(filename='example.log', level=logging.DEBUG)

logging.debug('This message should go to the log file该日志会被写入日志')

logging.info('So should this')

logging.warning('And this, too')
