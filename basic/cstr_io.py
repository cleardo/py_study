# coding=utf-8

__author__ = 'donglin'


from cStringIO import StringIO


str1 = StringIO()

str1.write("我们")
# str1.write("hello")

str1.seek(0)

print str1.read(1), str1.read(2)

