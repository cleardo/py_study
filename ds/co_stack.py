# coding=utf-8
__author__ = 'linzh'


class CoStack(object):
    def __init__(self, n=100):
        self.elements = list()
        self.capcity = n
        self.sp = 0

    def push(self, obj):
        self.elements.append(obj)
        self.sp += 1

    def pop(self):
        ele = self.elements.pop()
        self.sp -= 1
        return ele

    def is_full(self):
        if self.sp == self.capcity:
            return True
        else:
            return False

    def is_empty(self):
        pass

    def top(self):
        return self.elements[self.sp - 1]

    def show(self):
        print self.elements

if __name__ == "__main__":
    stk = CoStack(2)
    stk.push('a')
    stk.show()
    stk.push('b')
    print stk.is_full()
    stk.show()
    print "栈顶元素", stk.top()
    print stk.pop()
    print stk.sp
    print stk.is_full()
