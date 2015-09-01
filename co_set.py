# coding=utf-8

__author__ = 'linzh'

t = set()

t.add(1)

s = set()

s.add(1)

diff = t.difference(s)

if len(diff) == 0:
    # 集合相等
    print "t equal s"

