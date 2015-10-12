# coding=utf-8
__author__ = 'linzh'

# 方法一
import os

print os.popen('ls -l').read()


# 方法二
import subprocess

