# coding=utf-8

__author__ = 'linzh'

FCON = 1
ICON = 2


"""
生成的词法解析器
"""

# 起始状态
yystate = 0
yynstate = 0

# 状态转换表
yy_nxt = list()
yy_nxt.append([1, 2])
yy_nxt.append([1, 2])

def move(s, c):
    """
    状态转换函数
    :return:
    """
    return yy_nxt[s][c]

# 读入数据
if yystate == 2:
    pass




