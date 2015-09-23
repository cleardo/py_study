# coding=utf-8
__author__ = 'linzh'

import sys

print sys.stdin

sys.stdout.write("hello")

fp = open("test.tpl", 'r')

print "\n"

# print fp.readline()

c = fp.read(1)
print repr(c)
print c == '\f'
print repr('\f')

print fp.read(3)

# sys.stdin.read(1)
