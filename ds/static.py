# coding=utf-8
__author__ = 'linzh'


class MyCls(object):
    """
    测试类静态变量的初始化
    """

    first_call = 0

    def test(self):
        if not MyCls.first_call:
            MyCls.first_call = 1
            print "first call"


if __name__ == "__main__":
    o = MyCls()
    o.test()
    o.test()
