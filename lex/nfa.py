# coding=utf-8
__author__ = 'linzh'

class Nfa(object):
    """
    非确定状态机
    """
    def __init__(self):
        """

        :return:
        """
        self.state = 0
        # 边
        self.edge = ''
        # 下一个状态
        self.next1 = ''
        self.next2 = ''
        self.ccl = set()
        # 锚点（行首、行末、首尾、无）
        self.anchor = 0

    def gen(self):
        """
        生成非确定自动机

        基于tompson算法实现

        :return:
        """
        # 起始状态
        sstate = 0

        return sstate

