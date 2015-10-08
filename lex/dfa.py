# coding=utf-8
__author__ = 'linzh'

class Dfa(object):
    """
    确定状态机
    """
    def __init__(self):
        """

        :return:
        """

        # 接受状态的动作
        self.accept = ""

        # 状态数
        self.nstates = 0

        # 状态转换表数组指针
        self.dfap = list()

        # 接受状态数组指针
        self.acceptp = list()

    def set_dfa(self):
        """
        设置转换表

        :return:
        """

    def set_accept(self):
        """
        设置接受状态数组

        :return:
        """

    def is_accepted(self, s):
        """
        判断指定状态是否是被接受的

        :return:
        """

    def make_dfa(self):
        """
        构造一个确定性状态机

        :return:
        """

        return self.nstates

