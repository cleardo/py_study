# coding=utf-8
__author__ = 'donglin'


a = 2
b = "test"

exec "a = %s" % "b"

print a
