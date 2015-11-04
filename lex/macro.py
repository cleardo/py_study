# coding=utf-8
__author__ = 'linzh'


class Macro(object):
    def __init__(self):
        # 宏
        self.table = dict()

    def expand(self, key):
        """
        展开一个宏

        :param key:
        :return:
        """
        if key in self.table:
            return self.table[key]
        else:
            return None

    def create(self, key, val):
        """
        构造一个宏

        :return:
        """
        self.table[key] = val


