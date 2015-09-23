# coding=utf-8
__author__ = 'Administrator'

"""
异常捕获
"""


import sys, traceback


def lumberjack():
    bright_side_of_death()


def bright_side_of_death():
    return tuple()[0]

try:
    lumberjack()
#except Exception, exc_val:
#   print Exception, exc_val
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print "系统执行信息"
    print type(exc_type)
    # 错误消息
    print exc_value
    # traceback对象
    print exc_traceback

    print "*** print_tb:"
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

    print "*** print_exception:"
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print "*** print_exc:"
    traceback.print_exc()
    print "*** format_exc, first and last line:"
    formatted_lines = traceback.format_exc().splitlines()
    print formatted_lines[0]
    print formatted_lines[-1]
    print "*** format_exception:"
    print repr(traceback.format_exception(exc_type, exc_value,
                                          exc_traceback))
    print "*** extract_tb:"
    print repr(traceback.extract_tb(exc_traceback))

    print "*** format_tb:"
    print repr(traceback.format_tb(exc_traceback))

    print "*** tb_lineno:", exc_traceback.tb_lineno
