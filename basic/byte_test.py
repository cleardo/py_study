# coding=utf-8

__author__ = 'donglin'


fp = open("bin_file", "wb")

fp.write("GET /url\n")
fp.write("key=value\n")
fp.write("\r\n")

fp2 = open("test02.jpg", "rb")

pic_data = fp2.read(100)

fp.write(pic_data)

fp.close()

