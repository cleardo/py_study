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
        self.edge = ''
        self.next1 = ''
        self.next2 = ''

    def gen(self):
        """
        生成非确定自动机

        基于tompson算法实现

        :return:
        """
        # 起始状态
        sstate = 0

        return sstate

