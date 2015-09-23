# coding=utf-8

"""
大文本生成工具
"""

fp = open("big_txt.txt", "w")

for i in range(0, 999999):
    fp.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + str(i))

fp.close()
