# coding=utf-8
__author__ = 'linzh'


fp = open("busy_io_test.txt", "w")

for j in range(0, 1000000):
    for i in range(0, 10000000):
        fp.write("hello,wwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")

fp.close()
