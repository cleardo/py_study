# coding=utf-8

"""
scribe logger 日志记录测试
"""

__author__ = 'Administrator'

from cof.log import ScribeLogger

logger = ScribeLogger()

logger.write("hello, world")

logger.close()

