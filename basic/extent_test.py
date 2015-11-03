# coding=utf-8

__author__ = 'linzh'


class MyBase(object):
    def __init__(self):
        print "hello"
        self.val = 1


class MySubBase(MyBase):
    def __init__(self):
        print "world"
        MyBase.__init__(self)


class MySubBase2(MyBase):
    def __init__(self):
        super(MySubBase2, self).__init__()


if __name__ == "__main__":
    b = MyBase()
    print b.val

    s = MySubBase()
    print s.val

    s2 = MySubBase2()
    print s2.val
